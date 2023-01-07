from abc import abstractmethod, ABCMeta

class ICommand(metaclass=ABCMeta):        
    executing: bool = False

    def __init__(self):
        super().__init__()

    @abstractmethod
    def Execute(self):
        pass

    @abstractmethod
    def Have_Finished(self) -> bool:
        pass

    @abstractmethod
    def Get_Type(self):
        pass

    @abstractmethod
    def Equal(self, command):
        pass
