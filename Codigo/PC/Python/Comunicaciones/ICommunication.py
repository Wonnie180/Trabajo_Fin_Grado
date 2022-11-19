from abc import abstractmethod, ABCMeta
from numpy import uint8


class ICommunication(metaclass=ABCMeta):

    devices = []
    selected_device = []
    _interface = []
    
    received_data: any
    sended_data: any

    def __init__(self):
        super().__init__()

    @abstractmethod
    def Search_Devices(self):
        pass

    @abstractmethod
    def Get_Devices(self):
        pass

    @abstractmethod
    def Send_Data(self, action: uint8, data: list[uint8]):
        pass

    @abstractmethod
    def Get_Data(self):
        pass
