from PyQt5.QtWidgets import QApplication
import sys
from OsnWindow import Window


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
