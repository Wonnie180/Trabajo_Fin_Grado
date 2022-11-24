import os
import sys

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep)
)

from Utils.Frame import Frame
from IVideoSource import IVideoSource

class FakeVideo(IVideoSource):
    frame : Frame

    def __init__(self, frame: Frame):
        self.frame = frame
        self.frame.AddObserver(self)
        self.fps = 30
        super().__init__(frame.resolution)

    def Get_Frame(self):
        return self.frame.frame

    def Get_FPS(self):
        return self.fps

    def Set_FPS(self, fps):
        self.fps = fps

    def Set_Resolution(self, resolution):
        pass

    def Get_Resolution(self):
        return self.frame.resolution

    def __call__(self):
        self.has_new_frame = True


if __name__ == "__main__":
    from Utils.Resolution import Resolution
    prueba = FakeVideo(Frame(Resolution(800,800)))
    print(prueba.Get_Frame())

