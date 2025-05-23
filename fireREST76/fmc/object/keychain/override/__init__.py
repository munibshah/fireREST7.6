from firerest76.defaults import API_RELEASE_640
from firerest76.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'KeyChain'
    CONTAINER_PATH = '/object/keychains/{uuid}'
    PATH = '/object/keychains/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
