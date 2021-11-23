from .router import Router

from typing import Callable


class BaseService:
    name = "default"

    def __init__(self) -> None:
        """
        router is what we serve.
        client is what we make a call.
        """
        self.router = Router()
        self.is_registered = False

    def api(self, path: str, name: str) -> Callable:
        """
        set url
        """
        def wrapper(func):
            def wrapped_func(*args, **kwargs):
                resp = func(*args, **kwargs)
                assert isinstance(resp, dict), 'The service function should return dict'
                return resp
            self.router.set_url(path, name, wrapped_func)
            return wrapped_func
        return wrapper

    def get_api_func(self):
        return self.api


def api(url: str, name: str):
    pass
