# -*- coding: utf-8 -*-

import logging
from typing import Optional

from firerest76 import defaults
from firerest76.fmc import Connection
from firerest76.fmc.assignment import Assignment
from firerest76.fmc.audit import Audit
from firerest76.fmc.chassis import Chassis
from firerest76.fmc.deployment import Deployment
from firerest76.fmc.device import Device
from firerest76.fmc.devicecluster import DeviceCluster
from firerest76.fmc.devicegroup import DeviceGroup
from firerest76.fmc.devicehapair import DeviceHAPair
from firerest76.fmc.health import Health
from firerest76.fmc.integration import Integration
from firerest76.fmc.intelligence import Intelligence
from firerest76.fmc.job import Job
from firerest76.fmc.netmap import NetMap
from firerest76.fmc.object import Object
from firerest76.fmc.policy import Policy
from firerest76.fmc.system import System
from firerest76.fmc.troubleshoot import Troubleshoot
from firerest76.fmc.update import Update
from firerest76.fmc.user import User

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
