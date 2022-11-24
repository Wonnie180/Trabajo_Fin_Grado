import os
import sys

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep + ".." + os.path.sep)
)

from ICommand_Go_To_Position import ICommand_Go_To_Position
from Tropas.ITropa import ITropa
from Positions.Position_2D import Position_2D
from Arucos.IAruco import IAruco
import math


# Pathfinding parcial : Que mire solo un par de casillas por delante
# Espacio de configuraciones ?


class Command_Go_To_2D_Position(ICommand_Go_To_Position):
    threshold_angle = 46
    previous_angle = 0
    real_position = None
    topLeft = None
    movement_angle = None

    def __init__(
        self,
        aruco: IAruco,
        tropa: ITropa,
        objective_position: Position_2D,
        distance_threshold: int = 20,
    ):
        if tropa.distance_step > distance_threshold:
            distance_threshold = tropa.distance_step

        super().__init__(aruco, tropa, objective_position, distance_threshold)

    def Execute_Command(self):
        if not self.Have_Finished_Command():

            if self.real_position is None:
                return

            new_angle = (
                self.angles.Get_Angle_Between_Points_CounterClock(
                    self.real_position.Get_Position(),
                    self.objective_position.Get_Position(),
                ) - 90
            ) % 360


            difference_between_previous_and_new_angle = (
                self.angles.Get_Difference_Between_Angles(new_angle, self.previous_angle)
            )

            # Evita el efecto "Peonza"
            if difference_between_previous_and_new_angle < self.threshold_angle:
                new_angle = self.previous_angle
            else:
                self.previous_angle = new_angle

            self.Movement_Action(new_angle)
        else:
            print("Tropa:", self.tropa.id, "Ha llegado a su destino...")

    def Have_Finished_Command(self) -> bool:
        if self.tropa.Is_Moving():
            return False

        position = self.aruco.Get_Position_Of_Aruco(self.tropa.id)
        
        if position is None:
            self.real_position = None
            return False

        self.real_position = Position_2D(position)

        return self.Have_Reached_Objective()

    def Get_Type(self):
        return type(self)

    def Equal(self, command):
        return (
            self.Get_Type() == command.Get_Type() and self.tropa.id == command.tropa.id
        )

    def Have_Reached_Objective(self):
        return (
            self.distance.Manhattan(self.real_position, self.objective_position)
            < self.distance_threshold
        )

    def Is_Facing_Objective(self, angle):
        low_angle = (angle - self.threshold_angle) % 360
        high_angle = (angle + self.threshold_angle) % 360
        return self.angles.Is_Angle_In_Range(
            self.real_position.angle, low_angle, high_angle
        )

    def Is_Back_Facing_Objective(self, angle):
        backwards_angle = (angle + 180) % 360
        return self.Is_Facing_Objective(backwards_angle)

    def Has_To_Rotate_Right(self, angle):
        return (
            self.angles.Get_Difference_Between_Angles_CounterClock(
                self.real_position.angle, angle
            )
            > 180
        )

    def Movement_Action(self, angle):
        if self.Is_Facing_Objective(angle):
            self.tropa.Move_Forward()
        elif self.Is_Back_Facing_Objective(angle):
            self.tropa.Move_Backwards()
        elif self.Has_To_Rotate_Right(angle):
            self.tropa.Turn_Right()
        else:
            self.tropa.Turn_Left()


if __name__ == "__main__":
    from Tropas.Tropa import Tropa
    from Arucos.Aruco import Aruco
    import math
    import numpy as np

    aruco = Aruco(None, None)
    tropa = Tropa(1, None, None)
    test = Command_Go_To_2D_Position(aruco, tropa, Position_2D([0, 0, 0]))
    # print(test.Get_Nearest_Angle_Step(100,45))

    #   Angulo 0-> [622, 508, 0] [554, 510, 0]
    # Angulo 90-> [556, 429, 0] [554, 510, 0] |
    # Angulo 0-> [559, 579, 0] [554, 510, 0] | 40
    # ngulo 180-> [487, 514, 0] [554, 510, 0] | 130

    Cx = 10
    Cy = 10

    x1 = 15
    y1 = 11

    radian = math.atan2(y1 - Cy, x1 - Cx)
    angle = (radian * (180 / math.pi)) % 360
    # if (angle < 0.0):
    #     angle += 360.0;

    print((angle - 135) % 360)

    exit()
    dy = 0
    dx = 0

    def getAngle(a, b, c):
        ang = math.degrees(
            math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0])
        )
        return ang + 360 if ang < 0 else ang

    def getAnglenp(a, b, c):
        ba = a - b
        bc = c - b

        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        return np.degrees(np.arccos(cosine_angle))

    a = [0, 0]
    # b = [559,578]
    pos_actual = [20, 100]
    obj = [20, 20]
    # c = [554, 510]
    # a = c-1
    print(a, pos_actual, obj)

    radian = math.atan2(pos_actual[1] - obj[1], pos_actual[0] - obj[0])
    angle = radian * (180 / math.PI)
    if angle < 0.0:
        angle += 360.0

    print(angle)

    exit()
    # a = np.array([6,0])
    # b = np.array([0,0])
    # c = np.array([0,6])

    print(getAngle(a, b, c))
    print(getAnglenp(a, b, c))
    print(test.Get_Nearest_Angle_Step(getAnglenp(a, b, c), 45))

    # angle  = math.degrees(math.atan2(float(dy), float(dx)))

    # print("θ =",angle,"°")
    # print("θ =",test.Get_Nearest_Angle_Step(angle,45),"°")
