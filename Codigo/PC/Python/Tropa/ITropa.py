import sys
import os
from abc import abstractmethod, ABCMeta

sys.path.append(os.path.join(os.path.dirname(__file__),
                ".."+os.path.sep+"Comunicaciones"))

from ICommunication import ICommunication

class ITropa(metaclass=ABCMeta):
    def __init__(self, id, communication: ICommunication):
        self.communication = communication
        self.id = id
        self.rgb = (int, int, int)
        super().__init__()

    @abstractmethod
    def Set_Color(self, color):
        pass

    @abstractmethod
    def Get_Color(self):
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
