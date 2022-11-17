import os
import sys
from typing import List
import cv2

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep + ".." + os.path.sep)
)

from Geometries.Lines.Line import Line
from Color.Color import Color


class Line_Drawable(Line):
    color: Color
    thickness: int

    def __init__(
        self, begin: List[int], end: List[int], color: Color, thickness: int = 2
    ):
        self.color = color
        self.thickness = thickness
        super().__init__(begin, end)

    def Draw_To_Frame(self, frame: any):
        cv2.line(frame, self.begin, self.end, self.color.BGR, self.thickness)
