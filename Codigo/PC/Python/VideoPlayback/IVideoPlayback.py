from abc import abstractmethod, ABCMeta
import os
import sys
from typing import List


if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from VideoSource.IVideoSource import IVideoSource

class IVideoPlayback(metaclass=ABCMeta):
    has_to_stop: bool = False
    videoSource: IVideoSource = None
    title: str = ""

    def __init__(self, title: str, videoSource: IVideoSource):
        self.videoSource = videoSource
        self.title = title
        super().__init__()

    @abstractmethod
    def Run(self):
        pass

    @abstractmethod
    def Draw_Frame(self):
        pass

    @abstractmethod
    def Get_Title(self):
        pass

    @abstractmethod
    def Has_To_Stop(self):
        pass
