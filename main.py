"""
定义 url 的时候，其实就是定义函数的时候

定义 url，其实就是定义路由
定义 views，其实就是定义方法

可以继承一个新的类，来生成 views 所需要的参数。
"""

from typing import Callable
import bidict


class Router:
    def __init__(self) -> None:
        self.url_dict = {}
        self.name_dict = {}
        self.url_name = bidict({})

    def set_url(self, path: str, name: str, func: Callable):
        self.url_dict[path] = func
        self.name_dict[name] = func
        self.url_name[path] = name

    def get_func_by_name(self, name: str) -> Callable:
        return self.name_dict[name]

    def get_func(self, path: str) -> Callable:
        return self.url_dict[path]


class BaseService:
    def __init__(self) -> None:
        self.router = Router()

    def api(self, path: str, name: str):
        """
        set url
        """
        def wrapper(func):
            self.router.set_url(path, name, func)
        return wrapper


class Service(BaseService):
    name = 'WorkSerivce'

service = Service()


class Function:
    @service.api('/hello', name='hello')
    def hello(self):
        print('world')

