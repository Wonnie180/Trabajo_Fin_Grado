import sys
import os

if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

from ITropa import ITropa, TROPA_ACTIONS
from Color.Color import Color
from Positions.Position_2D import Position_2D

class Tropa(ITropa):
    degree_step = 45
    distance_step = 2
    position: Position_2D = Position_2D([0,0,0])

    def Move_Forward(self):
        self.is_moving = True
        self.communication.Send_Data(TROPA_ACTIONS.MOVE_FORWARD, True)
        self.is_moving = False

    def Move_Backwards(self):
        self.is_moving = True
        self.communication.Send_Data(TROPA_ACTIONS.MOVE_BACKWARD, True)
        self.is_moving = False

    def Turn_Left(self):
        self.is_moving = True
        self.communication.Send_Data(TROPA_ACTIONS.TURN_LEFT, True)
        self.is_moving = False

    def Turn_Right(self):
        self.is_moving = True
        self.communication.Send_Data(TROPA_ACTIONS.TURN_RIGHT, True)
        self.is_moving = False

    def Set_Color(self, color: Color):
        return super().Set_Color(color)

    def Is_Moving(self):
        return self.is_moving