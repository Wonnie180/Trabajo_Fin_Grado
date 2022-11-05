import asyncio
import os
import sys
import numpy as np
import cv2
from Resolution import Resolution

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
    frame_modified = None
    click_and_drag = None
    resolution = None
    imshow_title = "fakevideo"

    def __init__(self, resolution: Resolution, click_and_drag):
        self.resolution = resolution
        self.frame = np.zeros(
            (resolution.Get_Width(), resolution.Get_Height(), 3), dtype=np.uint8
        )
        self.click_and_drag = click_and_drag
        super().__init__(resolution)

    def Get_Frame(self):
        return self.frame

    def Get_FPS(self):
        return self.fps

    def Set_FPS(self, fps):
        self.fps = fps

    def Set_Resolution(self, resolution):
        self.resolution = resolution

    def Get_Resolution(self):
        return self.resolution

    def Show_Video(self):
        cv2.imshow(self.imshow_title, self.frame)
        cv2.setMouseCallback(
            self.imshow_title,
            self.click_and_drag,
            param=[self.frame, self.Get_Resolution(), self.imshow_title],
        )


refPt = []


def click_drag_callback(event, x, y, flags, param):
    global refPt
    frame = param[0]
    resolution: Resolution = param[1]
    imshow_title = param[2]

    color = (255, 0, 0)
    thickness = 5

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        if not resolution.Is_In_Bounds(x, y):
            refPt = []
            return

        cv2.rectangle(frame, refPt[0], refPt[1], color, thickness)
        # cv2.imshow(imshow_title, image)

    elif event == cv2.EVENT_RBUTTONUP:
        refPt = []


if __name__ == "__main__":
    resolution = Resolution(800, 800)

    prueba = FakeVideo(resolution, click_drag_callback)
    while 1:
        prueba.Show_Video()
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyWindow("i")
            break
