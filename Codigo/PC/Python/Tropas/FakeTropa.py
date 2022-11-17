import sys
import os
import numpy as np
import cv2


if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from Comunicaciones.ICommunication import ICommunication
from Utils.Resolution import Resolution
from Color.Color import Color
from ITropa import ITropa
from Positions.Position_2D import Position_2D


class FakeTropa(ITropa):
    matrix: np.ndarray = None
    footprint: np.ndarray = None
    degrees_90 = 0

    def __init__(
        self,
        id: np.uint8,
        communication: ICommunication,
        color: Color,
        matrix: np.ndarray,
        footprint: np.ndarray,
        position: Position_2D,
    ):

        if not self.isValidFootPrint(matrix, footprint):
            raise ValueError("The size of the Tropa is bigger than the matrix provided")

        self.footprint = footprint
        self.matrix = matrix
        self.position = position
        super().__init__(id, communication, color, position)

    def isValidFootPrint(self, matrix, footprint):
        ndim = 2
        for dimension in range(ndim):
            if matrix.shape[dimension] < footprint.shape[dimension]:
                return False
        return True

    def Place_Tropa(self, position: Position_2D):
        self.position = position

        self.matrix[
            self.position.x : self.position.x + self.footprint.shape[0],
            self.position.y : self.position.y + self.footprint.shape[1],
            :,
        ] = self.footprint

    def Move_Forward(self):
        pos_y = self.position.y
        pos_x = self.position.x
        angle = self.position.angle

        if angle == 0:
            pos_y += 1
        if angle == 45:
            pos_y += 1
            pos_x -= 1
        elif angle == 90:
            pos_x -= 1
        elif angle == 135:
            pos_x -= 1
            pos_y -= 1
        elif angle == 180:
            pos_y -= 1
        elif angle == 225:
            pos_y -= 1
            pos_x += 1
        elif angle == 270:
            pos_x += 1
        elif angle == 315:
            pos_x += 1
            pos_y += 1

        self.Update_Matrix(pos_x, pos_y)

    def Move_Backwards(self):
        pos_y = self.position.y
        pos_x = self.position.x
        angle = self.position.angle

        if angle == 0:
            pos_y -= 1
        if angle == 45:
            pos_y -= 1
            pos_x += 1
        elif angle == 90:
            pos_x += 1
        elif angle == 135:
            pos_x += 1
            pos_y += 1
        elif angle == 180:
            pos_y += 1
        elif angle == 225:
            pos_y += 1
            pos_x -= 1
        elif angle == 270:
            pos_x -= 1
        elif angle == 315:
            pos_x -= 1
            pos_y -= 1

        self.Update_Matrix(pos_x, pos_y)

    def Turn_Left(self):
        self.position.angle = (self.position.angle + 90) % 360

        if self.position.angle % 90 == 0:
            self.footprint = np.rot90(self.footprint, 1)
            self.Update_Matrix(self.position.x, self.position.y)

    def Turn_Right(self):
        self.position.angle = (self.position.angle - 90) % 360
        self.footprint = np.rot90(self.footprint, 3)
        self.Update_Matrix(self.position.x, self.position.y)

    def Update_Matrix(self, pos_x, pos_y):
        self.matrix[
            self.position.x : self.position.x + self.footprint.shape[0],
            self.position.y : self.position.y + self.footprint.shape[1],
            :,
        ] = (255, 255, 255)

        self.matrix[
            pos_x : pos_x + self.footprint.shape[0],
            pos_y : pos_y + self.footprint.shape[1],
            :,
        ] = self.footprint

        self.position.Set_Position([pos_x, pos_y, self.position.angle])


if __name__ == "__main__":
    from Aruco.Aruco import Aruco
    from Leds.Led import Led

    resolution = Resolution(600, 600)

    aruco = Aruco()
    aruco.Generate_Dictionary()
    footprint = cv2.cvtColor(
        aruco.Generate_new_Id(Resolution(100, 100)), cv2.COLOR_BGR2RGB
    )

    frame = np.zeros([resolution.Get_Width(), resolution.Get_Height(), 3])
    led = Led(255, 0, 0)
    prueba = FakeTropa(1, None, led, frame, footprint, Position_2D([0, 0, 0]))

    prueba.Turn_Right()
    for i in range(50):
        prueba.Move_Forward()

    cv2.imshow("asas", frame)
    cv2.waitKey(0)