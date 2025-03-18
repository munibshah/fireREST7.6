from fireREST76.defaults import API_RELEASE_660, API_RELEASE_710
from fireREST76.fmc import Resource


class AsPathList(Resource):
    PATH = '/object/aspathlists/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
