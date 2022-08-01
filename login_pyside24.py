from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from custom_qstacked_widgets import *
import sources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1590, 1000)
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/Jhonatan Deni/.designer/Jhonatan Deni/.designer/backup/src/home.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon1)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	\n"
"	\n"
"	background-color:rgb(196, 196, 196);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        MainWindow.setIconSize(QSize(120, 120))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setDockNestingEnabled(False)
        self.actionSalvar_automaticamente = QAction(MainWindow)
        self.actionSalvar_automaticamente.setObjectName(u"actionSalvar_automaticamente")
        self.actionSalvar_automaticamente.setCheckable(True)
        self.actionAtualizar_automaticamente = QAction(MainWindow)
        self.actionAtualizar_automaticamente.setObjectName(u"actionAtualizar_automaticamente")
        self.actionAtualizar_automaticamente.setCheckable(True)
        self.actionAbrir_DB = QAction(MainWindow)
        self.actionAbrir_DB.setObjectName(u"actionAbrir_DB")
        self.actionSalvar_Relatorio = QAction(MainWindow)
        self.actionSalvar_Relatorio.setObjectName(u"actionSalvar_Relatorio")
        self.actionAbrir_xlsx = QAction(MainWindow)
        self.actionAbrir_xlsx.setObjectName(u"actionAbrir_xlsx")
        self.actionImportar_xlsx = QAction(MainWindow)
        self.actionImportar_xlsx.setObjectName(u"actionImportar_xlsx")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	\n"
"	\n"
"	background-color:rgb(196, 196, 196);\n"
"	border-radius: 10px;\n"
"	font: 25 14pt \"Bahnschrift Light Condensed\";\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(39, 37, 36);")
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"background-color: qradialgradient(spread:pad, cx:0.49, cy:0.502304, radius:0.687, fx:0.489, fy:0.51, stop:0 rgba(0, 28, 206, 243), stop:0.985843 rgba(0, 0, 0, 255));\n"
"background-position: center;\n"
"background-repeat:no-repeat;\n"
"border: 0px;\n"
"")
        self.verticalLayout = QVBoxLayout(self.login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.conteudo = QFrame(self.login)
        self.conteudo.setObjectName(u"conteudo")
        self.conteudo.setStyleSheet(u"background-image: url();\n"
"background-color: rgba(255, 255, 255, 0); \n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"")
        self.conteudo.setFrameShape(QFrame.NoFrame)
        self.conteudo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.conteudo)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.login_area = QFrame(self.conteudo)
        self.login_area.setObjectName(u"login_area")
        self.login_area.setMinimumSize(QSize(0, 0))
        self.login_area.setMaximumSize(QSize(600, 673))
        self.login_area.setCursor(QCursor(Qt.ArrowCursor))
        self.login_area.setLayoutDirection(Qt.LeftToRight)
        self.login_area.setAutoFillBackground(False)
        self.login_area.setStyleSheet(u"border-image: url(:/login/login-src/5.jpg);\n"
"\n"
"\n"
"border-radius:13px;\n"
"background-position: center;\n"
"background-repeat:no-repeat;\n"
"\n"
"\n"
"")
        self.login_area.setFrameShape(QFrame.StyledPanel)
        self.login_area.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.login_area)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(80, -1, 80, -1)
        self.logo = QFrame(self.login_area)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(16777215, 16777215))
        self.logo.setLayoutDirection(Qt.LeftToRight)
        self.logo.setStyleSheet(u"background-image: url(:/menu/pngwing.com.png);\n"
"background-position: center;\n"
"background-color: rgba(255, 255, 255, 0); \n"
"border-image:url();\n"
"background-repeat:no-repeat;\n"
"")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Raised)
        self.top_spam = QFrame(self.logo)
        self.top_spam.setObjectName(u"top_spam")
        self.top_spam.setGeometry(QRect(-10, 0, 450, 30))
        self.top_spam.setMinimumSize(QSize(450, 20))
        self.top_spam.setMaximumSize(QSize(16777215, 30))
        self.top_spam.setStyleSheet(u"background-image: url();\n"
"background-color: rgba(255, 255, 255, 0); \n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"\n"
"background-image: url();")
        self.top_spam.setFrameShape(QFrame.NoFrame)
        self.top_spam.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.top_spam)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 5, 0, 0)
        self.pop_error = QFrame(self.top_spam)
        self.pop_error.setObjectName(u"pop_error")
        self.pop_error.setMaximumSize(QSize(16777215, 16777215))
        self.pop_error.setStyleSheet(u"border-radius: 5px;\n"
"background-color: rgb(180, 0, 0);")
        self.pop_error.setFrameShape(QFrame.StyledPanel)
        self.pop_error.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.pop_error)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 3, 10, 3)
        self.texto_error = QLabel(self.pop_error)
        self.texto_error.setObjectName(u"texto_error")
        font = QFont()
        font.setFamily(u"Bahnschrift Light Condensed")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.texto_error.setFont(font)
        self.texto_error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.texto_error)

        self.pushButton_7 = QPushButton(self.pop_error)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 21))
        self.pushButton_7.setMaximumSize(QSize(28, 35))
        self.pushButton_7.setStyleSheet(u"QPushButton {\n"
"	border-radius: 5px;\n"
"	border-image: url(:/menu/close.png);\n"
"	background-position: center;\n"
"	border : 2px solid rgb(0, 0, 0)\n"
"\n"
"	\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(50, 50, 50);\n"
"	color:rgb(202, 202, 202);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(34, 34, 34);\n"
"	color:rgb(202, 202, 202);\n"
"	border: 2px solid rgb(55,55,55)\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_7)


        self.horizontalLayout_7.addWidget(self.pop_error)


        self.verticalLayout_4.addWidget(self.logo)

        self.frame_3 = QFrame(self.login_area)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 48))
        self.frame_3.setStyleSheet(u"background-image: url();\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"border-radius:10px;\n"
"border-image:url();")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, -1, -1, -1)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(35, 0))
        self.frame_5.setMaximumSize(QSize(60, 16777215))
        self.frame_5.setStyleSheet(u"background-image: url(:/login/user.png);\n"
"border-image:url();\n"
"background-color: rgba(255, 255, 255, 0); \n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.enter_user = QLineEdit(self.frame_4)
        self.enter_user.setObjectName(u"enter_user")
        self.enter_user.setMinimumSize(QSize(0, 0))
        self.enter_user.setMaximumSize(QSize(16777215, 16777215))
        self.enter_user.setFont(font)
        self.enter_user.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0); \n"
"\n"
"border-radius:0px;\n"
"\n"
"\n"
"")
        self.enter_user.setMaxLength(35)

        self.verticalLayout_5.addWidget(self.enter_user)


        self.horizontalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.login_area)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 48))
        self.frame_6.setStyleSheet(u"background-image: url();\n"
"border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"border-image:url();")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(35, 0))
        self.frame_7.setMaximumSize(QSize(60, 16777215))
        self.frame_7.setStyleSheet(u"background-image: url(:/login/password.png);\n"
"background-color: rgba(255, 255, 255, 0); \n"
"")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.enter_pass = QLineEdit(self.frame_8)
        self.enter_pass.setObjectName(u"enter_pass")
        self.enter_pass.setMinimumSize(QSize(0, 0))
        self.enter_pass.setMaximumSize(QSize(16777215, 16777215))
        self.enter_pass.setFont(font)
        self.enter_pass.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgba(255, 255, 255, 0); \n"
"\n"
"border-radius:0px;\n"
"\n"
"\n"
"")
        self.enter_pass.setMaxLength(32767)
        self.enter_pass.setFrame(True)
        self.enter_pass.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.enter_pass)


        self.horizontalLayout_5.addWidget(self.frame_8)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.checkBox = QCheckBox(self.login_area)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet(u"border-image:url();\n"
"color: rgb(255, 255, 255);\n"
"background-image: url();\n"
"background-color: rgba(255, 255, 255, 0); \n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.checkBox)

        self.buton_login = QPushButton(self.login_area)
        self.buton_login.setObjectName(u"buton_login")
        self.buton_login.setMinimumSize(QSize(100, 60))
        self.buton_login.setMaximumSize(QSize(16777215, 16777215))
        self.buton_login.setFont(font)
        self.buton_login.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-image: url();\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"	border: 0px solid  rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	border-image:url();\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
" 	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(110, 72, 135, 255), stop:0.429961 rgba(100, 107, 132, 235), stop:1 rgba(162, 135, 165, 255));\n"
"	border: 0px solid rgb(55, 55, 55);\n"
"	\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
" 	\n"
"	\n"
"	background-color: rgb(91, 91, 91);\n"
"	border: 0px solid rgb(55, 55, 55);\n"
"	\n"
"}")

        self.verticalLayout_4.addWidget(self.buton_login)


        self.horizontalLayout_3.addWidget(self.login_area)


        self.verticalLayout.addWidget(self.conteudo)

        self.stackedWidget.addWidget(self.login)
        self.inicio = QWidget()
        self.inicio.setObjectName(u"inicio")
        self.inicio.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.inicio)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 6)
        self.bar_window = QFrame(self.inicio)
        self.bar_window.setObjectName(u"bar_window")
        self.bar_window.setMinimumSize(QSize(0, 26))
        self.bar_window.setStyleSheet(u"background-color: rgb(39, 37, 36);")
        self.bar_window.setFrameShape(QFrame.NoFrame)
        self.bar_window.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bar_window)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.credits = QLabel(self.bar_window)
        self.credits.setObjectName(u"credits")
        self.credits.setMinimumSize(QSize(120, 0))
        self.credits.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")

        self.horizontalLayout_2.addWidget(self.credits)

        self.horizontalSpacer_5 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.minimize = QPushButton(self.bar_window)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(40, 20))
        self.minimize.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-repeat:no-repeat;\n"
"	background-image: url(:/login/minimize.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"	background-position: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-image: url(:/login/minimize clik.png);\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.minimize)

        self.maxmize = QPushButton(self.bar_window)
        self.maxmize.setObjectName(u"maxmize")
        self.maxmize.setMinimumSize(QSize(40, 20))
        self.maxmize.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-repeat:no-repeat;\n"
"	background-image: url(:/login/max 1.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"	background-position: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-image: url(:/login/max_ click.png);\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.maxmize)

        self.exit = QPushButton(self.bar_window)
        self.exit.setObjectName(u"exit")
        self.exit.setMinimumSize(QSize(40, 20))
        self.exit.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-repeat:no-repeat;\n"
"	background-image: url(:/login/close.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"	background-position: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-image: url(:/login/close clik.png);\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.exit)


        self.verticalLayout_7.addWidget(self.bar_window)

        self.group = QFrame(self.inicio)
        self.group.setObjectName(u"group")
        self.group.setMinimumSize(QSize(0, 0))
        self.group.setStyleSheet(u"")
        self.group.setFrameShape(QFrame.StyledPanel)
        self.group.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.group)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, 0, 0, 0)
        self.menu = QFrame(self.group)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(80, 0))
        self.menu.setMaximumSize(QSize(80, 16777215))
        self.menu.setStyleSheet(u"background-color: rgb(49, 72, 106);\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"\n"
"")
        self.menu.setFrameShape(QFrame.NoFrame)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.menu)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.mainlogo = QFrame(self.menu)
        self.mainlogo.setObjectName(u"mainlogo")
        self.mainlogo.setMinimumSize(QSize(0, 60))
        self.mainlogo.setMaximumSize(QSize(16777215, 90))
        self.mainlogo.setStyleSheet(u"background-color: rgba(0, 0, 0, 70);\n"
"border-top-right-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-bottom-left-radius:0px;")
        self.mainlogo.setFrameShape(QFrame.StyledPanel)
        self.mainlogo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.mainlogo)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.icon_log = QFrame(self.mainlogo)
        self.icon_log.setObjectName(u"icon_log")
        self.icon_log.setMaximumSize(QSize(60, 60))
        self.icon_log.setStyleSheet(u"border-image: url(:/menu/pngwing.com.png);\n"
"background-color: rgba(0, 0, 0, 0); ")
        self.icon_log.setFrameShape(QFrame.StyledPanel)
        self.icon_log.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_14.addWidget(self.icon_log)


        self.verticalLayout_26.addWidget(self.mainlogo)

        self.categorias = QFrame(self.menu)
        self.categorias.setObjectName(u"categorias")
        self.categorias.setStyleSheet(u"background-color: rgba(0, 0, 0, 70);\n"
"border-top-left-radius:0px;\n"
"")
        self.categorias.setFrameShape(QFrame.StyledPanel)
        self.categorias.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.categorias)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.scrolbar = QFrame(self.categorias)
        self.scrolbar.setObjectName(u"scrolbar")
        self.scrolbar.setMinimumSize(QSize(5, 0))
        self.scrolbar.setMaximumSize(QSize(5, 16777215))
        self.scrolbar.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.scrolbar.setFrameShape(QFrame.StyledPanel)
        self.scrolbar.setFrameShadow(QFrame.Raised)
        self.animcurretnpage = QFrame(self.scrolbar)
        self.animcurretnpage.setObjectName(u"animcurretnpage")
        self.animcurretnpage.setGeometry(QRect(0, 1, 4, 60))
        self.animcurretnpage.setMinimumSize(QSize(0, 0))
        self.animcurretnpage.setMaximumSize(QSize(4, 60))
        self.animcurretnpage.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.animcurretnpage.setFrameShape(QFrame.HLine)
        self.animcurretnpage.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_28.addWidget(self.scrolbar)

        self.topmenu = QFrame(self.categorias)
        self.topmenu.setObjectName(u"topmenu")
        self.topmenu.setMinimumSize(QSize(0, 0))
        self.topmenu.setMaximumSize(QSize(16777215, 16777215))
        self.topmenu.setSizeIncrement(QSize(0, 20))
        self.topmenu.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.topmenu.setFrameShape(QFrame.StyledPanel)
        self.topmenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.topmenu)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.topmenu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/menu/menu/togle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.pushButton)

        self.pushButton_8 = QPushButton(self.topmenu)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(0, 0))
        self.pushButton_8.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_8.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_8.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/menu/menu/payout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.topmenu)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 0))
        self.pushButton_9.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/menu/menu/invest.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon4)
        self.pushButton_9.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.topmenu)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 0))
        self.pushButton_10.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/menu/menu/cards.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon5)
        self.pushButton_10.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.topmenu)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(0, 0))
        self.pushButton_11.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/menu/menu/transfer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon6)
        self.pushButton_11.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.pushButton_11)

        self.pushButton_15 = QPushButton(self.topmenu)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(0, 0))
        self.pushButton_15.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/menu/menu/food.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon7)
        self.pushButton_15.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.pushButton_15)

        self.pushButton_16 = QPushButton(self.topmenu)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(0, 0))
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/menu/menu/config.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon8)
        self.pushButton_16.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.pushButton_16)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_2)

        self.salvar_6 = QPushButton(self.topmenu)
        self.salvar_6.setObjectName(u"salvar_6")
        self.salvar_6.setMinimumSize(QSize(0, 0))
        self.salvar_6.setMaximumSize(QSize(16777215, 16777215))
        self.salvar_6.setFont(font)
        self.salvar_6.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/menu/menu/db.png", QSize(), QIcon.Normal, QIcon.Off)
        self.salvar_6.setIcon(icon9)
        self.salvar_6.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.salvar_6)

        self.salvar_5 = QPushButton(self.topmenu)
        self.salvar_5.setObjectName(u"salvar_5")
        self.salvar_5.setMinimumSize(QSize(0, 0))
        self.salvar_5.setMaximumSize(QSize(16777215, 16777215))
        self.salvar_5.setFont(font)
        self.salvar_5.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/login/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.salvar_5.setIcon(icon10)
        self.salvar_5.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.salvar_5)

        self.salvar_4 = QPushButton(self.topmenu)
        self.salvar_4.setObjectName(u"salvar_4")
        self.salvar_4.setMinimumSize(QSize(0, 0))
        self.salvar_4.setMaximumSize(QSize(16777215, 16777215))
        self.salvar_4.setFont(font)
        self.salvar_4.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/menu/menu/powerof.png", QSize(), QIcon.Normal, QIcon.Off)
        self.salvar_4.setIcon(icon11)
        self.salvar_4.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.salvar_4)

        self.pushButton_18 = QPushButton(self.topmenu)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(0, 0))
        self.pushButton_18.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"	border-radius:0px;\n"
