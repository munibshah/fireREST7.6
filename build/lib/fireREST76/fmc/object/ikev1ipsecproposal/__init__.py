from firerest76.defaults import API_RELEASE_630
from firerest76.fmc import Resource


class Ikev1IpsecProposal(Resource):
    PATH = '/object/ikev1ipsecproposals/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_630
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_630
