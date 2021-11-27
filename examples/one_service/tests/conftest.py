import pytest
from ..conf import Conf


@pytest.fixture
def work_service_cls():
    return Conf.service_list[0]
    