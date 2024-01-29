import pytest
from distributed import LocalCluster

from ncar_jobqueue import NCARCluster
from ncar_jobqueue.util import derecho_compute, derecho_login


def test_ncar_cluster():
    cluster = NCARCluster()
    assert isinstance(cluster, LocalCluster)
    assert str(cluster.scheduler_info['services']['dashboard']) in cluster.dashboard_link


@pytest.mark.parametrize(
    'hostname, expected',
    [
        ('dec2450.hsn.de.hpc.ucar.edu', True),
        ('derecho6.hsn.de.hpc.ucar.edu', False),
        ('random2450.hsn.de.hpc.ucar.edu', False),
        ('decABC.hsn.de.hpc.ucar.edu', False),
    ],
)
def test_derecho_compute(hostname, expected):
    assert (derecho_compute.match(hostname) is not None) == expected


@pytest.mark.parametrize(
    'hostname, expected',
    [
        ('derecho6.hsn.de.hpc.ucar.edu', True),
        ('dec2450.hsn.de.hpc.ucar.edu', False),
        ('derechoABC.hsn.de.hpc.ucar.edu', False),
        ('random6.hsn.de.hpc.ucar.edu', False),
    ],
)
def test_derecho_login(hostname, expected):
    assert (derecho_login.match(hostname) is not None) == expected
