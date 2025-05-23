from firerest76.defaults import API_RELEASE_610
from firerest76.fmc import Connection, Resource
from firerest76.fmc.device.devicerecord.bridgegroupinterface import BridgeGroupInterface
from firerest76.fmc.device.devicerecord.etherchannelinterface import EtherChannelInterface
from firerest76.fmc.device.devicerecord.fpinterfacestatistics import FpInterfaceStatistics
from firerest76.fmc.device.devicerecord.fplogicalinterface import FpLogicalInterface
from firerest76.fmc.device.devicerecord.fpphysicalinterface import FpPhysicalInterface
from firerest76.fmc.device.devicerecord.inlineset import InlineSet
from firerest76.fmc.device.devicerecord.interfaceevent import InterfaceEvent
from firerest76.fmc.device.devicerecord.operational import Operational
from firerest76.fmc.device.devicerecord.physicalinterface import PhysicalInterface
from firerest76.fmc.device.devicerecord.redundantinterface import RedundantInterface
from firerest76.fmc.device.devicerecord.routing import Routing
from firerest76.fmc.device.devicerecord.subinterface import SubInterface
from firerest76.fmc.device.devicerecord.virtualswitch import VirtualSwitch
from firerest76.fmc.device.devicerecord.virtualtunnelinterface import VirtualTunnelInterface
from firerest76.fmc.device.devicerecord.vlaninterface import VlanInterface


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
