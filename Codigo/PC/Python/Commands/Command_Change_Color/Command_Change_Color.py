import os
import sys
import cv2

if __name__ != "__main__":
    sys.path.append(os.path.dirname(__file__))

sys.path.append(
    os.path.join(os.path.dirname(__file__), ".." + os.path.sep + ".." + os.path.sep)
)

from Commands.ICommand import ICommand
from Tropas.ITropa import ITropa
from Leds.ILed import ILed

class Command_Change_Color(ICommand):
    tropa: ITropa
    color: ILed
    have_finished: bool = False

    def __init__(self, tropa: ITropa, color:ILed):
        self.tropa = tropa
        self.color = color
        super().__init__()

    def Execute_Command(self):
        if not self.Have_Finished_Command():
            self.tropa.color.Set_RGB(self.color.Get_RGB())
            # self.tropa.communication.Send_Data(TROPA_ACTIONS,tropa.color.Get_RGB())
            self.tropa.footprint[(self.tropa.footprint != 0).all(2)] = self.tropa.color.Get_RGB()
            self.have_finished = True

    def Have_Finished_Command(self) -> bool:
        return self.have_finished


if __name__ == "__main__":
    from Aruco.Aruco import Aruco
    from Leds.Led import Led
    from Utils.Resolution import Resolution
    import numpy as np
    from Tropas.FakeTropa import FakeTropa
    from Positions.Position_2D import Position_2D
    import cv2

    resolution = Resolution(600, 600)
    led = Led([255, 0, 0])
    aruco = Aruco()
    aruco.Generate_Dictionary()

    footprint = cv2.cvtColor(
        aruco.Generate_new_Id(Resolution(100, 100)), cv2.COLOR_GRAY2RGB 
    )



    frame = np.zeros([resolution.Get_Width(), resolution.Get_Height(), 3])
    tropa = FakeTropa(1, None,led , frame, footprint, Position_2D([0, 0, 0]))
    tropa.Update_Matrix(tropa.position.x, tropa.position.y)
    prueba = Command_Change_Color(tropa, Led([0,255,0]))
    
    cv2.imshow("a",frame)
    cv2.waitKey(0)
    prueba.Execute_Command()
    tropa.Update_Matrix(tropa.position.x, tropa.position.y)
    cv2.imshow("a",frame)
    cv2.waitKey(0)
    print(tropa.footprint)

