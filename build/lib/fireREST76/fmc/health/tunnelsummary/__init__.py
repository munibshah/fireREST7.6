from firerest76 import utils
from firerest76.defaults import API_RELEASE_710
from firerest76.fmc import Resource


class TunnelSummary(Resource):
    PATH = '/health/metrics/{uuid}'
    SUPPORTED_FILTERS = ['device_id', 'group_by', 'vpn_topology_id']
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710

    @utils.support_params
    def get(self, device_id=None, group_by=None, vpn_topology_id=None, params=None):
        return super().get(params=params)
