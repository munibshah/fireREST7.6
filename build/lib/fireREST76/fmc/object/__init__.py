from fireREST76.fmc import Connection
from fireREST76.fmc.object.anyconnectcustomattribute import AnyconnectCustomAttribute
from fireREST76.fmc.object.anyconnectpackage import AnyconnectPackage
from fireREST76.fmc.object.anyconnectprofile import AnyconnectProfile
from fireREST76.fmc.object.anyprotocolportobject import AnyProtocolPortObject
from fireREST76.fmc.object.application import Application
from fireREST76.fmc.object.applicationcategory import ApplicationCategory
from fireREST76.fmc.object.applicationfilter import ApplicationFilter
from fireREST76.fmc.object.applicationproductivities import ApplicationProductivity
from fireREST76.fmc.object.applicationrisk import ApplicationRisk
from fireREST76.fmc.object.applicationtag import ApplicationTag
from fireREST76.fmc.object.applicationtype import ApplicationType
from fireREST76.fmc.object.aspathlist import AsPathList
from fireREST76.fmc.object.certenrollment import CertEnrollment
from fireREST76.fmc.object.certificatemap import CertificateMap
from fireREST76.fmc.object.communitylist import CommunityList
from fireREST76.fmc.object.continent import Continent
from fireREST76.fmc.object.country import Country
from fireREST76.fmc.object.dnsservergroup import DnsServerGroup
from fireREST76.fmc.object.dynamicobject import DynamicObject
from fireREST76.fmc.object.endpointdevicetype import EndpointDeviceType
from fireREST76.fmc.object.expandedcommunitylist import ExpandedCommunityList
from fireREST76.fmc.object.extendedaccesslist import ExtendedAccessList
from fireREST76.fmc.object.fqdn import Fqdn
from fireREST76.fmc.object.geolocation import GeoLocation
from fireREST76.fmc.object.globaltimezone import GlobalTimeZone
from fireREST76.fmc.object.grouppolicy import GroupPolicy
from fireREST76.fmc.object.host import Host
from fireREST76.fmc.object.hostscanpackage import HostscanPackage
from fireREST76.fmc.object.icmpv4object import Icmpv4Object
from fireREST76.fmc.object.icmpv6object import Icmpv6Object
from fireREST76.fmc.object.ikev1ipsecproposal import Ikev1IpsecProposal
from fireREST76.fmc.object.ikev1policy import Ikev1Policy
from fireREST76.fmc.object.ikev2ipsecproposal import Ikev2IpsecProposal
from fireREST76.fmc.object.ikev2policy import Ikev2Policy
from fireREST76.fmc.object.interface import Interface
from fireREST76.fmc.object.interfacegroup import InterfaceGroup
from fireREST76.fmc.object.intrusionrule import IntrusionRule
from fireREST76.fmc.object.intrusionrulegroup import IntrusionRuleGroup
from fireREST76.fmc.object.ipv4addresspool import Ipv4AddressPool
from fireREST76.fmc.object.ipv4prefixlist import Ipv4PrefixList
from fireREST76.fmc.object.ipv6addresspool import Ipv6AddressPool
from fireREST76.fmc.object.ipv6prefixlist import Ipv6PrefixList
from fireREST76.fmc.object.isesecuritygrouptag import IseSecurityGroupTag
from fireREST76.fmc.object.keychain import KeyChain
from fireREST76.fmc.object.network import Network
from fireREST76.fmc.object.networkaddress import NetworkAddress
from fireREST76.fmc.object.networkgroup import NetworkGroup
from fireREST76.fmc.object.operational import Operational
from fireREST76.fmc.object.policylist import PolicyList
from fireREST76.fmc.object.port import Port
from fireREST76.fmc.object.portobjectgroup import PortObjectGroup
from fireREST76.fmc.object.protocolportobject import ProtocolPortObject
from fireREST76.fmc.object.radiusservergroup import RadiusServerGroup
from fireREST76.fmc.object.range import Range
from fireREST76.fmc.object.realm import Realm
from fireREST76.fmc.object.realmuser import RealmUser
from fireREST76.fmc.object.realmusergroup import RealmUserGroup
from fireREST76.fmc.object.routemap import RouteMap
from fireREST76.fmc.object.securitygrouptag import SecurityGroupTag
from fireREST76.fmc.object.securityzone import SecurityZone
from fireREST76.fmc.object.sidnsfeed import SiDnsFeed
from fireREST76.fmc.object.sidnslist import SiDnsList
from fireREST76.fmc.object.sinetworkfeed import SiNetworkFeed
from fireREST76.fmc.object.sinetworklist import SiNetworkList
from fireREST76.fmc.object.sinkhole import Sinkhole
from fireREST76.fmc.object.siurlfeed import SiUrlFeed
from fireREST76.fmc.object.siurllist import SiUrlList
from fireREST76.fmc.object.slamonitor import SlaMonitor
from fireREST76.fmc.object.ssoserver import SsoServer
from fireREST76.fmc.object.standardaccesslist import StandardAccessList
from fireREST76.fmc.object.standardcommunitylist import StandardCommunityList
from fireREST76.fmc.object.timerange import Timerange
from fireREST76.fmc.object.timezone import Timezone
from fireREST76.fmc.object.tunneltag import TunnelTag
from fireREST76.fmc.object.url import Url
from fireREST76.fmc.object.urlcategory import UrlCategory
from fireREST76.fmc.object.urlgroup import UrlGroup
from fireREST76.fmc.object.variableset import VariableSet
from fireREST76.fmc.object.vlangrouptag import VlanGroupTag
from fireREST76.fmc.object.vlantag import VlanTag


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
