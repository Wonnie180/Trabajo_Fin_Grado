import os
import sys
from typing import List

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep + ".." + os.path.sep)
)

class Rectangle:
    topLeft: List[int]
    topRight: List[int]
    bottomLeft: List[int]
    bottomRight: List[int]

    def __init__(
        self,
        topLeft: List[int],
        topRight: List[int],
        bottomLeft: List[int],
        bottomRight: List[int],
    ):
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
        super().__init__()