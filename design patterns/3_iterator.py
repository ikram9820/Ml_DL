'''
Allows iterating over an object without having to expose 
the objet's internal structure (which may change in the future).
'''

from abc import ABC, abstractmethod


class Aggregate(ABC):
    def __init__(self) -> None:
        pass
    @abstractmethod
    def createIterator():
        pass

class Iterator(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def current(self):
        pass

    @abstractmethod
    def isDone(self):
        pass 

class ConcreteAggregate(Aggregate):
    pass

class ConcreteIterator(Iterator):
    pass




