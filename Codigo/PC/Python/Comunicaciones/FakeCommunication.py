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
        self._interface = None
        super().__init__()

    def Search_Devices(self):
        pass

    def Get_Devices(self):
        return self.devices

    def Send_Data(self, action: uint8, data: list[uint8]):
        self.sended_data = [action,data]
        print("Enviado: Acción->",action," Datos->",data)

    def Get_Data(self):
        return self.received_data


if __name__ == '__main__':
    prueba = FakeCommunication()
    prueba.Send_Data(TROPA_ACTIONS.CHANGE_COLOR,[255,255,255])
    print(prueba.Get_Data())
