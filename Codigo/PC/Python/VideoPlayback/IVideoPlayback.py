from abc import abstractmethod, ABCMeta
import os
import sys


if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__),".." + os.path.sep + "VideoSource",))
sys.path.append(os.path.join(os.path.dirname(__file__),".." + os.path.sep + "Aruco",))

from VideoSource.IVideoSource import IVideoSource
from Aruco.IAruco import IAruco


class IVideoPlayback(metaclass=ABCMeta):
    videoSource : IVideoSource = None
    aruco : IAruco = None
    title : str = ""

    def __init__(self, title : str, videoSource : IVideoSource, aruco : IAruco):
        self.videoSource = videoSource
        self.aruco = aruco
        self.title = title
        super().__init__()

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def Get_Title(self):
        pass
    