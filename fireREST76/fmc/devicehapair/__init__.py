from firerest76.fmc import Connection
from firerest76.fmc.devicehapair.ftddevicehapair import FtdHAPair


class DeviceHAPair:
    def __init__(self, conn: Connection):
        self.ftdhapair = FtdHAPair(conn)
