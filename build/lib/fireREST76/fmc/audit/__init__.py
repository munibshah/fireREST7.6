from firerest76.fmc import Connection
from firerest76.fmc.audit.auditrecord import AuditRecord


class Audit:
    def __init__(self, conn: Connection):
        self.auditrecord = AuditRecord(conn)
