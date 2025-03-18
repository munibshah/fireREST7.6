from fireREST76.fmc import Connection
from fireREST76.fmc.audit.auditrecord import AuditRecord


class Audit:
    def __init__(self, conn: Connection):
        self.auditrecord = AuditRecord(conn)
