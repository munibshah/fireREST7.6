from firerest76.defaults import API_RELEASE_610
from firerest76.fmc import Resource


class UrlCategory(Resource):
    PATH = '/object/urlcategories/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
