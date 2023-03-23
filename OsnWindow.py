from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
import requests


class Window(QMainWindow):
    def __init__(self):
        color1 = "background-color: rgb(238, 212, 189);"  # бежевый
        color2 = "background-color: rgb(219, 173, 175);"  # розовый
        color3 = "background-color: rgb(173, 175, 219);\nborder: none;"  # синий для кнопок

        super(Window, self).__init__()
        self.setWindowTitle("Трекер плохого самочувствия")
        self.resize(1910, 1080)
        self.setStyleSheet(color1)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

######## Меню ##########################################################################################################

        self.fon_menu = QtWidgets.QLabel(self.centralwidget)
        self.fon_menu.setGeometry(QtCore.QRect(0, 0, 251, 1080))
        self.fon_menu.setStyleSheet("background-color: rgb(205, 185, 172);")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(25, 23, 180, 180))
        self.photo.setStyleSheet(color2)

        self.loginIn = QtWidgets.QPushButton(self.centralwidget)
        self.loginIn.setGeometry(QtCore.QRect(25, 210, 180, 45))
        self.loginIn.setStyleSheet(color3)
        self.loginIn.setText("Войти")
        self.loginIn.clicked.connect(self.logon)

        self.base = QtWidgets.QPushButton(self.centralwidget)
        self.base.setGeometry(QtCore.QRect(40, 370, 211, 45))
        self.base.setStyleSheet("background-color: rgb(238, 212, 189);\nborder: none;")
        self.base.setText("Главная")
        self.base.clicked.connect(self.baseWindow)

        self.sovets = QtWidgets.QPushButton(self.centralwidget)
        self.sovets.setGeometry(QtCore.QRect(25, 430, 180, 45))
        self.sovets.setStyleSheet(color3)
        self.sovets.setText("Советы")
        self.sovets.clicked.connect(self.sovetsWindow)

        self.profile = QtWidgets.QPushButton(self.centralwidget)
        self.profile.setGeometry(QtCore.QRect(25, 490, 180, 45))
        self.profile.setStyleSheet(color3)
        self.profile.setText("Аккаунт")
        self.profile.clicked.connect(self.profileWindow)

        self.setting = QtWidgets.QPushButton(self.centralwidget)
        self.setting.setGeometry(QtCore.QRect(25, 550, 180, 45))
        self.setting.setStyleSheet(color3)
        self.setting.setText("Настройки")
        self.setting.clicked.connect(self.settingWindow)

        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(24, 850, 180, 45))
        self.exit.setStyleSheet(color3)
        self.exit.setText("Выйти из акаунта")
        self.exit.clicked.connect(self.exitWindow)

######## Календарь #####################################################################################################

        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(300, 23, 640, 400))
        self.calendar.setStyleSheet(color2 + "\ngridline-color: rgb(219, 195, 173);")
        self.calendar.setGridVisible(True)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)

######## Дизайн виджета погоды #########################################################################################

        self.fon = QtWidgets.QLabel(self.centralwidget)
        self.fon.setGeometry(QtCore.QRect(970, 23, 640, 400))
        self.fon.setStyleSheet(color2)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1180, 25, 10, 235))
        self.line.setStyleSheet(color2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(1098, 250, 10, 170))
        self.line_3.setStyleSheet(color2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1226, 250, 10, 170))
        self.line_4.setStyleSheet(color2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(1354, 250, 10, 170))
        self.line_5.setStyleSheet(color2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(1482, 250, 10, 170))
        self.line_6.setStyleSheet(color2)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(970, 250, 640, 10))
        self.line_2.setStyleSheet(color2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)

######## Погода сейчас #################################################################################################

        self.label_now = QtWidgets.QLabel(self.centralwidget)
        self.label_now.setGeometry(QtCore.QRect(970, 23, 200, 60))
        self.label_now.setStyleSheet(color2)
        self.label_now.setAlignment(QtCore.Qt.AlignCenter)
        self.label_now.setText("Сейчас")

        self.label_weather_now = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_now.setGeometry(QtCore.QRect(975, 105, 200, 80))
        self.label_weather_now.setStyleSheet(color2)
        self.label_weather_now.setAlignment(QtCore.Qt.AlignCenter)

