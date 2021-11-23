from micro.client import Client


# Client
# As a user ... what do I want ?
# 这个调用应该是跨过不同的 server 和不同的 host
class WorkClient(Client):
    """
    I am writing this client...
    To test the service.
    To let another service use this client to call
    """
    def make_hello(self):
        service = self.get_service('workService')