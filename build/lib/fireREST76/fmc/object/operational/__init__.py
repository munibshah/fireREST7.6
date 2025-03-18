from fireREST76.fmc import Connection
from fireREST76.fmc.object.operational.usage import Usage


class Operational:
    def __init__(self, conn: Connection):
        self.usage = Usage(conn)
