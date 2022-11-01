import sys
import os
from abc import abstractmethod, ABCMeta

sys.path.append(os.path.join(os.path.dirname(__file__),
                ".."+os.path.sep+"Comunicaciones"))

sys.path.append(os.path.join(os.path.dirname(__file__),
                ".."+os.path.sep+"Leds"))

from ICommunication import ICommunication
from ILed import ILed

class ITropa(metaclass=ABCMeta):
    id : int = 0
    communication : ICommunication = None
    color : ILed = None

    def __init__(self, id : int, communication: ICommunication, color : ILed):
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
