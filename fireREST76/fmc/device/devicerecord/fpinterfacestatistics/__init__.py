from firerest76.defaults import API_RELEASE_610
from firerest76.fmc import ChildResource


class FpInterfaceStatistics(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/fpinterfacestatistics/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
