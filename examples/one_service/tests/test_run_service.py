from examples.one_service.conf import Conf
from micro.web import app


def test_run():
    WorkService = Conf.service_list[0]
    work_service = WorkService()
    app.register_service(work_service)
    webapp = app.get_app(work_service.name)
    webapp.run()

    