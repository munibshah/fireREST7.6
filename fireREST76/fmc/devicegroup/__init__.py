from fireREST76.fmc import Connection
from fireREST76.fmc.devicegroup.devicegrouprecord import DeviceGroupRecord


class DeviceGroup:
    def __init__(self, conn: Connection):
        self.devicegrouprecord = DeviceGroupRecord(conn)
