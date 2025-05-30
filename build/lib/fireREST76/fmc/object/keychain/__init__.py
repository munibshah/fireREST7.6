from firerest76.defaults import API_RELEASE_640
from firerest76.fmc import Resource, Connection
from firerest76.fmc.object.keychain.override import Override


class KeyChain(Resource):
    PATH = '/object/keychains/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_640
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_640

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.override = Override(conn)
