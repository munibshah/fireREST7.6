from fireREST76.defaults import API_RELEASE_670
from fireREST76.fmc import Resource


class RollbackRequest(Resource):
    PATH = '/deployment/rollbackrequests/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_670
