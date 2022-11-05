import sys
import os
import numpy as np

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))


from ITropa import ITropa


class FakeTropa(ITropa):
    matrix = None
    footprint = None
    pos_x = None
    pos_y = None
    orientacion = None  # 0 (>) | 90 (^) | 180 (<) | 270 (v)

    def __init__(self, id, communication, color, matrix, footprint):
        if not self.isValidFootPrint(matrix, footprint):
            raise ValueError("The size of the Tropa is bigger than the matrix provided")

        self.matrix = matrix
        self.footprint = footprint
        self.marix = matrix
        [self.max_x, self.max_y, _] = matrix.shape
        super().__init__(id, communication, color)

    def isValidFootPrint(self, matrix, footprint):
        for dimension in range(footprint.ndim):
            if (matrix.shape[dimension] < footprint.shape[dimension]):
                return False
        return True;

    def Place_Tropa(self, pos_x, pos_y):
        return

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

    def Turn_Right(self):
        self.orientacion = (self.orientacion - 90) % 360

    def Update_Matrix(self, pos_x, pos_y):
        return
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
    matrix = np.zeros((10,10,3))
    footprint = np.zeros((11,10,3))
    prueba = FakeTropa(1, None, None, matrix, footprint)
    for i in range(11):
        prueba.Move_Forward()

    