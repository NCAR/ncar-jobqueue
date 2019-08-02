#!/usr/bin/env python
""" Top-level module for ncar-jobqueue. """
from pkg_resources import DistributionNotFound, get_distribution

from . import config
from .cluster import NCARCluster

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
