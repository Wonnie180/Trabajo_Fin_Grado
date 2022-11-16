from abc import abstractmethod, ABCMeta
from numpy import uint8


class ILed(metaclass=ABCMeta):
    R : int = 0
    G : int = 0
    B : int = 0

    def __init__(self, RGB: list[uint8]):
        self.R = RGB[0]
        self.G = RGB[1]
        self.B = RGB[2]
        super().__init__()

    @abstractmethod
    def Get_RGB(self) -> list[uint8]:
        pass

    @abstractmethod
    def Set_RGB(self, RGB:list[uint8]):
        pass

    @abstractmethod
    def Get_BGR(self) -> list[uint8]:
        pass

    @abstractmethod
    def Set_BGR(self, BGR: list[uint8]):
        pass   
