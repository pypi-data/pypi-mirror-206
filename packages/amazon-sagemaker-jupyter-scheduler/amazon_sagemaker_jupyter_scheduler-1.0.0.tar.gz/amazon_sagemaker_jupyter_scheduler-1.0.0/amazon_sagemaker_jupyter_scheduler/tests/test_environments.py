import os
from unittest import mock
from amazon_sagemaker_jupyter_scheduler.environments import SagemakerEnvironmentManager


class TestSagemakerEnvironments:
    @mock.patch.dict(os.environ, {"REGION_NAME": "us-west-2", "HOME": "."}, clear=True)
    def test_default_sagemaker_defaults(self):
        envs_response = SagemakerEnvironmentManager().list_environments()
        assert envs_response[0].name == "sagemaker-default-env"
        for instance in envs_response[0].compute_types:
            assert instance.startswith("ml")
