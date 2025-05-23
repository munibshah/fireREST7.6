from firerest76.fmc import Connection
from firerest76.fmc.deployment.deployabledevice import DeployableDevice
from firerest76.fmc.deployment.deploymentrequest import DeploymentRequest
from firerest76.fmc.deployment.jobhistory import JobHistory
from firerest76.fmc.deployment.rollbackrequest import RollbackRequest


class Deployment:
    def __init__(self, conn: Connection):
        self.deployabledevices = DeployableDevice(conn)
        self.deploymentrequest = DeploymentRequest(conn)
        self.jobhistory = JobHistory(conn)
        self.rollbackrequest = RollbackRequest(conn)
