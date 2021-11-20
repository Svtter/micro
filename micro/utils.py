import threading
from typing import Callable


def start_background(func: Callable, daemon=True):
    thread = threading.Thread(target=func)
    thread.daemon = daemon
    thread.start()