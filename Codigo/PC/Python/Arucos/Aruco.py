import os
import sys
import cv2

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep))

from IAruco import IAruco
from Utils.Frame import Frame

class Aruco(IAruco):

    def __init__(self, dictionary, detector_parameters):
        super().__init__(dictionary, detector_parameters)

    def Get_Current_Id(self):
        return self.current_id

    def Generate_new_Id(self, size:int):
        aruco_marker = cv2.aruco.drawMarker(self.dictionary, self.current_id, size)
        self.current_id+=1
        return aruco_marker

    def Detect_Aruco(self, frame):
        (self.corners, self.ids, self.rejected) = cv2.aruco.detectMarkers(
            frame, self.dictionary, parameters=self.detector_parameters
        )

    def Get_Position_Of_Aruco(self, id):
        if self.ids is None or not id in self.ids:
            return None

        return (self.corners[id].mean(axis=1))[0].astype(int)
        



if __name__ == "__main__":
    diccionario = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
    detector_parameters = cv2.aruco.DetectorParameters_create()
    prueba = Aruco(diccionario, detector_parameters)

    cv2.imshow("frame", prueba.Generate_new_Id(100))
    cv2.waitKey(0)
    cv2.destroyAllWindows()