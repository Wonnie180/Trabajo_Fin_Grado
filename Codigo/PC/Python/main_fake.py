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


async def randomMovements(tropas):
    while not video_playback.has_to_stop:
        await asyncio.sleep(0.05)
        tropa_Seleccionada: FakeTropa = tropas[randrange(len(tropas))]
        movimiento_aleatorio = randrange(4)

        movimiento_aleatorio = 0
        if movimiento_aleatorio == 0:
            tropa_Seleccionada.Move_Forward()
        elif movimiento_aleatorio == 1:
            tropa_Seleccionada.Move_Backwards()
        elif movimiento_aleatorio == 2:
            tropa_Seleccionada.Turn_Right()
        elif movimiento_aleatorio == 3:
            tropa_Seleccionada.Turn_Left()
        # print(
        #     "x: "
        #     + str(tropa_Seleccionada.position.x)
        #     + " y: "
        #     + str(tropa_Seleccionada.position.y)
        #     + " a: "
        #     + str(tropa_Seleccionada.position.angle)
        # )
        print(aruco.Get_Position_Of_Aruco(0))
    return


num_tropas = 1


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
        tropas.append(tropa)
    # asyncio.run(randomMovements(tropas))

def end_of_loop():
    raise StopIteration

if __name__ == "__main__":
    import numpy as np
    from itertools import takewhile

    from Commands.Command_Change_Color.Command_Change_Color import Command_Change_Color

    prepare()

    thread_aruco = Thread(target=aruco.Run, args=()).start()
    thread_cmdmgr = Thread(target=command_manager.Run, args=()).start()
    thread_video = Thread(target=video_playback.Run, args=())
    thread_video.start()

    #print(tropas[0].position.Get_Position())
    # Position: [486, 530, 0]
    
    #command_manager.Add_Command(Command_Go_To_2D_Position(aruco, tropas[0], Position_2D((770, 510,0))))
    #command_manager.Add_Command(Command_Go_To_2D_Position(aruco, tropas[0], Position_2D((100, 510,0))))
    #command_manager.Add_Command(Command_Go_To_2D_Position(aruco, tropas[0], Position_2D((486, 200,0))))

    thread_video.join()
    aruco.Stop()
    command_manager.Stop()
