from fireREST76.fmc import Connection
from fireREST76.fmc.policy.accesspolicy import AccessPolicy
from fireREST76.fmc.policy.dnspolicy import DnsPolicy
from fireREST76.fmc.policy.dynamicaccesspolicy import DynamicAccessPolicy
from fireREST76.fmc.policy.filepolicy import FilePolicy
from fireREST76.fmc.policy.ftdnatpolicy import FtdNatPolicy
from fireREST76.fmc.policy.ftds2svpn import FtdS2sVpn
from fireREST76.fmc.policy.intrusionpolicy import IntrusionPolicy
from fireREST76.fmc.policy.networkanalysispolicy import NetworkAnalysisPolicy
from fireREST76.fmc.policy.prefilterpolicy import PrefilterPolicy
from fireREST76.fmc.policy.ravpn import RaVpn
from fireREST76.fmc.policy.snmpalert import SnmpAlert
from fireREST76.fmc.policy.syslogalert import SyslogAlert


class Policy:
    def __init__(self, conn: Connection):
        self.accesspolicy = AccessPolicy(conn)
        self.dnspolicy = DnsPolicy(conn)
        self.dynamicaccesspolicy = DynamicAccessPolicy(conn)
        self.filepolicy = FilePolicy(conn)
        self.ftdnatpolicy = FtdNatPolicy(conn)
        self.ftds2svpn = FtdS2sVpn(conn)
        self.intrusionpolicy = IntrusionPolicy(conn)
        self.networkanalysispolicy = NetworkAnalysisPolicy(conn)
        self.prefilterpolicy = PrefilterPolicy(conn)
        self.ravpn = RaVpn(conn)
        self.snmpalert = SnmpAlert(conn)
        self.syslogalert = SyslogAlert(conn)
