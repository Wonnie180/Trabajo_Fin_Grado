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


class Command_Go_To_2D_Position(ICommand_Go_To_Position):
    def __init__(self, tropa: ITropa, position: Position_2D):
        super().__init__(tropa, position)

    def Execute_Command(self):
        if not self.Have_Finished_Command():
            pass

    def Have_Finished_Command(self) -> bool:
        return self.tropa.position == self.position.x


if __name__ == "__main__":
    from Tropas.Tropa import Tropa

    tropa = Tropa(1, None, None, Position_2D([0, 0, 0]))
    test = Command_Go_To_2D_Position(tropa, Position_2D([0, 0, 0]))
    print(test.Have_Finished_Command())
