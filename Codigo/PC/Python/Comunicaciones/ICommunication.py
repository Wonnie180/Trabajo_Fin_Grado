from abc import abstractmethod, ABCMeta


class ICommunication(metaclass=ABCMeta):
    devices = []
    selected_device = []
    _interface = [] 

    def __init__(self):
        super().__init__()

    @abstractmethod
    def Search_Devices(self):
        pass

    @abstractmethod
    def Get_Devices(self):
        pass

    @abstractmethod
    def Send_Data(self, data):
        pass

    @abstractmethod
    def Get_Data(self):
        pass
