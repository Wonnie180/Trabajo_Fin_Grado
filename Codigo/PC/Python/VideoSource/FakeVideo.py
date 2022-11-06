import asyncio
from cmath import rect
from fractions import Fraction
import os
import sys
import numpy as np
import cv2
from Resolution import Resolution
from ndarray_listener import ndl
from threading import Thread

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        ".." + os.path.sep + "Patterns" + os.path.sep + "Observer",
    )
)


from IVideoSource import IVideoSource


class FakeVideo(IVideoSource):
    frame = None
    new_frame = True
    rectangles = []
    temporary_rectangle = []
    click_and_drag = None
    resolution = None
    imshow_title = "fakevideo"
    has_to_stop = False
    called_me = False
    have_to_draw = -1

    def __init__(self, resolution: Resolution, frame, click_and_drag):
        self.resolution = resolution
        self.frame = frame
        self.click_and_drag = click_and_drag
        self.frame.talk_to(self)
        super().__init__(resolution)

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        cv2.imshow(self.imshow_title, self.Draw_Frame())
        cv2.setMouseCallback(
            self.imshow_title, self.click_and_drag, param=[self],
        )
        cv2.namedWindow(self.imshow_title, cv2.WINDOW_NORMAL) # Creates a window
        while not self.has_to_stop:
            self.Update_Frame()
            self.Action_Video()

    def Get_Frame(self):
        return self.frame

    def Get_Title(self):
        return self.imshow_title

    def Get_FPS(self):
        return self.fps

    def Set_FPS(self, fps):
        self.fps = fps

    def Set_Resolution(self, resolution):
        self.resolution = resolution

    def Get_Resolution(self):
        return self.resolution

    def Add_Rectangle(self, rectangle):
        self.rectangles.append(rectangle)
        self.temporary_rectangle = []

    def Remove_Rectangles(self):
        self.rectangles = []

    def Draw_Rectangles(self, color, thickness):
        frame_with_rectangles = self.frame.copy()
        for rectangle in self.rectangles:
            cv2.rectangle(
                frame_with_rectangles, rectangle[0], rectangle[1], color, thickness
            )
        return frame_with_rectangles

    def Draw_Frame(self):
        if len(self.rectangles) > 0:
            return self.Draw_Rectangles((255, 0, 0), 5)

        return self.frame

    def Update_Frame(self):
        cv2.imshow(self.imshow_title, self.Draw_Frame())

    def Action_Video(self):
        miliseconds_delay = 50
        mask_for_keypress = 0xFF
        key_pressed = cv2.waitKey(miliseconds_delay) & mask_for_keypress

        if key_pressed == ord("r"):
            self.Remove_Rectangles()
        elif key_pressed == ord("q"):
            cv2.destroyWindow(self.imshow_title)
            self.has_to_stop = True

    def Has_to_stop(self):
        return self.has_to_stop

    def Add_Coordinate_Rectangle(self, coordinates):
        if len(self.temporary_rectangle) == 0:
            if not (self.resolution.Is_In_Bounds(coordinates)):
                return
            self.temporary_rectangle.append(coordinates)
        else:
            if not (self.resolution.Is_In_Bounds(coordinates)):
                self.temporary_rectangle = []
                return
            self.temporary_rectangle.append(coordinates)
            self.Add_Rectangle(self.temporary_rectangle)

    # TODO
    def Remove_Coordinate_Rectangle(self):
        self.temporary_rectangle = []

    def __call__(self):
        return


def click_drag_callback(event, x, y, flags, param):
    videofake: FakeVideo = param[0]

    if event == cv2.EVENT_LBUTTONDOWN:
        videofake.Add_Coordinate_Rectangle((x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        videofake.Add_Coordinate_Rectangle((x, y))
    elif event == cv2.EVENT_RBUTTONUP:
        videofake.Remove_Coordinate_Rectangle()


if __name__ == "__main__":
    resolution = Resolution(800, 800)
    fakeFrame = ndl(
        np.zeros([resolution.Get_Width(), resolution.Get_Width(), 3], dtype=np.uint8)
    )
    prueba = FakeVideo(resolution, fakeFrame, click_drag_callback)
    prueba.start()

