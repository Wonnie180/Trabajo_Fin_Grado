import os
import sys
import cv2

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep + ".." + os.path.sep)
)

from ICommand_Go_To_Position import ICommand_Go_To_Position
from Tropas.ITropa import ITropa
from Positions.Position_2D import Position_2D
from Arucos.IAruco import IAruco
from Utils.Distances import Distance
from time import sleep

class Command_Go_To_2D_Position(ICommand_Go_To_Position):
    distance: Distance = Distance()
    real_position:any = None
    threshold: int = 30

    def __init__(self, aruco: IAruco, tropa: ITropa, position: Position_2D):
        super().__init__(aruco, tropa, position)

    def Execute_Command(self):
        if not self.Have_Finished_Command():
            if self.real_position is None:
                return
            self.tropa.Move_Forward()

    def Have_Finished_Command(self) -> bool:
        self.real_position = self.aruco.Get_Position_Of_Aruco(self.tropa.id)
        if self.real_position is None:
            return False
        return self.distance.Manhattan(self.real_position, [self.position.x, self.position.y]) < self.threshold


if __name__ == "__main__":
    from Tropas.Tropa import Tropa

    tropa = Tropa(1, None, None, Position_2D([0, 0, 0]))
    test = Command_Go_To_2D_Position(tropa, Position_2D([0, 0, 0]))
    print(test.Have_Finished_Command())
