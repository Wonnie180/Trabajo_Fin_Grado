from abc import abstractmethod, ABCMeta
from enum import Enum
from numpy import uint8


class TROPA_ACTIONS(Enum):
    MOVE_FORWARD = 0
    MOVE_BACKWARD = 1
    TURN_LEFT = 2
    TURN_RIGHT = 3
    CHANGE_COLOR = 4
    
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
    def Send_Data(self, action: TROPA_ACTIONS, data: list[uint8]):
        pass

    @abstractmethod
    def Get_Data(self):
        pass
