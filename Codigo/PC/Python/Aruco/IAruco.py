from abc import abstractmethod, ABCMeta


class IAruco(metaclass=ABCMeta):
    current_id : int = 0
    dictionary = None
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
    def Generate_new_Id(self, img_size):
        pass

    @abstractmethod
    def Detect_Aruco(self):
        pass

    @abstractmethod
    def Draw_Detected_Aruco(self):
        pass


if __name__ == '__main__':
    print("Hello")
    print("AAA")
    print("BBB")
    print("CCC")
