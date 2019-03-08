
import dask_jobqueue
import socket
import re
import dask.distributed

def _get_base_class():
    """Function to determine which base class to use.
    """
    filter1 = r'^cheyenne'
    filter2 = r'r\d(i)\d(n)\d*'
    cheyenne_filter = re.compile('|'.join([filter1, filter2]))
    dav_filter = re.compile(r'^casper')
    hostname = socket.gethostname()
    host_on_cheyenne = cheyenne_filter.search(hostname)
    host_on_dav = dav_filter.search(hostname)
    try:
        if host_on_cheyenne:
            return dask_jobqueue.PBSCluster

        elif host_on_dav:
            return dask_jobqueue.SLURMCluster

        else:
            return dask.distributed.LocalCluster

    except:
        return dask.distributed.LocalCluster


_base_class = _get_base_class()
class NCARCluster(_base_class):
    """Class to launch Dask Clusters with NCAR's queueing systems (Slurm, PBS)

    Returns
    -------
    cluster : object

         - PBSCluster, if the host on Cheyenne cluster
         - SLURMCluster, if the host is on DAV cluster
         - LocalCluster, if the host is neither on Cheyenne nor DAV clusters
    """

    def __init__(self, **kwargs):
        super(NCARCluster, self).__init__(**kwargs)
