import os
import sys
from cv2 import aruco
from cv2 import imshow, waitKey, destroyAllWindows

if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

from IAruco import IAruco

class Aruco(IAruco):
    def Generate_Dictionary(self, dictionary = aruco.DICT_5X5_50):
        self.dictionary = aruco.Dictionary_get(dictionary)
        self.current_id = -1

    def Obtain_Current_Id(self):
        return self.current_id

    def Generate_new_Id(self, img_size = 500):
        self.current_id += 1
        return aruco.drawMarker(self.dictionary, self.current_id, img_size)
        
    def Detect_Aruco(self):
        pass

    def Draw_Detected_Aruco(self):
        pass


if __name__ == '__main__':
    prueba = Aruco()
    prueba.Generate_Dictionary()

    imshow('frame', prueba.Generate_new_Id())
    waitKey(0)
    destroyAllWindows()

    imshow('frame', prueba.Generate_new_Id())
    waitKey(0)
    destroyAllWindows()
