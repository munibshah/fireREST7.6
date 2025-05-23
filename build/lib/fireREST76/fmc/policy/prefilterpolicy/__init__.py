from firerest76.defaults import API_RELEASE_650
from firerest76.fmc import Connection, Resource
from firerest76.fmc.policy.prefilterpolicy.defaultaction import DefaultAction
from firerest76.fmc.policy.prefilterpolicy.operational import Operational
from firerest76.fmc.policy.prefilterpolicy.prefilterrule import PrefilterRule


class PrefilterPolicy(Resource):
    PATH = '/policy/prefilterpolicies/{uuid}'
    IGNORE_FOR_UPDATE = ['rules']
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_650
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_650

    def __init__(self, conn: Connection):
        super().__init__(conn)

        self.accessrule = PrefilterRule(conn)
        self.defaultaction = DefaultAction(conn)
        self.operational = Operational(conn)
