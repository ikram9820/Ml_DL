'''
Allows an object notify other objects when its state changes.
'''

from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update():
        pass

class ConcreteObserver(Observer):
    def __init__(self) -> None:
        super().__init__()

    def update(self):
        pass

class Subject(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def attach(obs):
        pass

    @abstractmethod
    def detatch(obs):
        pass 

    def notify(self):
        pass 

class ConcreteSubject(Subject):
    def __init__(self) -> None:
        super().__init__()

    def attach(obs):
        return super().attach()

    def detatch(obs):
        return super().detatch()

    