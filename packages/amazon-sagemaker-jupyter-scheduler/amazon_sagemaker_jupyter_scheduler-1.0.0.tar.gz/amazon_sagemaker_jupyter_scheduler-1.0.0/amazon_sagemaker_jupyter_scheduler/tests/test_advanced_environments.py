import os
import copy
import pytest
from unittest.mock import MagicMock, patch, mock_open
import botocore.exceptions

from amazon_sagemaker_jupyter_scheduler.clients import (
    IAMAsyncBotoClient,
    STSAsyncBotoClient,
    SageMakerAsyncBoto3Client,
    S3AsyncBoto3Client,
    EC2AsyncBotoClient,
)
from amazon_sagemaker_jupyter_scheduler.advanced_environments import SAGEMAKER_DEFAULT_S3_PREFIX
from amazon_sagemaker_jupyter_scheduler.advanced_environments import (
    get_advanced_environments,
    _get_compatible_subnets,
)
from botocore.session import Session

from amazon_sagemaker_jupyter_scheduler.internal_metadata_adapter import VanillaStaticImagesMetadataAdapter


TEST_ACCOUNT_ID = "123456789012"
TEST_DEFAULT_REGION = "us-east-1"
TEST_SUBNETS_IDS_ATTACHED_TO_DOMAIN = [
    "subnet-0a959d457c3d0ed01",
    "subnet-05305f168f2ef2ac7",
]
PUBLIC_SUBNETS = ["subnet-07fc038adc7621412", "subnet-0a959d457c3d0ed01"]
os.environ["REGION_NAME"] = TEST_DEFAULT_REGION
os.environ["AWS_ACCOUNT_ID"] = TEST_ACCOUNT_ID

MOCK_RESOURCE_METADATA = """
{
  "ResourceArn": "arn:aws:sagemaker:us-west-2:112233445566:app/d-1a2b3c4d5e6f/fake-user/JupyterServer/default",
  "UserProfileName": "sunp",
  "DomainId": "d-1a2b3c4d5e6f"
}
"""

