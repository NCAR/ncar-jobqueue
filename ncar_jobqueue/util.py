import re
import socket


def identify_host():
    """Function to determine which host the client is running from."""
    cheyenne = re.compile(r'cheyenne')
    casper = re.compile(r'casper')
    hobart = re.compile(r'h([a-zA-Z0-9]+).cgd.ucar.edu')
    izumi = re.compile(r'izumi')
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
