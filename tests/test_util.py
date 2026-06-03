from ncar_jobqueue.util import identify_host, in_notebook, is_running_from_jupyterhub


def test_identify_host(monkeypatch):
    monkeypatch.delenv('NCAR_HOST', raising=False)
    assert 'unknown' == identify_host()


def test_identify_host_from_ncar_host(monkeypatch):
    monkeypatch.setenv('NCAR_HOST', 'dav')

    assert 'casper-dav' == identify_host()


def test_in_notebook():
    assert not in_notebook()


def test_is_running_from_jupyterhub():
    assert not is_running_from_jupyterhub()
