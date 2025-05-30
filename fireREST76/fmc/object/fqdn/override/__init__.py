from firerest76.defaults import API_RELEASE_630
from firerest76.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Fqdn'
    CONTAINER_PATH = '/object/fqdns/{uuid}'
    PATH = '/object/fqdns/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_630
