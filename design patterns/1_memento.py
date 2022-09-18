'''
Allows restoring an object to a previous state.
'''

class Originator:
    def __init__(self) -> None:
        self.content: str 

    def createState(self):
        pass

    def restoreState(self, state):
        pass 
    

class Memento:
    def __init__(self,content :str) -> None:
        self.content:str = content


class CareTaker:
    def __init__(self) -> None:
        self.states :list

    def push(self, state):
        self.states.append(state)

    def pop(self):
        self.states.pop()
