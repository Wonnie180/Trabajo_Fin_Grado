from abc import abstractmethod, ABCMeta
import os
import sys

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep + "Utils")
)

from Utils.Resolution import Resolution

class IVideoSource(metaclass=ABCMeta):
    has_new_frame: bool = False
    resolution: Resolution = None

    def __init__(self, resolution: Resolution):
        self.resolution = resolution
        super().__init__()

    @abstractmethod
    def Has_New_Frame(self):        
        pass

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


if __name__ == "__main__":
    print("Hello")
    print("AAA")
    print("BBB")
    print("CCC")
