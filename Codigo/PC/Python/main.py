from Tropa.Tropa import Tropa
from Comunicaciones.Bluetooth import Bluetooth


if __name__ == '__main__':
    prueba = Tropa(id=1011, communication=Bluetooth())

    prueba.Set_Color([100, 100, 100])
    prueba.communication.Search_Devices()

    print(prueba.communication.Get_Devices())
    print(prueba.id)
