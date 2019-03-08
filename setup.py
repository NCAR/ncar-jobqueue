#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import sys
from setuptools import setup, find_packages
import versioneer
from os.path import exists

if exists('README.rst'):
    with open('README.rst') as f:
        long_description = f.read()
else:
    long_description = ''

install_requires = ['dask-jobqueue']


setup(
    maintainer='Anderson Banihirwe',
    maintainer_email='abanihi@ucar.edu',
    description="Utilities for expanding dask-jobqueue with appropriate settings for NCAR's clusters",
    install_requires=install_requires,
    license='Apache License 2.0',
    long_description=long_description,
    name='ncar-jobqueue',
    packages=find_packages(),
    url='https://github.com/NCAR/ncar-jobqueue',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=False,
)