"\n"
"	padding:15px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/menu/menu/notiy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon12)
        self.pushButton_18.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.pushButton_18)


        self.horizontalLayout_28.addWidget(self.topmenu)


        self.verticalLayout_26.addWidget(self.categorias)


        self.horizontalLayout_6.addWidget(self.menu)

        self.stackedWidget_2 = QStackedWidget(self.group)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"background-color:rgb(25, 37, 55);\n"
"border-radius: 10px;")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_2 = QVBoxLayout(self.page_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget_2.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"")
        self.verticalLayout_38 = QVBoxLayout(self.page_3)
        self.verticalLayout_38.setSpacing(30)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.backgroud_cartao = QFrame(self.page_3)
        self.backgroud_cartao.setObjectName(u"backgroud_cartao")
        self.backgroud_cartao.setStyleSheet(u"\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:0px;")
        self.backgroud_cartao.setFrameShape(QFrame.StyledPanel)
        self.backgroud_cartao.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.backgroud_cartao)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.pop_error_cartao = QFrame(self.backgroud_cartao)
        self.pop_error_cartao.setObjectName(u"pop_error_cartao")
        self.pop_error_cartao.setFrameShape(QFrame.StyledPanel)
        self.pop_error_cartao.setFrameShadow(QFrame.Raised)

        self.verticalLayout_39.addWidget(self.pop_error_cartao)

        self.cartao_options = QFrame(self.backgroud_cartao)
        self.cartao_options.setObjectName(u"cartao_options")
        self.cartao_options.setMinimumSize(QSize(0, 70))
        self.cartao_options.setMaximumSize(QSize(16777215, 16777215))
        self.cartao_options.setStyleSheet(u"background-color:rgb(42, 62, 93);\n"
"border-radius:none;")
        self.cartao_options.setFrameShape(QFrame.StyledPanel)
        self.cartao_options.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.cartao_options)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.grid = QPushButton(self.cartao_options)
        self.grid.setObjectName(u"grid")
        self.grid.setMinimumSize(QSize(216, 50))
        self.grid.setMaximumSize(QSize(0, 16777215))
        self.grid.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"	border-radius: 10px;\n"
"\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/backgroud/src-page-cartoes/cards.png", QSize(), QIcon.Normal, QIcon.Off)
        self.grid.setIcon(icon13)
        self.grid.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.grid)

        self.grid_2 = QPushButton(self.cartao_options)
        self.grid_2.setObjectName(u"grid_2")
        self.grid_2.setMinimumSize(QSize(216, 50))
        self.grid_2.setMaximumSize(QSize(0, 16777215))
        self.grid_2.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius: 10px;\n"
"\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/backgroud/src-page-cartoes/card_config.png", QSize(), QIcon.Normal, QIcon.Off)
        self.grid_2.setIcon(icon14)
        self.grid_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.grid_2)

        self.horizontalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout_39.addWidget(self.cartao_options)

        self.stackedWidget_3 = QStackedWidget(self.backgroud_cartao)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMinimumSize(QSize(0, 0))
        self.stackedWidget_3.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.page)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM "
                        "- SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
""
                        "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.scrollArea.setFrameShadow(QFrame.Raised)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1486, 870))
        self.scrollAreaWidgetContents_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.horizontalLayout_15 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_15.setSpacing(30)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.content_cartao = QFrame(self.scrollAreaWidgetContents_2)
        self.content_cartao.setObjectName(u"content_cartao")
        self.content_cartao.setMinimumSize(QSize(0, 0))
        self.content_cartao.setMaximumSize(QSize(440, 16777215))
        self.content_cartao.setFrameShape(QFrame.StyledPanel)
        self.content_cartao.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.content_cartao)
        self.verticalLayout_41.setSpacing(30)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.content_cartao)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setMinimumSize(QSize(0, 0))
        self.scrollArea_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 440, 870))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_41.addWidget(self.scrollArea_4)


        self.horizontalLayout_15.addWidget(self.content_cartao)

        self.detalhes_cartao = QStackedWidget(self.scrollAreaWidgetContents_2)
        self.detalhes_cartao.setObjectName(u"detalhes_cartao")
        self.detalhes_cartao.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 0); \n"
"	border-radius: 10px;\n"
"\n"
"\n"
"}")
        self.detalhes_cartao.setFrameShape(QFrame.StyledPanel)
        self.detalhes_cartao.setFrameShadow(QFrame.Raised)
        self.detalhes_cartaoPage1 = QWidget()
        self.detalhes_cartaoPage1.setObjectName(u"detalhes_cartaoPage1")
        self.verticalLayout_40 = QVBoxLayout(self.detalhes_cartaoPage1)
        self.verticalLayout_40.setSpacing(30)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 10, 0, 0)
        self.CONTAINER_geral = QFrame(self.detalhes_cartaoPage1)
        self.CONTAINER_geral.setObjectName(u"CONTAINER_geral")
        self.CONTAINER_geral.setMinimumSize(QSize(0, 0))
        self.CONTAINER_geral.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(49, 72, 106);\n"
"	border-radius: 10px;\n"
"	border-bottom: 0px solid rgb(45, 45, 68);\n"
"	border-right: 0px solid rgb(45, 45, 68);\n"
"\n"
"}")
        self.CONTAINER_geral.setFrameShape(QFrame.NoFrame)
        self.CONTAINER_geral.setFrameShadow(QFrame.Plain)
        self.CONTAINER_geral.setLineWidth(90)
        self.horizontalLayout_26 = QHBoxLayout(self.CONTAINER_geral)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.CONTAINER_geral)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setMinimumSize(QSize(0, 0))
        self.frame_29.setToolTipDuration(0)
        self.frame_29.setAutoFillBackground(False)
        self.frame_29.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"border-radius:0px;\n"
"border:none;\n"
"")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_29)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(30, -1, 30, -1)
        self.frame_12 = QFrame(self.frame_29)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(200, 200))
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.circularProgressBarBase_2 = QFrame(self.frame_12)
        self.circularProgressBarBase_2.setObjectName(u"circularProgressBarBase_2")
        self.circularProgressBarBase_2.setMinimumSize(QSize(200, 200))
        self.circularProgressBarBase_2.setMaximumSize(QSize(200, 200))
        self.circularProgressBarBase_2.setStyleSheet(u"border:none;\n"
"border-image:none;\n"
"background-color: rgba(255, 255, 255, 0); \n"
"")
        self.circularProgressBarBase_2.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase_2.setFrameShadow(QFrame.Raised)
        self.circularProgress_2 = QFrame(self.circularProgressBarBase_2)
        self.circularProgress_2.setObjectName(u"circularProgress_2")
        self.circularProgress_2.setGeometry(QRect(10, 10, 175, 175))
        self.circularProgress_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 85px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgress_2.setFrameShape(QFrame.NoFrame)
        self.circularProgress_2.setFrameShadow(QFrame.Raised)
        self.circularBg_2 = QFrame(self.circularProgressBarBase_2)
        self.circularBg_2.setObjectName(u"circularBg_2")
        self.circularBg_2.setGeometry(QRect(10, 9, 175, 175))
        self.circularBg_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 85px;\n"
"	background-image:none;\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.00214133 rgba(160, 160, 160, 255), stop:0.33833 rgba(54, 56, 121, 125), stop:0.66167 rgba(80, 58, 161, 27), stop:1 rgba(255, 255, 255, 192));\n"
"}")
        self.circularBg_2.setFrameShape(QFrame.NoFrame)
        self.circularBg_2.setFrameShadow(QFrame.Raised)
        self.container_2 = QFrame(self.circularBg_2)
        self.container_2.setObjectName(u"container_2")
        self.container_2.setGeometry(QRect(10, 10, 155, 155))
        self.container_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 75px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container_2.setFrameShape(QFrame.NoFrame)
        self.container_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.container_2)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 30, 111, 101))
        self.gridLayout_2 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelCredits_2 = QLabel(self.layoutWidget_3)
        self.labelCredits_2.setObjectName(u"labelCredits_2")
        self.labelCredits_2.setFont(font)
        self.labelCredits_2.setStyleSheet(u"\n"
"color: rgb(155, 155, 255);")
        self.labelCredits_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelCredits_2, 2, 0, 1, 1)

        self.labelTitle_2 = QLabel(self.layoutWidget_3)
        self.labelTitle_2.setObjectName(u"labelTitle_2")
        self.labelTitle_2.setFont(font)
        self.labelTitle_2.setStyleSheet(u"\n"
"color: #FFFFFF")
        self.labelTitle_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelTitle_2, 0, 0, 1, 1)

        self.labelPercentage_2 = QLabel(self.layoutWidget_3)
        self.labelPercentage_2.setObjectName(u"labelPercentage_2")
        self.labelPercentage_2.setFont(font)
        self.labelPercentage_2.setStyleSheet(u"\n"
"color: #FFFFFF")
        self.labelPercentage_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.labelPercentage_2, 1, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.circularProgressBarBase_2)

        self.frame_30 = QFrame(self.frame_12)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(38, 100))
        self.frame_30.setMaximumSize(QSize(1000, 16777215))
        self.frame_30.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"border:none;\n"
"border-image:none;")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_30)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 32)
        self.date_gui = QFrame(self.frame_30)
        self.date_gui.setObjectName(u"date_gui")
        self.date_gui.setMinimumSize(QSize(0, 20))
        self.date_gui.setFrameShape(QFrame.StyledPanel)
        self.date_gui.setFrameShadow(QFrame.Raised)

        self.verticalLayout_47.addWidget(self.date_gui)

        self.frame_34 = QFrame(self.frame_30)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(16777215, 12))
        self.frame_34.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-radius:5px;")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.disponivel = QFrame(self.frame_34)
        self.disponivel.setObjectName(u"disponivel")
        self.disponivel.setMaximumSize(QSize(1000, 16777215))
        self.disponivel.setStyleSheet(u"	font: 25 12pt \"Microsoft YaHei Light\";\n"
"\n"
"\n"
"background-color: rgb(0, 170, 0);\n"
"\n"
"	border: 0px;")
        self.disponivel.setFrameShape(QFrame.StyledPanel)
        self.disponivel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.disponivel)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.usado = QFrame(self.disponivel)
        self.usado.setObjectName(u"usado")
        self.usado.setMaximumSize(QSize(100, 16777215))
        self.usado.setStyleSheet(u"	font: 25 12pt \"Microsoft YaHei Light\";\n"
"\n"
"background-color: rgb(92, 155, 207);\n"
"\n"
"	border: 0px;")
        self.usado.setFrameShape(QFrame.StyledPanel)
        self.usado.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.usado)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_55.addWidget(self.usado)


        self.horizontalLayout_30.addWidget(self.disponivel)


        self.verticalLayout_47.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_30)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(1000, 16777215))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_35)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_35)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 6, 0, 0)
        self.labelTitle_8 = QLabel(self.frame)
        self.labelTitle_8.setObjectName(u"labelTitle_8")
        self.labelTitle_8.setFont(font)
        self.labelTitle_8.setLayoutDirection(Qt.LeftToRight)
        self.labelTitle_8.setAutoFillBackground(False)
        self.labelTitle_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.labelTitle_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.labelTitle_8)

        self.labelTitle_10 = QLabel(self.frame)
        self.labelTitle_10.setObjectName(u"labelTitle_10")
        self.labelTitle_10.setFont(font)
        self.labelTitle_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.labelTitle_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.labelTitle_10)


        self.verticalLayout_13.addWidget(self.frame)


        self.verticalLayout_47.addWidget(self.frame_35)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Ignored)

        self.verticalLayout_47.addItem(self.verticalSpacer_3)


        self.horizontalLayout_11.addWidget(self.frame_30)


        self.verticalLayout_46.addWidget(self.frame_12)

        self.frame_60 = QFrame(self.frame_29)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 0))
        self.frame_60.setMaximumSize(QSize(16777215, 90))
        self.frame_60.setStyleSheet(u"")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(6, 6, 6, 6)
        self.compras = QPushButton(self.frame_60)
        self.compras.setObjectName(u"compras")
        self.compras.setMinimumSize(QSize(0, 50))
        self.compras.setMaximumSize(QSize(250, 16777215))
        self.compras.setTabletTracking(False)
        self.compras.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	border-top-right-radius:0px;\n"
