from fireREST76.fmc import Connection
from fireREST76.fmc.troubleshoot.packettracer import PacketTracer


class Troubleshoot:
    def __init__(self, conn: Connection):
        self.packettracer = PacketTracer(conn)
