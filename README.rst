.. image:: https://img.shields.io/github/workflow/status/NCAR/ncar-jobqueue/CI?label=CI&style=for-the-badge
    :target: https://github.com/NCAR/ncar-jobqueue/actions
    :alt: GitHub Workflow Status
.. image:: https://img.shields.io/pypi/v/ncar-jobqueue.svg?style=for-the-badge
    :target: https://pypi.org/project/ncar-jobqueue
    :alt: Python Package Index

ncar-jobqueue
==============

Utilities for expanding dask-jobqueue_ with appropriate settings for NCAR's clusters.

.. _dask-jobqueue: https://dask-jobqueue.readthedocs.io/en/latest/

Supported clusters:

- Cheyenne
- Casper (DAV)
- CGD's Hobart

Installation
------------

``ncar-jobqueue`` can be installed from PyPI with pip:

.. code-block:: bash

    pip install ncar-jobqueue


Usage
------

Casper
~~~~~~

.. code-block:: python

    >>> from ncar_jobqueue import NCARCluster
    >>> from dask.distributed import Client
    >>> cluster = NCARCluster()
    >>> cluster
    NCARCluster(cores=0, memory=0 B, workers=0/0, jobs=0/0)
    >>> cluster.scale(2)
    >>> cluster
    NCARCluster(cores=2, memory=50.00 GB, workers=2/2, jobs=2/2)
    >>> client = Client(cluster)

Cheyenne
~~~~~~~~

.. code-block:: python

    >>> from ncar_jobqueue import NCARCluster
    >>> from dask.distributed import Client
    >>> cluster = NCARCluster()
    >>> cluster
    NCARCluster(cores=0, memory=0 B, workers=0/0, jobs=0/0)
    >>> cluster.scale(2)
    >>> cluster
    NCARCluster(cores=72, memory=218.00 GB, workers=2/2, jobs=2/2)
    >>> client = Client(cluster)


Hobart
~~~~~~

.. code-block:: python

    >>> from ncar_jobqueue import NCARCluster
    >>> from dask.distributed import Client
    >>> cluster = NCARCluster()
    >>> cluster
    NCARCluster(cores=0, memory=0 B, workers=0/0, jobs=0/0)
    >>> cluster.scale(2)
    >>> cluster
    NCARCluster(cores=96, memory=192.00 GB, workers=2/2, jobs=2/2)
    >>> client = Client(cluster)
