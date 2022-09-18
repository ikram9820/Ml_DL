'''
Allows adding new operations to an object structure without modifying it.
'''

from abc import ABC, abstractmethod

def Visitor(ABC):

    def visit(concreteElement):
        pass


class Element(ABC):
    @abstractmethod
    def accept(visitor:Visitor):
        pass

class ConcreteElementA(Element):
    def __init__(self) -> None:
        pass 

    def accept(self, visitor:Visitor):
        visitor.visit(self) 

class ConcreteElementB(Element):
    def __init__(self) -> None:
        pass 

    def accept(self, visitor:Visitor):
        visitor.visit(self)
