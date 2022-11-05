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

    Tropas_Azules[0].communication.Search_Devices()

if __name__ == '__main__':
    main()
