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
from Geometries.Rectangles.Rectangle import Rectangle

class Rectangle_Drawable(Rectangle):
    color: Color
    thickness: int

    def __init__(
        self,
        topLeft: List[int],
        topRight: List[int],
        bottomLeft: List[int],
        bottomRight: List[int],
        color: Color,
        thickness: int = 2,
    ):
        self.color = color
        self.thickness = thickness
        super().__init__(topLeft, topRight, bottomLeft, bottomRight)

    def Draw_To_Frame(self, frame: any):
        cv2.line(frame, self.topLeft, self.topRight, self.color.BGR, self.thickness)
        cv2.line(frame, self.topRight, self.bottomRight, self.color.BGR, self.thickness)
        cv2.line(frame, self.bottomRight, self.bottomLeft, self.color.BGR, self.thickness)
        cv2.line(frame, self.bottomLeft, self.topLeft, self.color.BGR, self.thickness)
