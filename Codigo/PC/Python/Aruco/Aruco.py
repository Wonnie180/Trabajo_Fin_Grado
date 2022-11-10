import os
import sys
import cv2

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep)
)

from Utils.Resolution import Resolution
from IAruco import IAruco

class Aruco(IAruco):

    def Generate_Dictionary(self, dictionary=cv2.aruco.DICT_4X4_50):
        self.dictionary = cv2.aruco.Dictionary_get(dictionary)
        self.detector_parameters = cv2.aruco.DetectorParameters_create()
        self.current_id = -1

    def Obtain_Current_Id(self):
        return self.current_id

    def Generate_new_Id(self, resolution:Resolution):
        self.current_id += 1
        return cv2.aruco.drawMarker(self.dictionary, self.current_id, resolution.Get_Height())

    def Detect_Aruco(self, frame):
        (corners, ids, rejected) = cv2.aruco.detectMarkers(
            frame, self.dictionary, parameters=self.detector_parameters
        )

        return (corners, ids, rejected)


if __name__ == "__main__":
    prueba = Aruco()
    prueba.Generate_Dictionary()

    cv2.imshow("frame", prueba.Generate_new_Id(Resolution(600,600)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()