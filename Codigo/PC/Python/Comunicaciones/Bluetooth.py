import sys
import os
import bluetooth
from numpy import uint8 

if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep)
)

from ICommunication import ICommunication, TROPA_ACTIONS


class Bluetooth(ICommunication):
    def __init__(self):
        self._interface = bluetooth
        super().__init__()

    def Search_Devices(self):
        self.devices = self._interface.discover_devices(lookup_names=True)

    def Get_Devices(self):
        return self.devices

    def Send_Data(self, action: uint8, data: list[uint8]):
        print(action, data)

    def Get_Data(self):
        print("recibido");  


if __name__ == '__main__':
    prueba = Bluetooth()
    # prueba.Search_Devices()    
    print(prueba.Get_Devices())
    prueba.Send_Data(TROPA_ACTIONS.CHANGE_COLOR,[255,255,255])
