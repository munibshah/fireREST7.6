from firerest76.fmc import Connection
from firerest76.fmc.intelligence.taxiiconfig import TaxiiConfig
from firerest76.fmc.intelligence.tid import Tid


class Intelligence:
    def __init__(self, conn: Connection):
        self.taxiiconfig = TaxiiConfig(conn)
        self.tid = Tid(conn)
