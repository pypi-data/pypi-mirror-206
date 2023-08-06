import os
import json
from typing import List, Dict
from functools import lru_cache
from jupyter_scheduler.models import RuntimeEnvironment
from jupyter_scheduler.environments import EnvironmentManager
from amazon_sagemaker_jupyter_scheduler.app_metadata import get_region_name

region_name_to_code = {
    "us-east-2": "US East (Ohio)",
    "us-east-1": "US East (N. Virginia)",
    "us-west-1": "US West (N. California)",
    "us-west-2": "US West (Oregon)",
    "af-south-1": "Africa (Cape Town)",
    "ap-east-1": "Asia Pacific (Hong Kong)",
    "ap-southeast-3": "Asia Pacific (Jakarta)",
    "ap-south-1": "Asia Pacific (Mumbai)",
    "ap-northeast-3": "Asia Pacific (Osaka)",
    "ap-northeast-2": "Asia Pacific (Seoul)",
    "ap-southeast-1": "Asia Pacific (Singapore)",
    "ap-southeast-2": "Asia Pacific (Sydney)",
    "ap-northeast-1": "Asia Pacific (Tokyo)",
    "ca-central-1": "Canada (Central)",
    "eu-central-1": "Europe (Frankfurt)",
    "eu-west-1": "Europe (Ireland)",
    "eu-west-2": "Europe (London)",
    "eu-south-1": "Europe (Milan)",
    "eu-west-3": "Europe (Paris)",
    "eu-north-1": "Europe (Stockholm)",
    "me-south-1": "Middle East (Bahrain)",
    "me-central-1": "Middle East (UAE)",
    "sa-east-1": "South America (São Paulo)",
    "us-gov-east-1": "AWS GovCloud (US-East)",
    "us-gov-west-1": "AWS GovCloud (US-West)",
}

# From Product Manger: “Choose the cheapest compute type by default: ml.m5.large”
# The problem with instances on Free tier is that those instances are more expensive than the ml.m5.large.
# So, I’m worried that we’ll end up charging the vast majority of the customers more with the default option by choosing
# a more expensive option.
# A Free Tier user can always choose to select the instances on their Free Tier.
# So, In summary, I think choosing the cheapest instance is a customer-first decision that will protect cusotmers from
# unintentional over-charges
# This instance is available in all regions
DEFAULT_COMPUTE_TYPE = "ml.m5.large"


class SagemakerEnvironmentManager(EnvironmentManager):
    """Provides a static list of environments, for demo purpose only"""

    def __init__(self):
        self.region_mapping = {}
        # TODO: Find a way read this value, For now hard coding it from
        # ideally we should get this information from Training API,
        # for now follow the instructions in readme file
        PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
        region_mapping_file = os.path.join(PACKAGE_ROOT, "host_region_mapping.json")
        with open(region_mapping_file) as file:
            self.region_mapping = json.load(file)

    @lru_cache(maxsize=5)
    def get_supported_compute_types(self, region_name):
        region = region_name_to_code.get(region_name, "us-east-2")
        instance_details = self.region_mapping.get("regions", {}).get(region, {})
        return [detail["Instance"] for detail in instance_details.values()]

    def list_environments(self) -> List[RuntimeEnvironment]:
        name = "sagemaker-default-env"
        path = os.path.join(os.environ["HOME"], name)
        supported_compute_types = self.get_supported_compute_types(get_region_name())

        return [
            RuntimeEnvironment(
                name=name,
                label=name,
                description=f"Virtual environment: {name}",
                file_extensions=["ipynb"],
                output_formats=[],
                compute_types=supported_compute_types,
                default_compute_type=DEFAULT_COMPUTE_TYPE,
                metadata={"path": path},
                # UTC Only because Event Bridge Rules only support UTC cron expressions.
                utc_only=True,
            )
        ]

    def manage_environments_command(self) -> str:
        return ""

    def output_formats_mapping(self) -> Dict[str, str]:
        return {"ipynb": "Notebook", "log": "Output Log"}