MOCK_DESCRIBE_SUBNET_RESPONSE = {
    "Subnets": [
        {
            "SubnetId": "subnet-05305f168f2ef2ac7",
            "VpcId": "vpc-05ce35bb227e86484",
        },
        {
            "SubnetId": "subnet-05bbc4eafbdc88920",
            "VpcId": "vpc-05ce35bb227e86484",
        },
        {
            "SubnetId": "subnet-0a959d457c3d0ed01",
            "VpcId": "vpc-05ce35bb227e86484",
        },
        {
            "SubnetId": "subnet-07fc038adc7621412",
            "VpcId": "vpc-05ce35bb227e86484",
        },
        {
            "SubnetId": "subnet-0f582c5947f35419f",
            "VpcId": "vpc-05ce35bb227e86484",
        },
        {
            "SubnetId": "subnet-07d359796424cd2a1",
            "VpcId": "vpc-05ce35bb227e86484",
        },
    ]
}
MOCK_DESCRIBE_ROUTE_TABLES_RESPONSE = {
    "RouteTables": [
        {
            "Associations": [
                {
                    "Main": False,
                    "RouteTableAssociationId": "rtbassoc-04635e2ca0290347e",
                    "RouteTableId": "rtb-0802b33f7aa6bed8b",
                    "SubnetId": "subnet-0f582c5947f35419f",
                    "AssociationState": {"State": "associated"},
                }
            ],
            "PropagatingVgws": [],
            "RouteTableId": "rtb-0802b33f7aa6bed8b",
            "Routes": [
                {
                    "DestinationCidrBlock": "172.31.0.0/16",
                    "GatewayId": "local",
                    "Origin": "CreateRouteTable",
                    "State": "active",
                },
                {
                    "DestinationCidrBlock": "0.0.0.0/0",
                    "NatGatewayId": "nat-0481f1af25a35f2fa",
                    "Origin": "CreateRoute",
                    "State": "active",
                },
            ],
            "VpcId": "vpc-05ce35bb227e86484",
            "OwnerId": "344324978117",
        },
        {
            "Associations": [
                {
                    "Main": True,
                    "RouteTableAssociationId": "rtbassoc-05d17845a7eec5c30",
                    "RouteTableId": "rtb-0411fbf75ee776835",
                    "AssociationState": {"State": "associated"},
                }
            ],
            "PropagatingVgws": [],
            "RouteTableId": "rtb-0411fbf75ee776835",
            "Routes": [
                {
                    "DestinationCidrBlock": "172.31.0.0/16",
                    "GatewayId": "local",
                    "Origin": "CreateRouteTable",
                    "State": "active",
                }
            ],
            "Tags": [],
            "VpcId": "vpc-05ce35bb227e86484",
            "OwnerId": "344324978117",
        },
        {
            "Associations": [
                {
                    "Main": False,
                    "RouteTableAssociationId": "rtbassoc-0f8e8a622b9eb36e5",
                    "RouteTableId": "rtb-0dbfc6eb83f98fdc0",
                    "SubnetId": "subnet-05bbc4eafbdc88920",
                    "AssociationState": {"State": "associated"},
                }
            ],
            "PropagatingVgws": [],
            "RouteTableId": "rtb-0dbfc6eb83f98fdc0",
            "Routes": [
                {
                    "DestinationCidrBlock": "172.31.0.0/16",
                    "GatewayId": "local",
                    "Origin": "CreateRouteTable",
                    "State": "active",
                },
                {
                    "DestinationCidrBlock": "0.0.0.0/0",
                    "NatGatewayId": "nat-0481f1af25a35f2fa",
                    "Origin": "CreateRoute",
                    "State": "active",
                },
            ],
            "VpcId": "vpc-05ce35bb227e86484",
            "OwnerId": "344324978117",
        },
        {
            "Associations": [
                {
                    "Main": False,
                    "RouteTableAssociationId": "rtbassoc-02b6aaa99c3165da3",
                    "RouteTableId": "rtb-09689a554e29259a8",
                    "SubnetId": "subnet-07d359796424cd2a1",
                    "AssociationState": {"State": "associated"},
                }
            ],
            "PropagatingVgws": [],
            "RouteTableId": "rtb-09689a554e29259a8",
            "Routes": [
                {
                    "DestinationCidrBlock": "172.31.0.0/16",
                    "GatewayId": "local",
                    "Origin": "CreateRouteTable",
                    "State": "active",
                },
                {
                    "DestinationCidrBlock": "0.0.0.0/0",
                    "NatGatewayId": "nat-0481f1af25a35f2fa",
                    "Origin": "CreateRoute",
                    "State": "active",
                },
            ],
            "VpcId": "vpc-05ce35bb227e86484",
            "OwnerId": "344324978117",
        },
        {
            "Associations": [
                {
                    "Main": False,
                    "RouteTableAssociationId": "rtbassoc-06b582f51d8e782f6",
                    "RouteTableId": "rtb-0f0bccdfc5dc5e3a8",
                    "SubnetId": "subnet-05305f168f2ef2ac7",
                    "AssociationState": {"State": "associated"},
                }
            ],
            "PropagatingVgws": [],
            "RouteTableId": "rtb-0f0bccdfc5dc5e3a8",
            "Routes": [
                {
                    "DestinationCidrBlock": "172.31.0.0/16",
                    "GatewayId": "local",
                    "Origin": "CreateRouteTable",
                    "State": "active",
                },
                {
                    "DestinationCidrBlock": "0.0.0.0/0",
                    "NatGatewayId": "nat-0481f1af25a35f2fa",
                    "Origin": "CreateRoute",
                    "State": "active",
                },
            ],
            "VpcId": "vpc-05ce35bb227e86484",
            "OwnerId": "344324978117",
        },
        {
            "Associations": [
                {
                    "Main": False,
                    "RouteTableAssociationId": "rtbassoc-0659af6f078bcd27a",
                    "RouteTableId": "rtb-001deff63b78e51d0",
                    "SubnetId": "subnet-07fc038adc7621412",
                    "AssociationState": {"State": "associated"},
                },
                {
                    "Main": False,
                    "RouteTableAssociationId": "rtbassoc-0659af6f078dflsd27a",
                    "RouteTableId": "rtb-001deff63b78e51d0",
                    "SubnetId": "subnet-0a959d457c3d0ed01",
                    "AssociationState": {"State": "associated"},
                },
            ],
            "PropagatingVgws": [],
            "RouteTableId": "rtb-001deff63b78e51d0",
            "Routes": [
                {
                    "DestinationCidrBlock": "172.31.0.0/16",
                    "GatewayId": "local",
                    "Origin": "CreateRouteTable",
                    "State": "active",
                },
                {
                    "DestinationCidrBlock": "0.0.0.0/0",
                    "GatewayId": "igw-0ff7becfe19b8145d",
                    "Origin": "CreateRoute",
                    "State": "active",
                },
            ],
            "VpcId": "vpc-05ce35bb227e86484",
            "OwnerId": "344324978117",
        },
    ]
}

