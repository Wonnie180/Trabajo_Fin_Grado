from abc import abstractmethod, ABCMeta
import os
import sys

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep + ".." + os.path.sep+ ".." + os.path.sep)
)

from Commands.Command_Go_To_Position.ICommand_Go_To_Position import ICommand_Go_To_Position
from Tropas.ITropa import ITropa
from Positions.IPosition import IPosition
from Arucos.IAruco import IAruco
from Utils.Distances import Distance
from Utils.Angles import Angle

class ICommand_Go_To_Position_2D(ICommand_Go_To_Position, metaclass=ABCMeta):
    threshold_angle: int

    def __init__(self,aruco: IAruco, tropa:ITropa, objective_position:IPosition, distance_threshold:int):
        self.aruco = aruco
        self.tropa = tropa
        self.objective_position = objective_position
        self.distance_threshold = distance_threshold
        super().__init__(aruco, tropa, objective_position, distance_threshold)

    @abstractmethod
    def Is_Facing_Objective(self, angle):
        pass

    @abstractmethod
    def Is_Back_Facing_Objective(self, angle):
       pass

    @abstractmethod
    def Has_To_Rotate_Right(self, angle):
        pass

    @abstractmethod
    def Movement_Action(self, angle):
        pass

