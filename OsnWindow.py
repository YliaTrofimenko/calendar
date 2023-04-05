from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow
import requests


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Трекер плохого самочувствия")
        self.resize(1910, 1080)
        self.setWindowIcon(QtGui.QIcon('photo/icon.png'))
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

    # Списки для форматирования
        self.btns = []
        self.fons = []
        self.ggvp = []

    # Списки раазных окон
        self.winAddpein = []
        self.leftMenu = []
        self.winAkkIN = []
        self.winAkk = []
        self.winAkkCreate = []
        self.winSovet = []
        self.winSetting = []

        with open('files/color.txt', 'r') as f:
            self.color1 = f.readline()
            self.color2 = f.readline()
            self.color3 = f.readline()
            self.color4 = f.readline()

        with open('files/akk.txt', 'r') as f:
            m = f.readline()
            if m == '1\n':
                self.nalichieakkaunta = True
                self.log = f.readline().rstrip()
                self.pas = f.readline().rstrip()
            else:
                self.nalichieakkaunta = False

######## Меню ##########################################################################################################

        self.fon_menu = QtWidgets.QLabel(self.centralwidget)
        self.fon_menu.setGeometry(QtCore.QRect(0, 0, 251, 1080))

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(25, 23, 180, 180))
        self.fons.append(self.photo)
        self.leftMenu.append(self.photo)

        self.base = QtWidgets.QPushButton(self.centralwidget)
        self.base.setGeometry(QtCore.QRect(40, 370, 211, 45))
        self.base.setText("Главная")
        self.base.clicked.connect(self.baseWindow)
        self.btns.append(self.base)
        self.leftMenu.append(self.base)

        self.sovets = QtWidgets.QPushButton(self.centralwidget)
        self.sovets.setGeometry(QtCore.QRect(25, 430, 180, 45))
        self.sovets.setText("Советы")
        self.sovets.clicked.connect(self.sovetsWindow)
        self.btns.append(self.sovets)
        self.leftMenu.append(self.sovets)

        self.profile = QtWidgets.QPushButton(self.centralwidget)
        self.profile.setGeometry(QtCore.QRect(25, 490, 180, 45))
        self.profile.setText("Аккаунт")
        self.profile.clicked.connect(self.profileWindow)
        self.btns.append(self.profile)
        self.leftMenu.append(self.profile)

        self.setting = QtWidgets.QPushButton(self.centralwidget)
        self.setting.setGeometry(QtCore.QRect(25, 550, 180, 45))
        self.setting.setText("Настройки")
        self.setting.clicked.connect(self.settingWindow)
        self.btns.append(self.setting)
        self.leftMenu.append(self.setting)

######## Календарь и заметки ###########################################################################################

        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(300, 23, 640, 400))
        self.calendar.setGridVisible(True)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.ggvp.append(self.calendar)

        self.zametki = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.zametki.setGeometry(QtCore.QRect(970, 450, 910, 523))
        self.fons.append(self.zametki)
        self.ggvp.append(self.zametki)

######## Дизайн виджета погоды #########################################################################################

        self.fon = QtWidgets.QLabel(self.centralwidget)
        self.fon.setGeometry(QtCore.QRect(970, 23, 640, 400))
        self.fons.append(self.fon)
        self.ggvp.append(self.fon)

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1180, 25, 10, 235))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fons.append(self.line)
        self.ggvp.append(self.line)

        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(1098, 250, 10, 170))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fons.append(self.line_3)
        self.ggvp.append(self.line_3)

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1226, 250, 10, 170))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fons.append(self.line_4)
        self.ggvp.append(self.line_4)

        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(1354, 250, 10, 170))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fons.append(self.line_5)
        self.ggvp.append(self.line_5)

        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(1482, 250, 10, 170))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fons.append(self.line_6)
        self.ggvp.append(self.line_6)

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(970, 250, 640, 10))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fons.append(self.line_2)
        self.ggvp.append(self.line_2)

######## Погода сейчас #################################################################################################

        self.label_now = QtWidgets.QLabel(self.centralwidget)
        self.label_now.setGeometry(QtCore.QRect(970, 23, 200, 60))
        self.label_now.setAlignment(QtCore.Qt.AlignCenter)
        self.label_now.setText("Сейчас")
        self.fons.append(self.label_now)
        self.ggvp.append(self.label_now)

        self.label_weather_now = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_now.setGeometry(QtCore.QRect(975, 105, 200, 80))
        self.label_weather_now.setAlignment(QtCore.Qt.AlignCenter)
        self.fons.append(self.label_weather_now)
        self.ggvp.append(self.label_weather_now)

