from abc import abstractmethod, ABCMeta
from numpy import uint8


class IAruco(metaclass=ABCMeta):
    current_id : uint8 = 0
    dictionary: any
    detector_parameters: any
    corners : any = []
    ids: any = []
    rejected: any = []

    def __init__(self, dictionary, detector_parameters):
        self.dictionary = dictionary
        self.detector_parameters = detector_parameters
        super().__init__()

    @abstractmethod
    def Get_Current_Id(self):
        pass

    @abstractmethod
    def Generate_new_Id(self, size: int):
        pass

    @abstractmethod
    def Detect_Aruco(self, frame):
        pass

    @abstractmethod
    def Get_Position_Of_Aruco(self, id):
        pass
