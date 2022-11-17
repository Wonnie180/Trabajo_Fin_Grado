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
from Utils.Resolution import Resolution
from Tropas.FakeTropa import FakeTropa
from VideoSource.WebCam import WebCam
from Leds.Led import Led
from VideoPlayback.CV2ImShow_Drawable import CV2ImShow_Drawable
from Geometries.Rectangles.Rectangle_Drawable import Rectangle_Drawable
from Geometries.Circles.Circle_Drawable import Circle_Drawable
from Geometries.Text.Text_Drawable import Text_Drawable
from Color.Color import Color


seed(0xDEADBEEF)
current_id = count(1)

resolution = Resolution(1280, 720)

aruco = Aruco()
aruco.Generate_Dictionary()

video_source = WebCam(resolution,0)
video_playback = CV2ImShow_Drawable("Video TFG Luis", video_source)




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

def main_random():
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
        random_orientation = possible_orientations[(randrange(4))]
        tropa.Place_Tropa(random_x, random_y, random_orientation)
        tropas.append(tropa)
    asyncio.run(randomMovements(tropas))



def draw_aruco(corners, ids):
    rectangles = []
    circles = []
    texts = []
    if len(corners) > 0:
        for (markerCorner, markerID) in zip(corners, ids):
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners

            topRight = (int(topRight[0]), int(topRight[1]))
            bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
            topLeft = (int(topLeft[0]), int(topLeft[1]))

            
            cX = int((topLeft[0] + bottomRight[0]) / 2.0)
            cY = int((topLeft[1] + bottomRight[1]) / 2.0)

            rectangle = Rectangle_Drawable(topLeft, topRight, bottomLeft, bottomRight, Color((255,0,0)))
            circle = Circle_Drawable((cX,cY), 4, Color((0,0,255)))
            text = Text_Drawable(topLeft, str(markerID),Color((255,0,255)))

            rectangles.append(rectangle)
            circles.append(circle)
            texts.append(text)

    video_playback.Add_Rectangles(rectangles)
    video_playback.Add_Circles(circles)
    video_playback.Add_Texts(texts)
            
            
def deteccion_aruco():
    while not video_playback.Has_To_Stop():
        (corners, ids, _) = aruco.Detect_Aruco(video_source.Get_Frame())
        draw_aruco(corners, ids)
        

if __name__ == "__main__":
    thread_video = Thread(target=video_playback.Play, args=()).start()
    thread_aruco = Thread(target=deteccion_aruco,args=()).start()
    #thread_main =  Thread(target=main_random, args=()).start()
