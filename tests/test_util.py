import pytest


def test_identify_host():
    with pytest.warns(UserWarning):
        from ncar_jobqueue.util import identify_host

        identify_host()
