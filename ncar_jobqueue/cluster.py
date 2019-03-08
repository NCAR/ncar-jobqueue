
import dask_jobqueue
import socket
import re
from dask_jobqueue.core import JobQueueCluster

class NCARCluster(JobQueueCluster):
    def __init__(self, **kwargs):
        self._host = self._get_host()

    def _get_host(self):
        filter1 = r'^cheyenne'
        filter2 = r'^r\d'
        cheyenne_filter = re.compile('|'.join([filter1, filter2]))
        hostname = socket.gethostname()
        host_on_cheyenne = cheyenne_filter.search(hostname)
        if host_on_cheyenne:
            return 'cheyenne'
        else:
            return 'dav'
