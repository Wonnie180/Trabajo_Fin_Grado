import sys
import os

if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

from ITropa import ITropa

class Tropa(ITropa):
    def Move_Forward(self):
        pass

    def Move_Backwards(self):
        pass

    def Turn_Left(self):
        pass

    def Turn_Right(self):
        pass
