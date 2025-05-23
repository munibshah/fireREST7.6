from firerest76.defaults import API_RELEASE_710
from firerest76.fmc import ChildResource


class PolicyBasedRoute(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/policybasedroutes/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_710
    MINIMUM_VERSION_REQUIRED_DELETE = API_RELEASE_710
