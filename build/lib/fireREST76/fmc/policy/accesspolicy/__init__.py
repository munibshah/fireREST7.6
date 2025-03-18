from fireREST76 import utils
from fireREST76.defaults import API_RELEASE_610
from fireREST76.fmc import Connection, Resource
from fireREST76.fmc.policy.accesspolicy.accessrule import AccessRule
from fireREST76.fmc.policy.accesspolicy.category import Category
from fireREST76.fmc.policy.accesspolicy.defaultaction import DefaultAction
from fireREST76.fmc.policy.accesspolicy.inheritancesettings import InheritanceSettings
from fireREST76.fmc.policy.accesspolicy.operational import Operational
from fireREST76.fmc.policy.accesspolicy.securityintelligencepolicy import SecurityIntelligencePolicy


class AccessPolicy(Resource):
    PATH = '/policy/accesspolicies/{uuid}'
    IGNORE_FOR_UPDATE = ['rules']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_610
    SUPPORTED_PARAMS = ['name']

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.accessrule = AccessRule(conn)
        self.category = Category(conn)
        self.defaultaction = DefaultAction(conn)
        self.inheritancesettings = InheritanceSettings(conn)
        self.operational = Operational(conn)
        self.securityintelligencepolicy = SecurityIntelligencePolicy(conn)

    @utils.support_params
    def get(self, uuid=None, name=None, params=None):
        return super().get(uuid=uuid, name=name, params=params)
