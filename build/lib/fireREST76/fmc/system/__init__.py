from fireREST76.fmc import Connection
from fireREST76.fmc.system.info import Info


class System:
    def __init__(self, conn: Connection):
        self.info = Info(conn)
