#! /usr/bin/env python3
import datetime
import os
import pathlib
import shutil

import dask
import pkg_resources
import yaml

from .util import identify_host


def ensure_file(source, destination_path):
    """This tries to move a default configuration file to a default location."""
    if destination_path.exists():
        last_modified = datetime.datetime.fromtimestamp(os.path.getmtime(destination_path))
        new_config_time = datetime.datetime.fromisoformat('2024-01-28')
        if last_modified < new_config_time:
            shutil.copyfile(source, destination_path)
    else:
        shutil.copyfile(source, destination_path)


def configure(destination_path):
    host = identify_host()
    if host == 'unknown':
        return
    with open(destination_path) as f:
        original_data = yaml.safe_load(f)[host]
    _, data = original_data.copy().popitem()
    for key in {'local-directory', 'log-directory'}:
        directory = data.get(key, None)
        if directory and isinstance(directory, str):
            full_path = dask.config.expand_environment_variables(directory)
            pathlib.Path(full_path).mkdir(parents=True, exist_ok=True)
    dask.config.update(
        dask.config.get('jobqueue'), dask.config.expand_environment_variables(original_data)
    )


config_data_file_path = pathlib.Path(
    pkg_resources.resource_filename('ncar_jobqueue', 'ncar-jobqueue.yaml')
)
destination_dir = pathlib.Path(dask.config.PATH)
destination_path = destination_dir / config_data_file_path.parts[-1]

ensure_file(source=config_data_file_path, destination_path=destination_path)
configure(destination_path)
