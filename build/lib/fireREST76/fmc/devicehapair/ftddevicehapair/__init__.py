from firerest76.defaults import API_RELEASE_623
from firerest76.fmc import Connection, Resource
from firerest76.fmc.devicehapair.ftddevicehapair.failoverinterfacemacaddressconfig import (
    FailoverInterfaceMacAddressConfig,
)
from firerest76.fmc.devicehapair.ftddevicehapair.monitoredinterface import MonitoredInterface


class FtdHAPair(Resource):
    PATH = '/devicehapairs/ftddevicehapairs/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_623
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_623
    SUPPORTED_PARAMS = ['name']

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.failoverinterfacemacaddressconfig = FailoverInterfaceMacAddressConfig(conn)
        self.monitoredinterface = MonitoredInterface(conn)