######## Погода сегодня ################################################################################################

        self.label_todey = QtWidgets.QLabel(self.centralwidget)
        self.label_todey.setGeometry(QtCore.QRect(1190, 23, 390, 60))
        self.label_todey.setAlignment(QtCore.Qt.AlignCenter)
        self.label_todey.setText("Сегодня")
        self.fons.append(self.label_todey)
        self.ggvp.append(self.label_todey)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1190, 70, 411, 81))
        self.ggvp.append(self.horizontalLayoutWidget)
        self.horizontalLayout_today = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_today.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_today.setSpacing(0)

        self.label_today_00 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.fons.append(self.label_today_00)
        self.ggvp.append(self.label_today_00)

        self.label_today_03 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.fons.append(self.label_today_03)
        self.ggvp.append(self.label_today_03)

        self.label_today_06 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.fons.append(self.label_today_06)
        self.ggvp.append(self.label_today_06)

        self.label_today_09 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.fons.append(self.label_today_09)
        self.ggvp.append(self.label_today_09)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(1190, 160, 411, 81))
        self.ggvp.append(self.horizontalLayoutWidget_2)
        self.horizontalLayout_today2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_today2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_today2.setSpacing(0)

        self.label_today_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.fons.append(self.label_today_12)
        self.ggvp.append(self.label_today_12)

        self.label_today_15 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.fons.append(self.label_today_15)
        self.ggvp.append(self.label_today_15)

        self.label_today_18 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.fons.append(self.label_today_18)
        self.ggvp.append(self.label_today_18)

        self.label_today_21 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.fons.append(self.label_today_21)
        self.ggvp.append(self.label_today_21)

######## Погода в следующие дни ########################################################################################

        self.label_tomorrow = QtWidgets.QLabel(self.centralwidget)
        self.label_tomorrow.setGeometry(QtCore.QRect(970, 260, 128, 40))
        self.label_tomorrow.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tomorrow.setText("Завтра")
        self.fons.append(self.label_tomorrow)
        self.ggvp.append(self.label_tomorrow)

        self.label_tomorrow_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_tomorrow_2.setGeometry(QtCore.QRect(1108, 260, 118, 40))
        self.label_tomorrow_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fons.append(self.label_tomorrow_2)
        self.ggvp.append(self.label_tomorrow_2)

        self.label_tomorrow_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_tomorrow_3.setGeometry(QtCore.QRect(1236, 260, 118, 40))
        self.label_tomorrow_3.setAlignment(QtCore.Qt.AlignCenter)
        self.fons.append(self.label_tomorrow_3)
        self.ggvp.append(self.label_tomorrow_3)

        self.label_tomorrow_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_tomorrow_4.setGeometry(QtCore.QRect(1364, 260, 118, 40))
        self.label_tomorrow_4.setAlignment(QtCore.Qt.AlignCenter)
        self.fons.append(self.label_tomorrow_4)
        self.ggvp.append(self.label_tomorrow_4)

        self.label_tomorrow_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_tomorrow_5.setGeometry(QtCore.QRect(1492, 260, 118, 40))
        self.label_tomorrow_5.setAlignment(QtCore.Qt.AlignCenter)
        self.fons.append(self.label_tomorrow_5)
        self.ggvp.append(self.label_tomorrow_5)

        self.label_weather_tomorrow = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_tomorrow.setGeometry(QtCore.QRect(980, 300, 110, 80))
        self.label_weather_tomorrow.setAlignment(QtCore.Qt.AlignCenter)
        self.fons.append(self.label_weather_tomorrow)
        self.ggvp.append(self.label_weather_tomorrow)

        self.label_weather_tomorrow_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_tomorrow_2.setGeometry(QtCore.QRect(1110, 300, 110, 80))
        self.label_weather_tomorrow_2.setAlignment(QtCore.Qt.AlignCenter)
        self.fons.append(self.label_weather_tomorrow_2)
        self.ggvp.append(self.label_weather_tomorrow_2)

        self.label_weather_tomorrow_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_tomorrow_3.setGeometry(QtCore.QRect(1240, 300, 110, 80))
        self.label_weather_tomorrow_3.setAlignment(QtCore.Qt.AlignCenter)
        self.fons.append(self.label_weather_tomorrow_3)
        self.ggvp.append(self.label_weather_tomorrow_3)

        self.label_weather_tomorrow_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_tomorrow_4.setGeometry(QtCore.QRect(1370, 300, 110, 80))
        self.label_weather_tomorrow_4.setAlignment(QtCore.Qt.AlignCenter)
        self.fons.append(self.label_weather_tomorrow_4)
        self.ggvp.append(self.label_weather_tomorrow_4)

        self.label_weather_tomorrow_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_weather_tomorrow_5.setGeometry(QtCore.QRect(1495, 300, 110, 80))
        self.label_weather_tomorrow_5.setAlignment(QtCore.Qt.AlignCenter)
        self.fons.append(self.label_weather_tomorrow_5)
        self.ggvp.append(self.label_weather_tomorrow_5)

