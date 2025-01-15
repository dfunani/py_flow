from enum import Enum
from typing import Any, Dict, List, Tuple, TypedDict
from pygame import Rect, draw
from console.window import Window


class NodeTypes(Enum):
    PRIMITIVE = "primitive"
    COMPLEX = "complex"



class NodeData(TypedDict):
    value: Any
    type: Any

class Node(TypedDict):
    node: Rect
    type: NodeTypes
    data: NodeData

class Canvas:
    __WIDTH = 20
    __SEGMENTS = 5
    __THIN_LINE = (1, (42, 42, 42))
    __THICK_LINE = (2, (58, 58, 58))
    __NODE_COLORS = {
        NodeTypes.PRIMITIVE: [(255, 255, 0), (0, 0, 0)],
        NodeTypes.COMPLEX: [(0, 255, 255), (0, 0, 0)],
    }
    __NODE_WIDTHS = {NodeTypes.PRIMITIVE: 100, NodeTypes.COMPLEX: 50}

    def __init__(self, window: Window) -> None:
        self.window = window
        self.nodes: List[Node] = []

    def draw(self):
        # here we create our grid.
        rect = self.window.screen.get_rect()
        left = rect.left
        right = rect.right
        top = rect.top
        bottom = rect.bottom

        first_left = left - (left % self.__WIDTH)
        first_top = top - (top % self.__WIDTH)

        # compute all lines to be drawn

        self.draw_vertical_lines(first_left, right, top, bottom)
        self.draw_horizontal_lines(first_top, left, right, bottom)

    def draw_vertical_lines(
        self, start: int, right: int, top: int, bottom: int
    ) -> None:
        for x in range(start, right, self.__WIDTH):
            if x % (self.__WIDTH * self.__SEGMENTS) != 0:
                line = self.__THIN_LINE
            else:
                line = self.__THICK_LINE

            draw.line(self.window.screen, line[1], (x, top), (x, bottom), line[0])

    def draw_horizontal_lines(
        self, start: int, left: int, right: int, bottom: int
    ) -> None:
        for y in range(start, bottom, self.__WIDTH):
            if y % (self.__WIDTH * self.__SEGMENTS) != 0:
                line = self.__THIN_LINE
            else:
                line = self.__THICK_LINE

            draw.line(self.window.screen, line[1], (left, y), (right, y), line[0])

    def add_node(self, position: Tuple[int, int], node_type: NodeTypes, data: NodeData):
        if node_type == NodeTypes.PRIMITIVE:
            node = self.__generate_primitive_node(position)
        else:
            node = self.__generate_complex_node(position)

        self.nodes.append({"node": node, "type": node_type, "data": data})

    def draw_node(self):
        for node in self.nodes:
            draw.rect(
                self.window.screen, self.__NODE_COLORS[node["type"]][0], node["node"]
            )
            self.window.screen.blit(
                self.window.font.render(
                    str(node["data"]["value"]), True, self.__NODE_COLORS[node["type"]][1]
                ),
                node["node"].topleft,
            )
            self.window.screen.blit(
                self.window.font.render(
                    str(node["data"]["type"]), True, self.__NODE_COLORS[node["type"]][1]
                ),
                (node["node"].topleft[0], node["node"].topleft[1] + 20),
            )

    def __generate_primitive_node(self, position: Tuple[int, int]):
        x, y = position
        node = Rect(x, y, 100, 100)
        return node

    def __generate_complex_node(self, position: Tuple[int, int]):
        x, y = position
        node = Rect(x, y, 100, 250)
        return node
