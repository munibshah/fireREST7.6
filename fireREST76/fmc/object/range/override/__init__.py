from firerest76.defaults import API_RELEASE_610
from firerest76.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Range'
    CONTAINER_PATH = '/object/ranges/{uuid}'
    PATH = '/object/ranges/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
