import requests


def test_run(main_app):
    """
    通过此框架创建的 web app
    应该能够被直接访问
    """
    main_app.get_app().get_url()
    resp = requests.get('http://localhost:5000')
    assert resp.status_code == 200
    