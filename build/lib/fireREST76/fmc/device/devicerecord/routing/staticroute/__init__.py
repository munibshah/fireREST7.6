from firerest76.defaults import API_RELEASE_623
from firerest76.fmc import ChildResource


class StaticRoute(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/staticroutes/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_623
