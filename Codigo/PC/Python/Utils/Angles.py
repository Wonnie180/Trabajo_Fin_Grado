import os
import sys

from numpy import ndarray, unsignedinteger, ones, uint8
import math

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from Positions.Position_2D import Position_2D

CONST_180_DIV_PI = 180 / math.pi


class Angle:
    def Get_Angle_Between_Points_CounterClock(
        self, position_1: Position_2D, position_2: Position_2D
    ):
        return (
            math.atan2(position_1.x - position_2.x, -(position_1.y - position_2.y))
            * CONST_180_DIV_PI
        )

    def Get_Angle_Aruco(self, center, topLeft):
        angle = ((
            math.atan2(topLeft[1] - center[1], -(topLeft[0] - center[0]))
            * CONST_180_DIV_PI
        )+135) % 360
        
        return angle

    def Is_Angle_In_Range(self, real_angle, low_t, high_t):
        if low_t < high_t:
            return low_t <= real_angle <= high_t
        else:
            if (real_angle > low_t):
                real_angle -= 360
            low_t = low_t - 360
            return low_t <= real_angle <= high_t

    def Get_Difference_Between_Angles(self, angle_origin, angle_destination):
        difference = abs(angle_origin - angle_destination)
        return min(difference, 360 - difference)

    def Get_Difference_Between_Angles_CounterClock(
        self, angle_origin, angle_destination
    ):

        return (angle_destination - angle_origin) % 360

    def Get_Nearest_Angle_Step(self, angle, angle_step):
        return round(float(angle) / angle_step) * angle_step

    def Calculate_Angle(
        self, position_1: Position_2D, position_2: Position_2D, offset=0
    ):
        return (
            (
                math.atan2(position_1.x - position_2.x, position_1.y - position_2.y)
                * CONST_180_DIV_PI
                + 360
                + offset
            )
        ) % 360


if __name__ == "__main__":
    i = 0
