#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The setup script."""


from setuptools import find_packages, setup

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')


setup(
    maintainer='NCAR XDev Team',
    maintainer_email='xdev@ucar.edu',
    description="Utilities for expanding dask-jobqueue with appropriate settings for NCAR's clusters",
    install_requires=requirements,
    license='Apache License 2.0',
    python_requires='>=3.6',
    long_description_content_type='text/markdown',
    long_description=long_description,
    include_package_data=True,
    name='ncar-jobqueue',
    packages=find_packages(),
    url='https://github.com/NCAR/ncar-jobqueue',
    project_urls={
        'Documentation': 'https://github.com/NCAR/ncar-jobqueue',
        'Source': 'https://github.com/NCAR/ncar-jobqueue',
        'Tracker': 'https://github.com/NCAR/ncar-jobqueue',
    },
    use_scm_version={'version_scheme': 'post-release', 'local_scheme': 'dirty-tag'},
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0'],
    zip_safe=False,
)
