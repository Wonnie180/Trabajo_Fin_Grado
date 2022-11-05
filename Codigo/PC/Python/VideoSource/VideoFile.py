import os
import sys

if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

from IVideoSource import IVideoSource

class VideoFile(IVideoSource):
    file = ""
    
    def __init__(self, file):
        self.file = file;
        super().__init__()

    def Get_Frame(self):
        pass

    def Get_FPS(self):
        pass

    def Set_FPS(self, fps):
        self.fps = fps

    def Set_Resolution(self, resolution):
        self.resolution = resolution

    def Get_Resolution(self):
        pass


if __name__ == '__main__':
    prueba = VideoFile("asasasas")
    print(prueba.file)

