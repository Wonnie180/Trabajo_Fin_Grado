from abc import abstractmethod, ABCMeta
from numpy import uint8


class ICommunication(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def Send_Data(self, action: uint8, data: list[uint8]):
        pass

    @abstractmethod
    def Get_Data(self):
        pass
