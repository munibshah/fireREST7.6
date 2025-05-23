from firerest76.fmc import Connection
from firerest76.fmc.object.anyconnectcustomattribute import AnyconnectCustomAttribute
from firerest76.fmc.object.anyconnectpackage import AnyconnectPackage
from firerest76.fmc.object.anyconnectprofile import AnyconnectProfile
from firerest76.fmc.object.anyprotocolportobject import AnyProtocolPortObject
from firerest76.fmc.object.application import Application
from firerest76.fmc.object.applicationcategory import ApplicationCategory
from firerest76.fmc.object.applicationfilter import ApplicationFilter
from firerest76.fmc.object.applicationproductivities import ApplicationProductivity
from firerest76.fmc.object.applicationrisk import ApplicationRisk
from firerest76.fmc.object.applicationtag import ApplicationTag
from firerest76.fmc.object.applicationtype import ApplicationType
from firerest76.fmc.object.aspathlist import AsPathList
from firerest76.fmc.object.certenrollment import CertEnrollment
from firerest76.fmc.object.certificatemap import CertificateMap
from firerest76.fmc.object.communitylist import CommunityList
from firerest76.fmc.object.continent import Continent
from firerest76.fmc.object.country import Country
from firerest76.fmc.object.dnsservergroup import DnsServerGroup
from firerest76.fmc.object.dynamicobject import DynamicObject
from firerest76.fmc.object.endpointdevicetype import EndpointDeviceType
from firerest76.fmc.object.expandedcommunitylist import ExpandedCommunityList
from firerest76.fmc.object.extendedaccesslist import ExtendedAccessList
from firerest76.fmc.object.fqdn import Fqdn
from firerest76.fmc.object.geolocation import GeoLocation
from firerest76.fmc.object.globaltimezone import GlobalTimeZone
from firerest76.fmc.object.grouppolicy import GroupPolicy
from firerest76.fmc.object.host import Host
from firerest76.fmc.object.hostscanpackage import HostscanPackage
from firerest76.fmc.object.icmpv4object import Icmpv4Object
from firerest76.fmc.object.icmpv6object import Icmpv6Object
from firerest76.fmc.object.ikev1ipsecproposal import Ikev1IpsecProposal
from firerest76.fmc.object.ikev1policy import Ikev1Policy
from firerest76.fmc.object.ikev2ipsecproposal import Ikev2IpsecProposal
from firerest76.fmc.object.ikev2policy import Ikev2Policy
from firerest76.fmc.object.interface import Interface
from firerest76.fmc.object.interfacegroup import InterfaceGroup
from firerest76.fmc.object.intrusionrule import IntrusionRule
from firerest76.fmc.object.intrusionrulegroup import IntrusionRuleGroup
from firerest76.fmc.object.ipv4addresspool import Ipv4AddressPool
from firerest76.fmc.object.ipv4prefixlist import Ipv4PrefixList
from firerest76.fmc.object.ipv6addresspool import Ipv6AddressPool
from firerest76.fmc.object.ipv6prefixlist import Ipv6PrefixList
from firerest76.fmc.object.isesecuritygrouptag import IseSecurityGroupTag
from firerest76.fmc.object.keychain import KeyChain
from firerest76.fmc.object.network import Network
from firerest76.fmc.object.networkaddress import NetworkAddress
from firerest76.fmc.object.networkgroup import NetworkGroup
from firerest76.fmc.object.operational import Operational
from firerest76.fmc.object.policylist import PolicyList
from firerest76.fmc.object.port import Port
from firerest76.fmc.object.portobjectgroup import PortObjectGroup
from firerest76.fmc.object.protocolportobject import ProtocolPortObject
from firerest76.fmc.object.radiusservergroup import RadiusServerGroup
from firerest76.fmc.object.range import Range
from firerest76.fmc.object.realm import Realm
from firerest76.fmc.object.realmuser import RealmUser
from firerest76.fmc.object.realmusergroup import RealmUserGroup
from firerest76.fmc.object.routemap import RouteMap
from firerest76.fmc.object.securitygrouptag import SecurityGroupTag
from firerest76.fmc.object.securityzone import SecurityZone
from firerest76.fmc.object.sidnsfeed import SiDnsFeed
from firerest76.fmc.object.sidnslist import SiDnsList
from firerest76.fmc.object.sinetworkfeed import SiNetworkFeed
from firerest76.fmc.object.sinetworklist import SiNetworkList
from firerest76.fmc.object.sinkhole import Sinkhole
from firerest76.fmc.object.siurlfeed import SiUrlFeed
from firerest76.fmc.object.siurllist import SiUrlList
from firerest76.fmc.object.slamonitor import SlaMonitor
from firerest76.fmc.object.ssoserver import SsoServer
from firerest76.fmc.object.standardaccesslist import StandardAccessList
from firerest76.fmc.object.standardcommunitylist import StandardCommunityList
from firerest76.fmc.object.timerange import Timerange
from firerest76.fmc.object.timezone import Timezone
from firerest76.fmc.object.tunneltag import TunnelTag
from firerest76.fmc.object.url import Url
from firerest76.fmc.object.urlcategory import UrlCategory
from firerest76.fmc.object.urlgroup import UrlGroup
from firerest76.fmc.object.variableset import VariableSet
from firerest76.fmc.object.vlangrouptag import VlanGroupTag
from firerest76.fmc.object.vlantag import VlanTag


