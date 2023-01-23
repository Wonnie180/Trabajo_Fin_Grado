# System Libraries
import asyncio
from typing import List
import cv2
from threading import Thread
from random import seed

# Custom Libraries
from Utils.Resolution import Resolution
from Tropas.Tropa import Tropa
from VideoSource.WebCam import WebCam
from VideoPlayback.CV2ImShow_Drawable import CV2ImShow_Drawable
from Comunicaciones.UDP_Client import UDP_Client
from Utils.Frame import Frame
from Positions.Position_2D import Position_2D
from Color.Color import Color
from Arucos.Aruco_Drawable import Aruco_Drawable
from CommandManagers.CommandManager import CommandManager
from Commands.Command_Go_To_Position.Command_Go_To_Position_2D.Command_Go_To_2D_Position import Command_Go_To_2D_Position

VERBOSE = True

tropas = []
command_manager = CommandManager()

seed(0xDEADBEEF)

resolution = Resolution(1280, 720)

video_source = WebCam(resolution,1)
video_playback = CV2ImShow_Drawable("Video TFG Luis", video_source, callback=None)
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
detector_parameters = cv2.aruco.DetectorParameters_create()
aruco = Aruco_Drawable(dictionary, detector_parameters, video_source, video_playback)

tropa_seleccionada = None
destino = None
SeleccionarTropa = any

def callback_test(event, x, y, flags, param):
    video_pb = param[0]
    global tropa_seleccionada
    global destino
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if tropa_seleccionada is None:
            tropa_seleccionada = SeleccionarTropa(tropas, Position_2D([x, y, 0]))
            if tropa_seleccionada != None:
                tropa_seleccionada.Set_Color(Color([255,255,255]))
        else:
            destino = Position_2D([x, y, 0])
            command_manager.Add_Command(Command_Go_To_2D_Position(aruco, tropa_seleccionada, destino))
            tropa_seleccionada.Set_Color(Color([0,0,0]))
    elif event == cv2.EVENT_RBUTTONDOWN:
        tropa_seleccionada.Set_Color(Color([0,0,0]))
        tropa_seleccionada = None
        destino = None

def SeleccionarTropa(tropas: List[Tropa], position: Position_2D):
    print("Seleccionando tropa...")
    for tropa in tropas:
        pos_aruco = aruco.Get_Position_Of_Aruco(tropa.id)
        if pos_aruco is not None:
            real_position = Position_2D(pos_aruco);
            print(real_position.x, real_position.y," | ",position.x, position.y);
            if real_position.Equals(position, offset=48):
                return tropa

    return None

video_playback.callback = callback_test

possible_orientations = [0, 90, 180, 270]
ips = ["192.168.1.120","192.168.1.117"]
num_tropas = 2

def prepare():
    for i in range(num_tropas):       
        tropa = Tropa(
            id=i,
            communication=UDP_Client(ips[i], 1234),
            color=Color((255, 0, 0)),
        )
        tropa.verbose = VERBOSE
        tropas.append(tropa)

    tropas[1].threshold_angle = 10

if __name__ == "__main__":
    prepare()

    thread_aruco = Thread(target=aruco.Run, args=()).start()
    thread_cmdmgr = Thread(target=command_manager.Run, args=()).start()
    thread_video = Thread(target=video_playback.Run, args=())
    
    thread_video.start()
    thread_video.join()

    aruco.Stop()
    command_manager.Stop()
