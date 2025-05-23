from firerest76.fmc import Connection
from firerest76.fmc.assignment.policyassignment import PolicyAssignment


class Assignment:
    def __init__(self, conn: Connection):
        self.policyassignment = PolicyAssignment(conn)
