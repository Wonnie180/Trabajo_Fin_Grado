import os
import sys
from typing import List
import cv2


if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from Geometries.Lines.Line_Drawable import Line_Drawable
from Geometries.Rectangles.Rectangle_Drawable import Rectangle_Drawable
from Geometries.Circles.Circle_Drawable import Circle_Drawable
from Geometries.Text.Text_Drawable import Text_Drawable

class Callback_Action_Drawable():
    lines: List[Line_Drawable] = []
    rectangles: List[Rectangle_Drawable] = []
    circles: List[Circle_Drawable] = []
    texts: List[Text_Drawable] = []

    callback: callable
    action: callable
    
    def Get_Callback(event, x, y, flags, param):
        video_playback = param[0]
        if event == cv2.EVENT_LBUTTONDOWN:
            print("llamada callback2 de", self.title)
    #     self.Add_Coordinate_Rectangle((x, y))
    # elif event == cv2.EVENT_LBUTTONUP:
    #     self.Add_Coordinate_Rectangle((x, y))
    # elif event == cv2.EVENT_RBUTTONUP:
    #     self.Remove_Coordinate_Rectangle()