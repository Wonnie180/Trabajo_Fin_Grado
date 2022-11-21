import os
import sys

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from IPosition import IPosition

class Position_2D(IPosition):
    x: int = 0
    y: int = 0
    angle: int = 0

    def __init__(self, position: list[int]):
        self.Set_Position(position)
        super().__init__()

    def Set_Position(self, new_position: list[int]):
        self.Check_Position_Length(new_position)
        self.x = new_position[0]
        self.y = new_position[1]
        self.angle = new_position[2]

    def Get_Position(self):
        return [self.x, self.y, self.angle]

    def Check_Position_Length(self, position: list[int]):
        if len(position) != 3:
            raise ValueError("Wrong length given for position Position_2D")

    def Equals(self, position: IPosition, offset=0):
        return  self.x - offset <= position.x <= self.x+offset and \
                self.y - offset <= position.y <= self.y+offset

        

if __name__ == "__main__":
    test = Position_2D([1, 2,3])
    print(test.Get_Position())
