from fireREST76.defaults import API_RELEASE_610
from fireREST76.fmc import Connection, Resource
from fireREST76.fmc.deployment.deployabledevice.deployment import Deployment
from fireREST76.fmc.deployment.deployabledevice.pendingchanges import PendingChanges


class DeployableDevice(Resource):
    PATH = '/deployment/deployabledevices/{uuid}'
    SUPPORTED_PARAMS = ['group_dependency']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610

    def __init__(self, conn: Connection):
        self.deployment = Deployment(conn)
        self.pendingchanges = PendingChanges(conn)
        super().__init__(conn)
