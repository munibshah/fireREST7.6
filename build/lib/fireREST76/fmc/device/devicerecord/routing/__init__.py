from fireREST76.fmc import Connection
from fireREST76.fmc.device.devicerecord.routing.bgp import Bgp
from fireREST76.fmc.device.devicerecord.routing.bgpgeneralsettings import BgpGeneralSettings
from fireREST76.fmc.device.devicerecord.routing.ipv4staticroute import Ipv4StaticRoute
from fireREST76.fmc.device.devicerecord.routing.ipv6staticroute import Ipv6StaticRoute
from fireREST76.fmc.device.devicerecord.routing.ospfinterface import OspfInterface
from fireREST76.fmc.device.devicerecord.routing.ospfv2route import Ospfv2Route
from fireREST76.fmc.device.devicerecord.routing.ospfv3interface import Ospfv3Interface
from fireREST76.fmc.device.devicerecord.routing.policybasedroute import PolicyBasedRoute
from fireREST76.fmc.device.devicerecord.routing.staticroute import StaticRoute
from fireREST76.fmc.device.devicerecord.routing.virtualrouter import VirtualRouter


class Routing:
    def __init__(self, conn: Connection):
        self.bgp = Bgp(conn)
        self.bgpgeneralsettings = BgpGeneralSettings(conn)
        self.ipv4staticroute = Ipv4StaticRoute(conn)
        self.ipv6staticroute = Ipv6StaticRoute(conn)
        self.ospfinterface = OspfInterface(conn)
        self.ospfv2route = Ospfv2Route(conn)
        self.ospfv3interface = Ospfv3Interface(conn)
        self.policybasedroute = PolicyBasedRoute(conn)
        self.staticroute = StaticRoute(conn)
        self.virtualrouter = VirtualRouter(conn)
