from micro.client import Client


"""
每个 service 应该都要通过 TDD 来写
这样就可以满足 sdk 的要求

同时我们也可以给用户生成对应的client
"""

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