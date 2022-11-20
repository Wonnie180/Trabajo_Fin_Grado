import os
import sys
import cv2


if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from Arucos.Aruco import Aruco

from time import sleep
from Geometries.Rectangles.Rectangle_Drawable import Rectangle_Drawable
from Geometries.Circles.Circle_Drawable import Circle_Drawable
from Geometries.Text.Text_Drawable import Text_Drawable
from Color.Color import Color
from Utils.Frame import Frame
from VideoPlayback.CV2ImShow_Drawable import CV2ImShow_Drawable
from VideoSource.IVideoSource import IVideoSource
from AbleInterfaces.Runnable import Runnable

class Aruco_Drawable(Aruco, Runnable):
    video_source: IVideoSource
    video_playback: CV2ImShow_Drawable

    def __init__(
        self, dictionary, detector_parameters,video_source:IVideoSource, video_playback: CV2ImShow_Drawable
    ):
        self.video_source = video_source
        self.video_playback = video_playback
        super().__init__(dictionary, detector_parameters)

    def Run(self):
        while not self.has_to_stop:
            self.Detect_Aruco(self.video_source.Get_Frame())
            sleep(0.0000)
            self.Draw_Detected_Aruco()
        return

    def Stop(self):
        self.has_to_stop = True

    def Draw_Detected_Aruco(self):        
        rectangles = []
        circles = []
        texts = []
        if len(self.corners) > 0:
            for (markerCorner, markerID) in zip(self.corners, self.ids):
                corners = markerCorner.reshape((4, 2))
                (topLeft, topRight, bottomRight, bottomLeft) = corners

                topRight = (int(topRight[0]), int(topRight[1]))
                bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
                bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
                topLeft = (int(topLeft[0]), int(topLeft[1]))

                cX = int((topLeft[0] + bottomRight[0]) / 2.0)
                cY = int((topLeft[1] + bottomRight[1]) / 2.0)

                rectangle = Rectangle_Drawable(
                    topLeft, topRight, bottomLeft, bottomRight, Color((255, 0, 0))
                )
                circle = Circle_Drawable((cX, cY), 4, Color((0, 0, 255)))
                text = Text_Drawable(topLeft, str(markerID), Color((255, 0, 255)))

                rectangles.append(rectangle)
                circles.append(circle)
                texts.append(text)

        self.video_playback.Add_Rectangles(rectangles)
        self.video_playback.Add_Circles(circles)
        self.video_playback.Add_Texts(texts)


if __name__ == "__main__":
    from Utils.Resolution import Resolution
    from VideoSource.FakeVideo import FakeVideo
    from threading import Thread

    diccionario = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
    detector_parameters = cv2.aruco.DetectorParameters_create()
    frame = Frame(Resolution(600, 600))
    video_src = FakeVideo(frame)
    video_pb = CV2ImShow_Drawable("a", video_src)
    prueba = Aruco_Drawable(diccionario, detector_parameters,video_src, video_pb)

    aruco_marker = cv2.cvtColor(
        prueba.Generate_new_Id(100), cv2.COLOR_GRAY2RGB
    )
    frame.frame[
        100 : 100 + aruco_marker.shape[0], 100 : 100 + aruco_marker.shape[1], :
    ] = aruco_marker

    Thread(target=video_pb.Run, args=()).start()
    Thread(target=prueba.Run, args=()).start()


    prueba.Stop()
