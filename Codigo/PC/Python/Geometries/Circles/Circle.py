import os
import sys
from typing import List

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep+".."+os.path.sep)
)


class Circle():
    center: List[int]
    radius: int
    diameter: int

    def __init__(self,center: List[int], radius: int ):
        self.center = center
        self.radius = radius
        self.diameter = radius * 2
