from firerest76.defaults import API_RELEASE_700
from firerest76.fmc import ChildResource


class BlockDnsRule(ChildResource):
    CONTAINER_NAME = 'DnsPolicy'
    CONTAINER_PATH = '/policy/dnspolicies/{uuid}'
    PATH = '/policy/dnspolicies/{container_uuid}/blockdnsrule/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
