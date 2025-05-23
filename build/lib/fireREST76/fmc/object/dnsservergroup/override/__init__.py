from firerest76.defaults import API_RELEASE_700
from firerest76.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'DnsServerGroup'
    CONTAINER_PATH = '/object/dnsservergroups/{uuid}'
    PATH = '/object/dnsservergroups/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
