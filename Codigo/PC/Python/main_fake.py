from asyncio import sleep
import asyncio
import time
from VideoSource.Resolution import Resolution
from Tropas.FakeTropa import FakeTropa
from VideoSource.FakeVideo import FakeVideo

from Leds.Led import Led
from itertools import count

import cv2

current_id = count(1)

refPt = []
resolution = Resolution(600,600)

def click_drag_callback(event, x, y, flags, param):
    global refPt
    frame = param[0]
    resolution: Resolution = param[1]
    imshow_title = param[2]

    color = (255, 0, 0)
    thickness = 5

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        if not resolution.Is_In_Bounds(x, y):
            refPt = []
            return

        cv2.rectangle(frame, refPt[0], refPt[1], color, thickness)
        # cv2.imshow(imshow_title, image)

    elif event == cv2.EVENT_RBUTTONUP:
        refPt = []

video = FakeVideo(resolution, click_drag_callback)


def Generar_Tropas(numero_Tropas, color=None):
    Tropas = [
        FakeTropa(
            id=next(current_id),
            communication=None,
            color=Led(),
            matrix=video.Get_Frame(),
            pos_y=x % resolution.Get_Height(),
            pos_x=x // resolution.Get_Width(),
            size=50,
        )
        for x in range(numero_Tropas)
    ]

    if color is not None:
        [i.color.Set_RGB(color[0], color[1], color[2]) for i in Tropas]

    return Tropas


async def moverTropas(tropa):

    for number in range(200):
        await asyncio.sleep(0.5)
        video.Show_Video()
        tropa.Move_Forward()
    return


def main() -> None:

    # Tropas_Azules = Generar_Tropas(5, [0, 0, 200])
    tropa = FakeTropa(
        id=next(current_id),
        communication=None,
        color=Led(),
        matrix=video.Get_Frame(),
        pos_y=0 % resolution.Get_Height(),
        pos_x=0 // resolution.Get_Width(),
        size=50,
    )
    # Tropas_Azules[4].Move_Forward()

    print(video.Get_Frame())


def click_drag_callback(event, x, y, flags, param):
    global refPt
    frame = param[0]
    resolution: Resolution = param[1]
    imshow_title = param[2]

    color = (255, 0, 0)
    thickness = 5

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        if not resolution.Is_In_Bounds(x, y):
            refPt = []
            return

        cv2.rectangle(frame, refPt[0], refPt[1], color, thickness)
        # cv2.imshow(imshow_title, image)

    elif event == cv2.EVENT_RBUTTONUP:
        refPt = []

if __name__ == "__main__":
    tropa = FakeTropa(
        id=next(current_id),
        communication=None,
        color=Led(),
        matrix=video.Get_Frame(),
        pos_y=0 % resolution.Get_Height(),
        pos_x=0 // resolution.Get_Width(),
        size=50,
    )

    asyncio.run(moverTropas(tropa))
    # loop = asyncio.get_event_loop()
    # single = asyncio.gather(test(), moverTropas(tropa))
    # loop.run_until_complete(single)


