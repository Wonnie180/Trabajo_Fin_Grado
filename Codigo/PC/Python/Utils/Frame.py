import os
import sys

from ndarray_listener import ndl
from numpy import ndarray, unsignedinteger, ones, uint8
if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep)
)

from Utils.Resolution import Resolution


class Frame:
    resolution: Resolution
    color_depth: int
    frame: ndl
    
    def __init__(self, resolution:Resolution, color_depth: int=3):
        self.resolution = resolution
        self.color_depth = color_depth
        self.frame = ndl(
            ones([resolution.Get_Width(), resolution.Get_Width(), color_depth], dtype=uint8)
        ) * 255

    def Get_Width(self):
        return self.resolution.width

    def Get_Height(self):
        return self.resolution.height
    
    def Get_Color_Depth(self):
        return self.color_depth
    
    def Get_Frame(self):
        return self.frame

    def AddObserver(self, observer):
        self.frame.talk_to(observer)

    