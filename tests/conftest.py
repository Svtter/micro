import pytest
import sys
import threading
from micro.web import app


@pytest.fixture
def main_app():
    thread = threading.Thread(target=app.run)
    thread.daemon = True
    thread.start()
    yield app

