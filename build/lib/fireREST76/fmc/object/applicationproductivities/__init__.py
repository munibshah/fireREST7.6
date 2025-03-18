from fireREST76.defaults import API_RELEASE_610
from fireREST76.fmc import Resource


class ApplicationProductivity(Resource):
    PATH = '/object/applicationproductivities/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
