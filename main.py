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


class Service(BaseService):
    """
    evert time a service was defined, 
    it should be added to a service list.
    """
    name = 'WorkSerivce'


# Is this must be ...?
service = Service()


# The name of this is function?
class Function:
    # Or use another way
    # like .. get('workService').api('/hello')
    @service.api('/hello', name='hello')
    def hello(self):
        print('world')


# It has its own web server.
# Might be flask?


def main():
    """
    The entrypoint ...
    """
    app.run()


if __name__ == "__main__":
    main()
    