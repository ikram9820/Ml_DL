'''
Allows an object to behave differently depending on the state it is in.
'''

import abc

class Context:
    def __init__(self) -> None:
        pass

    def request(self):
        pass 

class State(abc.ABC):
    def __init__(self) -> None:
        pass
    @abc.abstractmethod
    def handle(self):
        pass

class ConcreteStateA(State):
    def __init__(self) -> None:
        pass

    def handle(self):
        pass

class ConcreteStateB(State):
    def __init__(self) -> None:
        pass

    def handle(self):
        pass