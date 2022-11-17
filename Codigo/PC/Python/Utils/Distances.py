import os
import sys

from numpy import ndarray, unsignedinteger, ones, uint8

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep)
)


class Distance:

    def Manhattan(self, p1, p2):
        return sum(abs(value1 - value2) for value1, value2 in zip(p1, p2))
    