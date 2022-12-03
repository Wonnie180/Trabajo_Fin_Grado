import socket
import sys
import os
from numpy import uint8 

if __name__ != '__main__':
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep)
)

from ICommunication import ICommunication
from Tropas.ITropa import TROPA_ACTIONS

class UDP_Client(ICommunication):
    socket : any;
    ip_address: str;
    port: int;

    def __init__(self, ip_address:str, port:int):
        self.ip_address = ip_address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._interface = None
        super().__init__()

    def Search_Devices(self):
        pass

    def Get_Devices(self):
        return self.devices

    def Send_Data(self, action: uint8, data: list[uint8] =[]):
        self.socket.sendto(bytes(([action]+data)), (self.ip_address,self.port))

    def Get_Data(self):
        return ""


if __name__ == '__main__':    
    prueba = UDP_Client("192.168.1.112", 1234)
    prueba.Send_Data(TROPA_ACTIONS.MOVE_FORWARD.value)
    prueba.Send_Data(TROPA_ACTIONS.MOVE_BACKWARD.value)
    prueba.Send_Data(TROPA_ACTIONS.TURN_LEFT.value)
    prueba.Send_Data(TROPA_ACTIONS.TURN_RIGHT.value)
    #prueba.Send_Data(TROPA_ACTIONS.CHANGE_COLOR.value,[255,255,255])
    prueba.Send_Data(TROPA_ACTIONS.CHANGE_COLOR.value,[1,0,0])
    prueba.Send_Data(TROPA_ACTIONS.CHANGE_COLOR.value+1,[0,0,0])
    #print(prueba.Get_Data())
