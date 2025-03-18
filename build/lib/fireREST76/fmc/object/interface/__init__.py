from fireREST76.defaults import API_RELEASE_630
from fireREST76.fmc import Resource


class Interface(Resource):
    PATH = '/object/interfaceobjects/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
