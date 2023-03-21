from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import requests


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Календарик мигрени")
        self.setGeometry(0, 0, 1920, 1080)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 20, 640, 370))
        self.calendarWidget.setFont(font)

        self.btnMgr = QtWidgets.QPushButton(self.centralwidget)
        self.checkAlco = QtWidgets.QCheckBox(self.centralwidget)
        self.checkStress = QtWidgets.QCheckBox(self.centralwidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.Son = QtWidgets.QSlider(self.centralwidget)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.fon = QtWidgets.QLabel(self.centralwidget)
        self.label_now = QtWidgets.QLabel(self.centralwidget)
        self.weather_now = QtWidgets.QLabel(self.centralwidget)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.label_today = QtWidgets.QLabel(self.centralwidget)
        self.label_tomorrow = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_26 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_28 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_25 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_24 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_0 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.label__0 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label__3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label__6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label__9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label__12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label__15 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label__18 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label__21 = QtWidgets.QLabel(self.verticalLayoutWidget_4)

        self.btnMgr.setFont(font)
        self.checkAlco.setFont(font)
        self.checkStress.setFont(font)
        self.label.setFont(font)
        self.Son.setFont(font)
        self.textBrowser.setFont(font)
        self.fon.setFont(font)
        self.label_now.setFont(font)
        self.weather_now.setFont(font)
        self.horizontalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget_2.setFont(font)
        self.label_today.setFont(font)
        self.label_tomorrow.setFont(font)
        self.label_26.setFont(font)
        self.label_28.setFont(font)
        self.label_25.setFont(font)
        self.label_24.setFont(font)
        self.label_0.setFont(font)
        self.label_3.setFont(font)
        self.label_6.setFont(font)
        self.label_9.setFont(font)
        self.label_12.setFont(font)
        self.label_15.setFont(font)
        self.label_18.setFont(font)
        self.label_21.setFont(font)
        self.verticalLayoutWidget_3.setFont(font)
        self.verticalLayoutWidget_4.setFont(font)
        self.label__0.setFont(font)
        self.label__3.setFont(font)
        self.label__6.setFont(font)
        self.label__9.setFont(font)
        self.label__12.setFont(font)
        self.label__15.setFont(font)
        self.label__18.setFont(font)
        self.label__21.setFont(font)

        self.btnMgr.setGeometry(QtCore.QRect(20, 410, 640, 40))
        self.btnMgr.setText("У меня сегодня болит голова")

        self.checkAlco.setGeometry(QtCore.QRect(30, 460, 170, 40))
        self.checkAlco.setText("Употребление алкоголя")

        self.checkStress.setGeometry(QtCore.QRect(30, 500, 170, 40))
        self.checkStress.setText("Стресс")
        self.checkStress.clicked.connect(self.chekStresss)

        self.label.setGeometry(QtCore.QRect(48, 540, 610, 30))
        self.label.setText("Количество сна:")

        self.Son.setGeometry(QtCore.QRect(20, 570, 640, 20))
        self.Son.setOrientation(QtCore.Qt.Horizontal)

        self.textBrowser.setGeometry(QtCore.QRect(20, 610, 640, 420))

        self.weatherWidget()

    def weatherWidget(self):
        s_city = "Saint Petersburg"
        city_id = 0
        appid = "f1c0ccd792c501d9f5413632128b2da6"
        weather_now1 = ""
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/find",
                               params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
            data = res.json()
            city_id = data['list'][0]['id']
        except Exception as e:
            print("Exception (find):", e)
            pass

        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            weather_now_conditions = data['weather'][0]['description']
            weather_now1 = str(data['main']['temp'])
            weather_now_min = data['main']['temp_min']
            weather_now_max = data['main']['temp_max']
        except Exception as e:
            print("Exception (weather):", e)
            pass

        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            for i in data['list']:
                print(i['dt_txt'], '{0:+3.0f}'.format(i['main']['temp']), i['weather'][0]['description'])
        except Exception as e:
            print("Exception (weather):", e)
            pass


        self.fon.setGeometry(QtCore.QRect(1210, 90, 560, 310))
        self.fon.setStyleSheet("background-color: rgb(205, 199, 221);")

        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1210, 290, 560, 110))
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1450, 130, 40, 140))
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1600, 130, 41, 141))
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(1660, 130, 40, 140))
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(1510, 130, 41, 141))
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.label_now.setGeometry(QtCore.QRect(1250, 100, 60, 20))
        self.label_now.setText("Сейчас")

        self.weather_now.setGeometry(QtCore.QRect(1250, 140, 80, 70))
        self.weather_now.setFont(QFont('Segoe UI', 15))
        self.weather_now.setText(weather_now1)

        self.label_today.setGeometry(QtCore.QRect(1450, 100, 80, 20))
        self.label_today.setText("Сегодня")

        self.label_tomorrow.setText("Завтра")
        self.horizontalLayout.addWidget(self.label_tomorrow)

        self.horizontalLayout.addWidget(self.label_26)
        self.horizontalLayout.addWidget(self.label_28)
        self.horizontalLayout.addWidget(self.label_25)
        self.horizontalLayout.addWidget(self.label_24)

        self.label_0.setText("00:00")
        self.verticalLayout.addWidget(self.label_0)
        self.label_3.setText("03:00")
        self.verticalLayout.addWidget(self.label_3)
        self.label_6.setText("06:00")
        self.verticalLayout.addWidget(self.label_6)
        self.label_9.setText("09:00")
        self.verticalLayout.addWidget(self.label_9)
        self.label_12.setText("12:00")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_15.setText("15:00")
        self.verticalLayout_2.addWidget(self.label_15)
        self.label_18.setText("18:00")
        self.verticalLayout_2.addWidget(self.label_18)
        self.label_21.setText("21:00")
        self.verticalLayout_2.addWidget(self.label_21)

        self.verticalLayout_3.addWidget(self.label__0)
        self.verticalLayout_3.addWidget(self.label__3)
        self.verticalLayout_3.addWidget(self.label__6)
        self.verticalLayout_3.addWidget(self.label__9)
        self.verticalLayout_4.addWidget(self.label__12)
        self.verticalLayout_4.addWidget(self.label__15)
        self.verticalLayout_4.addWidget(self.label__18)
        self.verticalLayout_4.addWidget(self.label__21)

    def chekStresss(self):
        self.checkStress.setText("Вторая надпись")


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
