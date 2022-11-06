from pickletools import uint8
import sys
import os
import numpy as np
import cv2

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep + "Leds"))
sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep + "Aruco"))
sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep + "Comunicaciones")
)


from ICommunication import ICommunication
from ILed import ILed
from Led import Led
from ITropa import ITropa
from Aruco import Aruco


class FakeTropa(ITropa):
    matrix: np.ndarray = None
    footprint: np.ndarray = None
    pos_x: np.uint32 = None
    pos_y: np.uint32 = None
    orientacion: np.uint16 = None  # 0 (>) | 90 (^) | 180 (<) | 270 (v)

    def __init__(
        self,
        id: uint8,
        communication: ICommunication,
        color: ILed,
        matrix: np.ndarray,
        footprint: np.ndarray,
    ):

        if not self.isValidFootPrint(matrix, footprint):
            raise ValueError("The size of the Tropa is bigger than the matrix provided")

        self.footprint = self.Generate_Footprint(footprint, color)
        self.matrix = matrix
        [self.max_x, self.max_y, _] = matrix.shape
        super().__init__(id, communication, color)

    def isValidFootPrint(self, matrix, footprint):
        ndim = 2
        for dimension in range(ndim):
            if matrix.shape[dimension] < footprint.shape[dimension]:
                return False
        return True

    def Get_Footprint(self):
        return self.footprint

    def Generate_Footprint(self, footprint, color):
        #ootprint[np.all(footprint == (255, 255, 255), axis=-1)] = color.Get_RGB()
        return footprint

    def Place_Tropa(self, pos_x, pos_y, orientation):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.orientacion = orientation
        self.matrix[
            pos_x : pos_x + self.footprint.shape[0],
            pos_y : pos_y + self.footprint.shape[1],
            :,
        ] = self.footprint

    def Move_Forward(self):
        pos_y = self.pos_y
        pos_x = self.pos_x

        if self.orientacion == 0:
            pos_y += 1
        elif self.orientacion == 90:
            pos_x -= 1
        elif self.orientacion == 180:
            pos_y -= 1
        elif self.orientacion == 270:
            pos_x += 1

        self.Update_Matrix(pos_x, pos_y)

    def Move_Backwards(self):
        pos_y = self.pos_y
        pos_x = self.pos_x

        if self.orientacion == 0:
            pos_y -= 1
        elif self.orientacion == 90:
            pos_x += 1
        elif self.orientacion == 180:
            pos_y += 1
        elif self.orientacion == 270:
            pos_x -= 1

        self.Update_Matrix(pos_x, pos_y)

    def Turn_Left(self):
        self.orientacion = (self.orientacion + 90) % 360
        self.footprint = np.rot90(self.footprint, 1)
        self.Update_Matrix(self.pos_x, self.pos_y)

    def Turn_Right(self):
        self.orientacion = (self.orientacion - 90) % 360
        self.footprint = np.rot90(self.footprint, 3)
        self.Update_Matrix(self.pos_x, self.pos_y)
        

    def Update_Matrix(self, pos_x, pos_y):
        self.matrix[
            self.pos_x : self.pos_x + self.footprint.shape[0],
            self.pos_y : self.pos_y + +self.footprint.shape[1],
            :,
        ] = (0, 0, 0)

        self.matrix[
            pos_x : pos_x + self.footprint.shape[0],
            pos_y : pos_y + self.footprint.shape[1],
            :,
        ] = self.footprint

        self.pos_x = pos_x
        self.pos_y = pos_y
        # return
        # if not (
        #     (0 <= pos_x + (self.size // 2) < self.max_x)
        #     and (0 <= pos_y + (self.size // 2) < self.max_y)
        # ):
        #     return

        # pos_nueva = self.matrix[pos_x : pos_x + self.size, pos_y : pos_y + self.size]

        # # if np.any((pos_nueva != self.id) & (pos_nueva != 0)):
        # #     print(pos_nueva)
        # #     return

        # self.matrix[
        #     self.pos_x : self.pos_x + self.size, self.pos_y : self.pos_y + self.size
        # ] = 0

        # self.pos_x = pos_x
        # self.pos_y = pos_y

        # self.matrix[
        #     self.pos_x : self.pos_x + self.size, self.pos_y : self.pos_y + self.size
        # ] = self.id


if __name__ == "__main__":
    aruco = Aruco()
    aruco.Generate_Dictionary()
    footprint = cv2.cvtColor(aruco.Generate_new_Id(), cv2.COLOR_BGR2RGB)

    matrix = np.zeros([600, 600, 3])
    led = Led(255, 0, 0)
    prueba = FakeTropa(1, None, led, matrix, footprint)
    prueba.Place_Tropa(0, 0, 0)
    for i in range(11):
        prueba.Move_Forward()

    cv2.imshow(prueba.Get_Footprint())
    cv2.waitKey(0)

