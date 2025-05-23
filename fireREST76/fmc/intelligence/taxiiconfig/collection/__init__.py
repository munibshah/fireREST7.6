from firerest76.defaults import API_RELEASE_623
from firerest76.fmc import Resource


class Collection(Resource):
    NAMESPACE = 'tid'
    PATH = '/taxiiconfig/collections/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_623
