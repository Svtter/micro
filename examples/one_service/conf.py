import pathlib
from typing import List, Type
from micro.service import BaseService

BASE_DIR = pathlib.Path(__file__).parent

# Way 1
# Django import style.
# Or use class ..?
service_list = [
    'work_service'
]


# Way 2 
from .work_service.service import Service as WorkSerivce
service_list = [
    WorkSerivce,
]

"""
通过类加载 workService；
使用对应的类初始化
"""

# Way 3

class Conf:
    service_list: List[Type[BaseService]] = [
        WorkSerivce
    ]

    