import sys
import os
import bluetooth

if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

from ICommunication import ICommunication


class Bluetooth(ICommunication):
    def __init__(self):
        self._interface = bluetooth
        super().__init__()

    def Search_Devices(self):
        self.devices = self._interface.discover_devices(lookup_names=True)

    def Get_Devices(self):
        return self.devices

    def Send_Data(self, data):
        print(data)

    def Get_Data(self):
        print("recibido");  


if __name__ == '__main__':
    prueba = Bluetooth()
    prueba.Search_Devices()    
    print(prueba.Get_Devices())
