from firerest76.defaults import API_RELEASE_710
from firerest76.fmc import Resource


class DuoConfig(Resource):
    PATH = '/users/duoconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
