from firerest76.defaults import API_RELEASE_610
from firerest76.fmc import Resource


class IseSecurityGroupTag(Resource):
    PATH = '/object/isesecuritygrouptags/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
