'''
Allows passing different algorithms (behaviours) to an object.
'''

from abc import ABC


class Context:
    pass

class Strategy(ABC):
    pass 


class ConcreteStrategyA(Strategy):
    pass 

class ConcreteStrategyB(Strategy):
    pass 

