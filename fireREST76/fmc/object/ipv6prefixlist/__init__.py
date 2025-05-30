from firerest76.defaults import API_RELEASE_660, API_RELEASE_710
from firerest76.fmc import Resource


class Ipv6PrefixList(Resource):
    PATH = '/object/ipv6prefixlists/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
