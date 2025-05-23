from firerest76.defaults import API_RELEASE_700
from firerest76.fmc import ChildResource


class InspectorOverrideConfig(ChildResource):
    CONTAINER_NAME = 'NetworkAnalysisPolicy'
    CONTAINER_PATH = '/policy/networkanalysispolicies/{uuid}'
    PATH = '/policy/networkanalysispolicies/{container_uuid}/inspectoroverrideconfigs/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
    MINIMUM_VERSION_REQUIRED_UPDATE = API_RELEASE_700
