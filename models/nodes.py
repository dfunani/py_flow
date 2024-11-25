from abc import ABC, abstractmethod


class INode(ABC):
    @abstractmethod
    def draw(self, offset: int = 1):
        pass

