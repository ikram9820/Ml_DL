'''
Allows decouple a sender from a receiver. The sender will talk to 
the reveiver through a command. Commands can be undone and persisted.
'''

from abc import ABC, abstractmethod


class Invoker:
    def __init__(self) -> None:
        self.command:Command

    def operation(self):
        self.command.execute()


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Receiver:
    def __init__(self) -> None:
        pass

    def operation(self):
        pass

class ConcreteCommand(Command):
    def __init__(self) -> None:
        super().__init__()
        self.revceiver : Receiver

    def execute(self):
        self.revceiver.operation()

