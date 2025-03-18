from fireREST76.defaults import API_RELEASE_610
from fireREST76.fmc import Resource


class AuditRecord(Resource):
    NAMESPACE = 'platform_with_domain'
    PATH = '/audit/auditrecords/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_610
