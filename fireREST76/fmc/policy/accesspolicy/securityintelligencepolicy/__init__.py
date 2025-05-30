from firerest76.defaults import API_RELEASE_700
from firerest76.fmc import ChildResource


class SecurityIntelligencePolicy(ChildResource):
    CONTAINER_NAME = 'AccessPolicy'
    CONTAINER_PATH = '/policy/accesspolicies/{uuid}'
    PATH = '/policy/accesspolicies/{container_uuid}/securityintelligencepolicies/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_700
