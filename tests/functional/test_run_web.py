import requests


def test_run(main_app):
    resp = requests.get('http://localhost:5000')
    assert resp.status_code == 200
    