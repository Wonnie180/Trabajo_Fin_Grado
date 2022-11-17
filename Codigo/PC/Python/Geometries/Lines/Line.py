import os
import sys
from typing import List
import cv2

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep+".." + os.path.sep)
)

class Line():
    begin: List[int]
    end: List[int]

    def __init__(self,begin: List[int], end: List[int]):
        self.begin = begin
        self.end = end