# load_service could obtain current service.
# load_logger could obtain current logger
from micro.core import load_service, load_logger
from micro.service import api


service = load_service()
logger = load_logger()


# The name of this is function?
class ViewFunctions:
    def __init__(self, client, service) -> None:
        # Give a client to let service know who is calling.
        self.client = client
        self.service = service

    # Or use another way
    # like .. get('workService').api('/hello')
    @service.api('/hello', name='hello')
    def hello(self):
        logger.info("I'm ..., I've being called!")
        return {'hello': 'world'}

