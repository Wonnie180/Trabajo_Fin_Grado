import os
import sys

from numpy import ndarray, unsignedinteger, ones, uint8
import math

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

CONST_180_DIV_PI = 180 / math.pi


class Angle:
    def Get_Angle_Between_Points_CounterClock(self, position_1, position_2):
        return (
            math.atan2(position_1[0] - position_2[0], -(position_1[1] - position_2[1]))
            * CONST_180_DIV_PI
        )

    def Is_Angle_In_Range(self, angle, low_t, high_t):
        if low_t < high_t:
            return low_t <= angle <= high_t
        else:
            if angle > low_t:
                angle -= 360
            low_t = low_t - 360
            return low_t <= angle <= high_t

    def Get_Difference_Between_Angles(self, angle_origin, angle_destination):
        difference = abs(angle_origin - angle_destination)
        return min(difference, 360 - difference)

    def Get_Difference_Between_Angles_CounterClock(
        self, angle_origin, angle_destination
    ):
        return (angle_destination - angle_origin) % 360

    def Get_Nearest_Angle_Step(self, angle, angle_step):
        return (round(float(angle) / angle_step) * angle_step) % 360


if __name__ == "__main__":
    i = 0