"	border-bottom-right-radius:0px;\n"
"\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/backgroud/src-page-cartoes/shoop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.compras.setIcon(icon15)
        self.compras.setIconSize(QSize(35, 35))

        self.horizontalLayout_17.addWidget(self.compras)

        self.nova_despesa = QPushButton(self.frame_60)
        self.nova_despesa.setObjectName(u"nova_despesa")
        self.nova_despesa.setMinimumSize(QSize(0, 0))
        self.nova_despesa.setMaximumSize(QSize(250, 50))
        self.nova_despesa.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"\n"
"	border-radius:none;\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/backgroud/src-page-cartoes/cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nova_despesa.setIcon(icon16)
        self.nova_despesa.setIconSize(QSize(35, 35))

        self.horizontalLayout_17.addWidget(self.nova_despesa)

        self.pushButton_14 = QPushButton(self.frame_60)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 0))
        self.pushButton_14.setMaximumSize(QSize(250, 50))
        self.pushButton_14.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"\n"
"border-radius:none;\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/backgroud/src-page-cartoes/grafic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon17)
        self.pushButton_14.setIconSize(QSize(35, 35))

        self.horizontalLayout_17.addWidget(self.pushButton_14)

        self.faturas = QPushButton(self.frame_60)
        self.faturas.setObjectName(u"faturas")
        self.faturas.setMinimumSize(QSize(0, 0))
        self.faturas.setMaximumSize(QSize(250, 50))
        self.faturas.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"\n"
"border-radius:none;\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/backgroud/src-page-cartoes/calendarios.png", QSize(), QIcon.Normal, QIcon.Off)
        self.faturas.setIcon(icon18)
        self.faturas.setIconSize(QSize(30, 30))

        self.horizontalLayout_17.addWidget(self.faturas)

        self.pushButton_12 = QPushButton(self.frame_60)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 0))
        self.pushButton_12.setMaximumSize(QSize(250, 50))
        self.pushButton_12.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"	border-top-left-radius:00px;\n"
"	border-bottom-left-radius:0px;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")
        self.pushButton_12.setIconSize(QSize(30, 30))

        self.horizontalLayout_17.addWidget(self.pushButton_12)


        self.verticalLayout_46.addWidget(self.frame_60)

        self.line_2 = QFrame(self.frame_29)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(16777215, 3))
        self.line_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.00214133 rgba(160, 160, 160, 255), stop:0.33833 rgba(54, 56, 121, 125), stop:0.66167 rgba(80, 58, 161, 27), stop:1 rgba(255, 255, 255, 192));")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_46.addWidget(self.line_2)

        self.extrat_meses = QStackedWidget(self.frame_29)
        self.extrat_meses.setObjectName(u"extrat_meses")
        self.extrat_meses.setMaximumSize(QSize(16777215, 60))
        self.extrat_meses.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"border-radius:7px;\n"
"")
        self.extrat_meses.setFrameShape(QFrame.StyledPanel)
        self.extrat_meses.setFrameShadow(QFrame.Raised)
        self.extrat_mesesPage1 = QWidget()
        self.extrat_mesesPage1.setObjectName(u"extrat_mesesPage1")
        self.verticalLayout_28 = QVBoxLayout(self.extrat_mesesPage1)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.filter_dt_container = QFrame(self.extrat_mesesPage1)
        self.filter_dt_container.setObjectName(u"filter_dt_container")
        self.filter_dt_container.setMinimumSize(QSize(0, 50))
        self.filter_dt_container.setStyleSheet(u"")
        self.filter_dt_container.setFrameShape(QFrame.StyledPanel)
        self.filter_dt_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.filter_dt_container)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.frame_D = QFrame(self.filter_dt_container)
        self.frame_D.setObjectName(u"frame_D")
        self.frame_D.setMinimumSize(QSize(0, 0))
        self.frame_D.setMaximumSize(QSize(60, 16777215))
        self.frame_D.setStyleSheet(u"	border: 1px solid rgb(253, 253, 253);\n"
"	border-radius: 10px;\n"
"background-color: rgba(0, 0, 0,0);")
        self.frame_D.setFrameShape(QFrame.StyledPanel)
        self.frame_D.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_D)
        self.verticalLayout_82.setSpacing(0)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.line_d = QLineEdit(self.frame_D)
        self.line_d.setObjectName(u"line_d")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_d.sizePolicy().hasHeightForWidth())
        self.line_d.setSizePolicy(sizePolicy1)
        self.line_d.setMaximumSize(QSize(16777215, 90))
        self.line_d.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.line_d.setMaxLength(2)
        self.line_d.setAlignment(Qt.AlignCenter)

        self.verticalLayout_82.addWidget(self.line_d)


        self.horizontalLayout_31.addWidget(self.frame_D)

        self.frame_M = QFrame(self.filter_dt_container)
        self.frame_M.setObjectName(u"frame_M")
        self.frame_M.setMinimumSize(QSize(0, 0))
        self.frame_M.setMaximumSize(QSize(60, 16777215))
        self.frame_M.setStyleSheet(u"	border: 1px solid rgb(253, 253, 253);\n"
"	border-radius: 10px;\n"
"background-color: rgba(0, 0, 0,0);")
        self.frame_M.setFrameShape(QFrame.StyledPanel)
        self.frame_M.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_M)
        self.verticalLayout_85.setSpacing(0)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.line_m = QLineEdit(self.frame_M)
        self.line_m.setObjectName(u"line_m")
        sizePolicy1.setHeightForWidth(self.line_m.sizePolicy().hasHeightForWidth())
        self.line_m.setSizePolicy(sizePolicy1)
        self.line_m.setMaximumSize(QSize(16777215, 90))
        self.line_m.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.line_m.setMaxLength(2)
        self.line_m.setAlignment(Qt.AlignCenter)

        self.verticalLayout_85.addWidget(self.line_m)


        self.horizontalLayout_31.addWidget(self.frame_M)

        self.frame_A = QFrame(self.filter_dt_container)
        self.frame_A.setObjectName(u"frame_A")
        self.frame_A.setMinimumSize(QSize(0, 0))
        self.frame_A.setMaximumSize(QSize(80, 16777215))
        self.frame_A.setStyleSheet(u"	border: 1px solid rgb(253, 253, 253);\n"
"	border-radius: 10px;\n"
"background-color: rgba(0, 0, 0,0);")
        self.frame_A.setFrameShape(QFrame.StyledPanel)
        self.frame_A.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_A)
        self.verticalLayout_84.setSpacing(0)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.line_y = QLineEdit(self.frame_A)
        self.line_y.setObjectName(u"line_y")
        sizePolicy1.setHeightForWidth(self.line_y.sizePolicy().hasHeightForWidth())
        self.line_y.setSizePolicy(sizePolicy1)
        self.line_y.setMaximumSize(QSize(16777215, 90))
        self.line_y.setLayoutDirection(Qt.LeftToRight)
        self.line_y.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.line_y.setMaxLength(4)
        self.line_y.setAlignment(Qt.AlignCenter)

        self.verticalLayout_84.addWidget(self.line_y)


        self.horizontalLayout_31.addWidget(self.frame_A)

        self.pushButton_2 = QPushButton(self.filter_dt_container)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(16777215, 90))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border:none;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0,0);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"\n"
"	border: 1px solid  rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/backgroud/src-page-cartoes/lup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon19)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_31.addWidget(self.pushButton_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_6)

        self.pushButton_3 = QPushButton(self.filter_dt_container)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(80, 0))
        self.pushButton_3.setMaximumSize(QSize(16777214, 90))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border:none;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"\n"
"	border: 1px solid  rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/backgroud/src-page-cartoes/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon20)
        self.pushButton_3.setIconSize(QSize(16, 16))

        self.horizontalLayout_31.addWidget(self.pushButton_3)


        self.verticalLayout_28.addWidget(self.filter_dt_container)

        self.extrat_meses.addWidget(self.extrat_mesesPage1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_33 = QHBoxLayout(self.page_2)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.previus_month = QPushButton(self.page_2)
        self.previus_month.setObjectName(u"previus_month")
        self.previus_month.setMinimumSize(QSize(80, 0))
        self.previus_month.setMaximumSize(QSize(120, 50))
        self.previus_month.setTabletTracking(False)
        self.previus_month.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border:none;\n"
"\n"
"	background-color: rgba(0, 0, 0,0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"\n"
"	border: 1px solid  rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/backgroud/src-page-cartoes/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previus_month.setIcon(icon21)
        self.previus_month.setIconSize(QSize(20, 20))

        self.horizontalLayout_33.addWidget(self.previus_month)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_7)

        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(80, 0))
        self.label_3.setMaximumSize(QSize(80, 16777215))
        self.label_3.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")

        self.horizontalLayout_33.addWidget(self.label_3)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")

        self.horizontalLayout_33.addWidget(self.label_7)

        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")

        self.horizontalLayout_33.addWidget(self.label_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_8)

        self.next_month = QPushButton(self.page_2)
        self.next_month.setObjectName(u"next_month")
        self.next_month.setMinimumSize(QSize(80, 0))
        self.next_month.setMaximumSize(QSize(120, 50))
        self.next_month.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border:none;\n"
"\n"
"	background-color: rgba(0, 0, 0,0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"\n"
"	border: 1px solid  rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}")
        self.next_month.setIcon(icon20)

        self.horizontalLayout_33.addWidget(self.next_month)

        self.extrat_meses.addWidget(self.page_2)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.horizontalLayout_39 = QHBoxLayout(self.page_8)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.previus_month_3 = QPushButton(self.page_8)
        self.previus_month_3.setObjectName(u"previus_month_3")
        self.previus_month_3.setMinimumSize(QSize(80, 0))
        self.previus_month_3.setMaximumSize(QSize(120, 50))
        self.previus_month_3.setTabletTracking(False)
        self.previus_month_3.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border:none;\n"
"\n"
"	background-color: rgba(0, 0, 0,0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"\n"
"	border: 1px solid  rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}")
        self.previus_month_3.setIcon(icon21)
        self.previus_month_3.setIconSize(QSize(20, 20))

        self.horizontalLayout_39.addWidget(self.previus_month_3)

        self.horizontalSpacer_15 = QSpacerItem(339, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_15)

        self.label_35 = QLabel(self.page_8)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")

        self.horizontalLayout_39.addWidget(self.label_35)

        self.label_10 = QLabel(self.page_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")

        self.horizontalLayout_39.addWidget(self.label_10)

        self.horizontalSpacer_14 = QSpacerItem(338, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_14)

        self.next_month_3 = QPushButton(self.page_8)
        self.next_month_3.setObjectName(u"next_month_3")
        self.next_month_3.setMinimumSize(QSize(80, 0))
        self.next_month_3.setMaximumSize(QSize(120, 50))
        self.next_month_3.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border:none;\n"
"\n"
"	background-color: rgba(0, 0, 0,0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"\n"
"	border: 1px solid  rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}")
        self.next_month_3.setIcon(icon20)

        self.horizontalLayout_39.addWidget(self.next_month_3)

        self.extrat_meses.addWidget(self.page_8)

        self.verticalLayout_46.addWidget(self.extrat_meses)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"border:none;\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_31)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.frame_31)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 956, 503))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_53 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.frame_62 = QFrame(self.scrollAreaWidgetContents)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(0, 0))
        self.frame_62.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_62)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.frame_32 = QFrame(self.frame_62)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMaximumSize(QSize(16777215, 16777215))
        self.frame_32.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_32)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.stacked_configcartao0 = QStackedWidget(self.frame_32)
        self.stacked_configcartao0.setObjectName(u"stacked_configcartao0")
        self.stacked_configcartao0.setMinimumSize(QSize(0, 90))
        self.stacked_configcartao0.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"")
        self.stacked_configcartao0.setFrameShape(QFrame.StyledPanel)
        self.stacked_configcartao0.setFrameShadow(QFrame.Raised)
        self.page_extrato = QWidget()
        self.page_extrato.setObjectName(u"page_extrato")
        self.horizontalLayout_27 = QHBoxLayout(self.page_extrato)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.stack_extrato_pages = QStackedWidget(self.page_extrato)
        self.stack_extrato_pages.setObjectName(u"stack_extrato_pages")
        self.stack_extrato_pages.setMinimumSize(QSize(0, 0))
        self.stack_extrato_pages.setMaximumSize(QSize(16777215, 16777215))
        self.stack_extrato_pages.setFrameShape(QFrame.StyledPanel)
        self.stack_extrato_pages.setFrameShadow(QFrame.Raised)
        self.extrato_cards_dbs = QWidget()
        self.extrato_cards_dbs.setObjectName(u"extrato_cards_dbs")
        self.horizontalLayout_34 = QHBoxLayout(self.extrato_cards_dbs)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.extrato_cartao_0 = QTableWidget(self.extrato_cards_dbs)
        if (self.extrato_cartao_0.columnCount() < 10):
            self.extrato_cartao_0.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.extrato_cartao_0.setObjectName(u"extrato_cartao_0")
        self.extrato_cartao_0.setMaximumSize(QSize(16777215, 16777215))
        self.extrato_cartao_0.setFont(font)
        self.extrato_cartao_0.setLayoutDirection(Qt.LeftToRight)
        self.extrato_cartao_0.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.extrato_cartao_0.setFrameShadow(QFrame.Plain)
        self.extrato_cartao_0.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.extrato_cartao_0.setAlternatingRowColors(False)
        self.extrato_cartao_0.setIconSize(QSize(35, 35))
        self.extrato_cartao_0.setTextElideMode(Qt.ElideMiddle)
        self.extrato_cartao_0.setShowGrid(False)
        self.extrato_cartao_0.setGridStyle(Qt.DashLine)
        self.extrato_cartao_0.setSortingEnabled(False)
        self.extrato_cartao_0.setWordWrap(True)
        self.extrato_cartao_0.horizontalHeader().setVisible(False)
        self.extrato_cartao_0.horizontalHeader().setMinimumSectionSize(0)
        self.extrato_cartao_0.horizontalHeader().setDefaultSectionSize(100)
        self.extrato_cartao_0.horizontalHeader().setHighlightSections(True)
        self.extrato_cartao_0.horizontalHeader().setProperty("showSortIndicator", False)
        self.extrato_cartao_0.horizontalHeader().setStretchLastSection(False)
        self.extrato_cartao_0.verticalHeader().setVisible(False)
        self.extrato_cartao_0.verticalHeader().setCascadingSectionResizes(False)
        self.extrato_cartao_0.verticalHeader().setMinimumSectionSize(0)
        self.extrato_cartao_0.verticalHeader().setDefaultSectionSize(40)
        self.extrato_cartao_0.verticalHeader().setHighlightSections(False)
        self.extrato_cartao_0.verticalHeader().setProperty("showSortIndicator", False)
        self.extrato_cartao_0.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_34.addWidget(self.extrato_cartao_0)

        self.stack_extrato_pages.addWidget(self.extrato_cards_dbs)
        self.page_not_found = QWidget()
        self.page_not_found.setObjectName(u"page_not_found")
        self.verticalLayout_29 = QVBoxLayout(self.page_not_found)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_7)

        self.image_notfoud = QFrame(self.page_not_found)
        self.image_notfoud.setObjectName(u"image_notfoud")
        self.image_notfoud.setMinimumSize(QSize(0, 300))
        self.image_notfoud.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/not-found.png);\n"
