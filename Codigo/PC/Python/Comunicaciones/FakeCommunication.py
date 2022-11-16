import sys
import os
from numpy import uint8 

if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep)
)

from ICommunication import ICommunication, TROPA_ACTIONS

class FakeCommunication(ICommunication):
    datos_simulados = ""
    def __init__(self):
        self._interface = None
        super().__init__()

    def Search_Devices(self):
        pass

    def Get_Devices(self):
        return self.devices

    def Send_Data(self, action: TROPA_ACTIONS, data: list[uint8]):
        print("Enviado: Acción->",action.value," Datos->",data)

    def Get_Data(self):
        return "Recibido: "+self.datos_simulados


if __name__ == '__main__':
    prueba = FakeCommunication()
    prueba.Send_Data(TROPA_ACTIONS.CHANGE_COLOR,[255,255,255])
    print(prueba.Get_Data())
