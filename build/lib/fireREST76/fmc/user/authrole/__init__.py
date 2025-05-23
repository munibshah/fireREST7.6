from firerest76.defaults import API_RELEASE_670
from firerest76.fmc import Resource


class AuthRole(Resource):
    PATH = '/users/authroles/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670
