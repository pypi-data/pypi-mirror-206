import json
import logging

from traitlets.config import Config

from amazon_sagemaker_jupyter_scheduler.environments import SagemakerEnvironmentManager
from amazon_sagemaker_jupyter_scheduler.models import JobTag
from amazon_sagemaker_jupyter_scheduler.error_util import ErrorConverter, SageMakerSchedulerError
import pytest
from datetime import datetime
import botocore
from unittest.mock import AsyncMock, Mock, patch, mock_open
from jupyter_scheduler.models import (
    DescribeJob,
    ListJobDefinitionsQuery,
    DescribeJobDefinition,
    ListJobDefinitionsResponse,
    UpdateJobDefinition,
    Status,
)
from tornado import web

from amazon_sagemaker_jupyter_scheduler.tests.helpers.utils import (
    future_with_result,
    future_with_exception,
)
from amazon_sagemaker_jupyter_scheduler.scheduler import (
    SageMakerScheduler,
    EVENT_BRIDGE_RULE_TARGET_ID,
)


def create_scheduler_with_mocked_dependencies():
    return SageMakerScheduler(
        root_dir="mock-root-dir",
        environments_manager=SagemakerEnvironmentManager(),
        config=Config(),
        sagemaker_client=Mock(),
        event_bridge_client=Mock(),
        s3_client=Mock(),
        converter=Mock(),
        error_matcher=Mock(),
        error_converter=Mock(),
        error_factory=Mock(),
        log=logging.getLogger("test_logger"),
    )


MOCK_RESOURCE_METADATA = """
{
  "ResourceArn": "arn:aws:sagemaker:us-west-2:112233445566:app/d-1a2b3c4d5e6f/fake-user/JupyterServer/default",
  "UserProfileName": "sunp",
  "DomainId": "d-1a2b3c4d5e6f"
}
"""

# TODO: Reintroduce this unit test with some refactoring
# @pytest.mark.asyncio
# async def test_create_job_success():
#     # Given
#     scheduler = create_scheduler_with_mocked_dependencies()
#
#     create_training_job_input = {"TrainingJobName": "a-b-c-d"}
#     scheduler.converter.to_create_training_job_input.return_value = future_with_result(
#         create_training_job_input
#     )
#
#     scheduler.sagemaker_client.create_training_job.return_value = future_with_result(
#         create_training_job_input
#     )
#
#     # When
#     create_job_input = CreateJob(
#         input_filename="mock-input-uri",
#         runtime_environment_name="mock-environment-name",
#         runtime_environment_parameters={"s3_input": "s3://mock-bucket/mock-path"},
#     )
#     result = await scheduler.create_job(create_job_input)
#
#     # Then
#     scheduler.converter.to_create_training_job_input.assert_called_with(
#         upstream_model=create_job_input
#     )
#     scheduler.sagemaker_client.create_training_job.assert_called_with(
#         create_training_job_input
#     )
#     assert result == {"job_id": "a-b-c-d"}


@pytest.mark.asyncio
@patch("builtins.open", new_callable=mock_open, read_data=MOCK_RESOURCE_METADATA)
async def test_get_job_success(mock_open):
    # Given
    scheduler = create_scheduler_with_mocked_dependencies()

    scheduler._sagemaker_client.describe_training_job.return_value = future_with_result(
        {
            "TrainingJobArn": "mock-training-job-arn",
        }
    )
    scheduler._sagemaker_client.list_tags.return_value = future_with_result(
        {
            "Tags": [
                {"Key": "tag 1 key", "Value": "tag 1 value"},
            ]
        }
    )

    get_job_response = DescribeJob(
        name="my-job",
        input_filename="mock-input-filename",
        runtime_environment_name="mock-runtime-environment-name",
        job_id="a-b-c-d",
        url="mock-url",
        create_time=123,
        update_time=456,
    )
    scheduler.converter.to_tag_dict.return_value = {
        "tag 1 key": "tag 1 value",
    }
    scheduler.converter.to_jupyter_describe_job_output.return_value = get_job_response

    # When
    result = await scheduler.get_job("a-b-c-d")

    # Then
    scheduler._sagemaker_client.describe_training_job.assert_called_with(
        job_name="a-b-c-d"
    )
    scheduler._sagemaker_client.list_tags.assert_called_with(
        resource_arn="mock-training-job-arn"
    )
    scheduler.converter.to_jupyter_describe_job_output.assert_called_with(
        scheduler=scheduler,
        outputs=True,
        training_job_response={
            "TrainingJobArn": "mock-training-job-arn",
        },
        tag_dict={
            "tag 1 key": "tag 1 value",
        },
    )
    scheduler.converter.to_tag_dict.assert_called_with(
        [
            {"Key": "tag 1 key", "Value": "tag 1 value"},
        ]
    )
    assert result == get_job_response


