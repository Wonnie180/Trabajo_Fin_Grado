import sys
import os
from numpy import uint8
from abc import abstractmethod, ABCMeta

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from Comunicaciones.ICommunication import ICommunication
from Leds.ILed import ILed


class ITropa(metaclass=ABCMeta):
    id: uint8 = 0
    communication: ICommunication = None
    color: ILed = None

    def __init__(self, id: uint8, communication: ICommunication, color: ILed):
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
