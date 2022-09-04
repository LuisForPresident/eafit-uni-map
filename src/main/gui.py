import sys

# Will be changed to PyQt6 in the near future
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget

WINDOW_SIZE = 500


class guiWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)


def main():
    guiApp = QApplication([])
    guiWindow = guiWindow()
    guiWindow.show()
    sys.exit(guiApp.exec())


if __name__ == "__main__":
    main()
