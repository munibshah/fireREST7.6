from firerest76.defaults import API_RELEASE_660
from firerest76.fmc import ChildResource


class Deployment(ChildResource):
    CONTAINER_NAME = 'DeployableDevice'
    CONTAINER_PATH = '/deployment/deployabledevices/{uuid}'
    PATH = '/deployment/deployabledevices/{container_uuid}/deployments'
    SUPPORTED_FILTERS = ['start_time', 'end_time']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_660
