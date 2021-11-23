# The client could call service directly
# but only in other service or main threading.



class Client:
    """
    通过 TDD 的方式，允许自己编写 SDK
    """

    def __init__(self) -> None:
        self.service = None

    def get_service(self, name):
        return None
