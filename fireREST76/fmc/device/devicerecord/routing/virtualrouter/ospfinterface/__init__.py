from firerest76.defaults import API_RELEASE_660
from firerest76.fmc import NestedChildResource


class OspfInterface(NestedChildResource):
    CONTAINER_NAME = 'DeviceRecord'
    CONTAINER_PATH = '/devices/devicerecords/{uuid}'
    CHILD_CONTAINER_NAME = 'VirtualRouter'
    CHILD_CONTAINER_PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{uuid}'
    PATH = '/devices/devicerecords/{container_uuid}/routing/virtualrouters/{child_container_uuid}/ospfinterface/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
