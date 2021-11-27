from .client import Client


class BaseService:
    name = "default"
    views = None

    def client(self):
        return Client(self.name)