@pytest.mark.asyncio
@patch("builtins.open", new_callable=mock_open, read_data=MOCK_RESOURCE_METADATA)
async def test_get_job_definition_exception(mock_open):
    scheduler = create_scheduler_with_mocked_dependencies()
    scheduler.error_converter = ErrorConverter()
    scheduler._sagemaker_client.describe_pipeline.return_value = future_with_exception(
        botocore.exceptions.ClientError(
            {
                "Error": {"Code": "400", "Message": "No resource found"},
                "ResponseMetadata": {
                    "RequestId": "1234567890ABCDEF",
                    "HostId": "host ID data will appear here as a hash",
                    "HTTPStatusCode": 400,
                    "HTTPHeaders": {"header metadata key/values will appear here"},
                    "RetryAttempts": 0,
                },
            },
            "describe_pipeline",
        )
    )

    scheduler._event_bridge_client.describe_rule.return_value = future_with_result(
        {
            "Name": "string",
            "Arn": "string",
            "EventPattern": "string",
            "ScheduleExpression": "string",
            "State": "ENABLED",
            "Description": "string",
            "RoleArn": "string",
            "ManagedBy": "string",
            "EventBusName": "string",
            "CreatedBy": "string",
        }
    )

    scheduler._sagemaker_client.list_tags.return_value = future_with_result(
        {"Tags": [{"Key": "foo", "Value": "bar"}]}
    )

    with pytest.raises(SageMakerSchedulerError):
        await scheduler.get_job_definition("mock_id")


@pytest.mark.asyncio
@patch("builtins.open", new_callable=mock_open, read_data=MOCK_RESOURCE_METADATA)
async def test_delete_job_definition_happy_path(mock_open):
    scheduler = create_scheduler_with_mocked_dependencies()
    job_definition_id = "a-b-c-d"

    scheduler._event_bridge_client.disable_rule.return_value = future_with_result({})
    scheduler._sagemaker_client.delete_pipeline.return_value = future_with_result(
        {"PipelineArn": "string"}
    )
    scheduler._event_bridge_client.remove_targets.return_value = future_with_result(
        {"FailedEntryCount": 0}
    )
    scheduler._event_bridge_client.delete_rule.return_value = future_with_result({})

    result = await scheduler.delete_job_definition(job_definition_id)

    assert result is None
    # EB calls
    scheduler._event_bridge_client.disable_rule.assert_called_with(job_definition_id)
    scheduler._event_bridge_client.remove_targets.assert_called_with(
        job_definition_id, [EVENT_BRIDGE_RULE_TARGET_ID]
    )
    scheduler._event_bridge_client.delete_rule.assert_called_with(job_definition_id)

    # SM Pipeline calls
    scheduler._sagemaker_client.delete_pipeline.assert_called_with(job_definition_id)


@pytest.mark.asyncio
@patch("builtins.open", new_callable=mock_open, read_data=MOCK_RESOURCE_METADATA)
async def test_update_job_definition_happy_path(mock_open):
    scheduler = create_scheduler_with_mocked_dependencies()
    job_definition_id = "a-b-c-d"

    scheduler._event_bridge_client.put_rule.return_value = future_with_result(None)

    result = await scheduler.update_job_definition(
        job_definition_id, UpdateJobDefinition(schedule="30 12 * 1-12 MON-FRI")
    )

    assert result is None

    scheduler._event_bridge_client.put_rule.assert_called_with(
        name="a-b-c-d",
        description="Created for Notebook execution from notebook scheduler",
        schedule_expression="cron(30 12 ? 1-12 MON-FRI *)",
        state="ENABLED",
    )


