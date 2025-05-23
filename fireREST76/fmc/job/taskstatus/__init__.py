from firerest76.defaults import API_RELEASE_610
from firerest76.exceptions import UnsupportedOperationError
from firerest76.fmc import Resource


class TaskStatus(Resource):
    PATH = '/job/taskstatuses/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610

    def get(self, uuid=None, name=None, params=None):
        if not uuid:
            raise UnsupportedOperationError(msg='TaskStatus only supports GETBYID operations. UUID must be specified.')
        return super().get(uuid, params=params)
