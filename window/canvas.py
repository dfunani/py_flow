import math
from typing import List, Optional, Tuple
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtCore import QLine, QObject, QRectF
from PyQt5.QtGui import QColor, QPen, QPainter


class Canvas(QGraphicsScene):
    __WIDTH = 20
    __SEGMENTS = 5
    __THIN_LINE = (1, QColor("#2a2a2a"))
    __THICK_LINE = (2, QColor("#3a3a3a"))

    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

        # settings
        self.background_color = QColor("#0a0a0a")

        self.setBackgroundBrush(self.background_color)

    def drawBackground(self, painter: QPainter, rect: QRectF):
        super().drawBackground(painter, rect)

        # here we create our grid
        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.__WIDTH)
        first_top = top - (top % self.__WIDTH)

        # compute all lines to be drawn

        verticals = self.generate_vertical_lines(
            first_left, right, top, bottom
        )
        horizontals = self.generate_horizontal_lines(
            first_top, left, right, bottom
        )

        thin_lines = verticals[1] + horizontals[1]
        thick_lines = verticals[0] + horizontals[0]

        # draw the lines
        self.draw_grid_lines(painter, thin_lines, *self.__THIN_LINE)
        self.draw_grid_lines(painter, thick_lines, *self.__THICK_LINE)

    def draw_grid_lines(
        self, painter: QPainter, lines: List[QLine], width: int, color: QColor
    ):
        pen = QPen(color)
        pen.setWidth(width)
        painter.setPen(pen)
        painter.drawLines(*lines)

    def generate_vertical_lines(
        self, start: int, right: int, top: int, bottom: int
    ) -> Tuple[List[QLine], List[QLine]]:
        thick_lines: List[QLine] = []
        thin_lines: List[QLine] = []
        for x in range(start, right, self.__WIDTH):
            if x % (self.__WIDTH * self.__SEGMENTS) != 0:
                thin_lines.append(QLine(x, top, x, bottom))
            else:
                thick_lines.append(QLine(x, top, x, bottom))
        return thick_lines, thin_lines

    def generate_horizontal_lines(
        self, start: int, left: int, right: int, bottom: int
    ) -> Tuple[List[QLine], List[QLine]]:
        thick_lines: List[QLine] = []
        thin_lines: List[QLine] = []
        for y in range(start, bottom, self.__WIDTH):
            if y % (self.__WIDTH * self.__SEGMENTS) != 0:
                thin_lines.append(QLine(left, y, right, y))
            else:
                thick_lines.append(QLine(left, y, right, y))
        return thick_lines, thin_lines
