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
from Tropas.FakeTropa import FakeTropa
from VideoSource.WebCam import WebCam
from VideoPlayback.CV2ImShow_Drawable import CV2ImShow_Drawable
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

def Generate_new_footprint(border_color=[255, 0, 0], border_size=7):
    footprint = cv2.cvtColor(aruco.Generate_new_Id(), cv2.COLOR_BGR2RGB)

    if border_size < 7:
        border_size = 7

    white = (255,255,255)

    footprint_with_marco = cv2.copyMakeBorder(
        footprint,
        top=border_size-1,
        bottom=border_size-1,
        left=border_size-1,
        right=border_size-1,
        borderType=cv2.BORDER_CONSTANT,
        value=white,
    )
    footprint_with_marco[0:border_size-1,0:border_size-1] = border_color

    return cv2.copyMakeBorder(
        footprint_with_marco,
        top=1,
        bottom=1,
        left=1,
        right=1,
        borderType=cv2.BORDER_CONSTANT,
        value=border_color,
    )




possible_orientations = [0, 90, 180, 270]
num_tropas = 2


def main_console():
    tropas = []
    for i in range(num_tropas):
        tropa = FakeTropa(
            id=next(current_id),
            communication=None,
            color=Led(255, 0, 0),
            matrix=video_source.Get_Frame(),
            footprint=Generate_new_footprint(
                border_color=Led(255, 0, 0).Get_RGB()),
        )

        random_x = randrange(resolution.Get_Width()) + tropa.Get_Footprint().shape[0]
        random_y = randrange(resolution.Get_Height()) + tropa.Get_Footprint().shape[1]

        tropa.Place_Tropa(random_x, random_y, 180)
        tropas.append(tropa)
    asyncio.run(ConsoleInput(tropas))


async def randomMovements(tropas):
    while not video_playback.Has_to_stop():
        await asyncio.sleep(0.1)
        tropa_Seleccionada = randrange(len(tropas))
        movimiento_aleatorio = randrange(4)
        if movimiento_aleatorio == 0:
            tropas[tropa_Seleccionada].Move_Forward()
        elif movimiento_aleatorio == 1:
            tropas[tropa_Seleccionada].Move_Backwards()
        elif movimiento_aleatorio == 2:
            tropas[tropa_Seleccionada].Turn_Right()
        elif movimiento_aleatorio == 3:
            tropas[tropa_Seleccionada].Turn_Left()
    return
def prepare():
    for i in range(num_tropas):
        tropa_id = aruco.Get_Current_Id()
        random_orientation = possible_orientations[(randrange(4))]
        footprint = cv2.cvtColor(aruco.Generate_new_Id(50), cv2.COLOR_GRAY2RGB)
       
        tropa = FakeTropa(
            id=tropa_id,
            position=Position_2D((100, 200, random_orientation)),
            communication=None,
            color=Color((255, 0, 0)),
            matrix=video_source.Get_Frame(),
            footprint=footprint,
        )
        tropas.append(tropa)
    #asyncio.run(randomMovements(tropas))


if __name__ == "__main__":
    prepare()
    thread_aruco = Thread(target=aruco.Run, args=()).start()
    thread_cmdmgr = Thread(target=command_manager.Run, args=()).start()
    thread_video = Thread(target=video_playback.Run, args=())
    thread_video.start()
    #print(tropas[0].position.x, tropas[0].position.y)
    command_manager.Add_Command(Command_Go_To_2D_Position(aruco, tropas[0], Position_2D((770, 510,0))))
    #command_manager.Add_Command(Command_Go_To_2D_Position(aruco, tropas[0], Position_2D((100, 510,0))))
    thread_video.join()

    aruco.Stop()
    command_manager.Stop()

