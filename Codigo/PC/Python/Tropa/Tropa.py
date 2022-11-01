import sys
import os

if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

from ITropa import ITropa

class Tropa(ITropa):
    def Get_Color(self):
        return self.color

    def Set_Color(self, color):
        self.color = color
  
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
    prueba.Set_Color([100,100,100])
    print(prueba.Get_Color())
