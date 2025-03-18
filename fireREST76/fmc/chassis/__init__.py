from fireREST76.fmc import Connection, Resource
from fireREST76.defaults import API_RELEASE_710
from fireREST76.fmc.chassis.interface import Interface
from fireREST76.fmc.chassis.networkmodule import NetworkModule
from fireREST76.fmc.chassis.operational import Operational


class Chassis(Resource):
    PATH = '/chassis/fmcmanagedchassis/{uuid}'
    MINIMUM_VERSION_REQUIRED_GET = API_RELEASE_710

    def __init__(self, conn: Connection):
        super().__init__(conn)
        self.interface = Interface(conn)
        self.networkmodule = NetworkModule(conn)
        self.operational = Operational(conn)
