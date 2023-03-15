from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Календарик мигрени")
        self.setGeometry(0, 0, 1920, 1080)

        self.centralwidget = QtWidgets.QWidget(self)
        # self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 20, 640, 370))
        self.calendarWidget.setFont(font)
        # self.calendarWidget.setObjectName("Objectcentralwidget")

        self.btnMgr = QtWidgets.QPushButton(self.centralwidget)
        self.btnMgr.setGeometry(QtCore.QRect(20, 410, 640, 40))
        self.btnMgr.setFont(font)
        self.btnMgr.setText("У меня сегодня болит голова")
        # self.pushButton.setObjectName("Objectcentralwidget")

        self.checkAlco = QtWidgets.QCheckBox(self.centralwidget)
        self.checkAlco.setGeometry(QtCore.QRect(30, 460, 170, 40))
        self.checkAlco.setFont(font)
        self.checkAlco.setText("Употребление алкоголя")
        # self.checkAlco.setObjectName("Objectcentralwidget")

        self.checkStress = QtWidgets.QCheckBox(self.centralwidget)
        self.checkStress.setGeometry(QtCore.QRect(30, 500, 170, 40))
        self.checkStress.setFont(font)
        self.checkStress.setText("Стресс")
        # self.checkBox_2.setObjectName("Objectcentralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(48, 540, 610, 30))
        self.label.setFont(font)
        self.label.setText("Количество сна:")
        # self.label.setObjectName("Objectcentralwidget")

        self.Son = QtWidgets.QSlider(self.centralwidget)
        self.Son.setGeometry(QtCore.QRect(20, 570, 640, 20))
        self.Son.setFont(font)
        self.Son.setOrientation(QtCore.Qt.Horizontal)
        # self.horizontalSlider.setObjectName("Objectcentralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 610, 640, 420))
        self.textBrowser.setFont(font)
        # self.textBrowser.setObjectName("Objectcentralwidget")

        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setText("Нажми на меня")
        self.btn.clicked.connect(self.add_label)

        self.new_text = QtWidgets.QLabel(self.centralwidget)

    def add_label(self):
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100, 50)
        self.new_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()