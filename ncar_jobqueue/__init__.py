#!/usr/bin/env python3
# flake8: noqa
""" Top-level module for ncar-jobqueue. """
from importlib.metadata import version, PackageNotFoundError

from . import config
from .cluster import NCARCluster

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    # package is not installed
    _version__ = '0.0.0'  # pragma: no cover
