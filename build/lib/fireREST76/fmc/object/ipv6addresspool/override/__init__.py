from firerest76.defaults import API_RELEASE_700
from firerest76.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Ipv6AddressPool'
    CONTAINER_PATH = '/object/ipv6addresspools/{uuid}'
    PATH = '/object/ipv6addresspools/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
