import os
import sys
import numpy as np
from ndarray_listener import ndl

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep + "Utils")
)

from Utils.Resolution import Resolution
from IVideoSource import IVideoSource

class FakeVideo(IVideoSource):
    frame = None
    has_new_frame: bool = False

    def __init__(self, resolution: Resolution, frame: ndl):
        self.frame = frame
        self.frame.talk_to(self)
        super().__init__(resolution)

    def Has_New_Frame(self):
        return self.has_new_frame

    def Get_Frame(self):
        self.has_new_frame = False
        return self.frame

    def Get_FPS(self):
        return self.fps

    def Set_FPS(self, fps):
        self.fps = fps

    def Set_Resolution(self, resolution):
        self.resolution = resolution

    def Get_Resolution(self):
        return self.resolution

    def __call__(self):
        self.has_new_frame = True


if __name__ == "__main__":
    resolution = Resolution(800, 800)
    fakeFrame = ndl(
        np.zeros([resolution.Get_Width(), resolution.Get_Width(), 3], dtype=np.uint8)
    )
    prueba = FakeVideo(resolution, fakeFrame)
    prueba.start()

