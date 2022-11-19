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
    real_position: Position_2D = None
    threshold: int = 20
    x_threshold: int = 2
    y_threshold: int = 2

    def __init__(self, aruco: IAruco, tropa: ITropa, position: Position_2D):
        super().__init__(aruco, tropa, position)

    def Execute_Command(self):
        if not self.Have_Finished_Command():
            if self.real_position is None:
                return


            if (self.position.x - self.real_position.x) > self.x_threshold:
                if self.real_position.angle != 0:
                    if 90 <= self.real_position.angle <= 180:                        
                        self.tropa.Turn_Right()
                    else:
                        self.tropa.Turn_Left()
                else:
                    self.tropa.Move_Forward()
            elif (self.real_position.x - self.position.x) > self.x_threshold:
                if self.real_position.angle != 180:
                    if 270 <= self.real_position.angle <= 360:                        
                        self.tropa.Turn_Right()
                    else:
                        self.tropa.Turn_Left()
                else:
                    self.tropa.Move_Forward()
            elif (self.position.y - self.real_position.y) > self.y_threshold:
                if self.real_position.angle != 270:
                    if 0 <= self.real_position.angle <= 90:                        
                        self.tropa.Turn_Right()
                    else:
                        self.tropa.Turn_Left()
                else:
                    self.tropa.Move_Forward()
            elif (self.real_position.y - self.position.y) > self.y_threshold:
                if self.real_position.angle != 90:
                    if 180 <= self.real_position.angle <= 270:                        
                        self.tropa.Turn_Right()
                    else:
                        self.tropa.Turn_Left()
                else:
                    self.tropa.Move_Forward()

    def Have_Finished_Command(self) -> bool:
        real_position = self.aruco.Get_Position_Of_Aruco(self.tropa.id)

        if real_position is None:
            self.real_position = None
            return

        # TODO: Cambiar de self.tropa.position.angle a la posición que devuelva el Get_Position_Of_Aruco
        self.real_position = Position_2D([real_position[0], real_position[1], self.tropa.position.angle])

        return (
            self.distance.Manhattan(self.real_position, self.position) < self.threshold
        )

    def Get_Type(self):
        return type(self)

    def Equal(self, command):
        return (
            self.Get_Type() == command.Get_Type() and self.tropa.id == command.tropa.id
        )


if __name__ == "__main__":
    from Tropas.Tropa import Tropa

    tropa = Tropa(1, None, None, Position_2D([0, 0, 0]))
    test = Command_Go_To_2D_Position(tropa, Position_2D([0, 0, 0]))
    print(test.Have_Finished_Command())
