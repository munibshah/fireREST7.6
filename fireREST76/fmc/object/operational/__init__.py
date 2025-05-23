from firerest76.fmc import Connection
from firerest76.fmc.object.operational.usage import Usage


class Operational:
    def __init__(self, conn: Connection):
        self.usage = Usage(conn)
