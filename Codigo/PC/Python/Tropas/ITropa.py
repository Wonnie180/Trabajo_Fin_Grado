from enum import Enum
import sys
import os
from numpy import uint8
from abc import abstractmethod, ABCMeta

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from Comunicaciones.ICommunication import ICommunication
from Color.Color import Color
from enum import Enum


class TROPA_ACTIONS(Enum):
    MOVE_FORWARD = 0
    MOVE_BACKWARD = 1
    TURN_LEFT = 2
    TURN_RIGHT = 3
    CHANGE_COLOR = 4



class ITropa(metaclass=ABCMeta):
    id: uint8
    communication: ICommunication
    color: Color

    def __init__(self, id: uint8, communication: ICommunication, color: Color):
        self.id = id
        self.communication = communication
        self.color = color
        super().__init__()

    @abstractmethod
    def Move_Forward(self):
        pass

    @abstractmethod
    def Move_Backwards(self):
        pass

    @abstractmethod
    def Turn_Left(self):
        pass

    @abstractmethod
    def Turn_Right(self):
        pass
