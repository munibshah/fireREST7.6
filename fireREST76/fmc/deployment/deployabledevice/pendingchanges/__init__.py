from firerest76.defaults import API_RELEASE_660
from firerest76.fmc import ChildResource


class PendingChanges(ChildResource):
    CONTAINER_NAME = 'DeployableDevice'
    CONTAINER_PATH = '/deployment/deployabledevices/{uuid}'
    PATH = '/deployment/deployabledevices/{container_uuid}/pendingchanges'
    SUPPORTED_FILTERS = ['parent_entity_types', 'parent_uuid']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