@pytest.mark.asyncio
@patch("builtins.open", new_callable=mock_open, read_data=MOCK_RESOURCE_METADATA)
async def test_pause_job_definition_happy_path(mock_open):
    scheduler = create_scheduler_with_mocked_dependencies()
    job_definition_id = "a-b-c-d"

    scheduler._event_bridge_client.disable_rule.return_value = future_with_result(None)

    result = await scheduler.update_job_definition(
        job_definition_id, UpdateJobDefinition(active=False)
    )

    assert result is None

    scheduler._event_bridge_client.disable_rule.assert_called_with(job_definition_id)


@pytest.mark.asyncio
@patch("builtins.open", new_callable=mock_open, read_data=MOCK_RESOURCE_METADATA)
async def test_resume_job_definition_happy_path(mock_open):
    scheduler = create_scheduler_with_mocked_dependencies()
    job_definition_id = "a-b-c-d"

    scheduler._event_bridge_client.enable_rule.return_value = future_with_result(None)

    result = await scheduler.update_job_definition(
        job_definition_id, UpdateJobDefinition(active=True)
    )

    assert result is None

    scheduler._event_bridge_client.enable_rule.assert_called_with(job_definition_id)


def _create_mock_describe_job_definition(name, job_definition_id, status):
    return DescribeJobDefinition(
        input_filename="INPUT_FILENAME_STUB",
        # TODO: add this env to CreateJob
        runtime_environment_name="sagemaker-default-env",
        runtime_environment_parameters={},
        output_formats=["ipynb"],
        parameters={},
        tags=[],
        name=name,
        compute_type="m4.xl.large",
        schedule="cron()",
        timezone="UTC",
        job_definition_id=job_definition_id,
        create_time=1665485984,
        update_time=1665485984,
        active=status,
    )


def _create_mock_search_results(name, job_definition_id):
    return {
        "Pipeline": {
            "PipelineArn": "string",
            "PipelineName": job_definition_id,
            "PipelineDisplayName": "string",
            "PipelineDescription": "string",
            "RoleArn": "string",
            "PipelineStatus": "Active",
            "CreationTime": datetime(2015, 1, 1),
            "LastModifiedTime": datetime(2015, 1, 1),
            "LastRunTime": datetime(2015, 1, 1),
            "CreatedBy": {
                "UserProfileArn": "string",
                "UserProfileName": "string",
                "DomainId": "string",
            },
            "LastModifiedBy": {
                "UserProfileArn": "string",
                "UserProfileName": "string",
                "DomainId": "string",
            },
            "Tags": [
                {"Key": JobTag.NOTEBOOK_NAME.value, "Value": name},
            ],
        }
    }


@pytest.mark.asyncio
@patch("builtins.open", new_callable=mock_open, read_data=MOCK_RESOURCE_METADATA)
async def test_list_job_definition_happy_path(mock_open):

    scheduler = create_scheduler_with_mocked_dependencies()
    expected_results = [
        _create_mock_describe_job_definition("definition-1", "a-b-c-d", True),
        _create_mock_describe_job_definition("definition-2", "a1-b2-c3-d4", True),
        _create_mock_describe_job_definition("definition-3", "e1-f2-g3-h4", True),
    ]

    scheduler._sagemaker_client.search.return_value = future_with_result(
        {
            "Results": [
                _create_mock_search_results("definition-1", "a-b-c-d"),
                _create_mock_search_results("definition-2", "a1-b2-c3-d4"),
                _create_mock_search_results("definition-3", "e1-f2-g3-h4"),
            ],
            "NextToken": "token-1",
        }
    )

    scheduler.get_job_definition = Mock()
    scheduler.get_job_definition.side_effect = [
        future_with_result(
            _create_mock_describe_job_definition("definition-1", "a-b-c-d", True)
        ),
        future_with_result(
            _create_mock_describe_job_definition("definition-2", "a1-b2-c3-d4", True)
        ),
        future_with_result(
            _create_mock_describe_job_definition("definition-3", "e1-f2-g3-h4", True)
        ),
    ]

    query = ListJobDefinitionsQuery(name="definition", create_time=1665443057000)

    result = await scheduler.list_job_definitions(query)

    assert result == ListJobDefinitionsResponse(
        job_definitions=expected_results, next_token="token-1", total_count=-1
    )


