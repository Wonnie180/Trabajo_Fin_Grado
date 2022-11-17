from abc import abstractmethod, ABCMeta
import os
import sys
from typing import List

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from Commands.ICommand import ICommand

class Runnable(metaclass=ABCMeta):
    has_to_stop: bool = False

    def __init__(self):        
        super().__init__()

    @abstractmethod
    def Run(self):
        pass

    @abstractmethod
    def Stop(self):
        pass

    