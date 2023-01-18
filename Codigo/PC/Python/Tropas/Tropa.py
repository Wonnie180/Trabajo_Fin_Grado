import sys
import os

if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

from ITropa import ITropa, TROPA_ACTIONS
from Color.Color import Color
from Positions.Position_2D import Position_2D

class Tropa(ITropa):
    verbose: bool = False
    position: Position_2D = Position_2D([0,0,0])

    def Move_Forward(self):
        self.is_moving = True
        self.communication.Send_Data(TROPA_ACTIONS.MOVE_FORWARD.value)
        if (self.verbose):
            print(f"Tropa {self.id} --> Forward")        
        self.is_moving = False

    def Move_Backwards(self):
        self.communication.Send_Data(TROPA_ACTIONS.MOVE_BACKWARD.value)
        if (self.verbose):
            print(f"Tropa {self.id} --> Backward") 
        self.is_moving = False

    def Turn_Left(self):
        self.is_moving = True
        self.communication.Send_Data(TROPA_ACTIONS.TURN_LEFT.value)
        if (self.verbose):
            print(f"Tropa {self.id} --> Left") 
        self.is_moving = False

    def Turn_Right(self):
        self.is_moving = True
        self.communication.Send_Data(TROPA_ACTIONS.TURN_RIGHT.value)
        if (self.verbose):
            print(f"Tropa {self.id} --> Right") 
        self.is_moving = False

    def Set_Color(self, color: Color):
        if (self.verbose):
            print(f"Tropa {self.id} --> SetColor: ",[color.r,color.g,color.b]) 
        self.communication.Send_Data(TROPA_ACTIONS.CHANGE_COLOR.value,[color.r,color.g,color.b])

        return super().Set_Color(color)

    def Is_Moving(self):
        return self.is_moving