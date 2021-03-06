# create a app inside.
# for debug convinence.

from flask import Flask

from micro.service import BaseService
from .exceptions import AppException


# Like Service registry
class App:
    def __init__(self) -> None:
        # service_name, service
        self.service_dict = {}

        # service_name, app
        self.app_dict = {}

    def set_web_core(self):
        # The core should be changable.
        pass

    def get_web_core(self, service_name) -> Flask:
        return Flask(service_name)

    def get_app(self, name) -> Flask:
        """
        注册之后，用户可以通过 get_app 来获取已经注册服务的 app
        """
        # Please make sure app exist.
        if not self.app_dict[name]:
            raise AppException(f'No such serivce-{name}. We have {self.app_dict.keys()}')
        return self.app_dict[name]

    def register_service(self, service: BaseService):
        """
        注册服务，到 App 服务列表。
        这样就可以通过 app 快速拉起服务。
        """
        if self.service_dict.get(service.name):
            raise AppException(f"The {service.name} has been registerd.")
        self.service_dict[service.name] = service
        self.app_dict[service.name] = self.get_web_core(service_name=service.name)

        # When start app, check the service status
        service.is_registered = True

    def get_service(self, name: str='default'):
        """
        not finished yet.
        """
        # there should be a service register.
        return self.service_dict[name]


app = App()
