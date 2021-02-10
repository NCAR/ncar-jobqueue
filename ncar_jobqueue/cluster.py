from warnings import warn

import dask
import dask_jobqueue
import distributed

from .util import identify_host, in_notebook, is_running_from_jupyterhub

is_notebook = in_notebook()
running_from_jupyterhub = is_running_from_jupyterhub()
dashboard_links = {
    'cheyenne': 'https://jupyterhub.ucar.edu/ch/user/{USER}/proxy/{port}/status',
    'casper': 'https://jupyterhub.ucar.edu/dav/user/{USER}/proxy/{port}/status',
}


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
    if host == 'unknown':
        warn(
            'Unable to determine which NCAR cluster you are running on...'
            'Using a local cluster via `distributed.LocalCluster`.'
        )

    if is_notebook and running_from_jupyterhub and host in {'cheyenne', 'casper'}:
        dask.config.set({'distributed.dashboard.link': dashboard_links[host]})
    elif is_notebook and host != 'unknown':
        dask.config.set({'distributed.dashboard.link': '/proxy/{port}/status'})

    return base_classes[host]


class NCARCluster:
    """Launches Dask Clusters with NCAR's queueing systems (Slurm, PBS).

    This class relies on cluster classes defined by `dask-jobqueue`. For documentation,
    please see dask-joqueue's documentation at https://dask-jobqueue.readthedocs.io .

    Returns
    -------
    cluster : cluster object

         - `dask_jobqueue.PBSCluster`, if the host on Cheyenne, CGD's Hobart and Izumi clusters.
         - `dask_jobqueue.SLURMCluster`, if the host is on Casper (DAV) cluster.
         - `distributed.LocalCluster` otherwise.
    """

    def __new__(cls, *args, **kwargs):
        return _get_base_class()(*args, **kwargs)
