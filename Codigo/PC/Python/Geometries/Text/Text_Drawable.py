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


class Text_Drawable:
    topLeft: List[int]
    text: str
    color: Color
    thickness: int

    def __init__(
        self,
        topLeft: List[int],
        text: str,
        color: Color,
        thickness: int = 2,
    ):
        self.topLeft = topLeft
        self.text = text
        self.color = color
        self.thickness = thickness
        super().__init__()

    def Draw_To_Frame(self, frame: any):
        cv2.putText(
            frame,
            self.text,
            self.topLeft,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            self.color.BGR,
            self.thickness,
        )