######## Добавление стресса и боли #####################################################################################

        self.new_pain = QtWidgets.QPushButton(self.centralwidget)
        self.new_pain.setGeometry(QtCore.QRect(760, 450, 180, 100))
        self.new_pain.setText("Добавить\nплохое\nсамочувствие")
        self.new_pain.clicked.connect(self.addPein)
        self.btns.append(self.new_pain)
        self.ggvp.append(self.new_pain)

        self.new_stress = QtWidgets.QPushButton(self.centralwidget)
        self.new_stress.setGeometry(QtCore.QRect(300, 450, 180, 100))
        self.new_stress.setText("Добавить\nзапланированный\nстресс")
        self.btns.append(self.new_stress)
        self.ggvp.append(self.new_stress)

######## Страница советов ##############################################################################################

        self.sovet_1 = QtWidgets.QLabel(self.centralwidget)
        self.sovet_1.setGeometry(QtCore.QRect(300, 23, 640, 400))
        self.sovet_1.setAlignment(QtCore.Qt.AlignCenter)
        self.sovet_1.setText("PEITE PIVO CHASHE(V LENTE BUD LIGHT\n PO SKIDKE 30 RUB ZA BANKY)")
        self.fons.append(self.sovet_1)
        self.winSovet.append(self.sovet_1)

        self.sovet_2 = QtWidgets.QLabel(self.centralwidget)
        self.sovet_2.setGeometry(QtCore.QRect(970, 23, 640, 400))
        self.sovet_2.setAlignment(QtCore.Qt.AlignCenter)
        self.sovet_2.setText("PO ZAKONU архимеда после сытного обеда\nчтобы жиром не заплыть надо сижку покурить")
        self.fons.append(self.sovet_2)
        self.winSovet.append(self.sovet_2)

######## Страница входа в аккаунт ######################################################################################

        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(820, 325, 180, 40))
        self.label_login.setText("Логин:")
        self.winAkkIN.append(self.label_login)

        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(800, 360, 450, 40))
        self.fons.append(self.login)
        self.winAkkIN.append(self.login)

        self.label_pass = QtWidgets.QLabel(self.centralwidget)
        self.label_pass.setGeometry(QtCore.QRect(820, 400, 180, 40))
        self.label_pass.setText("Пароль:")
        self.winAkkIN.append(self.label_pass)

        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(800, 435, 450, 40))
        self.fons.append(self.password)
        self.winAkkIN.append(self.password)

        self.loginIn = QtWidgets.QPushButton(self.centralwidget)
        self.loginIn.setGeometry(QtCore.QRect(1050, 530, 200, 45))
        self.loginIn.setText("Войти")
        self.loginIn.clicked.connect(self.logon)
        self.btns.append(self.loginIn)
        self.winAkkIN.append(self.loginIn)

        self.new_akk = QtWidgets.QPushButton(self.centralwidget)
        self.new_akk.setGeometry(QtCore.QRect(800, 530, 200, 45))
        self.new_akk.setText("Создать новый аккаунт")
        self.new_akk.clicked.connect(self.createNewAkkountWindow)
        self.btns.append(self.new_akk)
        self.winAkkIN.append(self.new_akk)

        self.label_error1 = QtWidgets.QLabel(self.centralwidget)
        self.label_error1.hide()
        self.label_error1.setGeometry(QtCore.QRect(820, 480, 300, 40))
        self.label_error1.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_error1.setText("* неверный пароль")

        self.label_error2 = QtWidgets.QLabel(self.centralwidget)
        self.label_error2.hide()
        self.label_error2.setGeometry(QtCore.QRect(820, 480, 300, 40))
        self.label_error2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_error2.setText("* такого аккаунта не существует")