@pytest.mark.asyncio
@patch("builtins.open", new_callable=mock_open, read_data=MOCK_RESOURCE_METADATA)
async def test_get_system_dependencies_version(mock_open):
    scheduler = create_scheduler_with_mocked_dependencies()
    body_json = {"latest": 123456789}
    body_encoded = json.dumps(body_json).encode("utf-8")

    scheduler._s3_client.get_object_content.return_value = future_with_result(body_encoded)

    s3_uri = await scheduler._get_system_dependencies_version(region_name="us-west-2")

    assert (
        s3_uri
        == "s3://sagemakerheadlessexecution-prod-us-west-2/headless_system_dependencies/build_123456789"
    )


@pytest.mark.asyncio
@patch("builtins.open", new_callable=mock_open, read_data=MOCK_RESOURCE_METADATA)
async def test_get_staging_paths__job_completed__allows_downloading_all_outputs(
    mock_open,
):
    # Given
    scheduler = create_scheduler_with_mocked_dependencies()
    scheduler._sagemaker_client.describe_training_job.return_value = future_with_result(
        {
            "TrainingJobArn": "arn:aws:sagemaker:us-west-2:112233445566:training-job/example-job-id",
            "TrainingJobStatus": "Completed",
            "Environment": {"SM_OUTPUT_NOTEBOOK_NAME": "output-HelloWorld.ipynb"},
        }
    )

    # When
    result = await scheduler.get_staging_paths(
        DescribeJob(
            name="my-job",
            status=Status.COMPLETED,
            input_filename="HelloWorld.ipynb",
            runtime_environment_name="sagemaker-default-env",
            runtime_environment_parameters={
                "s3_input": "s3://sagemaker-us-east-1-177118115371",
                "s3_output": "s3://sagemaker-us-east-1-177118115371",
            },
            job_id="example-job-id",
            url="",
            create_time=123,
            update_time=456,
        )
    )

    # Then
    assert result == {
        "tar.gz": "s3://sagemaker-us-east-1-177118115371/example-job-id/output/output.tar.gz",
        "input": "HelloWorld.ipynb",
        "ipynb": "output-HelloWorld.ipynb",
        "log": "sagemaker_job_execution.log",
    }


@pytest.mark.asyncio
@patch("builtins.open", new_callable=mock_open, read_data=MOCK_RESOURCE_METADATA)
async def test_get_staging_paths__job_failed_with_all_outputs__allows_downloading_all_outputs(
    mock_open,
):
    # Given
    scheduler = create_scheduler_with_mocked_dependencies()
    scheduler._sagemaker_client.describe_training_job.return_value = future_with_result(
        {
            "TrainingJobArn": "arn:aws:sagemaker:us-west-2:112233445566:training-job/example-job-id",
            "TrainingJobStatus": "Failed",
            "Environment": {"SM_OUTPUT_NOTEBOOK_NAME": "output-HelloWorld.ipynb"},
            "FailureReason": "AlgorithmError: [SM-111] An error occurred",
        }
    )
    scheduler.converter.determine_available_output_formats_and_failure_reason.return_value = (
        ["input", "ipynb", "log"],
        "AlgorithmError: An error occurred",
    )

    # When
    result = await scheduler.get_staging_paths(
        DescribeJob(
            name="my-job",
            status=Status.FAILED,
            input_filename="HelloWorld.ipynb",
            runtime_environment_name="sagemaker-default-env",
            runtime_environment_parameters={
                "s3_input": "s3://sagemaker-us-east-1-177118115371",
                "s3_output": "s3://sagemaker-us-east-1-177118115371",
            },
            job_id="example-job-id",
            url="",
            create_time=123,
            update_time=456,
        )
    )

    # Then
    scheduler.converter.determine_available_output_formats_and_failure_reason.assert_called_with(
        Status.FAILED, "AlgorithmError: [SM-111] An error occurred"
    )
    assert result == {
        "tar.gz": "s3://sagemaker-us-east-1-177118115371/example-job-id/output/output.tar.gz",
        "input": "HelloWorld.ipynb",
        "ipynb": "output-HelloWorld.ipynb",
        "log": "sagemaker_job_execution.log",
    }


