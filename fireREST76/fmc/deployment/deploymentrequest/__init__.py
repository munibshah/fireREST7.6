from firerest76.defaults import API_RELEASE_610
from firerest76.fmc import Resource


class DeploymentRequest(Resource):
    PATH = '/deployment/deploymentrequests/{uuid}'
    MINIMUM_VERSION_REQUIRED_CREATE = API_RELEASE_610
