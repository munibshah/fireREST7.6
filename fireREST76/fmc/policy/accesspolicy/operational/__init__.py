from firerest76.fmc import Connection
from firerest76.fmc.policy.accesspolicy.operational.hitcounts import Hitcount


class Operational:
    def __init__(self, conn: Connection):
        self.hitcount = Hitcount(conn)
