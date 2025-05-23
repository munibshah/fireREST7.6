from firerest76.defaults import API_RELEASE_610
from firerest76.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Url'
    CONTAINER_PATH = '/object/urls/{uuid}'
    PATH = '/object/urls/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