class Object:
    def __init__(self, conn: Connection):
        self.anyprotocolportobject = AnyProtocolPortObject(conn)
        self.anyconnectcustomattribute = AnyconnectCustomAttribute(conn)
        self.anyconnectpackage = AnyconnectPackage(conn)
        self.anyconnectprofile = AnyconnectProfile(conn)
        self.application = Application(conn)
        self.applicationcategory = ApplicationCategory(conn)
        self.applicationfilter = ApplicationFilter(conn)
        self.applicationproductivities = ApplicationProductivity(conn)
        self.applicationrisk = ApplicationRisk(conn)
        self.applicationtag = ApplicationTag(conn)
        self.applicationtype = ApplicationType(conn)
        self.aspathlist = AsPathList(conn)
        self.certenrollment = CertEnrollment(conn)
        self.certificatemap = CertificateMap(conn)
        self.communitylist = CommunityList(conn)
        self.continent = Continent(conn)
        self.country = Country(conn)
        self.dnsservergroup = DnsServerGroup(conn)
        self.dynamicobject = DynamicObject(conn)
        self.endpointdevicetype = EndpointDeviceType(conn)
        self.expandedcommunitylist = ExpandedCommunityList(conn)
        self.extendedaccesslist = ExtendedAccessList(conn)
        self.fqdn = Fqdn(conn)
        self.geolocation = GeoLocation(conn)
        self.globaltimezone = GlobalTimeZone(conn)
        self.grouppolicy = GroupPolicy(conn)
        self.host = Host(conn)
        self.hostscanpackage = HostscanPackage(conn)
        self.icmpv4object = Icmpv4Object(conn)
        self.icmpv6object = Icmpv6Object(conn)
        self.ikev1ipsecproposal = Ikev1IpsecProposal(conn)
        self.ikev1policy = Ikev1Policy(conn)
        self.ikev2ipsecproposal = Ikev2IpsecProposal(conn)
        self.ikev2policy = Ikev2Policy(conn)
        self.interface = Interface(conn)
        self.interfacegroup = InterfaceGroup(conn)
        self.intrusionrule = IntrusionRule(conn)
        self.intrusionrulegroup = IntrusionRuleGroup(conn)
        self.ipv4addresspool = Ipv4AddressPool(conn)
        self.ipv4prefixlist = Ipv4PrefixList(conn)
        self.ipv6addresspool = Ipv6AddressPool(conn)
        self.ipv6prefixlist = Ipv6PrefixList(conn)
        self.isesecuritygrouptag = IseSecurityGroupTag(conn)
        self.keychain = KeyChain(conn)
        self.network = Network(conn)
        self.networkaddress = NetworkAddress(conn)
        self.networkgroup = NetworkGroup(conn)
        self.operational = Operational(conn)
        self.policylist = PolicyList(conn)
        self.port = Port(conn)
        self.portobjectgroup = PortObjectGroup(conn)
        self.protocolportobject = ProtocolPortObject(conn)
        self.radiusservergroup = RadiusServerGroup(conn)
        self.range = Range(conn)
        self.realm = Realm(conn)
        self.realmuser = RealmUser(conn)
        self.realmusergroup = RealmUserGroup(conn)
        self.routemap = RouteMap(conn)
        self.securitygrouptag = SecurityGroupTag(conn)
        self.securityzone = SecurityZone(conn)
        self.sidnsfeed = SiDnsFeed(conn)
        self.sidnslist = SiDnsList(conn)
        self.sinetworkfeed = SiNetworkFeed(conn)
        self.sinetworklist = SiNetworkList(conn)
        self.sinkhole = Sinkhole(conn)
        self.siurlfeed = SiUrlFeed(conn)
        self.siurllist = SiUrlList(conn)
        self.slamonitor = SlaMonitor(conn)
        self.ssoserver = SsoServer(conn)
        self.standardaccesslist = StandardAccessList(conn)
        self.standardcommunitylist = StandardCommunityList(conn)
        self.timerange = Timerange(conn)
        self.timezone = Timezone(conn)
        self.tunneltag = TunnelTag(conn)
        self.url = Url(conn)
        self.urlcategory = UrlCategory(conn)
        self.urlgroup = UrlGroup(conn)
        self.variableset = VariableSet(conn)
        self.vlangrouptag = VlanGroupTag(conn)
        self.vlantag = VlanTag(conn)
