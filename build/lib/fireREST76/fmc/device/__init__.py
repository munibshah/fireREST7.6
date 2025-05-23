from typing import Dict

from firerest76 import utils
from firerest76.defaults import API_RELEASE_630
from firerest76.fmc import Connection, Resource
from firerest76.fmc.device.devicerecord import DeviceRecord


class Device(Resource):
    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.devicerecord = DeviceRecord(conn)

    @utils.minimum_version_required(version=API_RELEASE_630)
    def copyconfigrequest(self, data: Dict):
        url = self.url(path='/devices/copyconfigrequests')
        return self.conn.post(url=url, data=data)
