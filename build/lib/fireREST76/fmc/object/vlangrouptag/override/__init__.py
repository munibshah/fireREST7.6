from firerest76.defaults import API_RELEASE_610
from firerest76.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'VlanGroupTag'
    CONTAINER_PATH = '/object/vlangrouptags/{uuid}'
    PATH = '/object/vlangrouptags/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
