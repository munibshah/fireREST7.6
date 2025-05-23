from firerest76.defaults import API_RELEASE_700
from firerest76.fmc import Resource


class FmcHaStatus(Resource):
    PATH = '/integration/fmchastatuses/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
