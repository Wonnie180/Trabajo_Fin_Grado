import os
import sys
from typing import List
import cv2

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from VideoSource.IVideoSource import IVideoSource
from VideoPlayback.CV2ImShow import CV2ImShow

from Geometries.Lines.Line_Drawable import Line_Drawable
from Geometries.Rectangles.Rectangle_Drawable import Rectangle_Drawable
from Geometries.Circles.Circle_Drawable import Circle_Drawable
from Geometries.Text.Text_Drawable import Text_Drawable


class CV2ImShow_Drawable(CV2ImShow):
    lines: List[Line_Drawable] = []
    rectangles: List[Rectangle_Drawable] = []
    circles: List[Circle_Drawable] = []
    texts: List[Text_Drawable] = []

    def __init__(self, title: str, videoSource: IVideoSource,action:callable = None , callback: callable = None):         
        super().__init__(title, videoSource, action, callback)

    def Draw_Frame(self):
        self.Initializate_Frame()
        self.Draw_Geometries()
        cv2.imshow(self.title, self.frame)

    def Draw_Geometries(self):
        self.Draw_Lines()
        self.Draw_Rectangles()
        self.Draw_Circles()
        self.Draw_Text()

    def Draw_Text(self):
        for text in self.texts:
            text.Draw_To_Frame(self.frame)

    def Draw_Lines(self):
        for line in self.lines:
            line.Draw_To_Frame(self.frame)

    def Draw_Rectangles(self):
        for rectangle in self.rectangles:
            rectangle.Draw_To_Frame(self.frame)

    def Draw_Circles(self):
        for circle in self.circles:
            circle.Draw_To_Frame(self.frame)

    def Add_Lines(self, lines: List[Line_Drawable]):
        self.lines = lines
    
    def Add_Rectangles(self, rectangles: List[Rectangle_Drawable]):
        self.rectangles = rectangles

    def Add_Circles(self, circles: List[Circle_Drawable]):
        self.circles = circles

    def Add_Texts(self, texts: List[Text_Drawable]):
        self.texts = texts
    

def click_drag_callback(event, x, y, flags, param):
    self = param[0]
    if event == cv2.EVENT_LBUTTONDOWN:
        print("llamada callback de", self.title)
    #     self.Add_Coordinate_Rectangle((x, y))
    # elif event == cv2.EVENT_LBUTTONUP:
    #     self.Add_Coordinate_Rectangle((x, y))
    # elif event == cv2.EVENT_RBUTTONUP:
    #     self.Remove_Coordinate_Rectangle()

def click_drag_callback2(event, x, y, flags, param):
    self = param[0]
    if event == cv2.EVENT_LBUTTONDOWN:
        print("llamada callback2 de", self.title)
    #     self.Add_Coordinate_Rectangle((x, y))
    # elif event == cv2.EVENT_LBUTTONUP:
    #     self.Add_Coordinate_Rectangle((x, y))
    # elif event == cv2.EVENT_RBUTTONUP:
    #     self.Remove_Coordinate_Rectangle()

def Action_Video(video_playback: CV2ImShow_Drawable):
    miliseconds_delay = 50
    mask_for_keypress = 0xFF
    key_pressed = cv2.waitKey(miliseconds_delay) & mask_for_keypress

    if key_pressed == ord("q"):
        video_playback.has_to_stop = True
    elif key_pressed == ord("r"):
        print(video_playback.rectangles)
        video_playback.rectangles = []
        print(video_playback.rectangles)


if __name__ == "__main__":

    from VideoSource.FakeVideo import FakeVideo
    from Utils.Resolution import Resolution
    from Color.Color import Color
    from Utils.Frame import Frame

    resolution = Resolution(800, 800)
    common_frame = Frame(resolution)

    video_source = FakeVideo(common_frame)

    video_playback = CV2ImShow_Drawable("Video TFG Luis", video_source)

    line = Line_Drawable((300,300),(250,250),Color((255,255,0)))

    rectangle = Rectangle_Drawable(
        (100, 100), (100, 200), (200, 100), (200, 200), Color((255, 0, 0))
    )

    circle = Circle_Drawable((500,500),75,Color((0,255,0)))
    text = Text_Drawable((100,600),"Texto",Color((0,0,0)))

    video_playback.Add_Rectangles([rectangle])
    video_playback.Add_Lines([line])
    video_playback.Add_Circles([circle])
    video_playback.Add_Texts([text])
    video_playback.Run()
