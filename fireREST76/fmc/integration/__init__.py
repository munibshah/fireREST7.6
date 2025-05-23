from firerest76.fmc import Connection
from firerest76.fmc.integration.cloudeventsconfig import CloudEventsConfig
from firerest76.fmc.integration.cloudregion import CloudRegion
from firerest76.fmc.integration.externallookup import ExternalLookup
from firerest76.fmc.integration.externalstorage import ExternalStorage
from firerest76.fmc.integration.fmchastatus import FmcHaStatus
from firerest76.fmc.integration.securexconfig import SecurexConfig


class Integration:
    def __init__(self, conn: Connection):
        self.cloudeventsconfig = CloudEventsConfig(conn)
        self.cloudregion = CloudRegion(conn)
        self.externallookup = ExternalLookup(conn)
        self.externalstorage = ExternalStorage(conn)
        self.fmchastatus = FmcHaStatus(conn)
        self.securexconfig = SecurexConfig(conn)
