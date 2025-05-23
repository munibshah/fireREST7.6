from firerest76.defaults import API_RELEASE_623
from firerest76.fmc import Resource


class DiscoveryInfo(Resource):
    NAMESPACE = 'tid'
    PATH = '/taxiiconfig/discoveryinfo/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_623
