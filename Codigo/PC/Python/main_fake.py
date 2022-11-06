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
from Aruco.Aruco import Aruco
from VideoSource.Resolution import Resolution
from Tropas.FakeTropa import FakeTropa
from VideoSource.FakeVideo import FakeVideo
from Leds.Led import Led


current_id = count(1)
aruco = Aruco()
aruco.Generate_Dictionary()
resolution = Resolution(800, 800)
seed(0xDEADBEEF)


def click_drag_callback(event, x, y, flags, param):
    videofake: FakeVideo = param[0]

    if event == cv2.EVENT_LBUTTONDOWN:
        videofake.Add_Coordinate_Rectangle((x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        videofake.Add_Coordinate_Rectangle((x, y))
    elif event == cv2.EVENT_RBUTTONUP:
        videofake.Remove_Coordinate_Rectangle()


common_frame = ndl(
    np.zeros([resolution.Get_Width(), resolution.Get_Width(), 3], dtype=np.uint8)
)
video = FakeVideo(resolution, common_frame, click_drag_callback)

async def ConsoleInput(tropas):
    input_text = [""]
    while not video.has_to_stop:
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


acciones = []


def Generate_new_footprint(border_color=[255, 0, 0], border_size=2):
    if border_size < 2:
        border_size = 2

    footprint_with_marco = cv2.copyMakeBorder(
        cv2.cvtColor(aruco.Generate_new_Id(), cv2.COLOR_BGR2RGB),
        top=border_size-1,
        bottom=border_size-1,
        left=border_size-1,
        right=border_size-1,
        borderType=cv2.BORDER_CONSTANT,
        value=(0,0,0),
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
            matrix=video.Get_Frame(),
            footprint=Generate_new_footprint(
                border_color=Led(255, 0, 0).Get_RGB(), border_size=10
            ),
        )

        random_x = randrange(resolution.Get_Width()) + tropa.Get_Footprint().shape[0]
        random_y = randrange(resolution.Get_Height()) + tropa.Get_Footprint().shape[1]

        tropa.Place_Tropa(random_x, random_y, 180)
        tropas.append(tropa)
    asyncio.run(ConsoleInput(tropas))


async def randomMovements(tropas):
    while not video.has_to_stop:
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

def main_random():
    tropas = []
    for i in range(num_tropas):
        tropa = FakeTropa(
            id=next(current_id),
            communication=None,
            color=Led(255, 0, 0),
            matrix=video.Get_Frame(),
            footprint=Generate_new_footprint(
                border_color=Led(255, 0, 0).Get_RGB(), border_size=5
            ),
        )

        random_x = randrange(resolution.Get_Width()) + tropa.Get_Footprint().shape[0]
        random_y = randrange(resolution.Get_Height()) + tropa.Get_Footprint().shape[1]
        random_orientation = possible_orientations[(randrange(4))]

        tropa.Place_Tropa(random_x, random_y, random_orientation)
        tropas.append(tropa)
    asyncio.run(randomMovements(tropas))

if __name__ == "__main__":
    video_thread = video.start()

    main_random()
    exit()
    thread = Thread(target=main_console)
    thread.start()
    thread.join()

