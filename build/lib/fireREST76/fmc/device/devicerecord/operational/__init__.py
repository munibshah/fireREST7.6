from firerest76.fmc import Connection
from firerest76.fmc.device.devicerecord.operational.command import Command
from firerest76.fmc.device.devicerecord.operational.metric import Metric


class Operational:
    def __init__(self, conn: Connection):
        self.command = Command(conn)
        self.metric = Metric(conn)
