from warnings import warn

import dask
import dask_jobqueue
import distributed

from .util import identify_host, in_notebook

is_notebook = in_notebook()


def _get_base_class():
    """Function to determine which base class to use."""

    base_classes = {
        'hobart': dask_jobqueue.PBSCluster,
        'izumi': dask_jobqueue.PBSCluster,
        'cheyenne': dask_jobqueue.PBSCluster,
        'casper': dask_jobqueue.SLURMCluster,
        'unknown': distributed.LocalCluster,
    }

    host = identify_host()
    dashboard_links = {
        'cheyenne': 'https://jupyterhub.ucar.edu/ch/user/{USER}/proxy/{port}/status',
        'casper': 'https://jupyterhub.ucar.edu/dav/user/{USER}/proxy/{port}/status',
    }

    if host == 'unknown':
        warn(
            'Unable to determine which NCAR cluster you are running on... Using an instance of `distributed.LocalCluster` class.'
        )

    if is_notebook and host != 'unknown':
        dask.config.set(
            {'distributed.dashboard.link': dashboard_links.get(host, '/proxy/{port}/status')}
        )

    return base_classes[host]


_base_class = _get_base_class()


class NCARCluster(_base_class):
    """Class to launch Dask Clusters with NCAR's queueing systems (Slurm, PBS)

    Returns
    -------
    cluster : cluster object

         - PBSCluster, if the host on Cheyenne cluster or Hobart or Izumi clusters.
         - SLURMCluster, if the host is on Casper cluster.
         - Uses distributed.LocalCluster otherwise.
    """

    def __init__(self, **kwargs):
        super(NCARCluster, self).__init__(**kwargs)
