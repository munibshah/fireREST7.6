from typing import Dict, Optional

from firerest76 import utils
from firerest76.defaults import API_RELEASE_710
from firerest76.fmc import Connection, Resource
from firerest76.fmc.troubleshoot.packettracer.file import File


class PacketTracer(Resource):
    NAMESPACE = 'troubleshoot'
    PATH = '/packettracer'

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.file = File(conn)

    @utils.minimum_version_required(version=API_RELEASE_710)
    def trace(self, data: Dict, params: Optional[Dict] = None):
        url = self.url(f'{self.PATH}/traces')
        return self.conn.post(url=url, data=data, params=params)

    @utils.minimum_version_required(version=API_RELEASE_710)
    def pcap_trace(self, data: Dict, params: Optional[Dict] = None):
        url = self.url(f'{self.PATH}/pcaptraces')
        return self.conn.post(url=url, data=data, params=params)
