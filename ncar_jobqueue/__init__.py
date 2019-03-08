#!/usr/bin/env python
""" Top-level module for ncar-jobqueue. """
from ._version import get_versions
from .cluster import NCARCluster
__version__ = get_versions()['version']
del get_versions
