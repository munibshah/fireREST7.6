from firerest76.defaults import API_RELEASE_660
from firerest76.fmc import ChildResource


class OspfInterface(ChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/ospfinterface/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
