from enum import Enum
import sys
import os
from numpy import uint8
from abc import abstractmethod, ABCMeta

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))


from Positions.IPosition import IPosition
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
    position: IPosition
    is_moving: bool = False
    threshold_angle: int

    def __init__(self, id: uint8, communication: ICommunication, color: Color, threshold_angle: int = 5):
        self.id = id
        self.communication = communication
        self.color = color
        self.threshold_angle = threshold_angle
        super().__init__()

    @abstractmethod
    def Is_Moving(self):
        pass

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

    @abstractmethod
    def Set_Color(self, color: Color):
        pass
