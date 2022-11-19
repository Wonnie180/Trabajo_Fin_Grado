import os
import sys

from numpy import ndarray, unsignedinteger, ones, uint8

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep)
)

from Positions.Position_2D import Position_2D

class Distance:

    def Manhattan(self, p1: Position_2D, p2: Position_2D):
        return sum(abs(value1 - value2) for value1, value2 in zip(p1.Get_Position()[:-1], p2.Get_Position()[:-1]))
    



if __name__ == '__main__':
    i = 0
