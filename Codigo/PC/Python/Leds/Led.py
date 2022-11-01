import sys
import os

if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

from ILed import ILed

class Led(ILed):
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
    prueba = Led()
    prueba.Set_RGB(10,20,30)
    print(prueba.Get_RGB())
    print(prueba.Get_BGR())
