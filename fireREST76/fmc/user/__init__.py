from fireREST76.fmc import Connection
from fireREST76.fmc.user.authrole import AuthRole
from fireREST76.fmc.user.duoconfig import DuoConfig
from fireREST76.fmc.user.ssoconfig import SsoConfig


class User:
    def __init__(self, conn: Connection):
        self.authrole = AuthRole(conn)
        self.duoconfig = DuoConfig(conn)
        self.ssoconfig = SsoConfig(conn)
