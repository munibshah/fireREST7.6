from firerest76.defaults import API_RELEASE_610
from firerest76.fmc import ChildResource


class Override(ChildResource):
    CONTAINER_NAME = 'Icmpv6Object'
    CONTAINER_PATH = '/object/icmpv6objects/{uuid}'
    PATH = '/object/icmpv6objects/{container_uuid}/overrides/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