######## Страница аккаунта #############################################################################################

        self.photo_in_akk = QtWidgets.QLabel(self.centralwidget)
        self.photo_in_akk.setGeometry(QtCore.QRect(1500, 100, 250, 250))
        self.fons.append(self.photo_in_akk)
        self.winAkk.append(self.photo_in_akk)

        self.nic_in_akk = QtWidgets.QLabel(self.centralwidget)
        self.nic_in_akk.setGeometry(QtCore.QRect(1500, 360, 250, 40))
        self.nic_in_akk.setAlignment(QtCore.Qt.AlignCenter)
        self.winAkk.append(self.nic_in_akk)

        self.label_name_in_akk = QtWidgets.QLabel(self.centralwidget)
        self.label_name_in_akk.setGeometry(QtCore.QRect(320, 110, 180, 40))
        self.label_name_in_akk.setText("Имя:")
        self.winAkk.append(self.label_name_in_akk)

        self.name_in_akk = QtWidgets.QLabel(self.centralwidget)
        self.name_in_akk.setGeometry(QtCore.QRect(520, 110, 180, 40))
        self.winAkk.append(self.name_in_akk)

        self.label_pol_in_akk = QtWidgets.QLabel(self.centralwidget)
        self.label_pol_in_akk.setGeometry(QtCore.QRect(320, 160, 180, 40))
        self.label_pol_in_akk.setText("Пол:")
        self.winAkk.append(self.label_pol_in_akk)

        self.pol_in_akk = QtWidgets.QLabel(self.centralwidget)
        self.pol_in_akk.setGeometry(QtCore.QRect(520, 160, 180, 40))
        self.winAkk.append(self.pol_in_akk)

        self.label_data = QtWidgets.QLabel(self.centralwidget)
        self.label_data.setGeometry(QtCore.QRect(320, 210, 180, 40))
        self.label_data.setText("Дата рождения:")
        self.winAkk.append(self.label_data)

        self.data_in_akk = QtWidgets.QLabel(self.centralwidget)
        self.data_in_akk.setGeometry(QtCore.QRect(520, 210, 180, 40))
        self.winAkk.append(self.data_in_akk)

        self.label_obraz_zizni = QtWidgets.QLabel(self.centralwidget)
        self.label_obraz_zizni.setGeometry(QtCore.QRect(320, 260, 180, 40))
        self.label_obraz_zizni.setText("Образ жизни:")
        self.winAkk.append(self.label_obraz_zizni)

        self.obraz_zizni = QtWidgets.QLabel(self.centralwidget)
        self.obraz_zizni.setGeometry(QtCore.QRect(520, 260, 180, 40))
        self.winAkk.append(self.obraz_zizni)

        self.label_vrednie_privichki = QtWidgets.QLabel(self.centralwidget)
        self.label_vrednie_privichki.setGeometry(QtCore.QRect(320, 310, 180, 40))
        self.label_vrednie_privichki.setText("Вредные привычки:")
        self.winAkk.append(self.label_vrednie_privichki)

        self.vrednie_privichki = QtWidgets.QLabel(self.centralwidget)
        self.vrednie_privichki.setGeometry(QtCore.QRect(520, 310, 180, 40))
        self.winAkk.append(self.vrednie_privichki)

        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(1650, 870, 180, 60))
        self.exit.setText("Выйти из акаунта")
        self.exit.clicked.connect(self.exitAkk)
        self.btns.append(self.exit)
        self.winAkk.append(self.exit)

