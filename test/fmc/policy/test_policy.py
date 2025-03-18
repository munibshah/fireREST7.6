# -*- coding: utf-8 -*-

from fireREST76.fmc.policy.accesspolicy import AccessPolicy
from fireREST76.fmc.policy.filepolicy import FilePolicy
from fireREST76.fmc.policy.ftdnatpolicy import FtdNatPolicy
from fireREST76.fmc.policy.ftds2svpn import FtdS2sVpn
from fireREST76.fmc.policy.intrusionpolicy import IntrusionPolicy
from fireREST76.fmc.policy.prefilterpolicy import PrefilterPolicy
from fireREST76.fmc.policy.snmpalert import SnmpAlert
from fireREST76.fmc.policy.syslogalert import SyslogAlert


def test_initialization(fmc):
    assert isinstance(fmc.policy.accesspolicy, AccessPolicy)
    assert isinstance(fmc.policy.filepolicy, FilePolicy)
    assert isinstance(fmc.policy.ftdnatpolicy, FtdNatPolicy)
    assert isinstance(fmc.policy.ftds2svpn, FtdS2sVpn)
    assert isinstance(fmc.policy.intrusionpolicy, IntrusionPolicy)
    assert isinstance(fmc.policy.prefilterpolicy, PrefilterPolicy)
    assert isinstance(fmc.policy.snmpalert, SnmpAlert)
    assert isinstance(fmc.policy.syslogalert, SyslogAlert)
