from fireREST76.defaults import API_RELEASE_610
from fireREST76.fmc import Connection, Resource
from fireREST76.fmc.device.devicerecord.bridgegroupinterface import BridgeGroupInterface
from fireREST76.fmc.device.devicerecord.etherchannelinterface import EtherChannelInterface
from fireREST76.fmc.device.devicerecord.fpinterfacestatistics import FpInterfaceStatistics
from fireREST76.fmc.device.devicerecord.fplogicalinterface import FpLogicalInterface
from fireREST76.fmc.device.devicerecord.fpphysicalinterface import FpPhysicalInterface
from fireREST76.fmc.device.devicerecord.inlineset import InlineSet
from fireREST76.fmc.device.devicerecord.interfaceevent import InterfaceEvent
from fireREST76.fmc.device.devicerecord.operational import Operational
from fireREST76.fmc.device.devicerecord.physicalinterface import PhysicalInterface
from fireREST76.fmc.device.devicerecord.redundantinterface import RedundantInterface
from fireREST76.fmc.device.devicerecord.routing import Routing
from fireREST76.fmc.device.devicerecord.subinterface import SubInterface
from fireREST76.fmc.device.devicerecord.virtualswitch import VirtualSwitch
from fireREST76.fmc.device.devicerecord.virtualtunnelinterface import VirtualTunnelInterface
from fireREST76.fmc.device.devicerecord.vlaninterface import VlanInterface


class DeviceRecord(Resource):
    PATH = '/devices/devicerecords/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610
    SUPPORTED_PARAMS = ['hostname']

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.bridgegroupinterface = BridgeGroupInterface(conn)
        self.etherchannelinterface = EtherChannelInterface(conn)
        self.fpinterfacestatistics = FpInterfaceStatistics(conn)
        self.fplogicalinterface = FpLogicalInterface(conn)
        self.fpphysicalinterface = FpPhysicalInterface(conn)
        self.inlineset = InlineSet(conn)
        self.interfaceevent = InterfaceEvent(conn)
        self.operational = Operational(conn)
        self.physicalinterface = PhysicalInterface(conn)
        self.redundantinterface = RedundantInterface(conn)
        self.routing = Routing(conn)
        self.subinterface = SubInterface(conn)
        self.virtualswitch = VirtualSwitch(conn)
        self.virtualtunnelinterface = VirtualTunnelInterface(conn)
        self.vlaninterface = VlanInterface(conn)
