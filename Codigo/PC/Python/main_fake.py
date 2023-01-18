# System Libraries
import asyncio
from typing import List
import cv2
from threading import Thread
from itertools import count
from random import randrange, seed
import numpy as np

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
from Tropas.ITropa import ITropa
from Commands.Command_Go_To_Position.Command_Go_To_Position_2D.Command_Go_To_2D_Position_Fake import (
    Command_Go_To_2D_Position_Fake,
)

num_tropas = 4

SeleccionarTropa: callable = None

tropas = []
command_manager = CommandManager()

seed(0xDEADBEEF)

resolution = Resolution(800, 800)
common_frame = Frame(resolution)
tropas = []
command_manager = CommandManager()

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
    global SeleccionarTropa

    if event == cv2.EVENT_LBUTTONDOWN:
        if tropa_seleccionada is None:
            tropa_seleccionada = SeleccionarTropa(tropas, Position_2D([x, y, 0]))
        else:
            destino = Position_2D([x, y, 0])
            command_manager.Add_Command(
                Command_Go_To_2D_Position_Fake(aruco, tropa_seleccionada, destino)
            )
            tropa_seleccionada = None

    elif event == cv2.EVENT_RBUTTONDOWN:
        tropa_seleccionada = None
        destino = None

def SeleccionarTropa(tropas: List[ITropa], position: Position_2D):
    print("Seleccionando tropa...")
    for tropa in tropas:
        real_position = Position_2D(aruco.Get_Position_Of_Aruco(tropa.id));
        print(real_position.x, real_position.y," | ",position.x, position.y);
        if real_position.Equals(position, offset=48):
            return tropa

    return None


video_playback.callback = callback_test


def no_colissions(x, y, frame, footprint):
    if (
        frame.shape[0] < x + footprint.shape[0]
        or frame.shape[1] < y + footprint.shape[1]
    ):
        return False

    window = frame[x : x + footprint.shape[0], y : y + footprint.shape[1]]
    return np.all(window == 255)


def prepare():
    for i in range(num_tropas):
        tropa_id = aruco.Get_Current_Id()
        footprint = cv2.cvtColor(
            np.pad(
                np.pad(
                    aruco.Generate_new_Id(50),pad_width=7, mode='constant', constant_values=255
                    ),pad_width=1, mode='constant', constant_values=0
                ),\
         cv2.COLOR_GRAY2RGB)

        while 1:
            random_x = randrange(resolution.Get_Width()) + footprint.shape[0]
            random_y = randrange(resolution.Get_Height()) + footprint.shape[1]
            if (
                random_x < resolution.Get_Width() - 100
                and random_y < resolution.Get_Height() - 100
                and no_colissions(random_x, random_y, common_frame.frame, footprint)
            ):
                break

        tropa = FakeTropa(
            id=tropa_id,
            position=Position_2D((random_y, random_x, 90)),
            communication=FakeCommunication(),
            color=Color((255, 0, 0)),
            matrix=common_frame.frame,
            footprint=footprint,
        )
        tropa.Update_Matrix(tropa.position.y, tropa.position.x)
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
