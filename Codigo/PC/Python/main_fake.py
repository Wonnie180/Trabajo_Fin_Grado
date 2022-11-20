# System Libraries
import asyncio
import cv2
from threading import Thread
from itertools import count
from random import randrange, seed

# Custom Libraries
from Comunicaciones.FakeCommunication import FakeCommunication
from Utils.Resolution import Resolution
from Tropas.FakeTropa import FakeTropa
from VideoSource.FakeVideo import FakeVideo
from VideoPlayback.CV2ImShow_Drawable import CV2ImShow_Drawable
from Utils.Frame import Frame
from Positions.Position_2D import Position_2D
from Color.Color import Color
from Arucos.Aruco_Drawable import Aruco_Drawable
from CommandManagers.CommandManager import CommandManager
from Commands.Command_Go_To_Position.Command_Go_To_2D_Position import (
    Command_Go_To_2D_Position,
)

tropas = []
command_manager = CommandManager()

seed(0xDEADBEEF)

resolution = Resolution(800, 800)
common_frame = Frame(resolution)
tropas = []
command_manager = CommandManager()

seed(0xDEADBEEF)


video_source = FakeVideo(common_frame)

video_playback = CV2ImShow_Drawable("Video TFG Luis", video_source, callback=None)
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
detector_parameters = cv2.aruco.DetectorParameters_create()
detector_parameters.cornerRefinementMethod = 1
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


num_tropas = 3


def prepare():
    for i in range(num_tropas):
        tropa_id = aruco.Get_Current_Id()
        random_orientation = possible_orientations[(randrange(4))]
        footprint = cv2.cvtColor(aruco.Generate_new_Id(50), cv2.COLOR_GRAY2RGB)
        while 1:
            random_x = randrange(resolution.Get_Width()) + footprint.shape[0]
            random_y = randrange(resolution.Get_Height()) + footprint.shape[1]
            if (
                random_x < resolution.Get_Width() - 100
                and random_y < resolution.Get_Height() - 100
            ):
                break

        tropa = FakeTropa(
            id=tropa_id,
            position=Position_2D((random_x, random_y, random_orientation)),
            communication=FakeCommunication(),
            color=Color((255, 0, 0)),
            matrix=common_frame.frame,
            footprint=footprint,
        )
        tropa.Turn_Left()
        tropa.Turn_Right()
        tropa.Turn_Left()
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
