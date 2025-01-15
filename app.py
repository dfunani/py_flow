from typing import Any, Optional

from components.complex import ComplexNode
from components.primitive import PrimitiveNode
from console.canvas import Canvas, NodeTypes
from console.window import Window
from models.files import JsonFileManager
from player.controls import Inputs, Player
from pygame import quit, time
from models.types import Primitive

class GameManager:
    __INSTANCE: Optional["GameManager"] = None

    def __new__(cls, player: Player, window: Window, canvas: Canvas, data: Any) -> "GameManager":
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super().__new__(cls)
            cls.player = player
            cls.window = window
            cls.canvas = canvas
            cls.data = data
            cls.position = (100, 100)
            cls.display_data()
        return cls.__INSTANCE
    
    @classmethod
    def display_data(cls):
        if isinstance(cls.data, Primitive):
            PrimitiveNode(cls.data, cls.canvas).draw(cls.position)
        else:
            ComplexNode(cls.data, cls.canvas).draw(cls.position)

    def start_game(self):
        while True:
            self.window.clear()
            self.canvas.draw()
            self.canvas.draw_node()

            if self.player.input() == Inputs.EXIT:
                break
            
            self.window.display.flip()
            self.window.display.update()

            fps = time.Clock()
            fps.tick(60)

        quit()


def main():
    window = Window()
    canvas = Canvas(window)
    player = Player(canvas)
    with open("./temp.json") as file:
        data = JsonFileManager().read(file)
        app = GameManager(player, window, canvas, data)
    app.start_game()


if __name__ == "__main__":
    main()
