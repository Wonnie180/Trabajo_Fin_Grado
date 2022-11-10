import os
import sys
import cv2


if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep)
)

from VideoSource.IVideoSource import IVideoSource
from Utils.Resolution import Resolution

class WebCam(IVideoSource):
    number_webcam: int = 0
    cap = None

    frame = None
    has_new_frame: bool = False

    def __init__(self, resolution: Resolution, number_webcam: int):
        self.number_webcam = number_webcam
        self.cap = cv2.VideoCapture(self.number_webcam, cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution.Get_Width())
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution.Get_Height())
        super().__init__(self.resolution)

    def Has_New_Frame(self):
        return True

    def Get_Frame(self):
        _, self.frame = self.cap.read()
        return self.frame

    def Get_FPS(self):
        return self.fps

    def Set_FPS(self, fps):
        self.fps = fps

    def Set_Resolution(self, resolution: Resolution):
        self.resolution = resolution
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution.Get_Width())
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution.Get_Height())

    def Get_Resolution(self):
        return self.resolution


if __name__ == "__main__":    
    from VideoPlayback.CV2ImShow import CV2ImShow
    from Aruco.Aruco import Aruco

    aruco = Aruco()
    aruco.Generate_Dictionary()

    video_source = WebCam(Resolution(1280, 720),0)
    video_playback = CV2ImShow("Prueba", video_source, aruco)

    video_playback.start()

