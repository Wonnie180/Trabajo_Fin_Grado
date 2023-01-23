import sys
import os
from numpy import uint8 

if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep)
)

from ICommunication import ICommunication

class FakeCommunication(ICommunication):
    def __init__(self):
        super().__init__()

    def Send_Data(self, action: uint8, data: list[uint8]):
        self.sended_data = [action,data]

    def Get_Data(self):
        return self.received_data


if __name__ == '__main__':
    prueba = FakeCommunication()
    prueba.Send_Data(TROPA_ACTIONS.CHANGE_COLOR,[255,255,255])
    print(prueba.Get_Data())
