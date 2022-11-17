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

class ICommand_Go_To_Position(ICommand, metaclass=ABCMeta):
    aruco: IAruco
    tropa: ITropa
    position: IPosition
    def __init__(self,aruco: IAruco, tropa:ITropa, position:IPosition):
        self.aruco = aruco
        self.tropa = tropa
        self.position = position
        super().__init__()

