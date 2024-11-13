from enum import Enum
from typing import Optional
from pygame import QUIT, event

class Inputs(Enum):
    EXIT = "Exited"
    PRESS = "Pressed"
    CLICK = "Clicked"

class Player:
    def __init__(self) -> None:
        pass

    def input(self) -> Optional[Inputs]:
        for target in event.get():
            if target.type == QUIT:
                return Inputs.EXIT
        return None
