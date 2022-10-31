
from abc import ABC, abstractmethod
from numpy import uint16
import cv2
import cv2.aruco as aruco

'''
    Interfaz de las Tropas
'''


class ITropa(ABC):
    def __init__(self, id: uint16):
        self.id = id
        super().__init__()

    @abstractmethod
    def Move_Forward(self):
        pass

    @abstractmethod
    def Move_Backwards(self):
        pass

    @abstractmethod
    def Turn_Left(self):
        pass

    @abstractmethod
    def Turn_Right(self):
        pass


'''
    Implementación de las Tropas
'''


class Tropa(ITropa):
    def Move_Forward(self):
        pass

    def Move_Backwards(self):
        pass

    def Turn_Left(self):
        pass

    def Turn_Right(self):
        pass


if __name__ == '__main__':
    prueba = Tropa(id=1011)
    print(prueba.id)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

    img = aruco.drawMarker(aruco_dict, 2, 700)
    print(img)
    cv2.imwrite("test_marker.jpg", img)

    # Display the image to us
    cv2.imshow('frame', img)
    # Exit on any key
    cv2.waitKey(0)
    cv2.destroyAllWindows()
