import pytest
from ..conf import Conf


"""
提供两种 fixure 或者 TestCase
分别用于启动实例测试和非启动实例测试

Client 本身也可以用于常规应用

用于记录请求，记录运行状态，日志，等等。
"""


@pytest.fixture
def work_service_cls():
    return Conf.service_list[0]
    