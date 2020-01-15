#! /usr/bin/env python
import os
import shutil
from tempfile import mkdtemp

import dask
import pkg_resources
import yaml
from jinja2 import Environment, FileSystemLoader

from .util import identify_host


def ensure_file(source, destination=None, comment=True):
    """
    Copy file to default location if it does not already exist
    This tries to move a default configuration file to a default location if
    if does not already exist.  It also comments out that file by default.
    This is to be used by downstream modules (like dask.distributed) that may
    have default configuration files that they wish to include in the default
    configuration path.
    Parameters
    ----------
    source : string, filename
        Source configuration file, typically within a source directory.
    destination : string, directory
        Destination directory. Configurable by ``DASK_CONFIG`` environment
        variable, falling back to ~/.config/dask.
    comment : bool, True by default
        Whether or not to comment out the config file when copying.
    """

    if destination is None:
        destination = dask.config.PATH

    # destination is a file and already exists, never overwrite
    if os.path.isfile(destination):
        return

    # If destination is not an existing file, interpret as a directory,
    # use the source basename as the filename
    directory = destination
    destination = os.path.join(directory, os.path.basename(source))

    try:
        if not os.path.exists(destination):
            os.makedirs(directory, exist_ok=True)

            # Atomically create destination.  Parallel testing discovered
            # a race condition where a process can be busy creating the
            # destination while another process reads an empty config file.
            tmp = "%s.tmp.%d" % (destination, os.getpid())
            with open(source) as f:
                lines = list(f)

            if comment:
                lines = [
                    "# " + line if line.strip() and not line.startswith("#") else line
                    for line in lines
                ]

            lines = [os.path.expandvars(line) for line in lines]

            with open(tmp, "w") as f:
                f.write("".join(lines))

            try:
                os.rename(tmp, destination)
            except OSError:
                os.remove(tmp)
    except OSError:
        pass


def _generate_config(config_data_file_path, template_file_path):

    host = identify_host()

    # Load data from YAML into Python dictionary
    config_data = yaml.safe_load(open(config_data_file_path))
    config_data["host"] = host

    # Load Jinja2 template
    template_dir = os.path.dirname(os.path.abspath(template_file_path))

    env = Environment(
        loader=FileSystemLoader(template_dir), trim_blocks=True, lstrip_blocks=True
    )

    template = env.get_template(os.path.basename(template_file_path))

    # Render the template with data and return it
    data = template.render(config_data)

    return data


config_data_file_path = pkg_resources.resource_filename(
    "ncar_jobqueue", "host_configs.yaml"
)

template_file_path = pkg_resources.resource_filename(
    "ncar_jobqueue", "jobqueue_template.yaml"
)

temp_dir = mkdtemp()

config_path = os.path.join(temp_dir, "jobqueue.yaml")
destination = os.path.join(os.path.expanduser("~"), ".dask")
with open(config_path, "w") as outfile:
    data = _generate_config(config_data_file_path, template_file_path)
    data = yaml.safe_load(data)
    yaml.dump(data, outfile, default_flow_style=False)
ensure_file(source=config_path, destination=destination, comment=False)

dask.config.collect(paths=[destination])
dask.config.refresh()
shutil.rmtree(temp_dir, ignore_errors=True)
