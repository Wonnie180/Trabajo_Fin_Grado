from abc import abstractmethod, ABCMeta
from pickletools import uint8


class ILed(metaclass=ABCMeta):
    R : int = 0
    G : int = 0
    B : int = 0

    def __init__(self, R:uint8, G:uint8, B:uint8):
        self.R = R
        self.G = G
        self.B = B
        super().__init__()

    @abstractmethod
    def Get_RGB(self):
        pass

    @abstractmethod
    def Set_RGB(self, R :int, G:int, B:int):
        pass

    @abstractmethod
    def Get_BGR(self):
        pass

    @abstractmethod
    def Set_BGR(self, B :int, G:int, R:int):
        pass   
