import os
import sys
import cv2
from threading import Thread

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from VideoSource.IVideoSource import IVideoSource
from IVideoPlayback import IVideoPlayback


class CV2ImShow(IVideoPlayback):

    def __init__(self, title: str, videoSource: IVideoSource, callback: callable):
        super().__init__(title, videoSource, callback)

    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        cv2.imshow(self.title, self.videoSource.Get_Frame())
        cv2.setMouseCallback(self.title, self.callback,param=[self])
        self.Action_Video()
        while not self.has_to_stop:
            if self.videoSource.Has_New_Frame():
                new_frame = self.videoSource.Get_Frame().copy()
                # (corners, ids, _) = self.aruco.Detect_Aruco(new_frame)
                # self.Draw_Arucos(new_frame, corners, ids)
                cv2.imshow(self.title, new_frame)
            self.Action_Video()

    def Get_Title(self):
        return self.title

    # def Draw_Arucos(self, frame, corners, ids):
    #     if len(corners) < 1:
    #         return

    #     for (markerCorner, markerID) in zip(corners, ids):
    #         corners = markerCorner.reshape((4, 2))
    #         (topLeft, topRight, bottomRight, bottomLeft) = corners

    #         topRight = (int(topRight[0]), int(topRight[1]))
    #         bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
    #         bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
    #         topLeft = (int(topLeft[0]), int(topLeft[1]))

    #         cv2.line(frame, topLeft, topRight, (0, 255, 0), 2)
    #         cv2.line(frame, topRight, bottomRight, (0, 255, 0), 2)
    #         cv2.line(frame, bottomRight, bottomLeft, (0, 255, 0), 2)
    #         cv2.line(frame, bottomLeft, topLeft, (0, 255, 0), 2)

    #         cX = int((topLeft[0] + bottomRight[0]) / 2.0)
    #         cY = int((topLeft[1] + bottomRight[1]) / 2.0)
    #         cv2.circle(frame, (cX, cY), 4, (0, 0, 255), -1)

    #         cv2.putText(
    #             frame,
    #             str(markerID),
    #             (topLeft[0], topLeft[1] - 15),
    #             cv2.FONT_HERSHEY_SIMPLEX,
    #             0.5,
    #             (0, 255, 0),
    #             2,
    #         )

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
        cv2.imshow(self.title, self.Draw_Frame())

    def Action_Video(self):
        miliseconds_delay = 50
        mask_for_keypress = 0xFF
        key_pressed = cv2.waitKey(miliseconds_delay) & mask_for_keypress

        if key_pressed == ord("r"):
            self.Remove_Rectangles()
        elif key_pressed == ord("q"):
            cv2.destroyWindow(self.title)
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



# def show_clicked(event,x,y,flags,param):

#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.putText(image, text='Clicked', org=(x,y),
#             fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0),
#             thickness=2, lineType=cv2.LINE_AA)



# cv2.namedWindow(winname='this_window')

# cv2.setMouseCallback('this_window', show_clicked)


def click_drag_callback(event, x, y, flags, param):
        self = param[0]
        print("llamada callback de",self.title)
        # if event == cv2.EVENT_LBUTTONDOWN:
        #     self.Add_Coordinate_Rectangle((x, y))
        # elif event == cv2.EVENT_LBUTTONUP:
        #     self.Add_Coordinate_Rectangle((x, y))
        # elif event == cv2.EVENT_RBUTTONUP:
        #     self.Remove_Coordinate_Rectangle()


if __name__ == "__main__":

    from VideoSource.FakeVideo import FakeVideo
    from Utils.Resolution import Resolution
    from ndarray_listener import ndl
    import numpy as np

    
    

    resolution = Resolution(800, 800)
    common_frame = ndl(
        np.ones([resolution.Get_Width(), resolution.Get_Width(), 3], dtype=np.uint8)
    ) * 255

    video_source = FakeVideo(resolution, common_frame) 

    video_playback = CV2ImShow("Video TFG Luis", video_source, click_drag_callback)

    video_playback.start()

