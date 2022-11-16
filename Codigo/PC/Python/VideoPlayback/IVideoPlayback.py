from abc import abstractmethod, ABCMeta
import os
import sys


if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        ".." + os.path.sep + "VideoSource",
    )
)
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        ".." + os.path.sep + "Aruco",
    )
)

from VideoSource.IVideoSource import IVideoSource
from Positions.Position_2D import Position_2D


class IVideoPlayback(metaclass=ABCMeta):
    has_to_stop: bool = False
    videoSource: IVideoSource = None
    callback: any = callable
    title: str = ""

    def __init__(self, title: str, videoSource: IVideoSource, callback: callable):
        self.videoSource = videoSource
        self.callback = callback
        self.title = title
        super().__init__()

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def Get_Title(self):
        pass

    @abstractmethod
    def Draw_Text(self, text: str, position: Position_2D):
        pass

    @abstractmethod
    def Draw_Rectangles(self, rectangles):
        pass
