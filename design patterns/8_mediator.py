'''
Allows an object to encapsulate the communicaton between other objects.
'''

from abc import ABC


class Mediator(ABC):
    pass 

class Colleague(ABC):
    pass 

class ConcreteMediator(Mediator):
    pass 

class ConcreteColleague(Colleague):
    pass