######## Погода сегодня ################################################################################################

        self.label_todey = QtWidgets.QLabel(self.centralwidget)
        self.label_todey.setGeometry(QtCore.QRect(1190, 23, 390, 60))
        self.label_todey.setStyleSheet(color2)
        self.label_todey.setAlignment(QtCore.Qt.AlignCenter)
        self.label_todey.setText("Сегодня")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1190, 70, 411, 81))
        self.horizontalLayout_today = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_today.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_today.setSpacing(0)

        self.label_today_00 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_today_00.setStyleSheet(color2)

        self.label_today_03 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_today_03.setStyleSheet(color2)

        self.label_today_06 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_today_06.setStyleSheet(color2)

        self.label_today_09 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_today_09.setStyleSheet(color2)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(1190, 160, 411, 81))
        self.horizontalLayout_today2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_today2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_today2.setSpacing(0)

        self.label_today_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_today_12.setStyleSheet(color2)

        self.label_today_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_today_15.setStyleSheet(color2)

        self.label_today_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_today_18.setStyleSheet(color2)

        self.label_today_21 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_today_21.setStyleSheet(color2)

######## Погода в следующие дни ########################################################################################

        self.label_tomorrow = QtWidgets.QLabel(self.centralwidget)
        self.label_tomorrow.setGeometry(QtCore.QRect(970, 260, 128, 40))
        self.label_tomorrow.setStyleSheet(color2)
        self.label_tomorrow.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tomorrow.setText("Завтра")

        self.label_tomorrow_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_tomorrow_2.setGeometry(QtCore.QRect(1108, 260, 118, 40))
        self.label_tomorrow_2.setStyleSheet(color2)
        self.label_tomorrow_2.setAlignment(QtCore.Qt.AlignCenter)

        self.label_tomorrow_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_tomorrow_3.setGeometry(QtCore.QRect(1236, 260, 118, 40))
        self.label_tomorrow_3.setStyleSheet(color2)
        self.label_tomorrow_3.setAlignment(QtCore.Qt.AlignCenter)

        self.label_tomorrow_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_tomorrow_4.setGeometry(QtCore.QRect(1364, 260, 118, 40))
        self.label_tomorrow_4.setStyleSheet(color2)
        self.label_tomorrow_4.setAlignment(QtCore.Qt.AlignCenter)

        self.label_tomorrow_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_tomorrow_5.setGeometry(QtCore.QRect(1492, 260, 118, 40))
        self.label_tomorrow_5.setStyleSheet(color2)
        self.label_tomorrow_5.setAlignment(QtCore.Qt.AlignCenter)

        self.label_weather_tomorrow = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_tomorrow.setGeometry(QtCore.QRect(980, 300, 110, 80))
        self.label_weather_tomorrow.setStyleSheet(color2)
        self.label_weather_tomorrow.setAlignment(QtCore.Qt.AlignCenter)

        self.label_weather_tomorrow_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_tomorrow_2.setGeometry(QtCore.QRect(1110, 300, 110, 80))
        self.label_weather_tomorrow_2.setStyleSheet(color2)
        self.label_weather_tomorrow_2.setAlignment(QtCore.Qt.AlignCenter)

        self.label_weather_tomorrow_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_tomorrow_3.setGeometry(QtCore.QRect(1240, 300, 110, 80))
        self.label_weather_tomorrow_3.setStyleSheet(color2)
        self.label_weather_tomorrow_3.setAlignment(QtCore.Qt.AlignCenter)

        self.label_weather_tomorrow_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_tomorrow_4.setGeometry(QtCore.QRect(1370, 300, 110, 80))
        self.label_weather_tomorrow_4.setStyleSheet(color2)
        self.label_weather_tomorrow_4.setAlignment(QtCore.Qt.AlignCenter)

        self.label_weather_tomorrow_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_tomorrow_5.setGeometry(QtCore.QRect(1495, 300, 110, 80))
        self.label_weather_tomorrow_5.setStyleSheet(color2)
        self.label_weather_tomorrow_5.setAlignment(QtCore.Qt.AlignCenter)

######## Ежедневные факторы ############################################################################################

        self.label_fakt = QtWidgets.QLabel(self.centralwidget)
        self.label_fakt.setGeometry(QtCore.QRect(300, 450, 440, 40))
        self.label_fakt.setText(" Факторы плохого самочувствия:")

        self.checkStress = QtWidgets.QCheckBox(self.centralwidget)
        self.checkStress.setGeometry(QtCore.QRect(320, 490, 420, 40))
        self.checkStress.setText("Стресс")

        self.checkAlko = QtWidgets.QCheckBox(self.centralwidget)
        self.checkAlko.setGeometry(QtCore.QRect(320, 530, 420, 40))
        self.checkAlko.setText("Употребление алкоголя")

        self.label_kolvo_sna = QtWidgets.QLabel(self.centralwidget)
        self.label_kolvo_sna.setGeometry(QtCore.QRect(300, 570, 440, 40))
        self.label_kolvo_sna.setText("Количество сна:")

        self.horizontalSlider_son = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_son.setGeometry(QtCore.QRect(313, 610, 385, 20))
        self.horizontalSlider_son.setOrientation(QtCore.Qt.Horizontal)

        self.label_son = QtWidgets.QLabel(self.centralwidget)
        self.label_son.setGeometry(QtCore.QRect(315, 630, 420, 30))
        self.label_son.setText("0    1    2    3    4    5    6    7    8    9    10    11    12+")

