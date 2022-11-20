import os
import sys
from typing import List
import cv2
from threading import Thread

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from VideoSource.IVideoSource import IVideoSource
from IVideoPlayback import IVideoPlayback
from AbleInterfaces.Runnable import Runnable

def Default_Action(video_playback):
    miliseconds_delay = 8
    mask_for_keypress = 0xFF
    key_pressed = cv2.waitKey(miliseconds_delay) & mask_for_keypress

    if key_pressed == ord("q"):
        video_playback.has_to_stop = True
    elif key_pressed == ord("r"):
        video_playback.rectangles = []


def Default_Callback(event, x, y, flags, param):
    self = param[0]
    if event == cv2.EVENT_LBUTTONDOWN:
        print("llamada callback de", self.title)


def click_drag_callback2(event, x, y, flags, param):
    self = param[0]
    if event == cv2.EVENT_LBUTTONDOWN:
        print("llamada callback2 de", self.title)
    #     self.Add_Coordinate_Rectangle((x, y))
    # elif event == cv2.EVENT_LBUTTONUP:
    #     self.Add_Coordinate_Rectangle((x, y))
    # elif event == cv2.EVENT_RBUTTONUP:
    #     self.Remove_Coordinate_Rectangle()


class CV2ImShow(IVideoPlayback, Runnable):
    action: callable = None
    callback: callable = None

    def __init__(
        self,
        title: str,
        videoSource: IVideoSource,
        action: callable = None,
        callback: callable = None,
    ):

        self.action = action
        self.callback = callback

        if self.action is None:
            self.action = Default_Action

        if self.callback is None:
            self.callback = Default_Callback
        super().__init__(title, videoSource)

    def Get_Title(self):
        return self.title

    def Draw_Frame(self):
        self.Initializate_Frame()
        cv2.imshow(self.title, self.frame)

  
    def Run(self):
        self.Draw_Frame()
        self.Add_Callback()
        self.action(self)
        while not self.has_to_stop:
            self.Draw_Frame()
            self.action(self)
        self.Destroy_Window()

    def Stop(self):
        self.has_to_stop = True
        
    def Initializate_Frame(self):
        self.frame = self.videoSource.Get_Frame().copy()

    def Add_Callback(self):
        cv2.setMouseCallback(self.title, self.callback, param=[self])

    def Destroy_Window(self):
        cv2.destroyWindow(self.title)


def Action_Video(video_playback: CV2ImShow):
    miliseconds_delay = 8
    mask_for_keypress = 0xFF
    key_pressed = cv2.waitKey(miliseconds_delay) & mask_for_keypress

    if key_pressed == ord("q"):
        video_playback.has_to_stop = True


def click_drag_callback(event, x, y, flags, param):
    self = param[0]
    if event == cv2.EVENT_LBUTTONDOWN:
        print("llamada callback de", self.title)
    #     self.Add_Coordinate_Rectangle((x, y))
    # elif event == cv2.EVENT_LBUTTONUP:
    #     self.Add_Coordinate_Rectangle((x, y))
    # elif event == cv2.EVENT_RBUTTONUP:
    #     self.Remove_Coordinate_Rectangle()


if __name__ == "__main__":

    from VideoSource.FakeVideo import FakeVideo
    from Utils.Resolution import Resolution
    from Utils.Frame import Frame

    resolution = Resolution(800, 800)
    common_frame = Frame(resolution)

    video_source = FakeVideo(common_frame)
    video_playback = CV2ImShow("Video TFG Luis", video_source)
    video_playback.Run()

    # Thread(target=video_playback.Play(), args=()).start()
