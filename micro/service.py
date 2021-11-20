from .router import Router
from typing import Callable


class BaseService:
    def __init__(self) -> None:
        self.router = Router()

    def api(self, path: str, name: str) -> Callable:
        """
        set url

        TODO: missing a wrapper
        """
        def wrapper(func):
            def wrapped_func(*args, **kwargs):
                return func(*args, **kwargs)
            self.router.set_url(path, name, wrapped_func)
            return wrapped_func
        return wrapper