"background-position: center;\n"
"background-repeat:no-repeat;\n"
"")
        self.image_notfoud.setFrameShape(QFrame.StyledPanel)
        self.image_notfoud.setFrameShadow(QFrame.Raised)

        self.verticalLayout_29.addWidget(self.image_notfoud)

        self.frame_page_not_found = QFrame(self.page_not_found)
        self.frame_page_not_found.setObjectName(u"frame_page_not_found")
        self.frame_page_not_found.setFrameShape(QFrame.StyledPanel)
        self.frame_page_not_found.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_page_not_found)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.text_page_notfound = QLabel(self.frame_page_not_found)
        self.text_page_notfound.setObjectName(u"text_page_notfound")
        self.text_page_notfound.setMaximumSize(QSize(16777215, 20))
        self.text_page_notfound.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.text_page_notfound.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.text_page_notfound)

        self.verticalSpacer_4 = QSpacerItem(20, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_30.addItem(self.verticalSpacer_4)


        self.verticalLayout_29.addWidget(self.frame_page_not_found)

        self.stack_extrato_pages.addWidget(self.page_not_found)
        self.page_emdia = QWidget()
        self.page_emdia.setObjectName(u"page_emdia")
        self.verticalLayout_31 = QVBoxLayout(self.page_emdia)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_6)

        self.image_emdia = QFrame(self.page_emdia)
        self.image_emdia.setObjectName(u"image_emdia")
        self.image_emdia.setMinimumSize(QSize(0, 300))
        self.image_emdia.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/payout.png);\n"
"background-position: center;\n"
"background-repeat:no-repeat;\n"
"")
        self.image_emdia.setFrameShape(QFrame.StyledPanel)
        self.image_emdia.setFrameShadow(QFrame.Raised)

        self.verticalLayout_31.addWidget(self.image_emdia)

        self.txt_pag_emdia = QLabel(self.page_emdia)
        self.txt_pag_emdia.setObjectName(u"txt_pag_emdia")
        self.txt_pag_emdia.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.txt_pag_emdia.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.txt_pag_emdia)

        self.verticalSpacer_5 = QSpacerItem(20, 95, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_31.addItem(self.verticalSpacer_5)

        self.stack_extrato_pages.addWidget(self.page_emdia)

        self.horizontalLayout_27.addWidget(self.stack_extrato_pages)

        self.frame_13 = QFrame(self.page_extrato)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(200, 0))
        self.frame_13.setMaximumSize(QSize(200, 16777215))
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_13)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 200))
        self.frame_14.setMaximumSize(QSize(16777215, 200))
        self.frame_14.setStyleSheet(u"border-image: url(:/charts_back/card_back/rezi.png);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_24.addWidget(self.frame_14)

        self.frame_21 = QFrame(self.frame_13)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"	border-radius: 10px;\n"
"\n"
"	\n"
"	background-color:rgb(25, 37, 55);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_21)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.apaga_compra = QPushButton(self.frame_21)
        self.apaga_compra.setObjectName(u"apaga_compra")
        self.apaga_compra.setMinimumSize(QSize(0, 30))
        self.apaga_compra.setMaximumSize(QSize(16777215, 30))
        self.apaga_compra.setLayoutDirection(Qt.LeftToRight)
        self.apaga_compra.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"	border-radius: 10px;\n"
"\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u":/icons-cards/src-page-cartoes/urgencia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.apaga_compra.setIcon(icon22)

        self.verticalLayout_25.addWidget(self.apaga_compra)

        self.edit_compra = QPushButton(self.frame_21)
        self.edit_compra.setObjectName(u"edit_compra")
        self.edit_compra.setMinimumSize(QSize(0, 30))
        self.edit_compra.setMaximumSize(QSize(16777215, 30))
        self.edit_compra.setLayoutDirection(Qt.LeftToRight)
        self.edit_compra.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"	border-radius: 10px;\n"
"\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u":/icons-cards/src-page-cartoes/icons8-etiquetas-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_compra.setIcon(icon23)

        self.verticalLayout_25.addWidget(self.edit_compra)

        self.paga_fatura = QPushButton(self.frame_21)
        self.paga_fatura.setObjectName(u"paga_fatura")
        self.paga_fatura.setMinimumSize(QSize(0, 30))
        self.paga_fatura.setMaximumSize(QSize(16777215, 30))
        self.paga_fatura.setLayoutDirection(Qt.LeftToRight)
        self.paga_fatura.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"	border-radius: 10px;\n"
"\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")
        icon24 = QIcon()
        icon24.addFile(u":/icons-cards/src-page-cartoes/money.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paga_fatura.setIcon(icon24)

        self.verticalLayout_25.addWidget(self.paga_fatura)

        self.parcela_fatura = QPushButton(self.frame_21)
        self.parcela_fatura.setObjectName(u"parcela_fatura")
        self.parcela_fatura.setMinimumSize(QSize(0, 30))
        self.parcela_fatura.setMaximumSize(QSize(16777215, 30))
        self.parcela_fatura.setLayoutDirection(Qt.LeftToRight)
        self.parcela_fatura.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"	border-radius: 10px;\n"
"\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")
        icon25 = QIcon()
        icon25.addFile(u":/icons-cards/src-page-cartoes/parcelas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.parcela_fatura.setIcon(icon25)

        self.verticalLayout_25.addWidget(self.parcela_fatura)

        self.filter_dates_btn = QPushButton(self.frame_21)
        self.filter_dates_btn.setObjectName(u"filter_dates_btn")
        self.filter_dates_btn.setMinimumSize(QSize(0, 30))
        self.filter_dates_btn.setFont(font)
        self.filter_dates_btn.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"	border-radius: 10px;\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")
        icon26 = QIcon()
        icon26.addFile(u":/icons-cards/src-page-cartoes/datase.png", QSize(), QIcon.Normal, QIcon.Off)
        self.filter_dates_btn.setIcon(icon26)

        self.verticalLayout_25.addWidget(self.filter_dates_btn)

        self.verticalSpacer = QSpacerItem(20, 247, QSizePolicy.Minimum, QSizePolicy.Ignored)

        self.verticalLayout_25.addItem(self.verticalSpacer)


        self.verticalLayout_24.addWidget(self.frame_21)


        self.horizontalLayout_27.addWidget(self.frame_13)

        self.stacked_configcartao0.addWidget(self.page_extrato)
        self.page_Faturas = QWidget()
        self.page_Faturas.setObjectName(u"page_Faturas")
        self.horizontalLayout_41 = QHBoxLayout(self.page_Faturas)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.central_cards_main_2 = QFrame(self.page_Faturas)
        self.central_cards_main_2.setObjectName(u"central_cards_main_2")
        self.central_cards_main_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-bottom: 0px;\n"
"border: 0px;")
        self.central_cards_main_2.setFrameShape(QFrame.StyledPanel)
        self.central_cards_main_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.central_cards_main_2)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.date_filters_fatura_2 = QFrame(self.central_cards_main_2)
        self.date_filters_fatura_2.setObjectName(u"date_filters_fatura_2")
        self.date_filters_fatura_2.setMaximumSize(QSize(16777215, 50))
        self.date_filters_fatura_2.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px;\n"
"border-right: 0px;")
        self.date_filters_fatura_2.setFrameShape(QFrame.StyledPanel)
        self.date_filters_fatura_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.date_filters_fatura_2)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(30, 0, 30, 0)

        self.verticalLayout_45.addWidget(self.date_filters_fatura_2)

        self.line_4 = QFrame(self.central_cards_main_2)
        self.line_4.setObjectName(u"line_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line_4.sizePolicy().hasHeightForWidth())
        self.line_4.setSizePolicy(sizePolicy2)
        self.line_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.00214133 rgba(160, 160, 160, 255), stop:0.33833 rgba(54, 56, 121, 125), stop:0.66167 rgba(80, 58, 161, 27), stop:1 rgba(255, 255, 255, 192));")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_4)

        self.datails_fatura_card_2 = QFrame(self.central_cards_main_2)
        self.datails_fatura_card_2.setObjectName(u"datails_fatura_card_2")
        self.datails_fatura_card_2.setMaximumSize(QSize(16777215, 80))
        self.datails_fatura_card_2.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom:0px;\n"
"border-right: 0px;")
        self.datails_fatura_card_2.setFrameShape(QFrame.StyledPanel)
        self.datails_fatura_card_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.datails_fatura_card_2)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.icon_2 = QFrame(self.datails_fatura_card_2)
        self.icon_2.setObjectName(u"icon_2")
        self.icon_2.setMaximumSize(QSize(48, 48))
        self.icon_2.setStyleSheet(u"border-bottom: 0px;\n"
"border-radius: 5px;\n"
"border-image: url(:/menu/bradesco-icon.png);")
        self.icon_2.setFrameShape(QFrame.StyledPanel)
        self.icon_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_40.addWidget(self.icon_2)

        self.name_bank_2 = QLabel(self.datails_fatura_card_2)
        self.name_bank_2.setObjectName(u"name_bank_2")
        self.name_bank_2.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"color:rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_40.addWidget(self.name_bank_2)

        self.horizontalSpacer_18 = QSpacerItem(40, 58, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_18)

        self.set_limite_card_2 = QFrame(self.datails_fatura_card_2)
        self.set_limite_card_2.setObjectName(u"set_limite_card_2")
        self.set_limite_card_2.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 1px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"color:rgb(255, 255, 255);\n"
"")
        self.set_limite_card_2.setFrameShape(QFrame.StyledPanel)
        self.set_limite_card_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.set_limite_card_2)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_27 = QLabel(self.set_limite_card_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"\n"
"border-radius:3px;")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_48.addWidget(self.label_27)

        self.label_28 = QLabel(self.set_limite_card_2)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"border-radius:3px;")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_48.addWidget(self.label_28)


        self.horizontalLayout_40.addWidget(self.set_limite_card_2)

        self.set_disponivel_cars_2 = QFrame(self.datails_fatura_card_2)
        self.set_disponivel_cars_2.setObjectName(u"set_disponivel_cars_2")
        self.set_disponivel_cars_2.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 1px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"color:rgb(255, 255, 255);\n"
"")
        self.set_disponivel_cars_2.setFrameShape(QFrame.StyledPanel)
        self.set_disponivel_cars_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.set_disponivel_cars_2)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_29 = QLabel(self.set_disponivel_cars_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"border-radius:3px;")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_49.addWidget(self.label_29)

        self.label_30 = QLabel(self.set_disponivel_cars_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)
        self.label_30.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"border-radius:3px;")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_49.addWidget(self.label_30)


        self.horizontalLayout_40.addWidget(self.set_disponivel_cars_2)

        self.set_fechamento_2 = QFrame(self.datails_fatura_card_2)
        self.set_fechamento_2.setObjectName(u"set_fechamento_2")
        self.set_fechamento_2.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 1px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"color:rgb(255, 255, 255);\n"
"")
        self.set_fechamento_2.setFrameShape(QFrame.StyledPanel)
        self.set_fechamento_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.set_fechamento_2)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_31 = QLabel(self.set_fechamento_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)
        self.label_31.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"border-radius:3px;")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.label_31)

        self.label_32 = QLabel(self.set_fechamento_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font)
        self.label_32.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"border-radius:3px;")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_50.addWidget(self.label_32)


        self.horizontalLayout_40.addWidget(self.set_fechamento_2)

        self.set_vencimento_2 = QFrame(self.datails_fatura_card_2)
        self.set_vencimento_2.setObjectName(u"set_vencimento_2")
        self.set_vencimento_2.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 0px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"color:rgb(255, 255, 255);\n"
