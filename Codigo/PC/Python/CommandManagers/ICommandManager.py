from abc import abstractmethod, ABCMeta
import os
import sys
from typing import List

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from Commands.ICommand import ICommand

class ICommandManager(metaclass=ABCMeta):
    commands: List[ICommand] = []
    
    def __init__(self):        
        super().__init__()

    @abstractmethod
    def Add_Command(self, command: ICommand):
        pass

    @abstractmethod
    def Execute_Commands(self):
        pass