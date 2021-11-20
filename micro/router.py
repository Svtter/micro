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

