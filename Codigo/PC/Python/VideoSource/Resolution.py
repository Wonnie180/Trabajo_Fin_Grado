import sys
import os

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))


class Resolution:
    width: int = 0
    height: int = 0

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def Get_Width(self):
        return self.width

    def Get_Height(self):
        return self.height

    def Is_In_Bounds(self, coordinates):
        return self._Is_In_Bounds(coordinates[0], coordinates[1])

    def _Is_In_Bounds(self, x, y):
        return (0 <= x < self.width) and (0 <= y < self.height)
