import requests


def test_run(main_app):
    """
    通过此框架创建的 web app
    应该能够被直接访问
    """

    # dynamic create threading for new app --> funny!
    # main_app.get_service()
    resp = requests.get('http://localhost:5000')
    assert resp.status_code == 200
    