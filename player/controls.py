from enum import Enum
from typing import List, Optional
from pygame import (
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    MOUSEMOTION,
    QUIT,
    event,
    K_ESCAPE,
    KEYDOWN,
)

from console.canvas import Canvas, Node


class Inputs(Enum):
    EXIT = "Exited"
    RELEASE = "Released"
    CLICK = "Clicked"
    DRAG = "DRAGGING"


class Player:
    def __init__(self, canvas: Canvas) -> None:
        self.dragging = False
        self.index = None
        self.x = None
        self.y = None
        self.canvas = canvas

    def input(self) -> Optional[Inputs]:
        for target in event.get():
            if target.type == QUIT:
                return Inputs.EXIT
            if target.type == KEYDOWN and target.key == K_ESCAPE:
                return Inputs.EXIT
            if target.type == MOUSEBUTTONDOWN:
                if target.button == 1:
                    for index, node in enumerate(self.canvas.nodes):
                        if node["node"].collidepoint(target.pos):
                            self.dragging = True
                            self.index = index

                            mouse_x, mouse_y = target.pos
                            self.x = node["node"].x - mouse_x
                            self.y = node["node"].y - mouse_y
                            return Inputs.CLICK

            if target.type == MOUSEBUTTONUP:
                if target.button == 1:
                    self.dragging = False
                    self.index = None
                    self.x = None
                    self.y = None
                    return Inputs.RELEASE

            if target.type == MOUSEMOTION:
                if self.dragging and self.index is not None:
                    mouse_x, mouse_y = target.pos
                    self.canvas.nodes[self.index]["node"].x = mouse_x + self.x
                    self.canvas.nodes[self.index]["node"].y = mouse_y + self.y
                    return Inputs.DRAG

        return None