MOCK_VANILLA_IMAGES = {
    "us-east-1": [
        {
            "ImageOrVersionArn": "arn:aws:sagemaker:us-east-1:081325390199:image/sagemaker-base-python-38",
            "AppImageUri": "081325390199.dkr.ecr.us-east-1.amazonaws.com/sagemaker-base-python-38@sha256:27779e7604272e1d15ba19f5de70baa31dcceb246d5021f8c2c5d9db39c208cc",
            "ImageMetadata": {
                "ImageDisplayName": "Base Python 2.0",
                "ImageDescription": "Official Python3.8 image from DockerHub https://hub.docker.@@DOMAIN_STUFFIX@@/_/python"
            },
            "IsGpuOptimized": "false",
            "AppImageConfig": {
                "FileSystemConfig": {
                    "MountPath": "/root",
                    "DefaultUid": "0",
                    "DefaultGid": "0"
                },
                "KernelSpecs": [
                    {
                        "Name": "python3",
                        "DisplayName": "Python 3 (Base Python 2.0)"
                    }
                ]
            },
            "FirstPartyImageOwner": "Studio",
            "IsVisibleInLauncher": "true"
        }
    ]
}

MOCK_ROLE_ARNS_WITH_MATCHING_PREFIX = ["roleArn1", "roleArn2"]

MOCK_REGION = "us-east-1"
MOCK_PARTITION = "aws"
MOCK_CALLER_IDENTITY = {'Account': '123456789012'}


mock_logger = MagicMock()



@patch.object(S3AsyncBoto3Client, "create_bucket")
@patch.object(S3AsyncBoto3Client, "enable_server_side_encryption_with_s3_keys")
@patch.object(S3AsyncBoto3Client, "enable_versioning")
@patch("builtins.open", new_callable=mock_open, read_data=MOCK_RESOURCE_METADATA)
@patch.object(EC2AsyncBotoClient, "list_subnets_by_vpc_id")
@patch.object(EC2AsyncBotoClient, "list_routetable_by_vpc_id")
@patch.object(Session, "get_scoped_config")
@patch.object(Session, "get_partition_for_region")
@patch.object(STSAsyncBotoClient, "get_caller_identity")
@patch.object(VanillaStaticImagesMetadataAdapter, "get_image_metadata")
@patch.object(IAMAsyncBotoClient, "list_role_arns_with_matching_prefix")

