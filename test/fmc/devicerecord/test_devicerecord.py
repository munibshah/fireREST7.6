# -*- coding: utf-8 -*-

from fireREST76.fmc.device.devicerecord.bridgegroupinterface import BridgeGroupInterface
from fireREST76.fmc.device.devicerecord.etherchannelinterface import EtherChannelInterface
from fireREST76.fmc.device.devicerecord.fpinterfacestatistics import FpInterfaceStatistics
from fireREST76.fmc.device.devicerecord.fplogicalinterface import FpLogicalInterface
from fireREST76.fmc.device.devicerecord.fpphysicalinterface import FpPhysicalInterface
from fireREST76.fmc.device.devicerecord.inlineset import InlineSet
from fireREST76.fmc.device.devicerecord.interfaceevent import InterfaceEvent
from fireREST76.fmc.device.devicerecord.operational import Operational
from fireREST76.fmc.device.devicerecord.physicalinterface import PhysicalInterface
from fireREST76.fmc.device.devicerecord.redundantinterface import RedundantInterface
from fireREST76.fmc.device.devicerecord.routing import Routing
from fireREST76.fmc.device.devicerecord.subinterface import SubInterface
from fireREST76.fmc.device.devicerecord.virtualswitch import VirtualSwitch
from fireREST76.fmc.device.devicerecord.virtualtunnelinterface import VirtualTunnelInterface
from fireREST76.fmc.device.devicerecord.vlaninterface import VlanInterface


def test_initialization(fmc):
    devicerecord = fmc.device.devicerecord
    assert isinstance(devicerecord.bridgegroupinterface, BridgeGroupInterface)
    assert isinstance(devicerecord.etherchannelinterface, EtherChannelInterface)
    assert isinstance(devicerecord.fpinterfacestatistics, FpInterfaceStatistics)
    assert isinstance(devicerecord.fplogicalinterface, FpLogicalInterface)
    assert isinstance(devicerecord.fpphysicalinterface, FpPhysicalInterface)
    assert isinstance(devicerecord.inlineset, InlineSet)
    assert isinstance(devicerecord.interfaceevent, InterfaceEvent)
    assert isinstance(devicerecord.operational, Operational)
    assert isinstance(devicerecord.physicalinterface, PhysicalInterface)
    assert isinstance(devicerecord.redundantinterface, RedundantInterface)
    assert isinstance(devicerecord.routing, Routing)
    assert isinstance(devicerecord.subinterface, SubInterface)
    assert isinstance(devicerecord.virtualswitch, VirtualSwitch)
    assert isinstance(devicerecord.virtualtunnelinterface, VirtualTunnelInterface)
    assert isinstance(devicerecord.vlaninterface, VlanInterface)
