from abc import abstractmethod, ABCMeta


class ILed(metaclass=ABCMeta):
    R : int = 0
    G : int = 0
    B : int = 0

    def __init__(self):
        super().__init__()

    @abstractmethod
    def Get_RGB(self):
        pass

    @abstractmethod
    def Set_RGB(self, R :int, G:int, B:int):
        pass

    @abstractmethod
    def Get_BGR(self):
        pass

    @abstractmethod
    def Set_BGR(self, B :int, G:int, R:int):
        pass
   

if __name__ == '__main__':
    print("Hello")
