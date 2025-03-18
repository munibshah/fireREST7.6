# -*- coding: utf-8 -*-

import logging
from typing import Optional

from fireREST76 import defaults
from fireREST76.fmc import Connection
from fireREST76.fmc.assignment import Assignment
from fireREST76.fmc.audit import Audit
from fireREST76.fmc.chassis import Chassis
from fireREST76.fmc.deployment import Deployment
from fireREST76.fmc.device import Device
from fireREST76.fmc.devicecluster import DeviceCluster
from fireREST76.fmc.devicegroup import DeviceGroup
from fireREST76.fmc.devicehapair import DeviceHAPair
from fireREST76.fmc.health import Health
from fireREST76.fmc.integration import Integration
from fireREST76.fmc.intelligence import Intelligence
from fireREST76.fmc.job import Job
from fireREST76.fmc.netmap import NetMap
from fireREST76.fmc.object import Object
from fireREST76.fmc.policy import Policy
from fireREST76.fmc.system import System
from fireREST76.fmc.troubleshoot import Troubleshoot
from fireREST76.fmc.update import Update
from fireREST76.fmc.user import User

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class FMC:
    def __init__(
        self,
        hostname: str,
        username: Optional[str] = None,
        password: Optional[str] = None,
        protocol=defaults.API_PROTOCOL,
        verify_cert=False,
        domain=defaults.API_DEFAULT_DOMAIN,
        timeout=defaults.API_REQUEST_TIMEOUT,
        dry_run=defaults.DRY_RUN,
        cdo=False,
        cdo_domain_id=defaults.API_CDO_DEFAULT_DOMAIN_ID,
    ):
        self.conn = Connection(
            hostname, username, password, protocol, verify_cert, domain, timeout, dry_run, cdo, cdo_domain_id
        )
        self.domain = self.conn.domain
        self.version = self.conn.version
        self.assignment = Assignment(self.conn)
        self.audit = Audit(self.conn)
        self.chassis = Chassis(self.conn)
        self.deployment = Deployment(self.conn)
        self.device = Device(self.conn)
        self.devicecluster = DeviceCluster(self.conn)
        self.devicegroup = DeviceGroup(self.conn)
        self.devicehapair = DeviceHAPair(self.conn)
        self.health = Health(self.conn)
        self.integration = Integration(self.conn)
        self.intelligence = Intelligence(self.conn)
        self.job = Job(self.conn)
        self.netmap = NetMap(self.conn)
        self.object = Object(self.conn)
        self.policy = Policy(self.conn)
        self.system = System(self.conn)
        self.troubleshoot = Troubleshoot(self.conn)
        self.update = Update(self.conn)
        self.user = User(self.conn)
