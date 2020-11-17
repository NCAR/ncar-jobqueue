#!/usr/bin/env python3
# flake8: noqa
""" Top-level module for ncar-jobqueue. """
from pkg_resources import DistributionNotFound, get_distribution

from . import config
from .cluster import NCARCluster

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:  # pragma: no cover
    # package is not installed
    _version__ = '0.0.0'  # pragma: no cover
