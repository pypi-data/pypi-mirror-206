import os
from unittest.mock import patch, mock_open

from amazon_sagemaker_jupyter_scheduler.app_metadata import (
    get_region_name,
    get_partition,
    get_aws_account_id,
)

TEST_DEFAULT_REGION = "us-east-1"

from botocore.session import Session

class TestAppMetadataUtils:
    @patch.object(Session, "get_scoped_config")
    def test_get_region_name(self, get_scoped_config_mock):
        os.environ["AWS_REGION"] = TEST_DEFAULT_REGION
        result = get_region_name()
        assert result == TEST_DEFAULT_REGION

        del os.environ['AWS_REGION']
        get_scoped_config_mock.return_value = { "region": "us-west-1" }
        result = get_region_name()
        assert result == "us-west-1"

        get_scoped_config_mock.return_value = {}
        os.environ["AWS_DEFAULT_REGION"] = "us-west-2"
        result = get_region_name()
        assert result == "us-west-2"

        del os.environ['AWS_DEFAULT_REGION']
        result = get_region_name()
        assert result == "us-east-2"


    @patch("amazon_sagemaker_jupyter_scheduler.app_metadata.get_region_name")
    def test_get_partition(self, get_region_name_mock):
        get_region_name_mock.return_value = "us-east-2"
        result = get_partition()
        assert result == "aws"

    @patch("amazon_sagemaker_jupyter_scheduler.app_metadata.get_region_name")
    def test_get_partition_roundtable_region(self, get_region_name_mock):
        get_region_name_mock.return_value = "cn-north-1"
        result = get_partition()
        assert result == "aws-cn"

    def test_get_aws_account_id(self):
        result = get_aws_account_id()
        assert result == "123456789012"
