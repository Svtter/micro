def test_client_call(work_service_cls):
    work_service = work_service_cls()
    client = work_service.client()

    resp = client.get('/hello', data=None)
    assert isinstance(resp, dict)