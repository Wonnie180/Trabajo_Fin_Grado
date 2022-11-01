from Tropas.Tropa import Tropa
from Comunicaciones.Bluetooth import Bluetooth
from Leds.Led import Led
from itertools import count


current_id = count(1)

def Generar_Tropas(numero_Tropas, color = None):
    Tropas = [Tropa(id=next(current_id), communication=Bluetooth(), color=Led()) for x in range(numero_Tropas)]
    
    if (color is not None):
        [i.color.Set_RGB(color[0],color[1],color[2]) for i in Tropas]

    return Tropas

def main() -> None:
    Tropas_Azules = Generar_Tropas(5, [0,0,200])
    Tropas_Rojas = Generar_Tropas(5)

    [i.color.Set_RGB(200,0,0) for i in Tropas_Rojas]

    [print(i.id, i.color.Get_RGB()) for i in Tropas_Azules]
    [print(i.id, i.color.Get_RGB()) for i in Tropas_Rojas]


    # prueba.color.Set_RGB(100, 200, 300)
    # print(prueba.color.Get_BGR())
    # print(prueba.color.Get_RGB())
    # # prueba.communication.Search_Devices()

    # # print(prueba.communication.Get_Devices())
    # print(prueba.id)

if __name__ == '__main__':
    main()
