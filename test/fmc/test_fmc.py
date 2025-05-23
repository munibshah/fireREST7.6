# -*- coding: utf-8 -*-

from firerest76.fmc.assignment import Assignment
from firerest76.fmc.audit import Audit
from firerest76.fmc.chassis import Chassis
from firerest76.fmc.device import Device
from firerest76.fmc.devicecluster import DeviceCluster
from firerest76.fmc.devicehapair import DeviceHAPair
from firerest76.fmc.devicegroup import DeviceGroup
from firerest76.fmc.deployment import Deployment
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


def test_initialization(fmc):
    assert isinstance(fmc.assignment, Assignment)
    assert isinstance(fmc.audit, Audit)
    assert isinstance(fmc.chassis, Chassis)
    assert isinstance(fmc.device, Device)
    assert isinstance(fmc.devicecluster, DeviceCluster)
    assert isinstance(fmc.devicehapair, DeviceHAPair)
    assert isinstance(fmc.devicegroup, DeviceGroup)
    assert isinstance(fmc.deployment, Deployment)
    assert isinstance(fmc.health, Health)
    assert isinstance(fmc.integration, Integration)
    assert isinstance(fmc.intelligence, Intelligence)
    assert isinstance(fmc.job, Job)
    assert isinstance(fmc.netmap, NetMap)
    assert isinstance(fmc.object, Object)
    assert isinstance(fmc.policy, Policy)
    assert isinstance(fmc.system, System)
    assert isinstance(fmc.troubleshoot, Troubleshoot)
    assert isinstance(fmc.update, Update)
    assert isinstance(fmc.user, User)
