from enum import Enum
import sys
import os
from typing import List
from numpy import uint8
from abc import abstractmethod, ABCMeta

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from Tropas.ITropa import ITropa
from Commands.ICommand import ICommand
from Aruco.IAruco import IAruco
from VideoSource.IVideoSource import IVideoSource
from VideoPlayback.IVideoPlayback import IVideoPlayback

from Positions.IPosition import IPosition


class IApp(metaclass=ABCMeta):
    tropas: List[ITropa]
    aruco: IAruco
    video_in: IVideoSource
    video_out: IVideoPlayback

    def __init__(
        self,
        tropas: List[ITropa],
        aruco: IAruco,
        video_in: IVideoSource,
        video_out: IVideoPlayback,
    ):
        self.tropas = tropas
        self.aruco = aruco
        self.video_in = video_in
        self.video_out = video_out
        super().__init__()

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
