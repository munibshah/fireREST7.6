from firerest76.fmc import Connection
from firerest76.fmc.system.info.domain import Domain
from firerest76.fmc.system.info.serverversion import ServerVersion


class Info:
    def __init__(self, conn: Connection):
        self.domain = Domain(conn)
        self.serverversion = ServerVersion(conn)
