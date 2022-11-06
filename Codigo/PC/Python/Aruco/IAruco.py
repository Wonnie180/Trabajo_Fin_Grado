from abc import abstractmethod, ABCMeta


class IAruco(metaclass=ABCMeta):
    current_id : int = 0
    dictionary = None
    img_size = 0
    detector_parameters = None
    image_source = None



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

    @abstractmethod
    def Draw_Detected_Aruco(self, frame):
        pass

