from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsView
from window.canvas import Canvas


class Window(QWidget):
    """Application's Canvas for Node Rendering."""

    __POSITION = (200, 200)
    __SIZE = (800, 600)
    __MARGINS = (0, 0, 0, 0)
    __TITLE = "Py-Flow Editor"

    def __init__(self):
        super().__init__(None)
        self.__layout = QVBoxLayout()
        self.__canvas = Canvas()
        self.__view = QGraphicsView(self)

        self.setup_window()
        self.show()

    def setup_window(self):
        self.setGeometry(*self.__POSITION, *self.__SIZE)
        self.setContentsMargins(*self.__MARGINS)

        self.setLayout(self.__layout)
        self.__view.setScene(self.__canvas)
        self.__layout.addWidget(self.__view)

        self.setWindowTitle(self.__TITLE)