"")
        self.set_vencimento_2.setFrameShape(QFrame.StyledPanel)
        self.set_vencimento_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.set_vencimento_2)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_33 = QLabel(self.set_vencimento_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"border-radius:3px;")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.label_33)

        self.label_34 = QLabel(self.set_vencimento_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"border-radius:3px;")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.label_34)


        self.horizontalLayout_40.addWidget(self.set_vencimento_2)


        self.verticalLayout_45.addWidget(self.datails_fatura_card_2)

        self.datalhed_fatura_mother_2 = QFrame(self.central_cards_main_2)
        self.datalhed_fatura_mother_2.setObjectName(u"datalhed_fatura_mother_2")
        self.datalhed_fatura_mother_2.setStyleSheet(u"border-bottom: 0px;\n"
"border-right: 0px;\n"
"border-radius:15px;")
        self.datalhed_fatura_mother_2.setFrameShape(QFrame.StyledPanel)
        self.datalhed_fatura_mother_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.datalhed_fatura_mother_2)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.table_faturas_ind = QTableWidget(self.datalhed_fatura_mother_2)
        if (self.table_faturas_ind.columnCount() < 5):
            self.table_faturas_ind.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.table_faturas_ind.setObjectName(u"table_faturas_ind")
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Light Condensed")
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(3)
        self.table_faturas_ind.setFont(font1)
        self.table_faturas_ind.setStyleSheet(u"QWidget {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"    color: #fffff8;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #b55ed3;\n"
"    font-size: 11;\n"
"	border:none;\n"
"	width:45px;\n"
"	height: 50px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #fffff8;\n"
"    font-size: 11pt;\n"
"	border-radius:15px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableView:item {\n"
"  border-bottom: 0.5px solid qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:0.45677 rgba(0, 0, 0, 0), stop:0.479846 rgba(255, 255, 255, 255), stop:0.50571 rgba(239, 236, 55, 0), stop:1 rgba(239, 236, 55, 0));\n"
"\n"
"}\n"
"\n"
"")
        self.table_faturas_ind.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_faturas_ind.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_faturas_ind.setAlternatingRowColors(False)
        self.table_faturas_ind.setIconSize(QSize(45, 40))
        self.table_faturas_ind.setTextElideMode(Qt.ElideLeft)
        self.table_faturas_ind.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_faturas_ind.setShowGrid(False)
        self.table_faturas_ind.setSortingEnabled(False)
        self.table_faturas_ind.horizontalHeader().setVisible(False)
        self.table_faturas_ind.horizontalHeader().setDefaultSectionSize(189)
        self.table_faturas_ind.verticalHeader().setVisible(False)

        self.verticalLayout_52.addWidget(self.table_faturas_ind)


        self.verticalLayout_45.addWidget(self.datalhed_fatura_mother_2)


        self.horizontalLayout_41.addWidget(self.central_cards_main_2)

        self.stacked_configcartao0.addWidget(self.page_Faturas)
        self.page_new_lancamento = QWidget()
        self.page_new_lancamento.setObjectName(u"page_new_lancamento")
        self.horizontalLayout_18 = QHBoxLayout(self.page_new_lancamento)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 20, 0, 20)
        self.scrollArea_3 = QScrollArea(self.page_new_lancamento)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 140, 469))
        self.verticalLayout_72 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 20, 0)
        self.frame_61 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setMinimumSize(QSize(120, 67))
        self.frame_61.setMaximumSize(QSize(16777215, 67))
        self.frame_61.setStyleSheet(u"\n"
"border-radius:10px;")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.frame_68 = QFrame(self.frame_61)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setMinimumSize(QSize(0, 0))
        self.frame_68.setMaximumSize(QSize(40, 40))
        self.frame_68.setStyleSheet(u"border-image: url(:/icons-cards/src-page-cartoes/nulsmal.png);\n"
"\n"
"")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_29.addWidget(self.frame_68)

        self.frame_74 = QFrame(self.frame_61)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(0, 0))
        self.frame_74.setMaximumSize(QSize(190, 40))
        self.frame_74.setStyleSheet(u"")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_74)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.label_19 = QLabel(self.frame_74)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 27))
        self.label_19.setMaximumSize(QSize(16777215, 18))
        self.label_19.setFont(font)
        self.label_19.setAutoFillBackground(False)
        self.label_19.setStyleSheet(u"border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_73.addWidget(self.label_19)


        self.horizontalLayout_29.addWidget(self.frame_74)

        self.frame_80 = QFrame(self.frame_61)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(200, 0))
        self.frame_80.setMaximumSize(QSize(16777215, 16777215))
        self.frame_80.setStyleSheet(u"	border: 1px solid rgb(253, 253, 253);\n"
"	border-radius: 10px;")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_80)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.comboBox_2 = QComboBox(self.frame_80)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMaximumSize(QSize(16777215, 90))
        self.comboBox_2.setStyleSheet(u"border: 0px;\n"
"font: 25 12pt \"Microsoft YaHei Light\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")

        self.verticalLayout_80.addWidget(self.comboBox_2)


        self.horizontalLayout_29.addWidget(self.frame_80)


        self.verticalLayout_72.addWidget(self.frame_61)

        self.frame_65 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(120, 67))
        self.frame_65.setMaximumSize(QSize(16777215, 67))
        self.frame_65.setStyleSheet(u"\n"
"border-radius:10px;")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_65)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_69 = QFrame(self.frame_65)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMinimumSize(QSize(40, 0))
        self.frame_69.setMaximumSize(QSize(40, 40))
        self.frame_69.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/etiqueta.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_25.addWidget(self.frame_69)

        self.frame_75 = QFrame(self.frame_65)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMinimumSize(QSize(190, 0))
        self.frame_75.setMaximumSize(QSize(190, 40))
        self.frame_75.setStyleSheet(u"")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_75)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.label_20 = QLabel(self.frame_75)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setMaximumSize(QSize(16777215, 18))
        self.label_20.setFont(font)
        self.label_20.setAutoFillBackground(False)
        self.label_20.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_75.addWidget(self.label_20)


        self.horizontalLayout_25.addWidget(self.frame_75)

        self.frame_81 = QFrame(self.frame_65)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(0, 0))
        self.frame_81.setMaximumSize(QSize(16777215, 16777215))
        self.frame_81.setStyleSheet(u"	border: 1px solid rgb(253, 253, 253);\n"
"	border-radius: 10px;")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_81)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.lineEdit = QLineEdit(self.frame_81)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMaximumSize(QSize(16777215, 90))
        self.lineEdit.setStyleSheet(u"border: 0px;\n"
"font: 25 12pt \"Microsoft YaHei Light\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")

        self.verticalLayout_81.addWidget(self.lineEdit)


        self.horizontalLayout_25.addWidget(self.frame_81)


        self.verticalLayout_72.addWidget(self.frame_65)

        self.frame_64 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setMinimumSize(QSize(120, 67))
        self.frame_64.setMaximumSize(QSize(16777215, 67))
        self.frame_64.setStyleSheet(u"\n"
"border-radius:10px;")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.frame_70 = QFrame(self.frame_64)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setMinimumSize(QSize(40, 0))
        self.frame_70.setMaximumSize(QSize(40, 40))
        self.frame_70.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/calendarios.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_23.addWidget(self.frame_70)

        self.frame_76 = QFrame(self.frame_64)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setMinimumSize(QSize(190, 0))
        self.frame_76.setMaximumSize(QSize(190, 16777215))
        self.frame_76.setStyleSheet(u"")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_76)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.label_22 = QLabel(self.frame_76)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 0))
        self.label_22.setMaximumSize(QSize(16777215, 18))
        self.label_22.setFont(font)
        self.label_22.setAutoFillBackground(False)
        self.label_22.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.label_22)


        self.horizontalLayout_23.addWidget(self.frame_76)

        self.frame_82 = QFrame(self.frame_64)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(0, 0))
        self.frame_82.setMaximumSize(QSize(16777215, 16777215))
        self.frame_82.setStyleSheet(u"	border: 1px solid rgb(253, 253, 253);\n"
"	border-radius: 10px;")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lineEdit_2 = QLineEdit(self.frame_82)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(16777215, 90))
        self.lineEdit_2.setStyleSheet(u"border: 0px;\n"
"font: 25 12pt \"Microsoft YaHei Light\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")

        self.horizontalLayout_12.addWidget(self.lineEdit_2)

        self.pushButton_17 = QPushButton(self.frame_82)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setMinimumSize(QSize(48, 0))
        self.pushButton_17.setMaximumSize(QSize(48, 48))
        self.pushButton_17.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"	border-radius: 10px;\n"
"   	background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_17)


        self.horizontalLayout_23.addWidget(self.frame_82)


        self.verticalLayout_72.addWidget(self.frame_64)

        self.frame_66 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMinimumSize(QSize(120, 67))
        self.frame_66.setMaximumSize(QSize(16777215, 67))
        self.frame_66.setStyleSheet(u"\n"
"border-radius:10px;")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_71 = QFrame(self.frame_66)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setMinimumSize(QSize(40, 0))
        self.frame_71.setMaximumSize(QSize(40, 40))
        self.frame_71.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/money2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22.addWidget(self.frame_71)

        self.frame_77 = QFrame(self.frame_66)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setMinimumSize(QSize(190, 0))
        self.frame_77.setMaximumSize(QSize(190, 16777215))
        self.frame_77.setStyleSheet(u"")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_77)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.label_24 = QLabel(self.frame_77)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 0))
        self.label_24.setMaximumSize(QSize(16777215, 18))
        self.label_24.setFont(font)
        self.label_24.setAutoFillBackground(False)
        self.label_24.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_77.addWidget(self.label_24)


        self.horizontalLayout_22.addWidget(self.frame_77)

        self.frame_83 = QFrame(self.frame_66)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMinimumSize(QSize(0, 0))
        self.frame_83.setMaximumSize(QSize(16777215, 16777215))
        self.frame_83.setStyleSheet(u"	border: 1px solid rgb(253, 253, 253);\n"
"	border-radius: 10px;")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_83)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.lineEdit_3 = QLineEdit(self.frame_83)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(16777215, 90))
        self.lineEdit_3.setStyleSheet(u"border: 0px;\n"
"font: 25 12pt \"Microsoft YaHei Light\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")

        self.verticalLayout_83.addWidget(self.lineEdit_3)


        self.horizontalLayout_22.addWidget(self.frame_83)


        self.verticalLayout_72.addWidget(self.frame_66)

        self.frame_63 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMinimumSize(QSize(120, 67))
        self.frame_63.setMaximumSize(QSize(16777215, 67))
        self.frame_63.setStyleSheet(u"\n"
"border-radius:10px;")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.frame_72 = QFrame(self.frame_63)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(40, 0))
        self.frame_72.setMaximumSize(QSize(40, 40))
        self.frame_72.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/credt.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_21.addWidget(self.frame_72)

        self.frame_78 = QFrame(self.frame_63)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMinimumSize(QSize(0, 0))
        self.frame_78.setMaximumSize(QSize(190, 16777215))
        self.frame_78.setFont(font)
        self.frame_78.setStyleSheet(u"")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_78)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.label_25 = QLabel(self.frame_78)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 0))
        self.label_25.setMaximumSize(QSize(16777215, 18))
        self.label_25.setFont(font)
        self.label_25.setAutoFillBackground(False)
        self.label_25.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_78.addWidget(self.label_25)


        self.horizontalLayout_21.addWidget(self.frame_78)

        self.frame_84 = QFrame(self.frame_63)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setMinimumSize(QSize(0, 0))
        self.frame_84.setMaximumSize(QSize(16777215, 16777215))
        self.frame_84.setStyleSheet(u"	border: 1px solid rgb(253, 253, 253);\n"
"	border-radius: 10px;")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_84)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.comboBox_4 = QComboBox(self.frame_84)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMaximumSize(QSize(16777215, 90))
        self.comboBox_4.setStyleSheet(u"border: 0px;\n"
"font: 25 12pt \"Microsoft YaHei Light\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")

        self.verticalLayout_54.addWidget(self.comboBox_4)


        self.horizontalLayout_21.addWidget(self.frame_84)


        self.verticalLayout_72.addWidget(self.frame_63)

        self.frame_67 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(120, 67))
        self.frame_67.setMaximumSize(QSize(16777215, 67))
        self.frame_67.setStyleSheet(u"\n"
"border-radius:10px;")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_73 = QFrame(self.frame_67)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setMinimumSize(QSize(40, 0))
        self.frame_73.setMaximumSize(QSize(40, 40))
        self.frame_73.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/parcelas2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_19.addWidget(self.frame_73)

        self.frame_79 = QFrame(self.frame_67)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setMinimumSize(QSize(190, 0))
        self.frame_79.setMaximumSize(QSize(190, 16777215))
        self.frame_79.setStyleSheet(u"")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_79)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.label_26 = QLabel(self.frame_79)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 0))
        self.label_26.setMaximumSize(QSize(16777215, 18))
        self.label_26.setFont(font)
        self.label_26.setAutoFillBackground(False)
        self.label_26.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_79.addWidget(self.label_26)


        self.horizontalLayout_19.addWidget(self.frame_79)

        self.frame_85 = QFrame(self.frame_67)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(0, 0))
        self.frame_85.setMaximumSize(QSize(16777215, 16777215))
        self.frame_85.setStyleSheet(u"	border: 1px solid rgb(253, 253, 253);\n"
"	border-radius: 10px;")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_85)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.comboBox_3 = QComboBox(self.frame_85)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMaximumSize(QSize(16777215, 90))
        self.comboBox_3.setStyleSheet(u"border: 0px;\n"
"font: 25 12pt \"Microsoft YaHei Light\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")

        self.verticalLayout_68.addWidget(self.comboBox_3)


        self.horizontalLayout_19.addWidget(self.frame_85)


        self.verticalLayout_72.addWidget(self.frame_67)

        self.frame_18 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(120, 67))
        self.frame_18.setMaximumSize(QSize(16777215, 67))
        self.frame_18.setStyleSheet(u"background-color:rgb(25, 37, 55);\n"
"border-radius:10px;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer = QSpacerItem(200, 0, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.lanca = QPushButton(self.frame_18)
        self.lanca.setObjectName(u"lanca")
        self.lanca.setMinimumSize(QSize(70, 0))
        self.lanca.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"	border-radius: 10px;\n"
"   	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.00398406 rgba(117, 160, 215, 255), stop:0.250614 rgba(0, 109, 187, 242), stop:0.641278 rgba(34, 121, 152, 159), stop:0.644963 rgba(34, 121, 152, 159), stop:1 rgba(106, 151, 221, 255));\n"
"\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.00398406 rgba(150, 167, 190, 255), stop:0.250614 rgba(74, 140, 187, 242), stop:0.641278 rgba(92, 136, 152, 159), stop:0.644963 rgba(34, 121, 152, 159), stop:1 rgba(172, 191, 221, 255));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")

        self.horizontalLayout_13.addWidget(self.lanca)

        self.horizontalSpacer_2 = QSpacerItem(200, 0, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)

        self.cancela_lanca = QPushButton(self.frame_18)
        self.cancela_lanca.setObjectName(u"cancela_lanca")
        self.cancela_lanca.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"	border-radius: 10px;\n"
"   	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.00398406 rgba(215, 138, 117, 255), stop:0.250614 rgba(187, 0, 0, 242), stop:0.619799 rgba(152, 34, 34, 159), stop:0.644963 rgba(152, 34, 34, 159), stop:1 rgba(221, 106, 106, 255));\n"
"   color:rgb(255, 255, 255);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.00398406 rgba(215, 168, 156, 255), stop:0.250614 rgba(187, 125, 125, 242), stop:0.619799 rgba(152, 108, 108, 159), stop:0.644963 rgba(152, 97, 97, 159), stop:1 rgba(221, 168, 168, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")

        self.horizontalLayout_13.addWidget(self.cancela_lanca)

        self.horizontalSpacer_3 = QSpacerItem(200, 0, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)


        self.verticalLayout_72.addWidget(self.frame_18)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.horizontalLayout_18.addWidget(self.scrollArea_3)

        self.stacked_configcartao0.addWidget(self.page_new_lancamento)
        self.charts_indvidual = QWidget()
        self.charts_indvidual.setObjectName(u"charts_indvidual")
        self.verticalLayout_12 = QVBoxLayout(self.charts_indvidual)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 5, 0, 0)
        self.scrolcharts = QScrollArea(self.charts_indvidual)
        self.scrolcharts.setObjectName(u"scrolcharts")
        self.scrolcharts.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrolcharts.setWidgetResizable(True)
        self.chatsscrroo = QWidget()
        self.chatsscrroo.setObjectName(u"chatsscrroo")
        self.chatsscrroo.setGeometry(QRect(0, 0, 266, 700))
        self.chatsscrroo.setMinimumSize(QSize(0, 700))
        self.verticalLayout_20 = QVBoxLayout(self.chatsscrroo)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.chatsscrroo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"\n"
