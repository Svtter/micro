# The client could call service directly
# but only in other service or main threading.
import requests


class Client:
    """
    通过 TDD 的方式，允许自己编写 SDK
    """

    def __init__(self, service_name) -> None:
        self.service_name = service_name

        self.served = False

    def get(self, url, data):
        """
        在没有启动实例的时候，应该直接请求服务
        """
        response = requests.get(url, data=data)
        return response.json()
