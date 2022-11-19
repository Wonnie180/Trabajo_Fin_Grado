import sys
import os
import numpy as np
import cv2


if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from ITropa import ITropa, TROPA_ACTIONS
from Comunicaciones.ICommunication import ICommunication
from Color.Color import Color
from Positions.Position_2D import Position_2D

class FakeTropa(ITropa):
    matrix: np.ndarray = None
    footprint: np.ndarray = None
    degrees_45 = 0
    position: Position_2D = None

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
        super().__init__(id, communication, color)

    def isValidFootPrint(self, matrix, footprint):
        ndim = 2
        for dimension in range(ndim):
            if matrix.shape[dimension] < footprint.shape[dimension]:
                return False
        return True

    def Move_Forward(self):
        self.communication.Send_Data(TROPA_ACTIONS.MOVE_FORWARD, True)
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
        self.communication.Send_Data(TROPA_ACTIONS.MOVE_BACKWARD, True)
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
        self.communication.Send_Data(TROPA_ACTIONS.TURN_LEFT, True)

        self.position.angle = (self.position.angle + 90) % 360

        if self.position.angle % 90 == 0:
            self.footprint = np.rot90(self.footprint, 1)
            self.Update_Matrix(self.position.x, self.position.y)

    def Turn_Right(self):
        self.communication.Send_Data(TROPA_ACTIONS.TURN_RIGHT, True)
        self.position.angle = (self.position.angle - 90) % 360
        self.footprint = np.rot90(self.footprint, 3)
        self.Update_Matrix(self.position.x, self.position.y)

    def Set_Color(self, color: Color):
        self.color = color
        self.communication.Send_Data(TROPA_ACTIONS.CHANGE_COLOR, Color.RGB)

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
    i = 0