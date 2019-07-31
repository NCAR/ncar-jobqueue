import re
import socket

import dask_jobqueue


def _get_base_class():
    """Function to determine which base class to use.
    """
    cheyenne = re.compile(r'cheyenne')
    casper = re.compile(r'casper')
    hobart = re.compile(r'hobart')

    hostname = socket.getfqdn()

    is_on_cheyenne = cheyenne.search(hostname)
    is_on_casper = casper.search(hostname)
    is_on_hobart = hobart.search(hostname)

    try:
        if is_on_cheyenne:
            return dask_jobqueue.PBSCluster

        elif is_on_casper:
            return dask_jobqueue.SLURMCluster

        elif is_on_hobart:
            return dask_jobqueue.PBSCluster

        else:
            raise RuntimeError(
                'Unable to determine which NCAR cluster you are running on...'
            )

    except Exception as exc:
        raise exc('Unable to determine which NCAR cluster you are running on...')


_base_class = _get_base_class()


class NCARCluster(_base_class):
    """Class to launch Dask Clusters with NCAR's queueing systems (Slurm, PBS)

    Returns
    -------
    cluster : object

         - PBSCluster, if the host on Cheyenne cluster or Hobart cluster.
         - SLURMCluster, if the host is on Casper cluster.
         - Throws exception otherwise.
    """

    def __init__(self, **kwargs):
        super(NCARCluster, self).__init__(**kwargs)