"	border-radius: 10px;\n"
"	border-bottom: 4px solid rgb(45, 45, 68);\n"
"	border-right: 4px solid rgb(45, 45, 68);\n"
"	border:none;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setStyleSheet(u"border-radius:10px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_24.setSpacing(20)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"border-image: url(:/charts_back/card_back/smma.jpg);\n"
"\n"
"")

        self.horizontalLayout_24.addWidget(self.label)

        self.baner = QFrame(self.frame_11)
        self.baner.setObjectName(u"baner")
        self.baner.setEnabled(True)
        self.baner.setMinimumSize(QSize(0, 0))
        self.baner.setMaximumSize(QSize(16777215, 16777215))
        self.baner.setAutoFillBackground(False)
        self.baner.setStyleSheet(u"border-image: url(:/charts_back/card_back/\u2014Pngtree\u20142 5d stereoscopic business cartoon_928799.jpg);\n"
"border-radius:10px;")
        self.baner.setFrameShape(QFrame.StyledPanel)
        self.baner.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_24.addWidget(self.baner)


        self.verticalLayout_8.addWidget(self.frame_11)

        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"QTabWidget::tab-bar {\n"
"  background: gray;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  background: rgb(134, 134, 191);\n"
"  color: black;\n"
"  padding: 10px;\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background: rgb(179, 178, 253)  ;\n"
" }\n"
"\n"
"QTabWidget::pane { border-top-left-radius:0px; border-top-right-radius:0px;}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMaximumSize(QSize(16777215, 16777215))
        self.tab.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.tab)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 10, 0)
        self.chart_main_category = QFrame(self.tab)
        self.chart_main_category.setObjectName(u"chart_main_category")
        self.chart_main_category.setStyleSheet(u"border-radius:10px;")
        self.chart_main_category.setFrameShape(QFrame.StyledPanel)
        self.chart_main_category.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.chart_main_category)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.chart_main_category)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 139, 135, 255), stop:0.427447 rgba(41, 138, 132, 255), stop:1 rgba(155, 119, 165, 255));")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_19)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_chart_category = QVBoxLayout()
        self.frame_chart_category.setObjectName(u"frame_chart_category")

        self.verticalLayout_21.addLayout(self.frame_chart_category)


        self.verticalLayout_17.addWidget(self.frame_19)


        self.verticalLayout_14.addWidget(self.chart_main_category)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"")
        self.verticalLayout_22 = QVBoxLayout(self.tab_2)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 10, 0)
        self.chart_main_date = QFrame(self.tab_2)
        self.chart_main_date.setObjectName(u"chart_main_date")
        self.chart_main_date.setStyleSheet(u"border-radius:10px;")
        self.chart_main_date.setFrameShape(QFrame.StyledPanel)
        self.chart_main_date.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.chart_main_date)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.chart_main_date)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 139, 135, 255), stop:0.427447 rgba(41, 138, 132, 255), stop:1 rgba(155, 119, 165, 255))\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_15)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_chart_date_day = QVBoxLayout()
        self.frame_chart_date_day.setObjectName(u"frame_chart_date_day")

        self.verticalLayout_18.addLayout(self.frame_chart_date_day)


        self.verticalLayout_15.addWidget(self.frame_15)


        self.verticalLayout_22.addWidget(self.chart_main_date)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_23 = QVBoxLayout(self.tab_3)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 10, 0)
        self.chart_main_evolution = QFrame(self.tab_3)
        self.chart_main_evolution.setObjectName(u"chart_main_evolution")
        self.chart_main_evolution.setStyleSheet(u"border-radius:10px;")
        self.chart_main_evolution.setFrameShape(QFrame.StyledPanel)
        self.chart_main_evolution.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.chart_main_evolution)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.chart_main_evolution)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 139, 135, 255), stop:0.427447 rgba(41, 138, 132, 255), stop:1 rgba(155, 119, 165, 255))\n"
"\n"
"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_chart_evolution_fat = QVBoxLayout()
        self.frame_chart_evolution_fat.setObjectName(u"frame_chart_evolution_fat")

        self.verticalLayout_19.addLayout(self.frame_chart_evolution_fat)


        self.verticalLayout_16.addWidget(self.frame_16)


        self.verticalLayout_23.addWidget(self.chart_main_evolution)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_8.addWidget(self.tabWidget)


        self.verticalLayout_20.addWidget(self.frame_2)

        self.scrolcharts.setWidget(self.chatsscrroo)

        self.verticalLayout_12.addWidget(self.scrolcharts)

        self.stacked_configcartao0.addWidget(self.charts_indvidual)

        self.verticalLayout_44.addWidget(self.stacked_configcartao0)


        self.verticalLayout_71.addWidget(self.frame_32)


        self.verticalLayout_53.addWidget(self.frame_62)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_42.addWidget(self.scrollArea_2)


        self.verticalLayout_46.addWidget(self.frame_31)


        self.horizontalLayout_26.addWidget(self.frame_29)


        self.verticalLayout_40.addWidget(self.CONTAINER_geral)

        self.detalhes_cartao.addWidget(self.detalhes_cartaoPage1)
        self.dashboard_cards = QWidget()
        self.dashboard_cards.setObjectName(u"dashboard_cards")
        self.verticalLayout_32 = QVBoxLayout(self.dashboard_cards)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.top_mainsd = QFrame(self.dashboard_cards)
        self.top_mainsd.setObjectName(u"top_mainsd")
        self.top_mainsd.setMinimumSize(QSize(0, 100))
        self.top_mainsd.setMaximumSize(QSize(16777215, 16777215))
        self.top_mainsd.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-bottom: 0px;\n"
"border: 0px;")
        self.top_mainsd.setFrameShape(QFrame.StyledPanel)
        self.top_mainsd.setFrameShadow(QFrame.Raised)

        self.verticalLayout_32.addWidget(self.top_mainsd)

        self.central_cards_main = QFrame(self.dashboard_cards)
        self.central_cards_main.setObjectName(u"central_cards_main")
        self.central_cards_main.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border-bottom: 0px;\n"
"border: 0px;")
        self.central_cards_main.setFrameShape(QFrame.StyledPanel)
        self.central_cards_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.central_cards_main)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(30, -1, 30, -1)
        self.date_filters_fatura = QFrame(self.central_cards_main)
        self.date_filters_fatura.setObjectName(u"date_filters_fatura")
        self.date_filters_fatura.setMaximumSize(QSize(16777215, 50))
        self.date_filters_fatura.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 1px solid rgb(45, 45, 68);\n"
"border-right: 0px;")
        self.date_filters_fatura.setFrameShape(QFrame.StyledPanel)
        self.date_filters_fatura.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.date_filters_fatura)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(30, 0, 30, 0)
        self.label_8 = QLabel(self.date_filters_fatura)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setFamily(u"Microsoft YaHei Light")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"font: 14pt \"Microsoft YaHei Light\";\n"
"color:rgb(255, 255, 255);\n"
"border-radius:3px;")

        self.horizontalLayout_36.addWidget(self.label_8)

        self.filter_main = QFrame(self.date_filters_fatura)
        self.filter_main.setObjectName(u"filter_main")
        self.filter_main.setStyleSheet(u"border-bottom: 0px;")
        self.filter_main.setFrameShape(QFrame.StyledPanel)
        self.filter_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.filter_main)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_12)

        self.previus_month_2 = QPushButton(self.filter_main)
        self.previus_month_2.setObjectName(u"previus_month_2")
        self.previus_month_2.setMinimumSize(QSize(80, 0))
        self.previus_month_2.setMaximumSize(QSize(120, 50))
        self.previus_month_2.setTabletTracking(False)
        self.previus_month_2.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"	font: 25 12pt \"Microsoft YaHei Light\";\n"
"	border:none;\n"
"	color:rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"\n"
"	border: 1px solid  rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}")
        self.previus_month_2.setIcon(icon21)
        self.previus_month_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_35.addWidget(self.previus_month_2)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_9)

        self.label_9 = QLabel(self.filter_main)
        self.label_9.setObjectName(u"label_9")
        font3 = QFont()
        font3.setFamily(u"Microsoft YaHei Light")
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"font:  16pt \"Microsoft YaHei Light\";\n"
"color:rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_35.addWidget(self.label_9)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_10)

        self.next_month_2 = QPushButton(self.filter_main)
        self.next_month_2.setObjectName(u"next_month_2")
        self.next_month_2.setMinimumSize(QSize(80, 0))
        self.next_month_2.setMaximumSize(QSize(120, 50))
        font4 = QFont()
        font4.setFamily(u"Microsoft YaHei Light")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(3)
        self.next_month_2.setFont(font4)
        self.next_month_2.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"	font: 25 12pt \"Microsoft YaHei Light\";\n"
"	border:none;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"\n"
"	border: 1px solid  rgb(255, 255, 255);\n"
"	border-radius:5px;\n"
"}")
        self.next_month_2.setIcon(icon20)

        self.horizontalLayout_35.addWidget(self.next_month_2)


        self.horizontalLayout_36.addWidget(self.filter_main)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_11)


        self.verticalLayout_33.addWidget(self.date_filters_fatura)

        self.datails_fatura_card = QFrame(self.central_cards_main)
        self.datails_fatura_card.setObjectName(u"datails_fatura_card")
        self.datails_fatura_card.setMaximumSize(QSize(16777215, 80))
        self.datails_fatura_card.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 1px solid rgb(45, 45, 68);\n"
"border-right: 0px;")
        self.datails_fatura_card.setFrameShape(QFrame.StyledPanel)
        self.datails_fatura_card.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.datails_fatura_card)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.icon = QFrame(self.datails_fatura_card)
        self.icon.setObjectName(u"icon")
        self.icon.setMaximumSize(QSize(48, 48))
        self.icon.setStyleSheet(u"border-bottom: 0px;\n"
"border-radius: 5px;\n"
"border-image: url(:/menu/bradesco-icon.png);")
        self.icon.setFrameShape(QFrame.StyledPanel)
        self.icon.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_37.addWidget(self.icon)

        self.name_bank = QLabel(self.datails_fatura_card)
        self.name_bank.setObjectName(u"name_bank")
        self.name_bank.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"font: 11pt \"Microsoft YaHei Light\";\n"
"color:rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_37.addWidget(self.name_bank)

        self.horizontalSpacer_13 = QSpacerItem(40, 58, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_13)

        self.set_limite_card = QFrame(self.datails_fatura_card)
        self.set_limite_card.setObjectName(u"set_limite_card")
        self.set_limite_card.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 1px solid rgb(45, 45, 68);\n"
"border-left: 1px solid rgb(45, 45, 68);\n"
"color:rgb(255, 255, 255);\n"
"")
        self.set_limite_card.setFrameShape(QFrame.StyledPanel)
        self.set_limite_card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.set_limite_card)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_11 = QLabel(self.set_limite_card)
        self.label_11.setObjectName(u"label_11")
        font5 = QFont()
        font5.setFamily(u"Microsoft YaHei Light")
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"font: 11pt \"Microsoft YaHei Light\";\n"
"\n"
"border-radius:3px;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_11)

        self.label_12 = QLabel(self.set_limite_card)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)
        self.label_12.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"font: 11pt \"Microsoft YaHei Light\";\n"
"\n"
"border-radius:3px;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_12)


        self.horizontalLayout_37.addWidget(self.set_limite_card)

        self.set_disponivel_cars = QFrame(self.datails_fatura_card)
        self.set_disponivel_cars.setObjectName(u"set_disponivel_cars")
        self.set_disponivel_cars.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 1px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"color:rgb(255, 255, 255);\n"
"")
        self.set_disponivel_cars.setFrameShape(QFrame.StyledPanel)
        self.set_disponivel_cars.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.set_disponivel_cars)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_13 = QLabel(self.set_disponivel_cars)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font5)
        self.label_13.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"font: 11pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_13)

        self.label_14 = QLabel(self.set_disponivel_cars)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)
        self.label_14.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"font: 11pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.label_14)


        self.horizontalLayout_37.addWidget(self.set_disponivel_cars)

        self.set_fechamento = QFrame(self.datails_fatura_card)
        self.set_fechamento.setObjectName(u"set_fechamento")
        self.set_fechamento.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 1px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"color:rgb(255, 255, 255);\n"
"")
        self.set_fechamento.setFrameShape(QFrame.StyledPanel)
        self.set_fechamento.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.set_fechamento)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_15 = QLabel(self.set_fechamento)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font5)
        self.label_15.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"font: 11pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_15)

        self.label_16 = QLabel(self.set_fechamento)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font5)
        self.label_16.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"font: 11pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_16)


        self.horizontalLayout_37.addWidget(self.set_fechamento)

        self.set_vencimento = QFrame(self.datails_fatura_card)
        self.set_vencimento.setObjectName(u"set_vencimento")
        self.set_vencimento.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 1px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"color:rgb(255, 255, 255);\n"
