from firerest76.fmc import Connection
from firerest76.fmc.netmap.host import Host
from firerest76.fmc.netmap.vulnerability import Vulnerability


class NetMap:
    def __init__(self, conn: Connection):
        self.host = Host(conn)
        self.vulnerability = Vulnerability(conn)
