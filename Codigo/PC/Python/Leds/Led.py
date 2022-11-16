import sys
import os
from numpy import uint8
if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

from ILed import ILed

class Led(ILed):

    def Get_RGB(self):
        return [self.R,self.G,self.B]

    def Set_RGB(self, RGB:list[uint8]):
        self.R = RGB[0]
        self.G = RGB[1]
        self.B = RGB[2]

    def Get_BGR(self):
        return [self.B,self.G,self.R]

    def Set_BGR(self, BGR: list[uint8]):
        self.R = BGR[0]
        self.G = BGR[1]
        self.B = BGR[2]

if __name__ == '__main__':
    prueba = Led([10,20,30])
    print(prueba.Get_RGB())
    print(prueba.Get_BGR())
