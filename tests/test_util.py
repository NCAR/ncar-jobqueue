import pytest


def test_identify_host():
    with pytest.raises(RuntimeError):
        from ncar_jobqueue.util import identify_host

        identify_host()