class TestAdvancedEnvironments:
    @pytest.mark.asyncio
    async def test_auto_detect_happy_path(
        self,
        mock_list_role_arns_with_matching_prefix,
        mock_get_image_metadata,
        mock_get_caller_identity,
        mock_get_partition_for_region,
        mock_get_scoped_config,
        mock_describe_routetables,
        mock_describe_subnets,
        mock_open,
        mock_versioning,
        mock_encryption,
        mock_create_bucket,

    ):
        mock_create_bucket.side_effect = botocore.exceptions.ClientError(
            {
                "Error": {
                    "Code": "BucketAlreadyExists",
                    "Message": "The request was rejected because the domain is in status Failed",
                }
            },
            "CreateBucket",
        )
        mock_describe_routetables.return_value = MOCK_DESCRIBE_ROUTE_TABLES_RESPONSE
        mock_describe_subnets.return_value = MOCK_DESCRIBE_SUBNET_RESPONSE
        mock_get_scoped_config.return_value.get.return_value = MOCK_REGION
        mock_get_partition_for_region.return_value = MOCK_PARTITION
        mock_get_caller_identity.return_value = MOCK_CALLER_IDENTITY
        mock_get_image_metadata.return_value = MOCK_VANILLA_IMAGES
        mock_list_role_arns_with_matching_prefix.return_value = MOCK_ROLE_ARNS_WITH_MATCHING_PREFIX

        response = await get_advanced_environments(mock_logger)
        for env in response.auto_detected_config:
            if env.name == "s3_input" or env.name == "s3_output":
                assert (
                    env.value
                    == f"s3://{SAGEMAKER_DEFAULT_S3_PREFIX}-{TEST_ACCOUNT_ID}-{TEST_DEFAULT_REGION}/"
                )
            if env.name == "role_arn":
                assert env.value == MOCK_ROLE_ARNS_WITH_MATCHING_PREFIX
            if env.name == "vpc_subnets":
                assert env.value == []

    @pytest.mark.asyncio
    async def test_auto_detect_domain_role_arn_with_no_user_role_arn(
        self,
        mock_list_role_arns_with_matching_prefix,
        mock_get_image_metadata,
        mock_get_caller_identity,
        mock_get_partition_for_region,
        mock_get_scoped_config,
        mock_describe_routetables,
        mock_describe_subnets,
        mock_open,
        mock_versioning,
        mock_encryption,
        mock_create_bucket,
    ):
        mock_describe_routetables.return_value = MOCK_DESCRIBE_ROUTE_TABLES_RESPONSE
        mock_describe_subnets.return_value = MOCK_DESCRIBE_SUBNET_RESPONSE
        mock_create_bucket.return_value = {
            "Location": "/aws-emr-resources-177118115371-us-east-1"
        }
        mock_get_scoped_config.return_value.get.return_value = MOCK_REGION
        mock_get_partition_for_region.return_value = MOCK_PARTITION
        mock_get_caller_identity.return_value = MOCK_CALLER_IDENTITY
        mock_get_image_metadata.return_value = MOCK_VANILLA_IMAGES
        mock_list_role_arns_with_matching_prefix.return_value = []
        response = await get_advanced_environments(mock_logger)
        for env in response.auto_detected_config:
            if env.name == "role_arn":
                assert env.value == []

    @pytest.mark.asyncio
    async def test_identifying_compatible_subnets(
        self,
        mock_list_role_arns_with_matching_prefix,
        mock_get_image_metadata,
        mock_get_caller_identity,
        mock_get_partition_for_region,
        mock_get_scoped_config,
        mock_describe_routetables,
        mock_describe_subnets,
        mock_open,
        mock_versioning,
        mock_encryption,
        mock_create_bucket,
    ):

        mock_describe_routetables.return_value = MOCK_DESCRIBE_ROUTE_TABLES_RESPONSE
        mock_describe_subnets.return_value = MOCK_DESCRIBE_SUBNET_RESPONSE

        response = await _get_compatible_subnets("vpc-05ce35bb227e86484")

        for subnet in response:
            assert subnet["name"] not in PUBLIC_SUBNETS

    @pytest.mark.asyncio
    async def test_identifying_compatible_subnets_default_vpc(
        self,
        mock_list_role_arns_with_matching_prefix,
        mock_get_image_metadata,
        mock_get_caller_identity,
        mock_get_partition_for_region,
        mock_get_scoped_config,
        mock_describe_routetables,
        mock_describe_subnets,
        mock_open,
        mock_versioning,
        mock_encryption,
        mock_create_bucket,
    ):

        mock_describe_routetables.return_value = {
            "RouteTables": [
                {
                    "Associations": [
                        {
                            "Main": True,
                            "RouteTableAssociationId": "rtbassoc-da4fdabf",
                            "RouteTableId": "rtb-62850107",
                            "AssociationState": {"State": "associated"},
                        }
                    ],
                    "PropagatingVgws": [],
                    "RouteTableId": "rtb-62850107",
                    "Routes": [
                        {
                            "DestinationCidrBlock": "172.31.0.0/16",
                            "GatewayId": "local",
                            "Origin": "CreateRouteTable",
                            "State": "active",
                        },
                        {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "GatewayId": "igw-9418c6f1",
                            "Origin": "CreateRoute",
                            "State": "active",
                        },
                    ],
                    "Tags": [],
                    "VpcId": "vpc-e6bd0183",
                    "OwnerId": "344324978117",
                }
            ]
        }
        mock_describe_subnets.return_value = {
            "Subnets": [
                {
                    "SubnetId": "subnet-3c9f7c17",
                    "VpcId": "vpc-e6bd0183",
                },
                {
                    "SubnetId": "subnet-462b8031",
                    "VpcId": "vpc-e6bd0183",
                },
                {
                    "SubnetId": "subnet-a8e32af1",
                    "VpcId": "vpc-e6bd0183",
                },
                {
                    "SubnetId": "subnet-3e7bee5b",
                    "VpcId": "vpc-e6bd0183",
                },
            ]
        }

        response = await _get_compatible_subnets("vpc-05ce35bb227e86484")

        assert not response
