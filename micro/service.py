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
            self.router.set_url(path, name, func)
        return wrapper

