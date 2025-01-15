from abc import ABC, abstractmethod
from typing import Tuple


class INode(ABC):
    @abstractmethod
    def draw(self, position: Tuple[int, int]):
        pass

