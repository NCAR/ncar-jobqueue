import re
import socket

import psutil


def identify_host():
    """Function to determine which host the client is running from."""
    cheyenne_login = re.compile(r'cheyenne([0-9]+).cheyenne.ucar.edu')
    cheyenne_compute = re.compile(r'r([a-zA-Z0-9]+).ib0.cheyenne.ucar.edu')
    dav_login = re.compile(r'casper')
    dav_compute = re.compile(r'crhtc([a-zA-Z0-9]+).hpc.ucar.edu')
    hobart = re.compile(r'h([a-zA-Z0-9]+).cgd.ucar.edu')
    izumi = re.compile(r'i([a-zA-Z0-9]+).unified.ucar.edu')

    regexes = [
        ('cheyenne-login', cheyenne_login),
        ('cheyenne-compute', cheyenne_compute),
        ('dav-login', dav_login),
        ('dav-compute', dav_compute),
        ('izumi', izumi),
        ('hobart', hobart),
    ]

    hostname = socket.getfqdn()
    host = 'unknown'

    for name, regex in regexes:
        if regex.search(hostname):
            host = name
            break
    return host


def in_notebook():
    """Check if the code is running inside a Jupyter Notebook.

    Adapted from https://github.com/tqdm/tqdm/blob/master/tqdm/autonotebook.py
    """
    try:
        from IPython import get_ipython

        interactive_shell = get_ipython()
        if hasattr(interactive_shell, 'config'):
            config = interactive_shell.config
        else:
            config = None
        if not config or 'IPKernelApp' not in config:  # pragma: no cover
            return False
    except ImportError:
        return False
    return True


def is_running_from_jupyterhub():
    """Find out if the code is running from a jupyterhub."""

    return any([re.search('jupyter-labhub', x) for x in psutil.Process().parent().cmdline()])
