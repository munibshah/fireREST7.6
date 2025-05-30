from firerest76.defaults import API_RELEASE_610, API_RELEASE_670
from firerest76.fmc import Connection, Resource
from firerest76.fmc.policy.intrusionpolicy.intrusionrule import IntrusionRule
from firerest76.fmc.policy.intrusionpolicy.intrusionrulegroup import IntrusionRuleGroup


class IntrusionPolicy(Resource):
    PATH = '/policy/intrusionpolicies/{uuid}'
    IGNORE_FOR_UPDATE = ['rules']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_670
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_670

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.intrusionrule = IntrusionRule(conn)
        self.intrusionrulegroup = IntrusionRuleGroup(conn)
