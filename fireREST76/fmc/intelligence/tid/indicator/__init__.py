from firerest76.defaults import API_RELEASE_623
from firerest76.fmc import Resource


class Indicator(Resource):
    NAMESPACE = 'tid'
    PATH = '/tid/indicator/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_623