"")
        self.set_vencimento.setFrameShape(QFrame.StyledPanel)
        self.set_vencimento.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.set_vencimento)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_18 = QLabel(self.set_vencimento)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font5)
        self.label_18.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"font: 11pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_18)

        self.label_21 = QLabel(self.set_vencimento)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font5)
        self.label_21.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"font: 11pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_21)


        self.horizontalLayout_37.addWidget(self.set_vencimento)


        self.verticalLayout_33.addWidget(self.datails_fatura_card)

        self.datalhed_fatura_mother = QFrame(self.central_cards_main)
        self.datalhed_fatura_mother.setObjectName(u"datalhed_fatura_mother")
        self.datalhed_fatura_mother.setStyleSheet(u"border-bottom: 0px;\n"
"border-right: 0px;")
        self.datalhed_fatura_mother.setFrameShape(QFrame.StyledPanel)
        self.datalhed_fatura_mother.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.datalhed_fatura_mother)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 9, 0, 0)
        self.tableWidget = QTableWidget(self.datalhed_fatura_mother)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        if (self.tableWidget.rowCount() < 2):
            self.tableWidget.setRowCount(2)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFlags(Qt.NoItemFlags);
        self.tableWidget.setItem(0, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem24.setFlags(Qt.ItemIsSelectable);
        self.tableWidget.setItem(0, 1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem25.setFlags(Qt.NoItemFlags);
        self.tableWidget.setItem(0, 2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem26.setFlags(Qt.NoItemFlags);
        self.tableWidget.setItem(0, 3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem27.setFlags(Qt.NoItemFlags);
        self.tableWidget.setItem(0, 4, __qtablewidgetitem27)
        icon27 = QIcon()
        icon27.addFile(u":/backgroud/src-page-cartoes/money2.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setCheckState(Qt.Unchecked);
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem28.setIcon(icon27);
        self.tableWidget.setItem(0, 5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem29.setFlags(Qt.NoItemFlags);
        self.tableWidget.setItem(1, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem30.setFlags(Qt.NoItemFlags);
        self.tableWidget.setItem(1, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem31.setFlags(Qt.NoItemFlags);
        self.tableWidget.setItem(1, 2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFlags(Qt.NoItemFlags);
        self.tableWidget.setItem(1, 3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem33.setFlags(Qt.NoItemFlags);
        self.tableWidget.setItem(1, 4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setCheckState(Qt.Unchecked);
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem34.setIcon(icon27);
        self.tableWidget.setItem(1, 5, __qtablewidgetitem34)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        self.tableWidget.setFont(font1)
        self.tableWidget.setStyleSheet(u"QWidget {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"    color: #fffff8;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #b55ed3;\n"
"    font-size: 11;\n"
"	border:none;\n"
"	width:45px;\n"
"	height: 50px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #fffff8;\n"
"    font-size: 11pt;\n"
"	border:0px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableView:item {\n"
"  border: 0px;\n"
"  padding: 0px 10px;\n"
"  margin-left: 0;\n"
"  border-bottom: 1px solid rgb(255	, 255, 255);\n"
"  border-right: 0px;\n"
"}\n"
"\n"
"")
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setIconSize(QSize(45, 40))
        self.tableWidget.setTextElideMode(Qt.ElideLeft)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_43.addWidget(self.tableWidget)


        self.verticalLayout_33.addWidget(self.datalhed_fatura_mother)


        self.verticalLayout_32.addWidget(self.central_cards_main)

        self.detalhes_cartao.addWidget(self.dashboard_cards)

        self.horizontalLayout_15.addWidget(self.detalhes_cartao)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_9.addWidget(self.scrollArea)

        self.stackedWidget_3.addWidget(self.page)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_9 = QVBoxLayout(self.page2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.scrollArea_5 = QScrollArea(self.page2)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM "
                        "- SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
""
                        "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 602, 318))
        self.horizontalLayout_20 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_9 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(502, 300))
        self.frame_9.setMaximumSize(QSize(500, 400))
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"	border-radius: 10px;\n"
"	border-bottom: 4px solid rgb(45, 45, 68);\n"
"	border-right: 4px solid rgb(45, 45, 68);\n"
"\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(40, -1, 40, -1)
        self.select_card = QComboBox(self.frame_9)
        self.select_card.addItem("")
        self.select_card.addItem("")
        self.select_card.addItem("")
        self.select_card.addItem("")
        self.select_card.addItem("")
        self.select_card.addItem("")
        self.select_card.addItem("")
        self.select_card.setObjectName(u"select_card")
        self.select_card.setMinimumSize(QSize(0, 30))
        font6 = QFont()
        font6.setFamily(u"Bahnschrift Light Condensed")
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setWeight(3)
        font6.setStrikeOut(False)
        font6.setKerning(True)
        font6.setStyleStrategy(QFont.PreferDefault)
        self.select_card.setFont(font6)
        self.select_card.setLayoutDirection(Qt.LeftToRight)
        self.select_card.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:10px;\n"
"")

        self.verticalLayout_10.addWidget(self.select_card)

        self.frameadc = QFrame(self.frame_9)
        self.frameadc.setObjectName(u"frameadc")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(65)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frameadc.sizePolicy().hasHeightForWidth())
        self.frameadc.setSizePolicy(sizePolicy4)
        self.frameadc.setMinimumSize(QSize(0, 0))
        self.frameadc.setMaximumSize(QSize(400, 200))
        self.frameadc.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(130, 10, 209);\n"
"border-radius: 10px;\n"
"border: 3px solid  rgb(0, 0, 0);\n"
"border:0px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"border: 3px solid  rgb(55, 50,50);\n"
"\n"
"}")
        self.frameadc.setFrameShape(QFrame.StyledPanel)
        self.frameadc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frameadc)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.logoadc = QFrame(self.frameadc)
        self.logoadc.setObjectName(u"logoadc")
        self.logoadc.setMaximumSize(QSize(40, 40))
        self.logoadc.setStyleSheet(u"border: 0px;\n"
"background-image: url(:/menu/nu-icon.png);\n"
"")
        self.logoadc.setFrameShape(QFrame.StyledPanel)
        self.logoadc.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.logoadc)

        self.frame_10 = QFrame(self.frameadc)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 142))
        self.frame_10.setStyleSheet(u"border:none;\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textcard = QLabel(self.frame_10)
        self.textcard.setObjectName(u"textcard")
        self.textcard.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard.setTextFormat(Qt.AutoText)
        self.textcard.setScaledContents(False)
        self.textcard.setAlignment(Qt.AlignCenter)
        self.textcard.setWordWrap(False)

        self.gridLayout.addWidget(self.textcard, 0, 0, 1, 1)

        self.textcard_2 = QLabel(self.frame_10)
        self.textcard_2.setObjectName(u"textcard_2")
        self.textcard_2.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard_2.setTextFormat(Qt.AutoText)
        self.textcard_2.setScaledContents(False)
        self.textcard_2.setAlignment(Qt.AlignCenter)
        self.textcard_2.setWordWrap(False)

        self.gridLayout.addWidget(self.textcard_2, 0, 1, 1, 1)

        self.adclimite = QLineEdit(self.frame_10)
        self.adclimite.setObjectName(u"adclimite")
        self.adclimite.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adclimite.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.adclimite, 1, 0, 1, 1)

        self.adctitular = QLineEdit(self.frame_10)
        self.adctitular.setObjectName(u"adctitular")
        self.adctitular.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adctitular.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.adctitular, 1, 1, 1, 1)

        self.textcard_3 = QLabel(self.frame_10)
        self.textcard_3.setObjectName(u"textcard_3")
        self.textcard_3.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard_3.setTextFormat(Qt.AutoText)
        self.textcard_3.setScaledContents(False)
        self.textcard_3.setAlignment(Qt.AlignCenter)
        self.textcard_3.setWordWrap(False)

        self.gridLayout.addWidget(self.textcard_3, 2, 0, 1, 1)

        self.textcard_4 = QLabel(self.frame_10)
        self.textcard_4.setObjectName(u"textcard_4")
        self.textcard_4.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard_4.setTextFormat(Qt.AutoText)
        self.textcard_4.setScaledContents(False)
        self.textcard_4.setAlignment(Qt.AlignCenter)
        self.textcard_4.setWordWrap(False)

        self.gridLayout.addWidget(self.textcard_4, 2, 1, 1, 1)

        self.adcfinal = QLineEdit(self.frame_10)
        self.adcfinal.setObjectName(u"adcfinal")
        self.adcfinal.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adcfinal.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.adcfinal, 3, 0, 1, 1)

        self.adcvencimento = QLineEdit(self.frame_10)
        self.adcvencimento.setObjectName(u"adcvencimento")
        self.adcvencimento.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adcvencimento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.adcvencimento, 3, 1, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_10)


        self.verticalLayout_10.addWidget(self.frameadc)

        self.menu_option_3 = QFrame(self.frame_9)
        self.menu_option_3.setObjectName(u"menu_option_3")
        self.menu_option_3.setMinimumSize(QSize(0, 58))
        self.menu_option_3.setMaximumSize(QSize(16777215, 30))
        self.menu_option_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"border-bottom:rgba(255, 255, 255, 0); \n"
"border-right: rgba(255, 255, 255, 0); ")
        self.menu_option_3.setFrameShape(QFrame.StyledPanel)
        self.menu_option_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.menu_option_3)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, -1, -1, -1)
        self.add_card_3 = QPushButton(self.menu_option_3)
        self.add_card_3.setObjectName(u"add_card_3")
        self.add_card_3.setMinimumSize(QSize(110, 30))
        self.add_card_3.setMaximumSize(QSize(110, 25))
        self.add_card_3.setFont(font)
        self.add_card_3.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"	border-radius: 10px;\n"
"\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")

        self.horizontalLayout_16.addWidget(self.add_card_3)

        self.remover_card_3 = QPushButton(self.menu_option_3)
        self.remover_card_3.setObjectName(u"remover_card_3")
        self.remover_card_3.setMinimumSize(QSize(110, 30))
        self.remover_card_3.setMaximumSize(QSize(110, 25))
        self.remover_card_3.setFont(font)
        self.remover_card_3.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"\n"
"	border-radius: 10px;\n"
"\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")

        self.horizontalLayout_16.addWidget(self.remover_card_3)


        self.verticalLayout_10.addWidget(self.menu_option_3)


        self.horizontalLayout_20.addWidget(self.frame_9)

        self.table_active_cards = QTableWidget(self.scrollAreaWidgetContents_5)
        if (self.table_active_cards.columnCount() < 5):
            self.table_active_cards.setColumnCount(5)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_active_cards.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_active_cards.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_active_cards.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_active_cards.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.table_active_cards.setHorizontalHeaderItem(4, __qtablewidgetitem39)
        self.table_active_cards.setObjectName(u"table_active_cards")
        self.table_active_cards.setMinimumSize(QSize(0, 0))
        self.table_active_cards.setMaximumSize(QSize(704, 500))
        self.table_active_cards.setTabletTracking(False)
        self.table_active_cards.setStyleSheet(u"QWidget {\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"    color: #fffff8;\n"
"\n"
"	border-bottom: 4px solid rgb(45, 45, 68);\n"
"	border-right: 4px solid rgb(45, 45, 68);\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #b55ed3;\n"
"    font-size: 14pt;\n"
"\n"
"\n"
"	letter-spacing:0px;\n"
"	margin-right: 5;\n"
"\n"
"	width:45px;\n"
"	height: 50px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #fffff8;\n"
"    font-size: 12pt;\n"
" 	padding: 10px\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"\n"
"}\n"
"\n"
"QTableView:item {\n"
"  border: 0px;\n"
"  padding: 0px 10px;\n"
"}\n"
"\n"
"")
        self.table_active_cards.setFrameShape(QFrame.StyledPanel)
        self.table_active_cards.setFrameShadow(QFrame.Plain)
        self.table_active_cards.setAutoScroll(True)
        self.table_active_cards.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_active_cards.setTabKeyNavigation(True)
        self.table_active_cards.setDragDropOverwriteMode(True)
        self.table_active_cards.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.table_active_cards.setAlternatingRowColors(False)
        self.table_active_cards.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table_active_cards.setShowGrid(False)
        self.table_active_cards.setGridStyle(Qt.DashLine)
        self.table_active_cards.setSortingEnabled(False)
        self.table_active_cards.setWordWrap(True)
        self.table_active_cards.horizontalHeader().setVisible(False)
        self.table_active_cards.horizontalHeader().setCascadingSectionResizes(True)
        self.table_active_cards.horizontalHeader().setDefaultSectionSize(136)
        self.table_active_cards.horizontalHeader().setHighlightSections(True)
        self.table_active_cards.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_active_cards.horizontalHeader().setStretchLastSection(False)
        self.table_active_cards.verticalHeader().setVisible(False)
        self.table_active_cards.verticalHeader().setCascadingSectionResizes(False)
        self.table_active_cards.verticalHeader().setMinimumSectionSize(23)
        self.table_active_cards.verticalHeader().setDefaultSectionSize(30)
        self.table_active_cards.verticalHeader().setHighlightSections(True)
        self.table_active_cards.verticalHeader().setProperty("showSortIndicator", False)
        self.table_active_cards.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_20.addWidget(self.table_active_cards)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_9.addWidget(self.scrollArea_5)

        self.stackedWidget_3.addWidget(self.page2)

        self.verticalLayout_39.addWidget(self.stackedWidget_3)


        self.verticalLayout_38.addWidget(self.backgroud_cartao)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_4 = QLabel(self.page_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(460, 250, 47, 13))
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_5 = QLabel(self.page_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(430, 260, 47, 13))
        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_6 = QLabel(self.page_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(340, 270, 47, 13))
        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.horizontalLayout_42 = QHBoxLayout(self.page_7)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.frame_17 = QFrame(self.page_7)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(800, 16777215))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_17)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalSpacer_8 = QSpacerItem(20, 207, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_57.addItem(self.verticalSpacer_8)

        self.frame_20 = QFrame(self.frame_17)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(500, 500))
        self.frame_20.setMaximumSize(QSize(16777215, 16777215))
        self.frame_20.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(400, 16777215))
        self.frame_22.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.frame_24 = QFrame(self.frame_22)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(300, 300))
        self.frame_24.setStyleSheet(u"border-image: url(:/dev/C:/Users/Jhonatan Deni/Desktop/58306583.jfif);")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_44.addWidget(self.frame_24)


        self.horizontalLayout_43.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_23)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.pushButton_4 = QPushButton(self.frame_23)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon28 = QIcon()
        icon28.addFile(u":/dev/dev/devs.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon28)
        self.pushButton_4.setIconSize(QSize(40, 40))

        self.verticalLayout_58.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_23)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon29 = QIcon()
        icon29.addFile(u":/dev/dev/academy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon29)
        self.pushButton_5.setIconSize(QSize(40, 40))

        self.verticalLayout_58.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_23)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"\n"
"border-radius:4px;\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")
        icon30 = QIcon()
        icon30.addFile(u":/dev/dev/git.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon30)
        self.pushButton_6.setIconSize(QSize(40, 40))

        self.verticalLayout_58.addWidget(self.pushButton_6)

        self.label_17 = QLabel(self.frame_23)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 100))
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_58.addWidget(self.label_17)

        self.pushButton_13 = QPushButton(self.frame_23)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_58.addWidget(self.pushButton_13)

        self.pushButton_19 = QPushButton(self.frame_23)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setMinimumSize(QSize(0, 40))
        self.pushButton_19.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"\n"