@pytest.mark.asyncio
@patch("builtins.open", new_callable=mock_open, read_data=MOCK_RESOURCE_METADATA)
async def test_get_staging_paths__job_failed_with_no_notebook__allows_downloading_only_input_and_log(
    mock_open,
):
    # Given
    scheduler = create_scheduler_with_mocked_dependencies()
    scheduler._sagemaker_client.describe_training_job.return_value = future_with_result(
        {
            "TrainingJobArn": "arn:aws:sagemaker:us-west-2:112233445566:training-job/example-job-id",
            "TrainingJobStatus": "Failed",
            "Environment": {"SM_OUTPUT_NOTEBOOK_NAME": "output-HelloWorld.ipynb"},
            "FailureReason": "AlgorithmError: [SM-101] An error occurred",
        }
    )
    scheduler.converter.determine_available_output_formats_and_failure_reason.return_value = (
        ["input", "log"],
        None,
    )

    # When
    result = await scheduler.get_staging_paths(
        DescribeJob(
            name="my-job",
            status=Status.FAILED,
            input_filename="HelloWorld.ipynb",
            runtime_environment_name="sagemaker-default-env",
            runtime_environment_parameters={
                "s3_input": "s3://sagemaker-us-east-1-177118115371",
                "s3_output": "s3://sagemaker-us-east-1-177118115371",
            },
            job_id="example-job-id",
            url="",
            create_time=123,
            update_time=456,
        )
    )

    # Then
    scheduler.converter.determine_available_output_formats_and_failure_reason.assert_called_with(
        Status.FAILED, "AlgorithmError: [SM-101] An error occurred"
    )
    assert result == {
        "tar.gz": "s3://sagemaker-us-east-1-177118115371/example-job-id/output/output.tar.gz",
        "input": "HelloWorld.ipynb",
        "log": "sagemaker_job_execution.log",
    }


@pytest.mark.asyncio
async def test_get_staging_paths__job_failed_with_no_outputs__allows_downloading_original_input():
    # Given
    scheduler = create_scheduler_with_mocked_dependencies()
    scheduler._sagemaker_client.describe_training_job.return_value = future_with_result(
        {
            "TrainingJobArn": "arn:aws:sagemaker:us-west-2:112233445566:training-job/example-job-id",
            "TrainingJobStatus": "Failed",
            "Environment": {"SM_OUTPUT_NOTEBOOK_NAME": "output-HelloWorld.ipynb"},
            "FailureReason": "AlgorithmError: An error occurred",
        }
    )
    scheduler.converter.determine_available_output_formats_and_failure_reason.return_value = (
        [],
        "AlgorithmError: An error occurred",
    )

    # When
    result = await scheduler.get_staging_paths(
        DescribeJob(
            name="my-job",
            status=Status.FAILED,
            input_filename="HelloWorld.ipynb",
            runtime_environment_name="sagemaker-default-env",
            runtime_environment_parameters={
                "s3_input": "s3://sagemaker-us-east-1-177118115371",
                "s3_output": "s3://sagemaker-us-east-1-177118115371",
            },
            job_id="example-job-id",
            url="",
            create_time=123,
            update_time=456,
        )
    )

    # Then
    scheduler.converter.determine_available_output_formats_and_failure_reason.assert_called_with(
        Status.FAILED, "AlgorithmError: An error occurred"
    )
    assert result == {
        "input": "s3://sagemaker-us-east-1-177118115371/example-job-id/input/HelloWorld.ipynb",
    }