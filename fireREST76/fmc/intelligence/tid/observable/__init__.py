from firerest76.defaults import API_RELEASE_623
from firerest76.fmc import Resource


class Observable(Resource):
    NAMESPACE = 'tid'
    PATH = '/tid/observable/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_623