######## Страница создания аккаунта ####################################################################################

        self.create_label_akk = QtWidgets.QLabel(self.centralwidget)
        self.create_label_akk.setGeometry(QtCore.QRect(400, 23, 450, 40))
        self.create_label_akk.setText("Создание аккаунта")
        self.winAkkCreate.append(self.create_label_akk)

        self.create_label_name = QtWidgets.QLabel(self.centralwidget)
        self.create_label_name.setGeometry(QtCore.QRect(320, 100, 200, 40))
        self.create_label_name.setText("Имя:")
        self.winAkkCreate.append(self.create_label_name)

        self.create_name = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.create_name.setGeometry(QtCore.QRect(540, 100, 450, 40))
        self.fons.append(self.create_name)
        self.winAkkCreate.append(self.create_name)

        self.create_label_login = QtWidgets.QLabel(self.centralwidget)
        self.create_label_login.setGeometry(QtCore.QRect(320, 160, 180, 40))
        self.create_label_login.setText("Логин:")
        self.winAkkCreate.append(self.create_label_login)

        self.create_login = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.create_login.setGeometry(QtCore.QRect(540, 160, 450, 40))
        self.fons.append(self.create_login)
        self.winAkkCreate.append(self.create_login)

        self.create_label_passs = QtWidgets.QLabel(self.centralwidget)
        self.create_label_passs.setGeometry(QtCore.QRect(320, 220, 180, 40))
        self.create_label_passs.setText("Пароль:")
        self.winAkkCreate.append(self.create_label_passs)

        self.create_passs = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.create_passs.setGeometry(QtCore.QRect(540, 220, 450, 40))
        self.fons.append(self.create_passs)
        self.winAkkCreate.append(self.create_passs)

        self.create_label_pol = QtWidgets.QLabel(self.centralwidget)
        self.create_label_pol.setGeometry(QtCore.QRect(320, 280, 180, 40))
        self.create_label_pol.setText("Пол:")
        self.winAkkCreate.append(self.create_label_pol)

        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(550, 280, 440, 40))
        self.winAkkCreate.append(self.horizontalLayoutWidget_3)
        self.horizontalLayout_pol = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_pol.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_pol.setSpacing(0)

        self.pol_jen = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.horizontalLayout_pol.addWidget(self.pol_jen)
        self.pol_jen.setText("Женский")
        self.winAkkCreate.append(self.pol_jen)

        self.pol_men = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.horizontalLayout_pol.addWidget(self.pol_men)
        self.pol_men.setText("Мужской")
        self.winAkkCreate.append(self.pol_men)

        self.create_label_data = QtWidgets.QLabel(self.centralwidget)
        self.create_label_data.setGeometry(QtCore.QRect(320, 340, 180, 40))
        self.create_label_data.setText("Дата рождения:")
        self.winAkkCreate.append(self.create_label_data)

        self.create_data = QtWidgets.QDateEdit(self.centralwidget)
        self.create_data.setGeometry(QtCore.QRect(540, 340, 450, 40))
        self.create_data.setMaximumDate(QtCore.QDate(2023, 1, 1))
        self.create_data.setMinimumDate(QtCore.QDate(1907, 3, 4))
        self.fons.append(self.create_data)
        self.winAkkCreate.append(self.create_data)

        self.create_label_pol = QtWidgets.QLabel(self.centralwidget)
        self.create_label_pol.setGeometry(QtCore.QRect(320, 400, 180, 40))
        self.create_label_pol.setText("Образ жизни:")
        self.winAkkCreate.append(self.create_label_pol)

        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(550, 400, 440, 40))
        self.winAkkCreate.append(self.horizontalLayoutWidget_4)
        self.horizontalLayout_obraz = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_obraz.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_obraz.setSpacing(0)

        self.aktivnoct_1 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.horizontalLayout_obraz.addWidget(self.aktivnoct_1)
        self.aktivnoct_1.setText("Сидячий")
        self.winAkkCreate.append(self.aktivnoct_1)

        self.aktivnoct_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.horizontalLayout_obraz.addWidget(self.aktivnoct_2)
        self.aktivnoct_2.setText("Умеренный")
        self.winAkkCreate.append(self.aktivnoct_2)

        self.aktivnoct_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        self.horizontalLayout_obraz.addWidget(self.aktivnoct_3)
        self.aktivnoct_3.setText("Активный")
        self.winAkkCreate.append(self.aktivnoct_3)

        self.create_label_privichki = QtWidgets.QLabel(self.centralwidget)
        self.create_label_privichki.setGeometry(QtCore.QRect(320, 460, 180, 40))
        self.create_label_privichki.setText("Вредные привычки:")
        self.winAkkCreate.append(self.create_label_privichki)

        self.create_kurenie = QtWidgets.QCheckBox(self.centralwidget)
        self.create_kurenie.setGeometry(QtCore.QRect(550, 460, 450, 40))
        self.create_kurenie.setText("Курение")
        self.winAkkCreate.append(self.create_kurenie)

        self.create_alkogol = QtWidgets.QCheckBox(self.centralwidget)
        self.create_alkogol.setGeometry(QtCore.QRect(550, 500, 450, 40))
        self.create_alkogol.setText("Алкоголь")
        self.winAkkCreate.append(self.create_alkogol)

        self.create_narko = QtWidgets.QCheckBox(self.centralwidget)
        self.create_narko.setGeometry(QtCore.QRect(550, 540, 450, 40))
        self.create_narko.setText("Что-то похуже)")
        self.winAkkCreate.append(self.create_narko)

        self.create_label_photo = QtWidgets.QLabel(self.centralwidget)
        self.create_label_photo.setGeometry(QtCore.QRect(320, 600, 180, 40))
        self.create_label_photo.setText("Фото профиля:")
        self.winAkkCreate.append(self.create_label_photo)

        self.create_new_akk = QtWidgets.QPushButton(self.centralwidget)
        self.create_new_akk.setGeometry(QtCore.QRect(790, 620, 200, 45))
        self.create_new_akk.setText("Создать новый аккаунт")
        self.create_new_akk.clicked.connect(self.createNewAkkount)
        self.btns.append(self.create_new_akk)
        self.winAkkCreate.append(self.create_new_akk)

######## Страница настроек #############################################################################################

        self.label_ask_color = QtWidgets.QLabel(self.centralwidget)
        self.label_ask_color.setGeometry(QtCore.QRect(350, 23, 180, 45))
        self.label_ask_color.setText("Цвета программы:")
        self.winSetting.append(self.label_ask_color)

        self.col1 = QtWidgets.QPushButton(self.centralwidget)
        self.col1.setGeometry(QtCore.QRect(300, 100, 180, 45))
        self.col1.setText("Цвета 1")
        self.col1.clicked.connect(self.BtnChanseColor1)
        self.col1.setStyleSheet("background-color: rgb(173, 175, 219);\nborder: none;")  # база
        self.winSetting.append(self.col1)

        self.col2 = QtWidgets.QPushButton(self.centralwidget)
        self.col2.setGeometry(QtCore.QRect(300, 180, 180, 45))
        self.col2.setText("Цвета 2")
        self.col2.clicked.connect(self.BtnChanseColor2)
        self.col2.setStyleSheet("background-color: rgb(148, 125, 115);\nborder: none;")  # кофе
        self.winSetting.append(self.col2)

        self.col3 = QtWidgets.QPushButton(self.centralwidget)
        self.col3.setGeometry(QtCore.QRect(300, 260, 180, 45))
        self.col3.setText("Цвета 3")
        self.col3.clicked.connect(self.BtnChanseColor3)
        self.col3.setStyleSheet("background-color: rgb(226, 203, 219);\nborder: none;")  # лиловый
        self.winSetting.append(self.col3)

