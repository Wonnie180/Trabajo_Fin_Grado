from abc import abstractmethod, ABCMeta

from Resolution import Resolution


class IVideoSource(metaclass=ABCMeta):
    
    def __init__(self, resolution : Resolution):    
        super().__init__()

    @abstractmethod
    def Get_Frame(self):
        pass

    @abstractmethod
    def Get_FPS(self):
        pass

    @abstractmethod
    def Set_FPS(self, fps):
        pass

    @abstractmethod
    def Set_Resolution(self, resolution):
        pass

    @abstractmethod
    def Get_Resolution(self):
        pass


if __name__ == '__main__':
    print("Hello")
    print("AAA")
    print("BBB")
    print("CCC")
