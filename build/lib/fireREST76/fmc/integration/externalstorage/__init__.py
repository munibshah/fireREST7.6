from firerest76.defaults import API_RELEASE_670
from firerest76.fmc import Resource


class ExternalStorage(Resource):
    PATH = '/integration/externalstorage/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_670
