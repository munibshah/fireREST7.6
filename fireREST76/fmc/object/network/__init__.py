from firerest76 import utils
from firerest76.defaults import API_RELEASE_610
from firerest76.fmc import Connection, Resource
from firerest76.fmc.object.network.override import Override


class Network(Resource):
    PATH = '/object/networks/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610
    SUPPORTED_FILTERS = ['name_or_value', 'unused_only']
    SUPPORTED_PARAMS = ['override_target_id']

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)

    @utils.support_params
    def get(self, uuid=None, name=None, name_or_value=None, unused_only=None, override_target_id=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
