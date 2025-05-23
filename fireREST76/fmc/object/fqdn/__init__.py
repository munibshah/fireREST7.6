from firerest76.defaults import API_RELEASE_630
from firerest76.fmc import Resource, Connection
from firerest76.fmc.object.fqdn.override import Override


class Fqdn(Resource):
    PATH = '/object/fqdns/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)
