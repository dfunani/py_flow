from typing import Optional

from components.complex import ComplexNode
from components.primitive import PrimitiveNode
from console.canvas import Canvas
from console.window import Window
from models.files import JsonFileManager
from player.controls import Player
from pygame import quit, time


class GameManager:
    __INSTANCE: Optional["GameManager"] = None

    def __new__(cls, player: Player, window: Window, canvas: Canvas) -> "GameManager":
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super().__new__(cls)
            cls.player = player
            cls.window = window
            cls.canvas = canvas
        return cls.__INSTANCE

    def start_game(self):
        while True:
            self.canvas.draw()

            if self.player.input() is not None:
                break

            self.window.display.flip()
            self.window.display.update()

            fps = time.Clock()
            fps.tick(60)

        quit()


def main():
    player = Player()
    window = Window()
    canvas = Canvas(window)
    app = GameManager(player, window, canvas)
    app.start_game()


if __name__ == "__main__":
    canvas_data = None
    with open("./temp.json") as file:
        data = JsonFileManager().read(file)
        ComplexNode(data).draw()
