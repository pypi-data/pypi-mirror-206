import asyncio
from typing import Dict, Union
from functools import lru_cache

from amazon_sagemaker_jupyter_scheduler.app_metadata import get_domain_id, get_user_profile_name
from amazon_sagemaker_jupyter_scheduler.clients import SageMakerAsyncBoto3Client
from amazon_sagemaker_jupyter_scheduler.internal_metadata_adapter import InternalMetadataAdapter, StaticImagesMetadataAdapter, VanillaStaticImagesMetadataAdapter

APP_IMAGE_CONFIG_KEY = "AppImageConfig"
FILE_SYSTEM_CONFIG_KEY = "FileSystemConfig"
MOUNT_PATH_KEY = "MountPath"
DEFAULT_UID_KEY = "DefaultUid"
DEFAULT_GID_KEY = "DefaultGid"
APP_IMAGE_ARN_KEY = "ImageOrVersionArn"
IMAGE_METADATA_KEY = "ImageMetadata"
IMAGE_DISPLAY_NAME_KEY = "ImageDisplayName"
IMAGE_DESCRIPTION_KEY = "ImageDescription"
KERNELSPECS_KEY = "KernelSpecs"
KERNEL_GATEWAY_IMAGE_CONFIG_KEY = "KernelGatewayImageConfig"
CUSTOM_ECR_IMAGE_DEFAULT_OWNER = "Custom ECR owner"
CUSTOM_ECR_IMAGE_DEFAULT_MOUNT_PATH = "/root"
CUSTOM_ECR_IMAGE_DEFAULT_GID = "0"
CUSTOM_ECR_IMAGE_DEFAULT_UID = "0"


class FirstPartyImageMetadata:
    def __init__(self, metadata: Dict):
        self.metadata = metadata

    @property
    def app_image_uri(self):
        return self.metadata.get("AppImageUri")

    @property
    def image_arn(self):
        return self.metadata.get(APP_IMAGE_ARN_KEY)

    @property
    def image_owner(self):
        return self.metadata.get("FirstPartyImageOwner")

    @property
    def image_display_name(self):
        return self.metadata.get(IMAGE_METADATA_KEY, {}).get(IMAGE_DISPLAY_NAME_KEY)

    @property
    def image_description(self):
        return self.metadata.get(IMAGE_METADATA_KEY, {}).get(IMAGE_DESCRIPTION_KEY)

    @property
    def kernelspecs(self):
        return self.metadata.get(APP_IMAGE_CONFIG_KEY, {}).get(KERNELSPECS_KEY)

    @property
    def mount_path(self):
        return (
            self.metadata.get(APP_IMAGE_CONFIG_KEY)
            .get(FILE_SYSTEM_CONFIG_KEY)
            .get(MOUNT_PATH_KEY)
        )

    @property
    def uid(self):
        return (
            self.metadata.get(APP_IMAGE_CONFIG_KEY)
            .get(FILE_SYSTEM_CONFIG_KEY)
            .get(DEFAULT_UID_KEY)
        )

    @property
    def gid(self):
        return (
            self.metadata.get(APP_IMAGE_CONFIG_KEY)
            .get(FILE_SYSTEM_CONFIG_KEY)
            .get(DEFAULT_GID_KEY)
        )


class ThirdPartyImageMetadata:
    def __init__(self, image_version: Dict, app_image_config: Dict):
        self.image_version = image_version
        self.app_image_config = app_image_config

    @property
    def app_image_uri(self):
        return self.image_version.get("BaseImage")

    @property
    def image_arn(self):
        return self.image_version.get("ImageArn")

    @property
    def image_owner(self):
        return ""

    @property
    def mount_path(self):
        return (
            self.app_image_config.get(KERNEL_GATEWAY_IMAGE_CONFIG_KEY)
            .get(FILE_SYSTEM_CONFIG_KEY)
            .get(MOUNT_PATH_KEY)
        )

    @property
    def uid(self):
        return str(
            self.app_image_config.get(KERNEL_GATEWAY_IMAGE_CONFIG_KEY)
            .get(FILE_SYSTEM_CONFIG_KEY)
            .get(DEFAULT_UID_KEY)
        )

    @property
    def gid(self):
        return str(
            self.app_image_config.get(KERNEL_GATEWAY_IMAGE_CONFIG_KEY)
            .get(FILE_SYSTEM_CONFIG_KEY)
            .get(DEFAULT_GID_KEY)
        )


class CustomImageMetadata:
    def __init__(self, image_uri: str):
        self.image_uri = image_uri

    @property
    def app_image_uri(self):
        return self.image_uri

    @property
    def image_arn(self):
        return self.image_uri

    @property
    def image_owner(self):
        return CUSTOM_ECR_IMAGE_DEFAULT_OWNER

    @property
    def mount_path(self):
        return CUSTOM_ECR_IMAGE_DEFAULT_MOUNT_PATH

    @property
    def uid(self):
        return CUSTOM_ECR_IMAGE_DEFAULT_GID

    @property
    def gid(self):
        return CUSTOM_ECR_IMAGE_DEFAULT_UID


