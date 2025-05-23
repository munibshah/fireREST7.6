from firerest76.fmc import Connection
from firerest76.fmc.policy.accesspolicy import AccessPolicy
from firerest76.fmc.policy.dnspolicy import DnsPolicy
from firerest76.fmc.policy.dynamicaccesspolicy import DynamicAccessPolicy
from firerest76.fmc.policy.filepolicy import FilePolicy
from firerest76.fmc.policy.ftdnatpolicy import FtdNatPolicy
from firerest76.fmc.policy.ftds2svpn import FtdS2sVpn
from firerest76.fmc.policy.intrusionpolicy import IntrusionPolicy
from firerest76.fmc.policy.networkanalysispolicy import NetworkAnalysisPolicy
from firerest76.fmc.policy.prefilterpolicy import PrefilterPolicy
from firerest76.fmc.policy.ravpn import RaVpn
from firerest76.fmc.policy.snmpalert import SnmpAlert
from firerest76.fmc.policy.syslogalert import SyslogAlert


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
