from micro.client import Client


"""
每个 service 应该都要通过 TDD 来写
这样就可以满足 sdk 的要求

1. 同时我们也可以给用户生成对应的client
2. 也可以作为 sidecar 来提供微服务的帮助。
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
    def __init__(self, service_name) -> None:
        # workService 在运行之前应该被检查
        self.service_name = 'WorkService'
        super().__init__(service_name)

    def make_hello(self) -> dict:
        # 手写，为后续的调用者提供便利
        return self.get('/hello', data=None)