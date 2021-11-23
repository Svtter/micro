from micro.router import Router


# allow plugin to hook in.
class WorkRouter(Router):
    pass


router = WorkRouter()
