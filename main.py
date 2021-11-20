"""
定义 url 的时候，其实就是定义函数的时候

定义 url，其实就是定义路由
定义 views，其实就是定义方法

可以继承一个新的类，来生成 views 所需要的参数。
"""

from micro.service import BaseService


class Service(BaseService):
    """
    evert time a service was defined, 
    it should be added to a service list.
    """
    name = 'WorkSerivce'

service = Service()


class Function:
    @service.api('/hello', name='hello')
    def hello(self):
        print('world')

