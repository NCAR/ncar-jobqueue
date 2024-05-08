| CI          | [![GitHub Workflow Status][github-ci-badge]][github-ci-link] [![Code Coverage Status][codecov-badge]][codecov-link] [![pre-commit.ci status][pre-commit.ci-badge]][pre-commit.ci-link] |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| **Docs**    |                                                                     [![Documentation Status][rtd-badge]][rtd-link]                                                                     |
| **Package** |                                                          [![Conda][conda-badge]][conda-link] [![PyPI][pypi-badge]][pypi-link]                                                          |
| **License** |                                                                         [![License][license-badge]][repo-link]                                                                         |

# ncar-jobqueue

- [ncar-jobqueue](#ncar-jobqueue)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
    - [Casper](#casper)
    - [Derecho](#derecho)
    - [Hobart](#hobart)
    - [Izumi](#izumi)
    - [Non-NCAR machines](#non-ncar-machines)

`ncar-jobqueue` provides utilities for configuring [dask-jobqueue](https://dask-jobqueue.readthedocs.io/en/latest/) with appropriate default settings for NCAR's clusters.

The following compute servers are supported:

- Casper (casper.hpc.ucar.edu)
- Derecho (derecho.hpc.ucar.edu)
- Hobart (hobart.cgd.ucar.edu)
- Izumi (izumi.unified.ucar.edu)

**CISL discourages the use of Derecho for Dask. Please use Casper instead unless you are sure you can properly utilize a significant portion of the CPU cores on a Derecho node (e.g., via [dask-mpi](https://mpi.dask.org/en/latest/)).**

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
casper:
  pbs:
    #project: XXXXXXXX
    name: dask-worker-casper
    cores: 1 # Total number of cores per job
    memory: '4GiB' # Total amount of memory per job
    processes: 1 # Number of Python processes per job
    interface: ext # Network interface to use (high-speed ethernet)
    walltime: '01:00:00'
    resource-spec: select=1:ncpus=1:mem=4GB
    queue: casper
    log-directory: '/glade/derecho/scratch/${USER}/dask/casper/logs'
    local-directory: '/glade/derecho/scratch/${USER}/dask/casper/local-dir'
    job-extra: ['-r n']
    env-extra: []
    death-timeout: 60

derecho:
  pbs:
    #project: XXXXXXXX
    name: dask-worker-derecho
    cores: 1 # Total number of cores per job
    memory: '4GiB' # Total amount of memory per job
    processes: 1 # Number of Python processes per job
    interface: hsn0 # Network interface to use (Slingshot)
    queue: develop
    walltime: '01:00:00'
    resource-spec: select=1:ncpus=128:mem=235GB
    log-directory: '/glade/derecho/scratch/${USER}/dask/derecho/logs'
    local-directory: '/glade/derecho/scratch/${USER}/dask/derecho/local-dir'
    job-extra: ['-l job_priority=economy', '-r -n']
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

### Derecho

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
>>> cluster = NCARCluster()
>>> cluster
PBSCluster(0f23b4bf, 'tcp://xx.xxx.x.x:xxxx', workers=0, threads=0, memory=0 B)
>>> cluster.scale(jobs=2)
>>> client = Client(cluster)
```

### Izumi

```python
>>> from ncar_jobqueue import NCARCluster
>>> from dask.distributed import Client
>>> cluster = NCARCluster()
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

[github-ci-badge]: https://img.shields.io/github/actions/workflow/status/NCAR/ncar-jobqueue/ci.yaml
[github-ci-link]: https://github.com/NCAR/ncar-jobqueue/actions?query=workflow%3ACI
[codecov-badge]: https://img.shields.io/codecov/c/github/NCAR/ncar-jobqueue.svg?logo=codecov
[codecov-link]: https://codecov.io/gh/NCAR/ncar-jobqueue
[rtd-badge]: https://img.shields.io/readthedocs/dask-jobqueue/latest.svg
[rtd-link]: https://jobqueue.dask.org/en/latest/
[pypi-badge]: https://img.shields.io/pypi/v/ncar-jobqueue?logo=pypi
[pypi-link]: https://pypi.org/project/ncar-jobqueue
[conda-badge]: https://img.shields.io/conda/vn/conda-forge/ncar-jobqueue?logo=anaconda
[conda-link]: https://anaconda.org/conda-forge/ncar-jobqueue
[license-badge]: https://img.shields.io/github/license/NCAR/ncar-jobqueue
[repo-link]: https://github.com/NCAR/ncar-jobqueue
[pre-commit.ci-badge]: https://results.pre-commit.ci/badge/github/NCAR/ncar-jobqueue/main.svg
[pre-commit.ci-link]: https://results.pre-commit.ci/latest/github/NCAR/ncar-jobqueue/main
