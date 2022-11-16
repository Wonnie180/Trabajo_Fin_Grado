from abc import abstractmethod, ABCMeta

class IPosition(metaclass=ABCMeta):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def Get_Position(self) -> list[int]:
        pass

    @abstractmethod
    def Set_Position(self, new_position: list[int]):
        pass

    @abstractmethod
    def Check_Position_Length(self, position: list[int]):
        pass