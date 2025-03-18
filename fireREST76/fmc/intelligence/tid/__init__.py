from fireREST76.fmc import Connection
from fireREST76.fmc.intelligence.tid.element import Element
from fireREST76.fmc.intelligence.tid.incident import Incident
from fireREST76.fmc.intelligence.tid.indicator import Indicator
from fireREST76.fmc.intelligence.tid.observable import Observable
from fireREST76.fmc.intelligence.tid.setting import Setting
from fireREST76.fmc.intelligence.tid.source import Source


class Tid:
    def __init__(self, conn: Connection):
        self.element = Element(conn)
        self.incident = Incident(conn)
        self.indicator = Indicator(conn)
        self.observable = Observable(conn)
        self.setting = Setting(conn)
        self.source = Source(conn)
