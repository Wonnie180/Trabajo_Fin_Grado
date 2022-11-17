import os
import sys

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(os.path.join(os.path.dirname(__file__), ".." + os.path.sep+".." + os.path.sep))

from Color.Color import Color


def test_color_R_G_B():
    color = Color((255,128,0))
    assert color.r == 255
    assert color.g == 128
    assert color.b == 0

def test_color_RGB():
    color = Color((255,128,0))
    assert color.RGB == (255,128,0)

def test_color_BGR():
    color = Color((255,128,0))
    assert color.BGR == (0,128,255)

def test_color_set_RGB():
    color = Color((255,128,0))
    color.Set_RGB((0,0,0))
    assert color.RGB == (0,0,0)