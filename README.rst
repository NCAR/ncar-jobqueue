ncar-jobqueue
==============

.. image:: https://img.shields.io/pypi/v/ncar-jobqueue.svg?style=for-the-badge
    :target: https://pypi.org/project/ncar-jobqueue
    :alt: Python Package Index

Utilities for expanding dask-jobqueue with appropriate settings for NCAR's clusters.


.. code-block:: python

    >>> from ncar_jobqueue import NCARCluster
    >>> from distributed import Client
    >>> cluster = NCARCluster(cores=2, memory='10GB')
    >>> cluster
    NCARCluster(cores=0, memory=0 B, workers=0/0, jobs=0/0)
    >>> cluster.scale(1)
    >>> cluster
    NCARCluster(cores=2, memory=10.00 GB, workers=1/1, jobs=1/1)
    >>> client = Client(cluster)
    >>> client
    <Client: scheduler='tcp://10.12.205.20:40698' processes=1 cores=2>
