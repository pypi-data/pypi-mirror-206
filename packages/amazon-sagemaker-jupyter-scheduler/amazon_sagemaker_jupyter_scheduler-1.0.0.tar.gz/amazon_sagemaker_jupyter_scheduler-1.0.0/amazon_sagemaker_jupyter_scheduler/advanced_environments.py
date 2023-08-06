import asyncio
import botocore.exceptions
from amazon_sagemaker_jupyter_scheduler.clients import (
    get_s3_client,
    get_ec2_client,
    get_iam_client,
)
from amazon_sagemaker_jupyter_scheduler.models import AdvancedEnvironment, AdvancedEnvironmentResponse
from amazon_sagemaker_jupyter_scheduler.app_metadata import get_region_name
from amazon_sagemaker_jupyter_scheduler.aws_config import get_aws_account_id
from amazon_sagemaker_jupyter_scheduler.image_metadata_resolver import FirstPartyImagesListProvider
from typing import List


SAGEMAKER_DEFAULT_S3_PREFIX = "sagemaker-automated-execution"
SAGEMAKER_ROLE_PREFIX = "SagemakerJupyterScheduler"
DEFAULT_IMAGE_NAME = "sagemaker-base-python-38"

def _does_routes_have_internet_gateway(route_details):
    for route in route_details["Routes"]:
        if route.get("GatewayId", "").startswith("igw"):
            return True
    return False


# TODO: Test with some more data, not sure if I am covering all possible use cases.
# Also it would be nice to find an easier to way to identify if a subnet is private or public
async def _get_compatible_subnets(vpc_id: str) -> List[str]:

    ec2_client = get_ec2_client()

    subnets = await ec2_client.list_subnets_by_vpc_id(vpc_id)
    route_tables = await ec2_client.list_routetable_by_vpc_id(vpc_id)

    # construct a dictionary for quick access
    subnet_dict = {subnet["SubnetId"]: subnet for subnet in subnets.get("Subnets", [])}
    route_dict = {
        route["RouteTableId"]: route for route in route_tables.get("RouteTables", [])
    }

    ## add 2 fields
    for id in subnet_dict.keys():
        subnet_dict[id][
            "RouteTables"
        ] = (
            []
        )  # if this list is empty then we associate it with main route table of the given vpc
        subnet_dict[id]["IsPublic"] = False

    main_route_table_id = ""
    # update subnet_details with any explict route association
    for id, route in route_dict.items():
        for association in route["Associations"]:
            if association["AssociationState"]["State"] == "associated":
                subnet_id = association.get("SubnetId")
                if subnet_id:
                    subnet_dict[subnet_id]["RouteTables"].append(route["RouteTableId"])
                if association["Main"]:
                    main_route_table_id = route["RouteTableId"]

    # attach main route table to all other subnets, implicit association
    for id in subnet_dict.keys():
        if not subnet_dict[id]["RouteTables"]:
            subnet_dict[id]["RouteTables"].append(main_route_table_id)

    for id in subnet_dict.keys():
        for route_table_id in subnet_dict[id]["RouteTables"]:
            if _does_routes_have_internet_gateway(
                route_details=route_dict[route_table_id]
            ):
                subnet_dict[id]["IsPublic"] = True

    return [
        {"name": v["SubnetId"], "is_selected": False}
        for k, v in subnet_dict.items()
        if not v["IsPublic"]
    ]


async def _create_s3_buckets(s3_bucket_name, logger):
    try:
        response = await get_s3_client().create_bucket(
            s3_bucket_name, get_region_name()
        )
        logger.info(f"S3 bucket created succesfully {s3_uri} - {response}")
        # If the bucket already exists, the versioning & encryption calls is not needed
        logger.info(f"Enable default server side encryption for {s3_uri}")
        await get_s3_client().enable_server_side_encryption_with_s3_keys(
            bucket_name=s3_bucket_name
        )
        logger.info(f"Enable versioning for {s3_uri}")
        await get_s3_client().enable_versioning(bucket_name=s3_bucket_name)

        logger.info(f"S3 bucket created succesfully {s3_uri} - {response}")
    except botocore.exceptions.ClientError as error:
        # TODO: Discuss with PM on the desired fail safe mechanism, what if the bucket creation failed due to permission issue
        # ideally we need the UI to prompt the user to create the bucket
        # some issue with bucket creation
        logger.error(
            f"error when calling S3 bucket creation - {s3_bucket_name} - {error}"
        )


async def get_advanced_environments(logger):
    iam_client = get_iam_client()

    # empty values if api calls fail
    aws_account_id = None
    all_compatible_subnets = []
    security_group_ids = []
    role_arns = []  # TODO: sync with UI to modify this to a single value

    [aws_account_id, list_role_arns_with_matching_prefix_response] = await asyncio.gather(
        get_aws_account_id(),
        iam_client.list_role_arns_with_matching_prefix(SAGEMAKER_ROLE_PREFIX),
        return_exceptions = True
    )

    # log list_role_with_prefix_response
    logger.info(f"list_role_arns_with_matching_prefix_response - {list_role_arns_with_matching_prefix_response}")

    if isinstance(aws_account_id, Exception):
        raise aws_account_id

    if isinstance(list_role_arns_with_matching_prefix_response, Exception):
        logger.error(f"Unable to retrieve available SageMaker roles from IAM - {list_role_arns_with_matching_prefix_response}")
    else:
        if list_role_arns_with_matching_prefix_response is not None:
            role_arns = list_role_arns_with_matching_prefix_response

    s3_bucket_name = (
        f"{SAGEMAKER_DEFAULT_S3_PREFIX}-{aws_account_id}-{get_region_name()}"
    )
    s3_uri = f"s3://{s3_bucket_name}/"

    [create_s3_bucket_response] = await asyncio.gather(
        _create_s3_buckets(s3_bucket_name, logger),
        return_exceptions = True
    )

    default_image = FirstPartyImagesListProvider().get_image_metadata_by_name(DEFAULT_IMAGE_NAME, get_region_name())
    default_image_arn = default_image.image_arn
    default_kernelspecs = default_image.kernelspecs
    default_kernel = default_kernelspecs[0].get("Name", "") if len(default_kernelspecs) > 0 else ""

    default_envs = [
        AdvancedEnvironment(
            name="s3_input",
            label="Input S3",
            description="S3 location to store all notebook related files",
            value=s3_uri,
        ),
        AdvancedEnvironment(
            name="s3_output",
            label="Output S3",
            description="S3 location to store all output artifacts",
            value=s3_uri,
        ),
        AdvancedEnvironment(
            name="role_arn",
            label="Execution Role ARN",
            description="IAM Role to be used by the Notebook Execution Engine",
            value=role_arns,
        ),
        AdvancedEnvironment(
            name="image",
            label="SageMaker Image",
            description="SageMaker Image to execute the notebook in",
            value=default_image_arn
        ),
        AdvancedEnvironment(
            name="kernel",
            label="Python Kernel",
            description="Python Kernel to execute the notebook in",
            value=default_kernel
        ),
        AdvancedEnvironment(
            name="vpc_security_group_ids",
            label="VPC Config Security Group IDs",
            description="List of Security GroupIDs for the notebook to be executed",
            value=security_group_ids,
        ),
        AdvancedEnvironment(
            name="vpc_subnets",
            label="VPC Config Subnets",
            description="List of Subnets for the notebook to be executed in",
            value=all_compatible_subnets,
        )
    ]
    logger.info(f"auto-detected env values - {default_envs}")
    return AdvancedEnvironmentResponse(auto_detected_config=default_envs)
