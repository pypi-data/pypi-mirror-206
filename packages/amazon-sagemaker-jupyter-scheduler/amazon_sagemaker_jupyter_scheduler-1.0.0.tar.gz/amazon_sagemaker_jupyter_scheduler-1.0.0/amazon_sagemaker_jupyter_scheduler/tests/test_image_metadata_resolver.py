import pytest
from unittest.mock import Mock, patch

from amazon_sagemaker_jupyter_scheduler.image_metadata_resolver import ImageMetadataResolver
from amazon_sagemaker_jupyter_scheduler.internal_metadata_adapter import InternalMetadataAdapter
from amazon_sagemaker_jupyter_scheduler.tests.data.mock_files import (
    MOCK_INTERNAL_METADATA,
    MOCK_RESOURCE_METADATA,
)
from amazon_sagemaker_jupyter_scheduler.tests.helpers.utils import (
    future_with_result,
    create_mock_open,
)


custom_mock_open = create_mock_open(
    {
        "/opt/.sagemakerinternal/internal-metadata.json": MOCK_INTERNAL_METADATA,
        "/opt/ml/metadata/resource-metadata.json": MOCK_RESOURCE_METADATA,
    }
)


def create_metadata_util_with_mocked_dependencies():
    mock_sagemaker_client = Mock(
        **{
            "describe_domain.return_value": future_with_result(
                {
                    "DefaultUserSettings": {
                        "KernelGatewayAppSettings": {
                            "CustomImages": [
                                {
                                    "ImageName": "custom-image",
                                    "AppImageConfigName": "custom-image-config",
                                },
                                {
                                    "ImageName": "multi-py-conda-image",
                                    "AppImageConfigName": "multi-py-conda-image-config",
                                },
                            ]
                        }
                    }
                }
            ),
            "describe_user_profile.return_value": future_with_result(
                {
                    "UserSettings": {
                        "KernelGatewayAppSettings": {
                            "CustomImages": [
                                {
                                    "ImageName": "another-custom-image",
                                    "AppImageConfigName": "another-custom-image-config",
                                },
                            ]
                        }
                    }
                }
            ),
            "describe_image_version.return_value": future_with_result(
                {
                    "BaseImage": "177118115371.dkr.ecr.us-east-1.amazonaws.com/multi-py-conda-image:0.0.1",
                    "ContainerImage": "177118115371.dkr.ecr.us-east-1.amazonaws.com/multi-py-conda-image@sha256:947aec5e04638b43db188fd51ab8e850ac31bf83281c5b61f2e2f4d5e0f06477",
                    "CreationTime": 1666064247.19,
                    "ImageArn": "arn:aws:sagemaker:us-east-1:177118115371:image/multi-py-conda-image",
                    "ImageVersionArn": "arn:aws:sagemaker:us-east-1:177118115371:image-version/multi-py-conda-image/2",
                    "ImageVersionStatus": "CREATED",
                    "LastModifiedTime": 1666064247.561,
                    "Version": 2,
                    "Horovod": False,
                }
            ),
            "describe_app_image_config.return_value": future_with_result(
                {
                    "AppImageConfigArn": "arn:aws:sagemaker:us-east-1:177118115371:app-image-config/multi-py-conda-image-config",
                    "AppImageConfigName": "multi-py-conda-image-config",
                    "CreationTime": 1666064286.771,
                    "LastModifiedTime": 1666064286.776,
                    "KernelGatewayImageConfig": {
                        "KernelSpecs": [
                            {
                                "Name": "conda-env-py310-py",
                                "DisplayName": "conda env py310",
                            },
                            {
                                "Name": "conda-env-py39-py",
                                "DisplayName": "conda env py39",
                            },
                            {
                                "Name": "conda-env-py37-py",
                                "DisplayName": "conda env py37",
                            },
                            {
                                "Name": "conda-env-py38-py",
                                "DisplayName": "conda env py38",
                            },
                        ],
                        "FileSystemConfig": {
                            "MountPath": "/home/sagemaker-user",
                            "DefaultUid": 1000,
                            "DefaultGid": 100,
                        },
                    },
                }
            ),
        }
    )
    return ImageMetadataResolver(InternalMetadataAdapter(), mock_sagemaker_client)


@pytest.mark.asyncio
@patch("builtins.open", custom_mock_open)
async def test_internal_metadata__first_party_image__success():
    # Given
    metadata_util = create_metadata_util_with_mocked_dependencies()

    # When
    image_metadata = await metadata_util.resolve_image_metadata(
        "us-west-2",
        "arn:aws:sagemaker:us-west-2:236514542706:image/datascience-1.0"
    )

    # Then
    assert (
        image_metadata.app_image_uri
        == "236514542706.dkr.ecr.us-west-2.amazonaws.com/sagemaker-data-science-environment:1.0"
    )
    assert (
        image_metadata.image_arn
        == "arn:aws:sagemaker:us-west-2:236514542706:image/datascience-1.0"
    )
    assert image_metadata.image_owner == "Studio"
    assert image_metadata.mount_path == "/root"
    assert image_metadata.uid == "0"
    assert image_metadata.gid == "0"


@pytest.mark.asyncio
@patch("builtins.open", custom_mock_open)
async def test_internal_metadata__third_party_image__success():
    # Given
    metadata_util = create_metadata_util_with_mocked_dependencies()

    # When
    image_metadata = await metadata_util.resolve_image_metadata(
        "us-west-2",
        "arn:aws:sagemaker:us-east-1:177118115371:image/multi-py-conda-image"
    )

    # Then
    assert (
        image_metadata.app_image_uri
        == "177118115371.dkr.ecr.us-east-1.amazonaws.com/multi-py-conda-image:0.0.1"
    )
    assert (
        image_metadata.image_arn
        == "arn:aws:sagemaker:us-east-1:177118115371:image/multi-py-conda-image"
    )
    assert image_metadata.image_owner == ""
    assert image_metadata.mount_path == "/home/sagemaker-user"
    assert image_metadata.uid == "1000"
    assert image_metadata.gid == "100"

    metadata_util.sagemaker_client.describe_domain.assert_called_with("d-1a2b3c4d5e6f")
    metadata_util.sagemaker_client.describe_user_profile.assert_called_with(
        "d-1a2b3c4d5e6f", "sunp"
    )
    metadata_util.sagemaker_client.describe_image_version.assert_called_with(
        "multi-py-conda-image"
    )
    metadata_util.sagemaker_client.describe_app_image_config.assert_called_with(
        "multi-py-conda-image-config"
    )
