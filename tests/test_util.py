from ncar_jobqueue.util import identify_host, in_notebook, is_running_from_jupyterhub


def test_identify_host():
    assert 'unknown' == identify_host()


def test_in_notebook():
    assert not in_notebook()


def test_is_running_from_jupyterhub():
    assert not is_running_from_jupyterhub()
