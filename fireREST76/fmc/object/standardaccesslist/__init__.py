from fireREST76.defaults import API_RELEASE_660
from fireREST76.fmc import Resource


class StandardAccessList(Resource):
    PATH = '/object/standardaccesslists/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
