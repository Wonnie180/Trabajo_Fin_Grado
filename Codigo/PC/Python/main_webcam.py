# System Libraries
import asyncio
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


tropas = []
command_manager = CommandManager()

seed(0xDEADBEEF)

resolution = Resolution(1280, 720)

video_source = WebCam(resolution,2)
video_playback = CV2ImShow_Drawable("Video TFG Luis", video_source, callback=None)
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
detector_parameters = cv2.aruco.DetectorParameters_create()
aruco = Aruco_Drawable(dictionary, detector_parameters, video_source, video_playback)

tropa_seleccionada = None
destino = None

def callback_test(event, x, y, flags, param):
    video_pb = param[0]
    global tropa_seleccionada
    global destino
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if tropa_seleccionada is None:
            tropa_seleccionada = tropas[0]
        else:
            destino = Position_2D([x,y,0])
            command_manager.Add_Command(Command_Go_To_2D_Position(aruco, tropa_seleccionada, destino))

    elif event == cv2.EVENT_RBUTTONDOWN:
        tropa_seleccionada = None
        destino = None


video_playback.callback = callback_test

possible_orientations = [0, 90, 180, 270]
num_tropas = 1

def prepare():
    for i in range(num_tropas):
        tropa_id = aruco.Get_Current_Id()
       
        tropa = Tropa(
            id=tropa_id,
            communication=UDP_Client("192.168.1.120", 1234),
            color=Color((255, 0, 0)),
        )
        tropas.append(tropa)


if __name__ == "__main__":
    prepare()

    thread_aruco = Thread(target=aruco.Run, args=()).start()
    thread_cmdmgr = Thread(target=command_manager.Run, args=()).start()
    thread_video = Thread(target=video_playback.Run, args=())
    
    thread_video.start()
    thread_video.join()

    aruco.Stop()
    command_manager.Stop()
