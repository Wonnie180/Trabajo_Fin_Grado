from abc import abstractmethod, ABCMeta
import os
import sys

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep + ".." + os.path.sep)
)

from Commands.ICommand import ICommand
from Tropas.ITropa import ITropa
from Positions.IPosition import IPosition
from Arucos.IAruco import IAruco
from Utils.Distances import Distance
from Utils.Angles import Angle

class ICommand_Go_To_Position(ICommand, metaclass=ABCMeta):
    aruco: IAruco
    tropa: ITropa
    real_position: IPosition
    objective_position: IPosition
    distance_threshold: int
    distance: Distance = Distance()
    angles: Angle = Angle()

    def __init__(self,aruco: IAruco, tropa:ITropa,objective_position:IPosition, distance_threshold:int):
        self.aruco = aruco
        self.tropa = tropa
        self.objective_position = objective_position
        self.distance_threshold = distance_threshold
        super().__init__()

