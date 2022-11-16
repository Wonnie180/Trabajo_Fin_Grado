from abc import abstractmethod, ABCMeta

class ICommand(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def Execute_Command(self):
        pass

    @abstractmethod
    def Have_Finished_Command(self) -> bool:
        pass
