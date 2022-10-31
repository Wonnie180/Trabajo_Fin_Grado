from abc import ABC, abstractmethod


class ITropa(ABC):
    def __init__(self, id):
        self.id = id
        super().__init__()

    @abstractmethod
    def Move_Forward(self):
        pass

    @abstractmethod
    def Move_Backwards(self):
        pass

    @abstractmethod
    def Turn_Left(self):
        pass

    @abstractmethod
    def Turn_Right(self):
        pass
      

