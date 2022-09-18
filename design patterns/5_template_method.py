'''
Allows defining a template (skeleton) for an operation. Specific 
steps will then be implemented in subclasses.
'''

from abc import ABC, abstractmethod


class Abstract(ABC):
    def __init__(self) -> None:
        super().__init__()

    def templateMethod():
        pass 

    @abstractmethod
    def primitiveOperation1():
        pass

    @abstractmethod
    def primitiveOperation2():
        pass 

class Concrete(Abstract):
    def __init__(self) -> None:
        super().__init__()

    def primitiveOperation1():
        pass

    def primitiveOperation2():
        pass
    