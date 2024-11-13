import sys
from PyQt5.QtWidgets import QApplication

from window.scene import Window



def main():
    app = QApplication([])

    scene = Window()
    scene.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
