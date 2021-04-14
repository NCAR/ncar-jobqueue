import os
from warnings import warn

import dask
import dask_jobqueue
import distributed

from .util import identify_host, in_notebook, is_running_from_jupyterhub

jupyterhub_server_name = os.environ.get('JUPYTERHUB_SERVER_NAME', None)
is_notebook = in_notebook()
running_from_jupyterhub = is_running_from_jupyterhub()


def _get_base_class():
    """Function to determine which base class to use."""

    base_classes = {
        'hobart': dask_jobqueue.PBSCluster,
        'izumi': dask_jobqueue.PBSCluster,
        'cheyenne-login': dask_jobqueue.PBSCluster,
        'cheyenne-compute': dask_jobqueue.PBSCluster,
        'dav-login': dask_jobqueue.PBSCluster,
        'dav-compute': dask_jobqueue.PBSCluster,
        'unknown': distributed.LocalCluster,
    }
    host = identify_host()
    if host == 'unknown':
        warn(
            'Unable to determine which NCAR cluster you are running on...'
            'Using a local cluster via `distributed.LocalCluster`.'
        )

    if (
        is_notebook
        and running_from_jupyterhub
        and host in {'cheyenne-login', 'dav-login', 'cheyenne-compute', 'dav-compute'}
    ):
        dashboard_link = 'https://jupyterhub.hpc.ucar.edu/stable/user/{USER}/proxy/{port}/status'
        if jupyterhub_server_name:
            dashboard_link = (
                'https://jupyterhub.hpc.ucar.edu/stable/user/'
                + '{USER}'
                + f'/{jupyterhub_server_name}/proxy/'
                + '{port}/status'
            )
        dask.config.set({'distributed.dashboard.link': dashboard_link})
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

         - `dask_jobqueue.PBSCluster`, if the host on Cheyenne, Casper (DAV), CGD's Hobart and Izumi clusters.
         - `distributed.LocalCluster` otherwise.
    """

    def __new__(cls, *args, **kwargs):
        return _get_base_class()(*args, **kwargs)
