from typing import Optional

# from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGraphicsView
# from console.canvas import Canvas


# class Window(QWidget):
#     """Application's Canvas for Node Rendering."""

#     __POSITION = (200, 200)
#     __SIZE = (800, 600)
#     __MARGINS = (0, 0, 0, 0)
#     __TITLE = "Py-Flow Editor"

#     def __init__(self):
#         super().__init__(None)
#         self.__layout = QVBoxLayout()
#         self.__canvas = Canvas()
#         self.__view = QGraphicsView(self)

#         self.setup_window()
#         self.show()

#     def setup_window(self):
#         self.setGeometry(*self.__POSITION, *self.__SIZE)
#         self.setContentsMargins(*self.__MARGINS)

#         self.setLayout(self.__layout)
#         self.__view.setScene(self.__canvas)
#         self.__layout.addWidget(self.__view)

#         self.setWindowTitle(self.__TITLE)


from pygame import display, RESIZABLE, init


class Window:
    __INSTANCE: Optional["Window"] = None
    __SIZE = (800, 600)
    __TITLE = "Py-Flow Editor"
    __BACKGROUND_COLOR = (10, 10, 10)

    def __new__(cls) -> "Window":
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super().__new__(cls)
            init()
            cls.display = display
            cls.screen = cls.display.set_mode(cls.__SIZE, RESIZABLE)
            cls.display.set_caption(cls.__TITLE)
            cls.screen.fill(cls.__BACKGROUND_COLOR)
        return cls.__INSTANCE
