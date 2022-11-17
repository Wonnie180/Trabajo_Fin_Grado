import os
import sys
import cv2
from typing import List

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep + ".." + os.path.sep)
)

from Color.Color import Color
from Geometries.Circles.Circle import Circle


class Circle_Drawable(Circle):
    color: Color
    thickness: int

    def __init__(
        self,
        center: List[int],
        radius: int,
        color: Color,
        thickness: int = 2,
    ):
        self.color = color
        self.thickness = thickness
        super().__init__(center, radius)

    def Draw_To_Frame(self, frame: any):
        cv2.circle(frame,  self.center, self.radius, self.color.BGR, self.thickness)

