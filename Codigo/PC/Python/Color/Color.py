import os
import sys
from typing import List
from numpy import uint8

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep)
)

class Color():
    r: uint8
    g: uint8
    b: uint8
    RGB: List[uint8]
    BGR: List[uint8]

    def __init__(self, RGB: List[int]):
        self.Set_RGB(RGB)

    def Set_RGB(self, RGB: List[int]):
        self.r = RGB[0]
        self.g = RGB[1]
        self.b = RGB[2]
        self.RGB = RGB
        self.BGR = RGB[::-1]