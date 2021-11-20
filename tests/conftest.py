import pytest
from micro.web import app
from .utils import start_background


@pytest.fixture
def main_app():
    start_background(app.get_app('default').run)
    yield app

