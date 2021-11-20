"""
定义 url 的时候，其实就是定义函数的时候

定义 url，其实就是定义路由
定义 views，其实就是定义方法

可以继承一个新的类，来生成 views 所需要的参数。
"""

# Parser should be applied to create name ...
from micro.service import BaseService

# Use core_app ... to make debug avaliable.
from micro.web import app
import logging


def obtain_logger():
    logger = logging.getLogger('micro.main')
    logger.setLevel(logging.DEBUG)
    log_formatter = logging.Formatter(fmt=' %(name)s :: %(levelname)-8s :: %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(log_formatter)
    logger.addHandler(handler)
    return logger


logger = obtain_logger()


class Service(BaseService):
    """
    evert time a service was defined, 
    it should be added to a service list.
    """
    name = 'WorkSerivce'


# Is this must be ...?
service = Service()


# The name of this is function?
class Functions:
    # Or use another way
    # like .. get('workService').api('/hello')
    @service.api('/hello', name='hello')
    def hello(self):
        logger.info("I'm ..., I've being called!")
        return {'hello': 'world'}


# It has its own web server.
# Might be flask?


def main():
    """
    The entrypoint ...
    """

    # The app could be start by others ..?
    # app.run()

    # make call
    f = Functions()

    # This call should be in service.
    logger.info(f.hello())


if __name__ == "__main__":
    main()
    