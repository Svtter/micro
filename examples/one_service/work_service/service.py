# Parser should be applied to create name ...
from micro.service import BaseService
from .views import ViewFunctions


class Service(BaseService):
    """
    every time a service was defined, 
    it should be added to a service list.
    """
    name = 'WorkService'
    views = ViewFunctions


# Is this must be ...?
# service = Service()