# System Libraries
import asyncio
import cv2
from threading import Thread
from itertools import count
from random import randrange, seed

# Custom Libraries
from Utils.Resolution import Resolution
from Tropas.FakeTropa import FakeTropa
from VideoSource.FakeVideo import FakeVideo
from VideoPlayback.CV2ImShow_Drawable import CV2ImShow_Drawable
from Utils.Frame import Frame
from Positions.Position_2D import Position_2D
from Color.Color import Color
from Arucos.Aruco_Drawable import Aruco_Drawable

seed(0xDEADBEEF)

resolution = Resolution(800, 800)
common_frame = Frame(resolution)

video_source = FakeVideo(common_frame)
video_playback = CV2ImShow_Drawable("Video TFG Luis", video_source)
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
detector_parameters =  cv2.aruco.DetectorParameters_create()
aruco = Aruco_Drawable(dictionary,detector_parameters,video_source, video_playback)

possible_orientations = [0, 90, 180, 270]
num_tropas = 10

async def randomMovements(tropas):
    while not video_playback.Has_To_Stop():
        await asyncio.sleep(0.05)
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
            communication=None,
            color=Color((255, 0, 0)),
            matrix=video_source.Get_Frame(),
            footprint=footprint,
        )

        tropas.append(tropa)
    asyncio.run(randomMovements(tropas))

if __name__ == "__main__":
    thread_main = Thread(target=main_random, args=()).start()
    thread_aruco = Thread(target=aruco.Run, args=()).start()
    thread_video = Thread(target=video_playback.Run, args=()).start()

    exit()
