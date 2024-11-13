from typing import Tuple

from pygame import draw
from console.window import Window


class Canvas:
    __WIDTH = 20
    __SEGMENTS = 5
    __THIN_LINE = (1, (42, 42, 42))
    __THICK_LINE = (2, (58, 58, 58))

    def __init__(self, window: Window) -> None:
        self.window = window

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
