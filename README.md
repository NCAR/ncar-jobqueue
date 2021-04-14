# ncar-jobqueue

- [ncar-jobqueue](#ncar-jobqueue)
  - [Badges](#badges)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
    - [Casper](#casper)
    - [Cheyenne](#cheyenne)
    - [Hobart](#hobart)
    - [Izumi](#izumi)
    - [Non-NCAR machines](#non-ncar-machines)

`ncar-jobqueue` provides utilities for configuring [dask-jobqueue](https://dask-jobqueue.readthedocs.io/en/latest/) with appropriate default settings for NCAR's clusters.

Supported clusters are:

- Cheyenne (cheyenne.ucar.edu)
- Casper (DAV) (casper.ucar.edu)
- Hobart (hobart.cgd.ucar.edu)
- Izumi (izumi.unified.ucar.edu)

## Badges

| CI          | [![GitHub Workflow Status][github-ci-badge]][github-ci-link] [![GitHub Workflow Status][github-lint-badge]][github-lint-link] [![Code Coverage Status][codecov-badge]][codecov-link] |
| :---------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Package** |                                                         [![Conda][conda-badge]][conda-link] [![PyPI][pypi-badge]][pypi-link]                                                         |
| **License** |                                                                        [![License][license-badge]][repo-link]                                                                        |

## Installation

NCAR-jobqueue can be installed from PyPI with pip:

```bash
python -m pip install ncar-jobqueue
```

NCAR-jobqueue is also available from conda-forge for conda installations:

```bash
conda install -c conda-forge ncar-jobqueue
```

## Configuration

`ncar-jobqueue` provides a custom configuration file with appropriate default settings for different clusters. This configuration file resides in `~/.config/dask/ncar-jobqueue.yaml`:

<details>
<summary>ncar-jobqueue.yaml</summary>

```yaml
cheyenne:
  pbs:
    #project: XXXXXXXX
    name: dask-worker-cheyenne
    cores: 18 # Total number of cores per job
    memory: '109GB' # Total amount of memory per job
    processes: 18 # Number of Python processes per job
    interface: ib0 # Network interface to use like eth0 or ib0
    queue: regular
    walltime: '01:00:00'
    resource-spec: select=1:ncpus=36:mem=109GB
    log-directory: '/glade/scratch/${USER}/dask/cheyenne/logs'
    local-directory: '/glade/scratch/${USER}/dask/cheyenne/local-dir'
    job-extra: []
    env-extra: []
    death-timeout: 60

casper-dav:
  pbs:
    #project: XXXXXXXX
    name: dask-worker-casper-dav
    cores: 2 # Total number of cores per job
    memory: '25GB' # Total amount of memory per job
    processes: 1 # Number of Python processes per job
    interface: ib0
    walltime: '01:00:00'
    resource-spec: select=1:ncpus=1:mem=25GB
    queue: casper
    log-directory: '/glade/scratch/${USER}/dask/casper-dav/logs'
    local-directory: '/glade/scratch/${USER}/dask/casper-dav/local-dir'
    job-extra: []
    env-extra: []
    death-timeout: 60

hobart:
  pbs:
    name: dask-worker-hobart
    cores: 10 # Total number of cores per job
    memory: '96GB' # Total amount of memory per job
    processes: 10 # Number of Python processes per job
    # interface: null              # ib0 doesn't seem to be working on Hobart
    queue: medium
    walltime: '08:00:00'
    resource-spec: nodes=1:ppn=48
    log-directory: '/scratch/cluster/${USER}/dask/hobart/logs'
    local-directory: '/scratch/cluster/${USER}/dask/hobart/local-dir'
    job-extra: ['-r n']
    env-extra: []
    death-timeout: 60

izumi:
  pbs:
    name: dask-worker-izumi
    cores: 10 # Total number of cores per job
    memory: '96GB' # Total amount of memory per job
    processes: 10 # Number of Python processes per job
    # interface: null              # ib0 doesn't seem to be working on Hobart
    queue: medium
    walltime: '08:00:00'
    resource-spec: nodes=1:ppn=48
    log-directory: '/scratch/cluster/${USER}/dask/izumi/logs'
    local-directory: '/scratch/cluster/${USER}/dask/izumi/local-dir'
    job-extra: ['-r n']
    env-extra: []
    death-timeout: 60
```

</details>

**Note:**

- To configure a default project account that is used by `dask-jobqueue` when submitting batch jobs, uncomment the `project` key/line in `~/.config/dask/ncar-jobqueue.yaml` and set it to an appropriate value.

## Usage

**Note:**

⚠️ Online documentation for `dask-jobqueue` is available [here][rtd-link]. ⚠️

### Casper

```python
>>> from ncar_jobqueue import NCARCluster
>>> from dask.distributed import Client
>>> cluster = NCARCluster(project='XXXXXXXX')
>>> cluster
PBSCluster(0f23b4bf, 'tcp://xx.xxx.x.x:xxxx', workers=0, threads=0, memory=0 B)
>>> cluster.scale(jobs=2)
>>> client = Client(cluster)
```

### Cheyenne

```python
>>> from ncar_jobqueue import NCARCluster
>>> from dask.distributed import Client
>>> cluster = NCARCluster(project='XXXXXXXX')
>>> cluster
PBSCluster(0f23b4bf, 'tcp://xx.xxx.x.x:xxxx', workers=0, threads=0, memory=0 B)
>>> cluster.scale(jobs=2)
>>> client = Client(cluster)
```

### Hobart

```python
>>> from ncar_jobqueue import NCARCluster
>>> from dask.distributed import Client
>>> cluster = NCARCluster(project='XXXXXXXX')
>>> cluster
PBSCluster(0f23b4bf, 'tcp://xx.xxx.x.x:xxxx', workers=0, threads=0, memory=0 B)
>>> cluster.scale(jobs=2)
>>> client = Client(cluster)
```

### Izumi

```python
>>> from ncar_jobqueue import NCARCluster
>>> from dask.distributed import Client
>>> cluster = NCARCluster(project='XXXXXXXX')
>>> cluster
PBSCluster(0f23b4bf, 'tcp://xx.xxx.x.x:xxxx', workers=0, threads=0, memory=0 B)
>>> cluster.scale(jobs=2)
>>> client = Client(cluster)
```

### Non-NCAR machines

On non-NCAR machines, `ncar-jobqueue` will warn the user, and it will use `distributed.LocalCluster`:

```python
>>> from ncar_jobqueue import NCARCluster
.../ncar_jobqueue/cluster.py:17: UserWarning: Unable to determine which NCAR cluster you are running on... Returning a `distributed.LocalCluster` class.
warn(message)
>>> from dask.distributed import Client
>>> cluster = NCARCluster()
>>> cluster
LocalCluster(3a7dd0f6, 'tcp://127.0.0.1:64184', workers=4, threads=8, memory=17.18 GB)
```

[github-ci-badge]: https://img.shields.io/github/workflow/status/NCAR/ncar-jobqueue/CI?label=CI&logo=github&style=for-the-badge
[github-lint-badge]: https://img.shields.io/github/workflow/status/NCAR/ncar-jobqueue/linting?label=linting&logo=github&style=for-the-badge
[github-ci-link]: https://github.com/NCAR/ncar-jobqueue/actions?query=workflow%3ACI
[github-lint-link]: https://github.com/NCAR/ncar-jobqueue/actions?query=workflow%3Alinting
[codecov-badge]: https://img.shields.io/codecov/c/github/NCAR/ncar-jobqueue.svg?logo=codecov&style=for-the-badge
[codecov-link]: https://codecov.io/gh/NCAR/ncar-jobqueue
[rtd-badge]: https://img.shields.io/readthedocs/dask-jobqueue/latest.svg?style=for-the-badge
[rtd-link]: https://jobqueue.dask.org/en/latest/?badge=latest
[pypi-badge]: https://img.shields.io/pypi/v/ncar-jobqueue?logo=pypi&style=for-the-badge
[pypi-link]: https://pypi.org/project/ncar-jobqueue
[conda-badge]: https://img.shields.io/conda/vn/conda-forge/ncar-jobqueue?logo=anaconda&style=for-the-badge
[conda-link]: https://anaconda.org/conda-forge/ncar-jobqueue
[license-badge]: https://img.shields.io/github/license/NCAR/ncar-jobqueue?style=for-the-badge
[repo-link]: https://github.com/NCAR/ncar-jobqueue