######## Меню добавления плохого самочувствия ##########################################################################

        self.fonAddPein = QtWidgets.QLabel(self.centralwidget)
        self.fonAddPein.setGeometry(QtCore.QRect(970, 23, 910, 950))
        self.fons.append(self.fonAddPein)
        self.winAddpein.append(self.fonAddPein)

        self.label_ask_pein = QtWidgets.QLabel(self.centralwidget)
        self.label_ask_pein.setGeometry(QtCore.QRect(1040, 43, 400, 40))
        self.label_ask_pein.setText("Что вас беспокоит?")
        self.fons.append(self.label_ask_pein)
        self.winAddpein.append(self.label_ask_pein)

        self.check_pein_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_pein_1.setGeometry(QtCore.QRect(1015, 83, 420, 40))
        self.check_pein_1.setText("Усталость")
        self.fons.append(self.check_pein_1)
        self.winAddpein.append(self.check_pein_1)

        self.check_pein_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_pein_2.setGeometry(QtCore.QRect(1015, 123, 420, 40))
        self.check_pein_2.setText("Головная боль")
        self.fons.append(self.check_pein_2)
        self.winAddpein.append(self.check_pein_2)

        self.check_pein_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_pein_3.setGeometry(QtCore.QRect(1015, 163, 420, 40))
        self.check_pein_3.setText("Бессонница")
        self.fons.append(self.check_pein_3)
        self.winAddpein.append(self.check_pein_3)

        self.check_pein_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_pein_4.setGeometry(QtCore.QRect(1015, 203, 420, 40))
        self.check_pein_4.setText("Тошнота")
        self.fons.append(self.check_pein_4)
        self.winAddpein.append(self.check_pein_4)

        self.check_pein_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_pein_5.setGeometry(QtCore.QRect(1015, 243, 420, 40))
        self.check_pein_5.setText("Боль в животе")
        self.fons.append(self.check_pein_5)
        self.winAddpein.append(self.check_pein_5)

        self.check_pein_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.check_pein_6.setGeometry(QtCore.QRect(1015, 283, 420, 40))
        self.check_pein_6.setText("Болезнь или травма")
        self.fons.append(self.check_pein_6)
        self.winAddpein.append(self.check_pein_6)

        self.checkStress = QtWidgets.QCheckBox(self.centralwidget)
        self.checkStress.setGeometry(QtCore.QRect(320, 490, 420, 40))
        self.checkStress.setText("Стресс")
        self.fons.append(self.checkStress)
        self.winAddpein.append(self.checkStress)

        self.checkAlko = QtWidgets.QCheckBox(self.centralwidget)
        self.checkAlko.setGeometry(QtCore.QRect(320, 530, 420, 40))
        self.checkAlko.setText("Употребление алкоголя")
        self.fons.append(self.checkAlko)
        self.winAddpein.append(self.checkAlko)

        self.label_kolvo_sna = QtWidgets.QLabel(self.centralwidget)
        self.label_kolvo_sna.setGeometry(QtCore.QRect(300, 570, 440, 40))
        self.label_kolvo_sna.setText("Количество сна:")
        self.fons.append(self.label_kolvo_sna)
        self.winAddpein.append(self.label_kolvo_sna)

        self.horizontalSlider_son = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_son.setGeometry(QtCore.QRect(313, 610, 385, 20))
        self.horizontalSlider_son.setOrientation(QtCore.Qt.Horizontal)
        self.winAddpein.append(self.horizontalSlider_son)

        self.label_son = QtWidgets.QLabel(self.centralwidget)
        self.label_son.setGeometry(QtCore.QRect(315, 630, 420, 30))
        self.label_son.setText("0    1    2    3    4    5    6    7    8    9    10    11    12+")
        self.fons.append(self.label_son)
        self.winAddpein.append(self.label_son)

        self.add_new_pein = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_pein.setGeometry(QtCore.QRect(1650, 870, 180, 60))
        self.add_new_pein.setText("Добавить")
        self.add_new_pein.clicked.connect(self.addaddPein)
        self.btns.append(self.add_new_pein)
        self.winAddpein.append(self.add_new_pein)