######## Добавление стресса и боли #####################################################################################

        self.new_pain = QtWidgets.QPushButton(self.centralwidget)
        self.new_pain.setGeometry(QtCore.QRect(760, 450, 180, 100))
        self.new_pain.setStyleSheet(color3)
        self.new_pain.setText("Добавить\nплохое\nсамочувствие")

        self.new_stress = QtWidgets.QPushButton(self.centralwidget)
        self.new_stress.setGeometry(QtCore.QRect(760, 570, 180, 100))
        self.new_stress.setStyleSheet(color3)
        self.new_stress.setText("Добавить\nзапланированный\nстресс")

########################################################################################################################

        self.zametki = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.zametki.setGeometry(QtCore.QRect(970, 450, 910, 600))

        self.mySetFont()
        self.weather()

    def logon(self):
        self.loginIn.hide()
        self.exit.show()

    def baseWindow(self):
        self.base.setStyleSheet("background-color: rgb(238, 212, 189);\nborder: none;")
        self.base.setGeometry(QtCore.QRect(40, 370, 211, 45))

        color = "background-color: rgb(173, 175, 219);\nborder: none;"
        self.sovets.setStyleSheet(color)
        self.sovets.setGeometry(QtCore.QRect(25, 430, 180, 45))
        self.profile.setStyleSheet(color)
        self.profile.setGeometry(QtCore.QRect(25, 490, 180, 45))
        self.setting.setStyleSheet(color)
        self.setting.setGeometry(QtCore.QRect(25, 550, 180, 45))

        self.calendar.show()
        self.fon.show()
        self.line.show()
        self.line_3.show()
        self.line_4.show()
        self.line_5.show()
        self.line_6.show()
        self.line_2.show()
        self.label_now.show()
        self.label_weather_now.show()
        self.label_todey.show()
        self.horizontalLayoutWidget.show()
        self.label_today_00.show()
        self.label_today_03.show()
        self.label_today_06.show()
        self.label_today_09.show()
        self.horizontalLayoutWidget_2.show()
        self.label_today_12.show()
        self.label_today_15.show()
        self.label_today_18.show()
        self.label_today_21.show()
        self.label_tomorrow.show()
        self.label_tomorrow_2.show()
        self.label_tomorrow_3.show()
        self.label_tomorrow_4.show()
        self.label_tomorrow_5.show()
        self.label_weather_tomorrow.show()
        self.label_weather_tomorrow_2.show()
        self.label_weather_tomorrow_3.show()
        self.label_weather_tomorrow_4.show()
        self.label_weather_tomorrow_5.show()
        self.label_fakt.show()
        self.checkStress.show()
        self.checkAlko.show()
        self.label_kolvo_sna.show()
        self.horizontalSlider_son.show()
        self.label_son.show()
        self.new_pain.show()
        self.new_stress.show()
        self.zametki.show()

    def sovetsWindow(self):
        self.sovets.setStyleSheet("background-color: rgb(238, 212, 189);\nborder: none;")
        self.sovets.setGeometry(QtCore.QRect(40, 430, 211, 45))

        color = "background-color: rgb(173, 175, 219);\nborder: none;"
        self.base.setStyleSheet(color)
        self.base.setGeometry(QtCore.QRect(25, 370, 180, 45))
        self.profile.setStyleSheet(color)
        self.profile.setGeometry(QtCore.QRect(25, 490, 180, 45))
        self.setting.setStyleSheet(color)
        self.setting.setGeometry(QtCore.QRect(25, 550, 180, 45))

        self.hideAll()

    def profileWindow(self):
        self.profile.setStyleSheet("background-color: rgb(238, 212, 189);\nborder: none;")
        self.profile.setGeometry(QtCore.QRect(40, 490, 211, 45))

        color = "background-color: rgb(173, 175, 219);\nborder: none;"
        self.base.setStyleSheet(color)
        self.base.setGeometry(QtCore.QRect(25, 370, 180, 45))
        self.sovets.setStyleSheet(color)
        self.sovets.setGeometry(QtCore.QRect(25, 430, 180, 45))
        self.setting.setStyleSheet(color)
        self.setting.setGeometry(QtCore.QRect(25, 550, 180, 45))

        self.hideAll()

    def settingWindow(self):
        self.setting.setStyleSheet("background-color: rgb(238, 212, 189);\nborder: none;")
        self.setting.setGeometry(QtCore.QRect(40, 550, 211, 45))

        color = "background-color: rgb(173, 175, 219);\nborder: none;"
        self.base.setStyleSheet(color)
        self.base.setGeometry(QtCore.QRect(25, 370, 180, 45))
        self.sovets.setStyleSheet(color)
        self.sovets.setGeometry(QtCore.QRect(25, 430, 180, 45))
        self.profile.setStyleSheet(color)
        self.profile.setGeometry(QtCore.QRect(25, 490, 180, 45))

        self.hideAll()

    def exitWindow(self):
        self.loginIn.show()

    def mySetFont(self):
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)

        self.setFont(font)
        self.calendar.setFont(font)
        self.loginIn.setFont(font)
        self.exit.setFont(font)
        self.profile.setFont(font)
        self.base.setFont(font)
        self.setting.setFont(font)
        self.sovets.setFont(font)
        self.label_todey.setFont(font)
        self.label_now.setFont(font)
        self.label_weather_now.setFont(QtGui.QFont("Segoe UI", 15))
        self.label_tomorrow.setFont(font)
        self.label_tomorrow_2.setFont(font)
        self.label_tomorrow_3.setFont(font)
        self.label_tomorrow_4.setFont(font)
        self.label_tomorrow_5.setFont(font)
        self.label_weather_tomorrow_2.setFont(font)
        self.label_weather_tomorrow_3.setFont(font)
        self.label_weather_tomorrow_4.setFont(font)
        self.label_weather_tomorrow_5.setFont(font)
        self.label_today_00.setFont(font)
        self.label_today_03.setFont(font)
        self.label_today_06.setFont(font)
        self.label_today_09.setFont(font)
        self.label_today_12.setFont(font)
        self.label_today_15.setFont(font)
        self.label_today_18.setFont(font)
        self.label_today_21.setFont(font)
        self.new_pain.setFont(font)
        self.new_stress.setFont(font)
        self.label_fakt.setFont(font)
        self.checkStress.setFont(font)
        self.checkAlko.setFont(font)
        self.label_kolvo_sna.setFont(font)
        self.label_son.setFont(font)

    def hideAll(self):
        self.calendar.hide()
        self.fon.hide()
        self.line.hide()
        self.line_3.hide()
        self.line_4.hide()
        self.line_5.hide()
        self.line_6.hide()
        self.line_2.hide()
        self.label_now.hide()
        self.label_weather_now.hide()
        self.label_todey.hide()
        self.horizontalLayoutWidget.hide()
        self.label_today_00.hide()
        self.label_today_03.hide()
        self.label_today_06.hide()
        self.label_today_09.hide()
        self.horizontalLayoutWidget_2.hide()
        self.label_today_12.hide()
        self.label_today_15.hide()
        self.label_today_18.hide()
        self.label_today_21.hide()
        self.label_tomorrow.hide()
        self.label_tomorrow_2.hide()
        self.label_tomorrow_3.hide()
        self.label_tomorrow_4.hide()
        self.label_tomorrow_5.hide()
        self.label_weather_tomorrow.hide()
        self.label_weather_tomorrow_2.hide()
        self.label_weather_tomorrow_3.hide()
        self.label_weather_tomorrow_4.hide()
        self.label_weather_tomorrow_5.hide()
        self.label_fakt.hide()
        self.checkStress.hide()
        self.checkAlko.hide()
        self.label_kolvo_sna.hide()
        self.horizontalSlider_son.hide()
        self.label_son.hide()
        self.new_pain.hide()
        self.new_stress.hide()
        self.zametki.hide()

    def weather(self):
        segodna = 0
        s_city = "Saint Petersburg"
        city_id = 0
        appid = "f1c0ccd792c501d9f5413632128b2da6"
        weather_now1 = ""
        l__00, l__03, l__06, l__09, l__12, l__15, l__18, l__21 = "~", "~", "~", "~", "~", "~", "~", "~"
        weath_tomm, weath_tomm2, weath_tomm3, weath_tomm4, weath_tomm5 = 0, 0, 0, 0, 0

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
            weather_now1 = str(round(data['main']['temp']))
            if weather_now1[0] != '-':
                weather_now1 = "+" + weather_now1
            weather_now_conditions = data['weather'][0]['description']
            weather_now_min = data['main']['temp_min']
            weather_now_max = data['main']['temp_max']
        except Exception as e:
            print("Exception (weather):", e)
            pass

        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            segodna = data['list'][0]['dt_txt'][8:10]
            co = 0
            for i in data['list']:
                if i['dt_txt'][11:13] == '00' and i['dt_txt'][8:10] == segodna:
                    l__00 = '{0:+3.0f}'.format(i['main']['temp'])
                if i['dt_txt'][11:13] == '03' and i['dt_txt'][8:10] == segodna:
                    l__03 = '{0:+3.0f}'.format(i['main']['temp'])
                if i['dt_txt'][11:13] == '06' and i['dt_txt'][8:10] == segodna:
                    l__06 = '{0:+3.0f}'.format(i['main']['temp'])
                if i['dt_txt'][11:13] == '09' and i['dt_txt'][8:10] == segodna:
                    l__09 = '{0:+3.0f}'.format(i['main']['temp'])
                if i['dt_txt'][11:13] == '12' and i['dt_txt'][8:10] == segodna:
                    l__12 = '{0:+3.0f}'.format(i['main']['temp'])
                if i['dt_txt'][11:13] == '15' and i['dt_txt'][8:10] == segodna:
                    l__15 = '{0:+3.0f}'.format(i['main']['temp'])
                if i['dt_txt'][11:13] == '18' and i['dt_txt'][8:10] == segodna:
                    l__18 = '{0:+3.0f}'.format(i['main']['temp'])
                if i['dt_txt'][11:13] == '21' and i['dt_txt'][8:10] == segodna:
                    l__21 = '{0:+3.0f}'.format(i['main']['temp'])
                if i['dt_txt'][8:10] == segodna + 1:
                    weath_tomm += '{0:+3.0f}'.format(i['main']['temp'])
                if i['dt_txt'][8:10] == segodna + 2:
                    weath_tomm2 += '{0:+3.0f}'.format(i['main']['temp'])
                if i['dt_txt'][8:10] == segodna + 3:
                    weath_tomm3 += '{0:+3.0f}'.format(i['main']['temp'])
                if i['dt_txt'][8:10] == segodna + 4:
                    weath_tomm4 += '{0:+3.0f}'.format(i['main']['temp'])
                if i['dt_txt'][8:10] == segodna + 5:
                    weath_tomm5 += '{0:+3.0f}'.format(i['main']['temp'])
                    co += 1

        except Exception as e:
            print("Exception (weather):", e)
            pass


        self.label_weather_now.setText(weather_now1)

        # Определение чисел следующих дней
        self.label_tomorrow_2.setText(str(int(segodna) + 2))
        self.label_tomorrow_3.setText(str(int(segodna) + 3))
        self.label_tomorrow_4.setText(str(int(segodna) + 4))
        self.label_tomorrow_5.setText(str(int(segodna) + 5))

        # Погода в течении дня
        self.label_today_00.setAlignment(QtCore.Qt.AlignCenter)
        self.label_today_00.setText("00:00\n" + l__00)
        self.horizontalLayout_today.addWidget(self.label_today_00)
        self.label_today_03.setAlignment(QtCore.Qt.AlignCenter)
        self.label_today_03.setText("03:00\n" + l__03)
        self.horizontalLayout_today.addWidget(self.label_today_03)
        self.label_today_06.setAlignment(QtCore.Qt.AlignCenter)
        self.label_today_06.setText("06:00\n" + l__06)
        self.horizontalLayout_today.addWidget(self.label_today_06)
        self.label_today_09.setAlignment(QtCore.Qt.AlignCenter)
        self.label_today_09.setText("09:00\n" + l__09)
        self.horizontalLayout_today.addWidget(self.label_today_09)
        self.label_today_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_today_12.setText("12:00\n" + l__12)
        self.horizontalLayout_today2.addWidget(self.label_today_12)
        self.label_today_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_today_15.setText("15:00\n" + l__15)
        self.horizontalLayout_today2.addWidget(self.label_today_15)
        self.label_today_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_today_18.setText("18:00\n" + l__18)
        self.horizontalLayout_today2.addWidget(self.label_today_18)
        self.label_today_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_today_21.setText("21:00\n" + l__21)
        self.horizontalLayout_today2.addWidget(self.label_today_21)

        # Погода на следующие дни
        self.label_weather_tomorrow.setText(str(weath_tomm))
