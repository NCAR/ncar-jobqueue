# ncar-jobqueue

- [ncar-jobqueue](#ncar-jobqueue)
  - [Badges](#badges)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Casper](#casper)
    - [Cheyenne](#cheyenne)
    - [Hobart](#hobart)
    - [Izumi](#izumi)
    - [Non-NCAR machines](#non-ncar-machines)

## Badges

| CI          | [![GitHub Workflow Status][github-ci-badge]][github-ci-link] [![GitHub Workflow Status][github-lint-badge]][github-lint-link] [![Code Coverage Status][codecov-badge]][codecov-link] |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Docs**    |                                                                    [![Documentation Status][rtd-badge]][rtd-link]                                                                    |
| **Package** |                                                         [![Conda][conda-badge]][conda-link] [![PyPI][pypi-badge]][pypi-link]                                                         |
| **License** |                                                                        [![License][license-badge]][repo-link]                                                                        |

Utilities for expanding [dask-jobqueue](https://dask-jobqueue.readthedocs.io/en/latest/) with appropriate settings for NCAR's clusters.

Supported clusters:

- Cheyenne
- Casper (DAV)
- CGD's Hobart
- CGD's Izumi

## Installation

NCAR-jobqueue can be installed from PyPI with pip:

```bash
python -m pip install ncar-jobqueue
```

NCAR-jobqueue is also available from conda-forge for conda installations:

```bash
conda install -c conda-forge ncar-jobqueue
```

## Usage

### Casper

```python
>>> from ncar_jobqueue import NCARCluster
>>> from dask.distributed import Client
>>> cluster = NCARCluster()
>>> cluster
NCARCluster(cores=0, memory=0 B, workers=0/0, jobs=0/0)
>>> cluster.scale(jobs=2)
>>> cluster
NCARCluster(cores=2, memory=50.00 GB, workers=2/2, jobs=2/2)
>>> client = Client(cluster)
```

### Cheyenne

```python
>>> from ncar_jobqueue import NCARCluster
>>> from dask.distributed import Client
>>> cluster = NCARCluster()
>>> cluster
NCARCluster(cores=0, memory=0 B, workers=0/0, jobs=0/0)
>>> cluster.scale(jobs=2)
>>> cluster
NCARCluster(cores=72, memory=218.00 GB, workers=2/2, jobs=2/2)
>>> client = Client(cluster)
```

### Hobart

```python
>>> from ncar_jobqueue import NCARCluster
>>> from dask.distributed import Client
>>> cluster = NCARCluster()
>>> cluster
NCARCluster(cores=0, memory=0 B, workers=0/0, jobs=0/0)
>>> cluster.scale(jobs=2)
>>> cluster
NCARCluster(cores=96, memory=192.00 GB, workers=2/2, jobs=2/2)
>>> client = Client(cluster)
```

### Izumi

```python
>>> from ncar_jobqueue import NCARCluster
>>> from dask.distributed import Client
>>> cluster = NCARCluster()
>>> cluster
NCARCluster(cores=0, memory=0 B, workers=0/0, jobs=0/0)
>>> cluster.scale(jobs=2)
>>> cluster
NCARCluster(cores=96, memory=192.00 GB, workers=2/2, jobs=2/2)
>>> client = Client(cluster)
```

### Non-NCAR machines

On non-NCAR machines, `ncar-jobqueue` will warn the user, and it will use `distributed.LocalCluster`:

```python
>>> from ncar_jobqueue import NCARCluster
.../ncar_jobqueue/cluster.py:42: UserWarning: Unable to determine which NCAR cluster you are running on... Returning a `distributed.LocalCluster` class.
warn(message)
>>> from dask.distributed import Client
>>> cluster = NCARCluster()
>>> cluster
NCARCluster('tcp://127.0.0.1:49334', workers=4, threads=8, memory=17.18 GB)
```

[github-ci-badge]: https://img.shields.io/github/workflow/status/NCAR/ncar-jobqueue/CI?label=CI&logo=github&style=for-the-badge
[github-lint-badge]: https://img.shields.io/github/workflow/status/NCAR/ncar-jobqueue/linting?label=linting&logo=github&style=for-the-badge
[github-ci-link]: https://github.com/NCAR/ncar-jobqueue/actions?query=workflow%3ACI
[github-lint-link]: https://github.com/NCAR/ncar-jobqueue/actions?query=workflow%3Alinting
[codecov-badge]: https://img.shields.io/codecov/c/github/NCAR/ncar-jobqueue.svg?logo=codecov&style=for-the-badge
[codecov-link]: https://codecov.io/gh/NCAR/ncar-jobqueue
[rtd-badge]: https://img.shields.io/readthedocs/ncar-jobqueue/latest.svg?style=for-the-badge
[rtd-link]: https://ncar-jobqueue.readthedocs.io/en/latest/?badge=latest
[pypi-badge]: https://img.shields.io/pypi/v/ncar-jobqueue?logo=pypi&style=for-the-badge
[pypi-link]: https://pypi.org/project/ncar-jobqueue
[conda-badge]: https://img.shields.io/conda/vn/conda-forge/ncar-jobqueue?logo=anaconda&style=for-the-badge
[conda-link]: https://anaconda.org/conda-forge/ncar-jobqueue
[license-badge]: https://img.shields.io/github/license/NCAR/ncar-jobqueue?style=for-the-badge
[repo-link]: https://github.com/NCAR/ncar-jobqueue
