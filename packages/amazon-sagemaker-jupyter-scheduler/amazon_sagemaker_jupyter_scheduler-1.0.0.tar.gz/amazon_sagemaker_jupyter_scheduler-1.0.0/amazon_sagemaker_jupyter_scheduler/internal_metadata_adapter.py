import json
import os

SAGEMAKER_INTERNAL_METADATA_FILE = "/opt/.sagemakerinternal/internal-metadata.json"
STATIC_IMAGE_METADATA_PATH = '/opt/amazon/sagemaker/image-metadata-static.json'

class InternalMetadataAdapter:
    def __init__(
        self,
        filename=SAGEMAKER_INTERNAL_METADATA_FILE,
    ):
        try:
            with open(filename, "r") as file:
                self.metadata = json.load(file)
        except:
            self.metadata = {}

    def get_stage(self) -> str:
        return self.metadata.get("Stage", "prod")

    def get_first_party_images(self):
        return self.metadata.get("FirstPartyImages", [])

    def get_custom_images(self):
        return self.metadata.get("CustomImages", [])


class StaticImagesMetadataAdapter:
    def __init__(
        self,
        filename=STATIC_IMAGE_METADATA_PATH,
    ):
        try:
            with open(filename, "r") as file:
                self.metadata = json.load(file)
        except:
            self.metadata = {}

    def get_image_metadata(self):
        return self.metadata

class VanillaStaticImagesMetadataAdapter:

    def __init__(self):
        try:
            PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
            filename = os.path.join(PACKAGE_ROOT, "vanilla-image-metadata-static.json")
            with open(filename, "r") as file:
                self.metadata = json.load(file)
        except:
            self.metadata = {}

    def get_image_metadata(self):
        return self.metadata