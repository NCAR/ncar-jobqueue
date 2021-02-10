# For some reason this is required in python >= 3.9
# TODO: remove this once https://github.com/dask/distributed/pull/4460 is merged
import multiprocessing.popen_spawn_posix  # noqa: F401

from distributed import LocalCluster

from ncar_jobqueue import NCARCluster


def test_ncar_cluster():
    cluster = NCARCluster()
    assert isinstance(cluster, LocalCluster)
    assert str(cluster.scheduler_info['services']['dashboard']) in cluster.dashboard_link