"border-radius:4px;\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(121, 121, 121);\n"
"	border: 2px solid  rgb(55, 55, 55);\n"
"}")

        self.verticalLayout_58.addWidget(self.pushButton_19)


        self.horizontalLayout_43.addWidget(self.frame_23)


        self.verticalLayout_57.addWidget(self.frame_20)

        self.verticalSpacer_9 = QSpacerItem(20, 207, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_57.addItem(self.verticalSpacer_9)


        self.horizontalLayout_42.addWidget(self.frame_17)

        self.stackedWidget_2.addWidget(self.page_7)

        self.horizontalLayout_6.addWidget(self.stackedWidget_2)


        self.verticalLayout_7.addWidget(self.group)

        self.stackedWidget.addWidget(self.inicio)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.pushButton_12, self.enter_user)
        QWidget.setTabOrder(self.enter_user, self.enter_pass)
        QWidget.setTabOrder(self.enter_pass, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.buton_login)
        QWidget.setTabOrder(self.buton_login, self.minimize)
        QWidget.setTabOrder(self.minimize, self.maxmize)
        QWidget.setTabOrder(self.maxmize, self.exit)
        QWidget.setTabOrder(self.exit, self.grid)
        QWidget.setTabOrder(self.grid, self.grid_2)
        QWidget.setTabOrder(self.grid_2, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.scrollArea_2)
        QWidget.setTabOrder(self.scrollArea_2, self.nova_despesa)
        QWidget.setTabOrder(self.nova_despesa, self.pushButton_14)
        QWidget.setTabOrder(self.pushButton_14, self.faturas)
        QWidget.setTabOrder(self.faturas, self.pushButton_7)
        QWidget.setTabOrder(self.pushButton_7, self.scrollArea_3)
        QWidget.setTabOrder(self.scrollArea_3, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pushButton_17)
        QWidget.setTabOrder(self.pushButton_17, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.comboBox_4)
        QWidget.setTabOrder(self.comboBox_4, self.comboBox_3)
        QWidget.setTabOrder(self.comboBox_3, self.lanca)
        QWidget.setTabOrder(self.lanca, self.cancela_lanca)
        QWidget.setTabOrder(self.cancela_lanca, self.scrollArea_5)
        QWidget.setTabOrder(self.scrollArea_5, self.select_card)
        QWidget.setTabOrder(self.select_card, self.adclimite)
        QWidget.setTabOrder(self.adclimite, self.adctitular)
        QWidget.setTabOrder(self.adctitular, self.adcfinal)
        QWidget.setTabOrder(self.adcfinal, self.adcvencimento)
        QWidget.setTabOrder(self.adcvencimento, self.add_card_3)
        QWidget.setTabOrder(self.add_card_3, self.remover_card_3)
        QWidget.setTabOrder(self.remover_card_3, self.table_active_cards)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(0)
        self.detalhes_cartao.setCurrentIndex(0)
        self.extrat_meses.setCurrentIndex(1)
        self.stacked_configcartao0.setCurrentIndex(0)
        self.stack_extrato_pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSalvar_automaticamente.setText(QCoreApplication.translate("MainWindow", u"Salvar automaticamente", None))
        self.actionAtualizar_automaticamente.setText(QCoreApplication.translate("MainWindow", u"Atualizar automaticamente", None))
        self.actionAbrir_DB.setText(QCoreApplication.translate("MainWindow", u"Abrir DB", None))
        self.actionSalvar_Relatorio.setText(QCoreApplication.translate("MainWindow", u"Salvar Relatorio", None))
        self.actionAbrir_xlsx.setText(QCoreApplication.translate("MainWindow", u"Abrir xlsx", None))
        self.actionImportar_xlsx.setText(QCoreApplication.translate("MainWindow", u"Importar xlsx", None))
        self.texto_error.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.pushButton_7.setText("")
        self.enter_user.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Usuario", None))
        self.enter_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Senha", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Lembrar senha", None))
        self.buton_login.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.credits.setText(QCoreApplication.translate("MainWindow", u"   Home Aplication Ver: 1.0", None))
        self.minimize.setText("")
        self.maxmize.setText("")
        self.exit.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"    Home APP", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"     Inicio", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"     Investimentos", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"     Cartoes", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"     Transferencias", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"     Estoque", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"     Preferencias", None))
        self.salvar_6.setText(QCoreApplication.translate("MainWindow", u"    Cria banco de Dados", None))
        self.salvar_5.setText(QCoreApplication.translate("MainWindow", u"    Trocar Usuario", None))
        self.salvar_4.setText(QCoreApplication.translate("MainWindow", u"    Sair", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"    Desenvolvedor", None))
        self.grid.setText(QCoreApplication.translate("MainWindow", u"    Meus Cart\u00f5es", None))
        self.grid_2.setText(QCoreApplication.translate("MainWindow", u"   Configurar Cart\u00f5es", None))
        self.labelCredits_2.setText(QCoreApplication.translate("MainWindow", u"Uso de limte", None))
        self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#9b9bff;\">Nubank</span></p></body></html>", None))
        self.labelPercentage_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">0</span><span style=\" font-size:20pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.frame_35.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: rgba(255, 255, 255, 0);", None))
        self.labelTitle_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#5c9bcf;\">Limite Utilizado:</span></p><p><span style=\" font-size:11pt; font-weight:600; color:#5c9bcf;\">R$0,00</span></p></body></html>", None))
        self.labelTitle_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#00aa00;\">Limite Disponivel</span></p><p><span style=\" font-size:11pt; font-weight:600; color:#00aa00;\">R$0,00</span></p></body></html>", None))
        self.compras.setText(QCoreApplication.translate("MainWindow", u"Compras", None))
        self.nova_despesa.setText(QCoreApplication.translate("MainWindow", u"   Nova Despesa", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"   DashBoard", None))
        self.faturas.setText(QCoreApplication.translate("MainWindow", u"   Faturas", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"function", None))
        self.line_d.setInputMask("")
        self.line_d.setText("")
        self.line_d.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dia", None))
        self.line_m.setText("")
        self.line_m.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00eas", None))
        self.line_y.setText("")
        self.line_y.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Ano", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Procurar  ", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.previus_month.setText(QCoreApplication.translate("MainWindow", u" Previus ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Novembro", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"de", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"2022", None))
        self.next_month.setText(QCoreApplication.translate("MainWindow", u" Next", None))
        self.previus_month_3.setText(QCoreApplication.translate("MainWindow", u" Previus ", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Ano", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"2022", None))
        self.next_month_3.setText(QCoreApplication.translate("MainWindow", u" Next", None))
        ___qtablewidgetitem = self.extrato_cartao_0.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"icon_cartegori", None));
        ___qtablewidgetitem1 = self.extrato_cartao_0.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Categoria", None));
        ___qtablewidgetitem2 = self.extrato_cartao_0.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Transa\u00e7\u00e3o", None));
        ___qtablewidgetitem3 = self.extrato_cartao_0.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem4 = self.extrato_cartao_0.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Opera\u00e7\u00e3o", None));
        ___qtablewidgetitem5 = self.extrato_cartao_0.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Parcela", None));
        ___qtablewidgetitem6 = self.extrato_cartao_0.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem7 = self.extrato_cartao_0.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem8 = self.extrato_cartao_0.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"data_filter", None));
        ___qtablewidgetitem9 = self.extrato_cartao_0.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"status_payment", None));
#if QT_CONFIG(whatsthis)
        self.extrato_cartao_0.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">asdasdasdsad</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.text_page_notfound.setText(QCoreApplication.translate("MainWindow", u"Compra n\u00e3o localizada", None))
        self.txt_pag_emdia.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o h\u00e1 despesas este mes!", None))
        self.apaga_compra.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.edit_compra.setText(QCoreApplication.translate("MainWindow", u"Editar Compra", None))
        self.paga_fatura.setText(QCoreApplication.translate("MainWindow", u"Pagar Fatura", None))
        self.parcela_fatura.setText(QCoreApplication.translate("MainWindow", u"Parcelar Fatura", None))
        self.filter_dates_btn.setText(QCoreApplication.translate("MainWindow", u"Filtrar por Data  ", None))
        self.name_bank_2.setText(QCoreApplication.translate("MainWindow", u"Bradesco", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Limite", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Disponivel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Fechamento", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Vencimento", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        ___qtablewidgetitem10 = self.table_faturas_ind.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"M\u00eas", None));
        ___qtablewidgetitem11 = self.table_faturas_ind.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o da fatura", None));
        ___qtablewidgetitem12 = self.table_faturas_ind.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Valor da fatura", None));
        ___qtablewidgetitem13 = self.table_faturas_ind.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Valor pago", None));
        ___qtablewidgetitem14 = self.table_faturas_ind.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Pagamento", None));
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Selecione a Categoria", None))
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Delivery", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Apps Transporte", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Comida", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Mercado", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Lazer", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Casa", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Coisas Inuteis", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Servi\u00e7os", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Streaming", None))
        self.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Urgencia", None))
        self.comboBox_2.setItemText(11, QCoreApplication.translate("MainWindow", u"Gatos", None))
        self.comboBox_2.setItemText(12, QCoreApplication.translate("MainWindow", u"Dogs", None))
        self.comboBox_2.setItemText(13, QCoreApplication.translate("MainWindow", u"Medico", None))
        self.comboBox_2.setItemText(14, QCoreApplication.translate("MainWindow", u"Viagem", None))
        self.comboBox_2.setItemText(15, QCoreApplication.translate("MainWindow", u"Eletronicos", None))
        self.comboBox_2.setItemText(16, QCoreApplication.translate("MainWindow", u"Domesticos", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Nome desta Transa\u00e7\u00e3o", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Data da Transa\u00e7\u00e3o", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText("")
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Hoje", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Valor do Lan\u00e7amento", None))
        self.lineEdit_3.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Opera\u00e7\u00e3o", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"Credito", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"Debito", None))

        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Parcelas", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Avista", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_3.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_3.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_3.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_3.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))

        self.lanca.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.cancela_lanca.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Ol\u00e1, Bem vindo ao seu Dashboard</span></p><p align=\"center\"><br/><br/></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">Aqui encontrar\u00e1 seus graficos por categoria, </span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">selecione o tipo que deseja verificar</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Grafico de gastos neste cart\u00e3o por Categoria", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Grafico de gastos neste cart\u00e3o por Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Evolu\u00e7\u00e3o de faturas", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Faturas do cart\u00e3o", None))
        self.previus_month_2.setText(QCoreApplication.translate("MainWindow", u" Previus ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"2022", None))
        self.next_month_2.setText(QCoreApplication.translate("MainWindow", u" Next", None))
        self.name_bank.setText(QCoreApplication.translate("MainWindow", u"Bradesco", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Limite", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Disponivel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Fechamento", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Vencimento", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"M\u00eas", None));
        ___qtablewidgetitem16 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Cart\u00e3o", None));
        ___qtablewidgetitem17 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o da fatura", None));
        ___qtablewidgetitem18 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Valor da fatura", None));
        ___qtablewidgetitem19 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Valor pago", None));
        ___qtablewidgetitem20 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Pagamento", None));
        ___qtablewidgetitem21 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem22 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem23 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Julho", None));
        ___qtablewidgetitem24 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Bradesco", None));
        ___qtablewidgetitem25 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Pago", None));
        ___qtablewidgetitem26 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"R$467,70", None));
        ___qtablewidgetitem27 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"R$467,70", None));
        ___qtablewidgetitem28 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Pago", None));
        ___qtablewidgetitem29 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"C6", None));
        ___qtablewidgetitem30 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Atual", None));
        ___qtablewidgetitem31 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"R$90,90", None));
        ___qtablewidgetitem32 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"R$90,90", None));
        ___qtablewidgetitem33 = self.tableWidget.item(1, 5)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Pagar", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.select_card.setItemText(0, QCoreApplication.translate("MainWindow", u"C6", None))
        self.select_card.setItemText(1, QCoreApplication.translate("MainWindow", u"NUBANK", None))
        self.select_card.setItemText(2, QCoreApplication.translate("MainWindow", u"BTG", None))
        self.select_card.setItemText(3, QCoreApplication.translate("MainWindow", u"SANTANDER", None))
        self.select_card.setItemText(4, QCoreApplication.translate("MainWindow", u"ITAU", None))
        self.select_card.setItemText(5, QCoreApplication.translate("MainWindow", u"BRADESCO", None))
        self.select_card.setItemText(6, QCoreApplication.translate("MainWindow", u"CAIXA ECONOMICA", None))

        self.textcard.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Limite Total do Cartao</span></p></body></html>", None))
        self.textcard_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Titular</span></p></body></html>", None))
        self.adclimite.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.adctitular.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.textcard_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Final do Cart\u00e3o</span></p></body></html>", None))
        self.textcard_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Vencimento</span></p></body></html>", None))
        self.adcfinal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXX", None))
        self.adcvencimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"00", None))
        self.add_card_3.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR", None))
        self.remover_card_3.setText(QCoreApplication.translate("MainWindow", u"REMOVER", None))
        ___qtablewidgetitem34 = self.table_active_cards.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Cartao", None));
        ___qtablewidgetitem35 = self.table_active_cards.horizontalHeaderItem(1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Titular", None));
        ___qtablewidgetitem36 = self.table_active_cards.horizontalHeaderItem(2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Limite", None));
        ___qtablewidgetitem37 = self.table_active_cards.horizontalHeaderItem(3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Final do cartao", None));
        ___qtablewidgetitem38 = self.table_active_cards.horizontalHeaderItem(4)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Vencimento", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PAGE3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PAGE4", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PAGE5", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Desenvolvido por Jhonatan Deni", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Estudante de Analise e desenvolvimento de Sistemas", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Meu primeiro projetinho de Finan\u00e7as, inicialmente apenas com uma pagina</p><p align=\"center\">Com intuito de organiza\u00e7\u00e3o e controle de Cartoes de Credito</p><p align=\"center\">Demais op\u00e7oes ainda serao implementadas</p><p align=\"center\">Obrigado :)</p><p align=\"center\"><br/></p><p align=\"justify\"><br/></p></body></html>", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Doa\u00e7\u00e3o para pagar as parcelas da faculdade :)", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PicPay: @jhonatan.deni", None))
    # retranslateUi

