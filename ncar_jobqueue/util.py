import re
import socket

import psutil


def identify_host():
    """Function to determine which host the client is running from."""
    cheyenne = re.compile(r'cheyenne')
    casper = re.compile(r'casper')
    hobart = re.compile(r'h([a-zA-Z0-9]+).cgd.ucar.edu')
    izumi = re.compile(r'i([a-zA-Z0-9]+).unified.ucar.edu')
    hostname = socket.getfqdn()

    is_on_cheyenne = cheyenne.search(hostname)
    is_on_casper = casper.search(hostname)
    is_on_hobart = hobart.search(hostname)
    is_on_izumi = izumi.search(hostname)

    if is_on_cheyenne:
        return 'cheyenne'

    elif is_on_casper:
        return 'casper'

    elif is_on_hobart:
        return 'hobart'

    elif is_on_izumi:
        return 'izumi'

    else:
        return 'unknown'


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

    return any([re.search('jupyterhub-singleuser', x) for x in psutil.Process().parent().cmdline()])
