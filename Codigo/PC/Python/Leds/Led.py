from pickletools import uint8
import sys
import os

if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

from ILed import ILed

class Led(ILed):
    def __init__(self, R:uint8 = 0, G:uint8 = 0, B:uint8 = 0):
        super().__init__(R,G,B)

    def Get_RGB(self):
        return [self.R,self.G,self.B]

    def Set_RGB(self, R :int, G:int, B:int):
        self.R = R
        self.G = G
        self.B = B

    def Get_BGR(self):
        return [self.B,self.G,self.R]

    def Set_BGR(self, B :int, G:int, R:int):
        self.R = R
        self.G = G
        self.B = B

if __name__ == '__main__':
    prueba = Led(10,20,30)
    print(prueba.Get_RGB())
    print(prueba.Get_BGR())
