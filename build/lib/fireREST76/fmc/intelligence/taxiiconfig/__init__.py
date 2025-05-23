from firerest76.fmc import Connection
from firerest76.fmc.intelligence.taxiiconfig.collection import Collection
from firerest76.fmc.intelligence.taxiiconfig.discoveryinfo import DiscoveryInfo


class TaxiiConfig:
    def __init__(self, conn: Connection):
        self.collection = Collection(conn)
        self.discoveryinfo = DiscoveryInfo(conn)
