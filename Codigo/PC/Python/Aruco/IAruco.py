from abc import abstractmethod, ABCMeta
from numpy import uint8

class IAruco(metaclass=ABCMeta):
    current_id : uint8 = 0
    dictionary = None
    detector_parameters = None

    def __init__(self):
        super().__init__()

    @abstractmethod
    def Generate_Dictionary(self):
        pass

    @abstractmethod
    def Obtain_Current_Id(self):
        pass

    @abstractmethod
    def Generate_new_Id(self):
        pass

    @abstractmethod
    def Detect_Aruco(self, frame):
        pass
