'''
Allows building a chain of objects to process a request.
'''

from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def handle():
        pass 

class Sender:
    def __init__(self) -> None:
        self.handler : Handler

    def handle(self, request):
        self.handler.handle(request)


class ConcreteHandler1(Handler):
    def  __init__(self) -> None:
        pass 

    def handle():
        pass

class ConcreteHandler2(Handler):
    def __init__(self) -> None:
        pass 
    
    def handle():
        pass