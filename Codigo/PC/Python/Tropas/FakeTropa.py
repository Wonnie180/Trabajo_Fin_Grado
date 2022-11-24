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
from Utils.Angles import Angle
from time import sleep
angles = Angle()



class FakeTropa(ITropa):
    time_delay = 0.01
    matrix: np.ndarray = None
    footprint: np.ndarray = None
    degree_step = 45
    distance_step = 2
    movement_change = [
        [0, 1],  # 0 | 360
        [-1, 1],  # 45
        [-1, 0],  # 90
        [-1, -1],  # 135
        [0, -1],  # 180
        [1, -1],  # 225
        [1, 0],  # 270
        [1, 1],  # 315
    ]

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

    def Is_Moving(self):
        return self.is_moving

    def isValidFootPrint(self, matrix, footprint):
        ndim = 2
        for dimension in range(ndim):
            if matrix.shape[dimension] < footprint.shape[dimension]:
                return False
        return True

    def Move_Forward(self, degree_of_movement=90):
        self.communication.Send_Data(TROPA_ACTIONS.MOVE_FORWARD, True)
        self.is_moving = True

        pos_x, pos_y, angle = self.position.Get_Position()

        movement = self.Get_Movement_Parameters(angle, degree_of_movement)

        if movement is None:
            self.is_moving = False
            return

        for _ in range(self.distance_step):
            pos_x += movement[0]
            pos_y += movement[1]
            self.Update_Matrix(pos_x, pos_y)
        self.is_moving = False

    def Move_Backwards(self, degree_of_movement=90):
        self.communication.Send_Data(TROPA_ACTIONS.MOVE_BACKWARD, True)
        self.is_moving = True

        pos_x, pos_y, angle = self.position.Get_Position()

        movement = self.Get_Movement_Parameters(angle, degree_of_movement)

        if movement is None:
            self.is_moving = False
            return

        for _ in range(self.distance_step):
            pos_x -= movement[0]
            pos_y -= movement[1]
            self.Update_Matrix(pos_x, pos_y)
        self.is_moving = False

    def Turn_Left(self, forward: bool = True):
        self.communication.Send_Data(TROPA_ACTIONS.TURN_LEFT, True)

        self.Do_Turn(1, forward)

        if self.position.angle % 90 == 0:
            self.footprint = np.rot90(self.footprint, 1)
            self.Update_Matrix(self.position.x, self.position.y)

        self.is_moving = False

    def Turn_Right(self, forward: bool = True):
        self.communication.Send_Data(TROPA_ACTIONS.TURN_RIGHT, True)

        self.Do_Turn(-1, forward)

        if self.position.angle % 90 == 0:
            self.footprint = np.rot90(self.footprint, 3)
            self.Update_Matrix(self.position.x, self.position.y)

        self.is_moving = False

    def Do_Turn(self, angle_direction, forward: bool = True):
        do_movement = self.Move_Forward

        if not forward:
            do_movement = self.Move_Backwards
            angle_direction *= -1

        self.is_moving = True

        self.position.angle = (
                self.position.angle - (angle_direction * (self.degree_step))
            ) % 360

        n = 1
        for _ in range(n):
            self.position.angle = (
                self.position.angle + (angle_direction * (self.degree_step))
            ) % 360

            for _ in range(2*n):            
                do_movement(45)

            self.position.angle = (
                self.position.angle + (angle_direction * (self.degree_step))
            ) % 360

            for _ in range(n):            
                do_movement(45)

            self.position.angle = (
                self.position.angle - (2*(angle_direction * (self.degree_step)))
            ) % 360

        self.position.angle = (
                self.position.angle + (2*(angle_direction * (self.degree_step)))
            ) % 360
       

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
        sleep(self.time_delay)

    def Get_Movement_Parameters(self, angle, degree_of_movement=45):

        movement = None

        angle_step = 360 // len(self.movement_change)
        factor = angle_step / degree_of_movement
        
        angle_tolerance = degree_of_movement * factor
        lower_bound = (angle - angle_tolerance)
        high_bound = (angle + angle_tolerance) 

        test_angle = (degree_of_movement * factor)
        

        for i in range(len(self.movement_change)):
            if lower_bound < (test_angle * i % 360) <= high_bound:
                movement = self.movement_change[i] 
                break  
        return movement


if __name__ == "__main__":
    i = 0
