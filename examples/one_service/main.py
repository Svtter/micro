"""
定义 url 的时候，其实就是定义函数的时候

定义 url，其实就是定义路由
定义 views，其实就是定义方法

可以继承一个新的类，来生成 views 所需要的参数。
"""

# Use core_app ... to make debug avaliable.
from micro.web import app


# It has its own web server.
# Might be flask?


def make_call():
    # make call
    # TODO[question]: 服务的调度，应该是可以自动补全的，还是不能自动补全的呢？
    # 运行时提醒？还是编码时提醒？
    c = WorkClient()
    f = ViewFunctions(c)

    # This call should be in service.
    # 直接调用是不可取的，容易产生依赖。我们应该采用其他的方法。
    logger.info(f.hello())


def main():
    """
    The entrypoint ...
    """

    # The app could be start by others ..?
    # app.run()
    app.register_service(service=service)
    service_app = app.get_app('WorkService')
    service_app.run()


if __name__ == "__main__":
    main()
    