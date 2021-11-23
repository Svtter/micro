# load_service could obtain current service.
# load_logger could obtain current logger

from .router import router
from .logger import logger


"""
我想直接可以使用 service 赋值
"""

# The name of this is function?
class ViewFunctions:
    router = router
    def __init__(self, client) -> None:
        # Give a client to let service know who is calling.
        self.client = client

    # Or use another way
    # like .. get('workService').api('/hello')
    @router.api('/hello', name='hello')
    def hello(self):
        logger.info("I'm ..., I've being called!")
        return {'hello': 'world'}
