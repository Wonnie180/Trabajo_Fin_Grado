# System Libraries
import asyncio
import aioconsole
import cv2
import numpy as np
from threading import Thread
from ndarray_listener import ndl
from itertools import count
from random import randrange, seed

# Custom Libraries
from Utils.Resolution import Resolution
from Tropas.Tropa import Tropa
from VideoSource.WebCam import WebCam
from VideoPlayback.CV2ImShow_Drawable import CV2ImShow_Drawable
from Comunicaciones.FakeCommunication import FakeCommunication
from Utils.Frame import Frame
from Positions.Position_2D import Position_2D
from Color.Color import Color
from Arucos.Aruco_Drawable import Aruco_Drawable
from CommandManagers.CommandManager import CommandManager
from Commands.Command_Go_To_Position.Command_Go_To_2D_Position import Command_Go_To_2D_Position


tropas = []
command_manager = CommandManager()

seed(0xDEADBEEF)


resolution = Resolution(1280, 720)

video_source = WebCam(resolution,0)
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



async def ConsoleInput(tropas):
    input_text = [""]
    while not video_playback.Has_to_stop():
        input_text = (await aioconsole.ainput("Comando: ")).split(" ")

        command = input_text[0]
        troop = int(input_text[1]) if len(input_text) > 1 else 0
        reps = int(input_text[2]) if len(input_text) > 2 else 1

        if command == "move_f":
            for i in range(reps):
                tropas[troop].Move_Forward()
        elif command == "move_b":
            for i in range(reps):
                tropas[troop].Move_Backwards()
        elif command == "turn_r":
            for i in range(reps):
                tropas[troop].Turn_Right()
        elif command == "turn_l":
            for i in range(reps):
                tropas[troop].Turn_Left()
    return



possible_orientations = [0, 90, 180, 270]
num_tropas = 1

def prepare():
    for i in range(num_tropas):
        tropa_id = aruco.Get_Current_Id()
       
        tropa = Tropa(
            id=tropa_id,
            communication=FakeCommunication(),
            color=Color((255, 0, 0)),
        )
        tropas.append(tropa)
    #asyncio.run(randomMovements(tropas))


if __name__ == "__main__":
    prepare()

    thread_aruco = Thread(target=aruco.Run, args=()).start()
    thread_cmdmgr = Thread(target=command_manager.Run, args=()).start()
    thread_video = Thread(target=video_playback.Run, args=())
    
    thread_video.start()
    thread_video.join()

    aruco.Stop()
    command_manager.Stop()
