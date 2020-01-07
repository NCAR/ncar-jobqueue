#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import sys
from os.path import exists

from setuptools import find_packages, setup

if exists("README.rst"):
    with open("README.rst") as f:
        long_description = f.read()
else:
    long_description = ""

install_requires = ["dask-jobqueue", "jinja2", "dask", "pyyaml"]


setup(
    maintainer="Anderson Banihirwe",
    maintainer_email="abanihi@ucar.edu",
    description="Utilities for expanding dask-jobqueue with appropriate settings for NCAR's clusters",
    install_requires=install_requires,
    license="Apache License 2.0",
    long_description=long_description,
    include_package_data=True,
    name="ncar-jobqueue",
    packages=find_packages(),
    url="https://github.com/NCAR/ncar-jobqueue",
    use_scm_version={"version_scheme": "post-release", "local_scheme": "dirty-tag"},
    setup_requires=["setuptools_scm", "setuptools>=30.3.0"],
    zip_safe=False,
)
