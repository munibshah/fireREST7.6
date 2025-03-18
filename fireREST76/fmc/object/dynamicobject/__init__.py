from fireREST76.defaults import API_RELEASE_700
from fireREST76.fmc import Resource, Connection
from fireREST76.fmc.object.dynamicobject.mapping import Mapping


class DynamicObject(Resource):
    PATH = '/object/dynamicobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_700

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.mapping = Mapping(conn)
