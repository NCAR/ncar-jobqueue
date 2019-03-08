#!/usr/bin/env python
""" Top-level module for ncar-jobqueue. """
from ._version import get_versions


import dask_jobqueue
import socket
import re

__version__ = get_versions()['version']
del get_versions


def get_cluster():
    filter1 = r'^cheyenne'
    filter2 = r'^r\d'
    cheyenne_filter = re.compile('|'.join([filter1, filter2]))
    hostname = socket.gethostname()
    host_on_cheyenne = cheyenne_filter.search(hostname)

    if host_on_cheyenne:
        cluster = dask_jobqueue.PBSCluster()

    else:
        cluster = dask_jobqueue.SLURMCluster()

    return cluster

cluster = get_cluster()
