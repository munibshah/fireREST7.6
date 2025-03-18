from fireREST76.fmc import Connection
from fireREST76.fmc.health.alert import Alert
from fireREST76.fmc.health.metric import Metric
from fireREST76.fmc.health.tunnelstatus import TunnelStatus
from fireREST76.fmc.health.tunnelsummary import TunnelSummary


class Health:
    def __init__(self, conn: Connection):
        self.alert = Alert(conn)
        self.metric = Metric(conn)
        self.tunnelstatus = TunnelStatus(conn)
        self.tunnelsummary = TunnelSummary(conn)