########################################################################################################################

    # Форматирование
        self.mySetFont()

    # Запрос прогноза погоды
        self.weather()

    # Установка цветов
        self.setcolors(self.color1, self.color2, self.color3, self.color4)
        self.base.setStyleSheet("border: none;")
        self.setting.setStyleSheet("background-color:" + self.color3)

    # Скрытие ненужных окон
        self.hideSovets()
        self.hideProfile()
        self.hideSetting()
        self.hideAddPein()

    def addPein(self):
        self.new_pain.hide()
        for i in self.winAddpein:
            i.show()

    def addaddPein(self):
        for i in self.winAddpein:
            i.hide()
        self.new_pain.show()

    def hideAddPein(self):
        for i in self.winAddpein:
            i.hide()

    def baseWindow(self):
        self.base.setStyleSheet("border: none;")
        self.base.setGeometry(QtCore.QRect(40, 370, 211, 45))

        self.sovets.setStyleSheet("background-color:" + self.color3)
        self.sovets.setGeometry(QtCore.QRect(25, 430, 180, 45))
        self.profile.setStyleSheet("background-color:" + self.color3)
        self.profile.setGeometry(QtCore.QRect(25, 490, 180, 45))
        self.setting.setStyleSheet("background-color:" + self.color3)
        self.setting.setGeometry(QtCore.QRect(25, 550, 180, 45))

        self.hideSovets()
        self.hideProfile()
        self.hideSetting()

        for i in self.ggvp:
            i.show()

    def sovetsWindow(self):
        self.sovets.setStyleSheet("border: none;")
        self.sovets.setGeometry(QtCore.QRect(40, 430, 211, 45))

        self.base.setStyleSheet("background-color:" + self.color3)
        self.base.setGeometry(QtCore.QRect(25, 370, 180, 45))
        self.profile.setStyleSheet("background-color:" + self.color3)
        self.profile.setGeometry(QtCore.QRect(25, 490, 180, 45))
        self.setting.setStyleSheet("background-color:" + self.color3)
        self.setting.setGeometry(QtCore.QRect(25, 550, 180, 45))

        self.hideBase()
        self.hideProfile()
        self.hideSetting()

        for i in self.winSovet:
            i.show()

    def profileWindow(self):
        self.profile.setStyleSheet("border: none;")
        self.profile.setGeometry(QtCore.QRect(40, 490, 211, 45))

        self.base.setStyleSheet("background-color:" + self.color3)
        self.base.setGeometry(QtCore.QRect(25, 370, 180, 45))
        self.sovets.setStyleSheet("background-color:" + self.color3)
        self.sovets.setGeometry(QtCore.QRect(25, 430, 180, 45))
        self.setting.setStyleSheet("background-color:" + self.color3)
        self.setting.setGeometry(QtCore.QRect(25, 550, 180, 45))

        self.hideBase()
        self.hideSovets()
        self.hideSetting()

        if self.nalichieakkaunta:
            self.postroenieAkkaunta()
        else:
            for i in self.winAkkIN:
                i.show()

    def settingWindow(self):
        self.setting.setStyleSheet("border: none;")
        self.setting.setGeometry(QtCore.QRect(40, 550, 211, 45))

        self.base.setStyleSheet("background-color:" + self.color3)
        self.base.setGeometry(QtCore.QRect(25, 370, 180, 45))
        self.sovets.setStyleSheet("background-color:" + self.color3)
        self.sovets.setGeometry(QtCore.QRect(25, 430, 180, 45))
        self.profile.setStyleSheet("background-color:" + self.color3)
        self.profile.setGeometry(QtCore.QRect(25, 490, 180, 45))

        self.hideBase()
        self.hideSovets()
        self.hideProfile()

        for i in self.winSetting:
            i.show()

    def postroenieAkkaunta(self):
        with open('files/profils/' + self.log + '.txt', 'r') as f:
            p = f.readline().rstrip()
            if p == self.pas:
                self.label_error1.hide()
                for i in self.winAkk:
                    i.show()
                self.nic_in_akk.setText(self.log)
                self.name_in_akk.setText(f.readline().rstrip())
                self.pol_in_akk.setText(f.readline().rstrip())
                self.data_in_akk.setText(f.readline().rstrip())
                self.obraz_zizni.setText(f.readline().rstrip())
                self.vrednie_privichki.setText(f.readline().rstrip())
                self.nalichieakkaunta = True
                with open('files/akk.txt', 'w') as f:
                    f.write('1\n')
                    f.write(self.log + '\n')
                    f.write(self.pas + '\n')
                for i in self.winAkkIN:
                    i.hide()

            else:
                self.label_error1.show()

    def logon(self):
        with open('files/list_akk.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if line.rstrip() == self.login.text():
                    self.label_error2.hide()
                    self.log = self.login.text()
                    self.pas = self.password.text()
                    self.postroenieAkkaunta()
                    break
                else:
                    self.label_error2.show()

    def createNewAkkount(self):
        login = self.create_login.toPlainText()
        pasword = self.create_passs.toPlainText()
        if login.isalnum() and pasword.isalnum():
            with open('files/profils/' + login + '.txt', 'w') as f:
                f.write(pasword + '\n')
                f.write(self.create_name.toPlainText() + '\n')
                if self.pol_jen.isChecked():
                    f.write("жен" + '\n')
                else:
                    f.write("муж" + '\n')
                f.write(format(self.create_data.dateTime().toString('dd-MM-yyyy')) + '\n')
                if self.aktivnoct_1.isChecked():
                    f.write("Сидячий" + '\n')
                else:
                    if self.aktivnoct_2.isChecked():
                        f.write("Умеренный" + '\n')
                    else:
                        f.write("Активный" + '\n')
                if self.create_kurenie.isChecked():
                    f.write("Курение" + '\n')
                if self.create_alkogol.isChecked():
                    f.write("Алкоголь" + '\n')
                if self.create_narko.isChecked():
                    f.write("Что-то похуже)" + '\n')

            self.nalichieakkaunta = True
            self.log = login
            self.pas = pasword
            for i in self.winAkkCreate:
                i.hide()
            with open('files/list_akk.txt', 'a') as f:
                f.write('\n' + self.log)
            with open('files/akk.txt', 'w') as f:
                f.write('1\n')
                f.write(self.log + '\n')
                f.write(self.pas + '\n')
            self.postroenieAkkaunta()
        # self.create_label_photo = QtWidgets.QLabel(self.centralwidget)

    def createNewAkkountWindow(self):
        for i in self.winAkkIN:
            i.hide()
        for i in self.winAkkCreate:
            i.show()

    def exitAkk(self):
        self.nalichieakkaunta = False
        with open('files/akk.txt', 'w') as f:
            f.write('0')
        for i in self.winAkkIN:
            i.show()
        for i in self.winAkk:
            i.hide()
        self.create_login.clear()
        self.create_passs.clear()

    def hideBase(self):
        for i in self.ggvp:
            i.hide()

    def hideSovets(self):
        for i in self.winSovet:
            i.hide()

    def hideProfile(self):
        for i in self.winAkk:
            i.hide()
        for i in self.winAkkIN:
            i.hide()
        for i in self.winAkkCreate:
            i.hide()

    def hideSetting(self):
        for i in self.winSetting:
            i.hide()

    def setcolors(self, color_1, color_2, color_3, color_4):
        self.color1 = color_1
        self.color2 = color_2
        self.color3 = color_3
        self.color4 = color_4

        for i in self.fons:
            i.setStyleSheet("background-color:" + color_2)
        for i in self.btns:
            i.setStyleSheet("background-color:" + color_3)

        self.setting.setStyleSheet("border: none;")
        self.calendar.setStyleSheet("background-color:" + color_2 + "\ngridline-color:" + color_1)
        self.setStyleSheet("background-color:" + color_1)
        self.fon_menu.setStyleSheet(color_4)
        self.sovet_1.setStyleSheet("background-color:" + color_2 + "\npadding :10px")
        self.sovet_2.setStyleSheet("background-color:" + color_2 + "\npadding :10px")

        with open('files/color.txt', 'w') as f:
            f.write(color_1 + color_2 + color_3 + color_4)

    def BtnChanseColor1(self):
        self.setcolors("rgb(238, 212, 189);\n", "rgb(219, 173, 175);\n", "rgb(173, 175, 219); border: none;\n",
                       "background-color: rgb(205, 185, 172);")

    def BtnChanseColor2(self):
        self.setcolors("rgb(233, 213, 202);\n", "rgb(193, 164, 149);\n", "rgb(148, 125, 115); border: none;\n",
                       "background-color: rgb(116, 97, 89);")

    def BtnChanseColor3(self):
        self.setcolors("rgb(232, 226, 240);\n", "rgb(211, 209, 228);\n", "rgb(226, 203, 219); border: none;\n",
                       "background-color: rgb(171, 171, 203);")

    def mySetFont(self):
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)

        for i in self.ggvp:
            i.setFont(font)
        for i in self.leftMenu:
            i.setFont(font)
        for i in self.winAddpein:
            i.setFont(font)
        for i in self.winAkkIN:
            i.setFont(font)
        for i in self.winAkk:
            i.setFont(font)
        for i in self.winAkkCreate:
            i.setFont(font)
        for i in self.winSovet:
            i.setFont(font)
        for i in self.winSetting:
            i.setFont(font)

        self.setFont(font)
        self.label_weather_now.setFont(QtGui.QFont("Segoe UI", 15))
        self.create_label_akk.setFont(QtGui.QFont("Segoe UI", 15))
        self.label_ask_color.setFont(QtGui.QFont("Segoe UI", 15))

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
                if int(i['dt_txt'][8:10]) == int(segodna) + 1:
                    weath_tomm += i['main']['temp']
                if int(i['dt_txt'][8:10]) == int(segodna) + 2:
                    weath_tomm2 += i['main']['temp']
                if int(i['dt_txt'][8:10]) == int(segodna) + 3:
                    weath_tomm3 += i['main']['temp']
                if int(i['dt_txt'][8:10]) == int(segodna) + 4:
                    weath_tomm4 += i['main']['temp']
                if int(i['dt_txt'][8:10]) == int(segodna) + 5:
                    weath_tomm5 += i['main']['temp']
                    co += 1

            weath_tomm5 /= co

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
        self.label_weather_tomorrow.setText(str(round(weath_tomm / 8)))
        self.label_weather_tomorrow_2.setText(str(round(weath_tomm2 / 8)))
        self.label_weather_tomorrow_3.setText(str(round(weath_tomm3 / 8)))
        self.label_weather_tomorrow_4.setText(str(round(weath_tomm4 / 8)))
        self.label_weather_tomorrow_5.setText(str(round(weath_tomm5)))
