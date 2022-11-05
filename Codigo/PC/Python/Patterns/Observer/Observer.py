from abc import ABC, abstractmethod
from Observable import Observable

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Observable) -> None:
        """
        Receive update from subject.
        """
        pass