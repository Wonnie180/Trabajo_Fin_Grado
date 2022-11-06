import os
import sys
from cv2 import aruco,putText,FONT_HERSHEY_SIMPLEX, line, circle, imshow, waitKey, destroyAllWindows

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

from IAruco import IAruco


class Aruco(IAruco):
    img_size = 0
    arucoParams = None

    def Generate_Dictionary(self, img_size=50, dictionary=aruco.DICT_4X4_50):
        self.img_size = img_size
        self.dictionary = aruco.Dictionary_get(dictionary)
        self.detector_parameters = aruco.DetectorParameters_create()
        self.current_id = -1

    def Obtain_Current_Id(self):
        return self.current_id

    def Generate_new_Id(self):
        self.current_id += 1
        return aruco.drawMarker(self.dictionary, self.current_id, self.img_size)

    def Detect_Aruco(self, frame):
        (corners, ids, rejected) = aruco.detectMarkers(
            frame, self.dictionary, parameters=self.arucoParams
        )

        return (corners, ids, rejected)

    def Draw_Rejected_Aruco(self, frame, rejected):
        if len(rejected) < 1:
            return None
            
        new_frame = frame.copy()

        for markerCorner in rejected:
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners

            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))

            line(new_frame, topLeft, topRight, (0, 255, 0), 2)
            line(new_frame, topRight, bottomRight, (0, 255, 0), 2)
            line(new_frame, bottomRight, bottomLeft, (0, 255, 0), 2)
            line(new_frame, bottomLeft, topLeft, (0, 255, 0), 2)

            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)
            circle(new_frame, (cX, cY), 4, (0, 0, 255), -1)

        return new_frame

    def Draw_Detected_Aruco(self, frame, corners, ids):
        if len(corners) < 1:
            return None

        new_frame = frame.copy()
        
        for (markerCorner, markerID) in zip(corners, ids):
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners

            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))

            line(new_frame, topLeft, topRight, (0, 255, 0), 2)
            line(new_frame, topRight, bottomRight, (0, 255, 0), 2)
            line(new_frame, bottomRight, bottomLeft, (0, 255, 0), 2)
            line(new_frame, bottomLeft, topLeft, (0, 255, 0), 2)
       
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)
            circle(new_frame, (cX, cY), 4, (0, 0, 255), -1)

            putText(new_frame, str(markerID),
                (topLeft[0], topLeft[1] - 15), FONT_HERSHEY_SIMPLEX,
                0.5, (0, 255, 0), 2)
            print("[INFO] ArUco marker ID: {}".format(markerID))

        return new_frame


if __name__ == "__main__":
    prueba = Aruco()
    prueba.Generate_Dictionary()

    imshow("frame", prueba.Generate_new_Id())
    waitKey(0)
    destroyAllWindows()

    # imshow('frame', prueba.Generate_new_Id())
    # waitKey(0)
    # destroyAllWindows()
