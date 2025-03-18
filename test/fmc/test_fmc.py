# -*- coding: utf-8 -*-

from fireREST76.fmc.assignment import Assignment
from fireREST76.fmc.audit import Audit
from fireREST76.fmc.chassis import Chassis
from fireREST76.fmc.device import Device
from fireREST76.fmc.devicecluster import DeviceCluster
from fireREST76.fmc.devicehapair import DeviceHAPair
from fireREST76.fmc.devicegroup import DeviceGroup
from fireREST76.fmc.deployment import Deployment
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
