from fireREST76.fmc import Connection
from fireREST76.fmc.deployment.deployabledevice import DeployableDevice
from fireREST76.fmc.deployment.deploymentrequest import DeploymentRequest
from fireREST76.fmc.deployment.jobhistory import JobHistory
from fireREST76.fmc.deployment.rollbackrequest import RollbackRequest


class Deployment:
    def __init__(self, conn: Connection):
        self.deployabledevices = DeployableDevice(conn)
        self.deploymentrequest = DeploymentRequest(conn)
        self.jobhistory = JobHistory(conn)
        self.rollbackrequest = RollbackRequest(conn)