class FirstPartyImagesListProvider:
    def __init__(self, internal_metadata=None, static_metadata=None, vanilla_static_metadata=None):
        self.internal_metadata = internal_metadata or InternalMetadataAdapter()
        self.static_metadata = static_metadata or StaticImagesMetadataAdapter()
        self.vanilla_static_metadata = vanilla_static_metadata or VanillaStaticImagesMetadataAdapter()

    def _parse_image_arn(self, arn):
        elements = arn.split(':', 5)
        result = {
            'arn': elements[0],
            'partition': elements[1],
            'service': elements[2],
            'region': elements[3],
            'account': elements[4],
            'resource': elements[5],
            'resource_type': None
        }
        if '/' in result['resource']:
            result['resource_type'], result['resource'] = result['resource'].split(
                '/', 1)
        elif ':' in result['resource']:
            result['resource_type'], result['resource'] = result['resource'].split(
                ':', 1)
        return result

    '''
    Returns a map between region and image metadata within that region
    '''
    @lru_cache(maxsize=1)
    def _get_available_image_map(self):
        # Get image from internal_metadata.json
        image_map = {}
        images_from_internal_metadata = [FirstPartyImageMetadata(
            first_party_image_metadata) for first_party_image_metadata in self.internal_metadata.get_first_party_images()]
        for image in images_from_internal_metadata:
            image_region = self._parse_image_arn(image.image_arn)["region"]
            if not image_region in image_map:
                image_map[image_region] = []
            image_map[image_region].append(image)

        # For regions that are not available in internal_metadata.json, fall back
        # to use static definition file
        images_data_from_static_metadata = self.static_metadata.get_image_metadata()
        for region in images_data_from_static_metadata:
            if region not in image_map:
                image_map[region] = [FirstPartyImageMetadata(
                    image_metadata) for image_metadata in images_data_from_static_metadata[region]]

        # Fallback to vanilla static metadata
        images_data_from_vanilla_static_metadata = self.vanilla_static_metadata.get_image_metadata()
        for region in images_data_from_vanilla_static_metadata:
            if region not in image_map:
                image_map[region] = [FirstPartyImageMetadata(
                    image_metadata) for image_metadata in images_data_from_vanilla_static_metadata[region]]

        return image_map

    @lru_cache(maxsize=15)
    def get_first_party_images_list(self, region):
        image_map = self._get_available_image_map()
        if region in image_map:
            return [
                {
                    "image_arn": image.image_arn,
                    "image_display_name": image.image_display_name,
                    "image_description": image.image_description,
                    "kernelspecs": image.kernelspecs,
                    "group": "smeImage",
                }
                for image in image_map[region]
            ]
        else:
            return []

    def get_image_metadata_by_name(self, image_name, region):
        first_party_images_list = self._get_available_image_map().get(region)
        for first_party_image in first_party_images_list:
            if self._parse_image_arn(first_party_image.image_arn).get("resource") == image_name:
                return first_party_image
        return None

    def get_image_metadata_by_arn(self, image_arn, region):
        first_party_images_list = self._get_available_image_map().get(region)
        for first_party_image in first_party_images_list:
            if first_party_image.image_arn == image_arn:
                return first_party_image
        return None


class ImageMetadataResolver:
    def __init__(
        self,
        metadata: InternalMetadataAdapter,
        sagemaker_client: SageMakerAsyncBoto3Client,
    ):
        self.metadata = metadata
        self.sagemaker_client = sagemaker_client
        self.image_list_provider = FirstPartyImagesListProvider()

    async def _fetch_custom_images(self):
        [domain_details, user_details] = await asyncio.gather(
            self.sagemaker_client.describe_domain(get_domain_id()),
            self.sagemaker_client.describe_user_profile(
                get_domain_id(), get_user_profile_name()
            ),
        )

        return domain_details.get("DefaultUserSettings", {}).get(
            "KernelGatewayAppSettings", {}
        ).get("CustomImages", []) + user_details.get("UserSettings", {}).get(
            "KernelGatewayAppSettings", {}
        ).get(
            "CustomImages", []
        )

    async def resolve_image_metadata(
        self, region, image_arn: str
    ) -> Union[FirstPartyImageMetadata, ThirdPartyImageMetadata]:
        first_party_image_metadata = self.image_list_provider.get_image_metadata_by_arn(
            image_arn, region)
        if first_party_image_metadata is not None:
            return first_party_image_metadata

        for third_party_image_metadata in self.metadata.get_custom_images():
            if image_arn == third_party_image_metadata.get(APP_IMAGE_ARN_KEY):
                image_name = image_arn.split("image/")[1]
                [image_version, custom_images] = await asyncio.gather(
                    self.sagemaker_client.describe_image_version(image_name),
                    self._fetch_custom_images(),
                )

                # Search custom images to find image config name
                app_image_config_name = next(
                    image["AppImageConfigName"]
                    for image in custom_images
                    if image["ImageName"] == image_name
                )
                app_image_config = (
                    await self.sagemaker_client.describe_app_image_config(
                        app_image_config_name
                    )
                )

                return ThirdPartyImageMetadata(image_version, app_image_config)

        return CustomImageMetadata(image_arn)

        raise RuntimeError(
            f"Image metadata does not exist for the specified image: {image_arn}"
        )
