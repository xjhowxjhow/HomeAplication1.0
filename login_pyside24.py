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
        icon = QIcon()
        icon.addFile(u"C:/Users/Jhonatan Deni/.designer/Jhonatan Deni/.designer/backup/src/home.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
"background-color: rgb(54, 54, 54);\n"
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
"background-color:rgb(54, 54, 54);\n"
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
        self.buton_login.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"	border-image:url('');\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
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
        self.group.setStyleSheet(u"color: rgb(255, 255, 255);")
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
        self.menu.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/menu/menu/togle2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
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
        icon2 = QIcon()
        icon2.addFile(u":/menu/menu/payout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon2)
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
        icon3 = QIcon()
        icon3.addFile(u":/menu/menu/invest.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon3)
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
        icon4 = QIcon()
        icon4.addFile(u":/menu/menu/cards.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon4)
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
        icon5 = QIcon()
        icon5.addFile(u":/menu/menu/transfer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon5)
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
        icon6 = QIcon()
        icon6.addFile(u":/menu/menu/food.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon6)
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
        icon7 = QIcon()
        icon7.addFile(u":/menu/menu/config.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_16.setIcon(icon7)
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
        icon8 = QIcon()
        icon8.addFile(u":/menu/menu/db.png", QSize(), QIcon.Normal, QIcon.Off)
        self.salvar_6.setIcon(icon8)
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
        icon9 = QIcon()
        icon9.addFile(u":/login/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.salvar_5.setIcon(icon9)
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
        icon10 = QIcon()
        icon10.addFile(u":/menu/menu/powerof.png", QSize(), QIcon.Normal, QIcon.Off)
        self.salvar_4.setIcon(icon10)
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
        icon11 = QIcon()
        icon11.addFile(u":/menu/menu/notiy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon11)
        self.pushButton_18.setIconSize(QSize(30, 30))

        self.verticalLayout_27.addWidget(self.pushButton_18)


        self.horizontalLayout_28.addWidget(self.topmenu)


        self.verticalLayout_26.addWidget(self.categorias)


        self.horizontalLayout_6.addWidget(self.menu)

        self.stackedWidget_2 = QStackedWidget(self.group)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"border-radius: 10px;")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.page_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_40 = QFrame(self.page_1)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"border-radius:7px;")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_40)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_40)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_6 = QScrollArea(self.frame_42)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setMinimumSize(QSize(0, 0))
        self.scrollArea_6.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 5px;\n"
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
"/* BTN BOTTOM -"
                        " SCROLLBAR */\n"
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
        self.scrollArea_6.setFrameShadow(QFrame.Raised)
        self.scrollArea_6.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_6.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1486, 950))
        self.scrollAreaWidgetContents_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.horizontalLayout_51 = QHBoxLayout(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.content_cartao_2 = QFrame(self.scrollAreaWidgetContents_6)
        self.content_cartao_2.setObjectName(u"content_cartao_2")
        self.content_cartao_2.setMinimumSize(QSize(0, 0))
        self.content_cartao_2.setMaximumSize(QSize(440, 16777215))
        self.content_cartao_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.content_cartao_2.setFrameShape(QFrame.StyledPanel)
        self.content_cartao_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.content_cartao_2)
        self.verticalLayout_43.setSpacing(30)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_51.addWidget(self.content_cartao_2)

        self.detalhes_cartao_2 = QStackedWidget(self.scrollAreaWidgetContents_6)
        self.detalhes_cartao_2.setObjectName(u"detalhes_cartao_2")
        self.detalhes_cartao_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.detalhes_cartao_2.setFrameShape(QFrame.StyledPanel)
        self.detalhes_cartao_2.setFrameShadow(QFrame.Raised)
        self.dashboard_cards_2 = QWidget()
        self.dashboard_cards_2.setObjectName(u"dashboard_cards_2")
        self.dashboard_cards_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.verticalLayout_34 = QVBoxLayout(self.dashboard_cards_2)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.scrollArea_9 = QScrollArea(self.dashboard_cards_2)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setMinimumSize(QSize(0, 0))
        self.scrollArea_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.scrollArea_9.setFrameShape(QFrame.StyledPanel)
        self.scrollArea_9.setFrameShadow(QFrame.Plain)
        self.scrollArea_9.setLineWidth(1)
        self.scrollArea_9.setMidLineWidth(0)
        self.scrollArea_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 1463, 958))
        self.scrollAreaWidgetContents_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.verticalLayout_108 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_108.setSpacing(10)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.main_dasht_top_2 = QFrame(self.scrollAreaWidgetContents_9)
        self.main_dasht_top_2.setObjectName(u"main_dasht_top_2")
        self.main_dasht_top_2.setMinimumSize(QSize(200, 200))
        self.main_dasht_top_2.setMaximumSize(QSize(16777215, 16777215))
        self.main_dasht_top_2.setStyleSheet(u"")
        self.main_dasht_top_2.setFrameShape(QFrame.StyledPanel)
        self.main_dasht_top_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.main_dasht_top_2)
        self.horizontalLayout_65.setSpacing(10)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.main_dasht_top_2)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(80, 0))
        self.frame_43.setMaximumSize(QSize(80, 16777215))
        self.frame_43.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_43)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.hide_cards_main_2 = QPushButton(self.frame_43)
        self.hide_cards_main_2.setObjectName(u"hide_cards_main_2")
        self.hide_cards_main_2.setMinimumSize(QSize(40, 53))
        self.hide_cards_main_2.setMaximumSize(QSize(16777215, 16777215))
        self.hide_cards_main_2.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/backgroud/src-page-cartoes/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hide_cards_main_2.setIcon(icon12)
        self.hide_cards_main_2.setIconSize(QSize(40, 40))

        self.verticalLayout_36.addWidget(self.hide_cards_main_2)

        self.show_cards_main_2 = QPushButton(self.frame_43)
        self.show_cards_main_2.setObjectName(u"show_cards_main_2")
        self.show_cards_main_2.setMinimumSize(QSize(40, 53))
        self.show_cards_main_2.setMaximumSize(QSize(16777215, 16777215))
        self.show_cards_main_2.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/menu/menu/dashc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.show_cards_main_2.setIcon(icon13)
        self.show_cards_main_2.setIconSize(QSize(40, 40))

        self.verticalLayout_36.addWidget(self.show_cards_main_2)

        self.pushButton_24 = QPushButton(self.frame_43)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setMinimumSize(QSize(40, 53))
        self.pushButton_24.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_24.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons-cards/src-page-cartoes/credit-debit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_24.setIcon(icon14)
        self.pushButton_24.setIconSize(QSize(40, 40))

        self.verticalLayout_36.addWidget(self.pushButton_24)


        self.horizontalLayout_65.addWidget(self.frame_43)

        self.welcome_2 = QFrame(self.main_dasht_top_2)
        self.welcome_2.setObjectName(u"welcome_2")
        self.welcome_2.setMinimumSize(QSize(200, 200))
        self.welcome_2.setMaximumSize(QSize(200, 200))
        self.welcome_2.setStyleSheet(u"\n"
"border-image:none;\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")
        self.welcome_2.setFrameShape(QFrame.NoFrame)
        self.welcome_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.welcome_2)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_44 = QFrame(self.welcome_2)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setMinimumSize(QSize(0, 60))
        self.frame_44.setStyleSheet(u"background-color:none;\n"
"border:none;")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_22 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_22)

        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(60, 0))
        self.frame_45.setStyleSheet(u"background-image: url(:/time/menu/night.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_52.addWidget(self.frame_45)

        self.horizontalSpacer_23 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_23)


        self.verticalLayout_37.addWidget(self.frame_44)

        self.label_41 = QLabel(self.welcome_2)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border:none;")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_41)

        self.label_42 = QLabel(self.welcome_2)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border:none;")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.verticalLayout_37.addWidget(self.label_42)


        self.horizontalLayout_65.addWidget(self.welcome_2)

        self.frame_51 = QFrame(self.main_dasht_top_2)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(400, 200))
        self.frame_51.setStyleSheet(u"border:1px solid rgba(255,255,255,40);\n"
"border-image:none;\n"
"background-color: rgba(255, 255, 255, 30); ")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Plain)
        self.frame_51.setLineWidth(1)
        self.frame_51.setMidLineWidth(0)
        self.frame_97 = QFrame(self.frame_51)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setGeometry(QRect(10, 10, 51, 51))
        self.frame_97.setMinimumSize(QSize(40, 0))
        self.frame_97.setStyleSheet(u"border-image: url(:/menu/c6.jpg);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.label_68 = QLabel(self.frame_51)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(150, 10, 182, 55))
        self.label_68.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"font-size:12pt;\n"
"border:none;")
        self.label_68.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_69 = QLabel(self.frame_51)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(10, 80, 141, 41))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Light Condensed")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(3)
        self.label_69.setFont(font1)
        self.label_69.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"font-size:12pt;\n"
"border:none;")
        self.label_69.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_70 = QLabel(self.frame_51)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(10, 120, 201, 71))
        self.label_70.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"font-size:20pt;\n"
"border:none;")
        self.label_70.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_65.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.main_dasht_top_2)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(38, 100))
        self.frame_52.setMaximumSize(QSize(16777215, 16777215))
        self.frame_52.setStyleSheet(u"border:none;\n"
"border-image:none;")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_120 = QVBoxLayout(self.frame_52)
        self.verticalLayout_120.setSpacing(0)
        self.verticalLayout_120.setObjectName(u"verticalLayout_120")
        self.verticalLayout_120.setContentsMargins(0, 0, 0, 0)
        self.date_gui_5 = QFrame(self.frame_52)
        self.date_gui_5.setObjectName(u"date_gui_5")
        self.date_gui_5.setMinimumSize(QSize(0, 20))
        self.date_gui_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")
        self.date_gui_5.setFrameShape(QFrame.StyledPanel)
        self.date_gui_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.date_gui_5)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_75 = QLabel(self.date_gui_5)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"border:none;")

        self.verticalLayout_47.addWidget(self.label_75)

        self.progressBar_2 = QProgressBar(self.date_gui_5)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setMaximumSize(QSize(16777215, 30))
        self.progressBar_2.setStyleSheet(u"QProgressBar\n"
"{\n"
"    background: green;\n"
"    color: black;\n"
"    border-style: outset;\n"
"	border:none;\n"
"\n"
"    border-radius: 7px;\n"
"\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"   		\n"
"	background-color: rgb(92, 155, 179);\n"
"	border-top-left-radius:7px;\n"
"	 border-bottom-left-radius:7px;\n"
"\n"
"}")
        self.progressBar_2.setValue(24)
        self.progressBar_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.progressBar_2)


        self.verticalLayout_120.addWidget(self.date_gui_5)

        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMaximumSize(QSize(1000, 16777215))
        self.frame_53.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_53)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_54 = QFrame(self.frame_53)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(0, 0))
        self.frame_54.setStyleSheet(u"")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_54)
        self.horizontalLayout_69.setSpacing(10)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 10, 0, 0)
        self.labelTitle_14 = QLabel(self.frame_54)
        self.labelTitle_14.setObjectName(u"labelTitle_14")
        self.labelTitle_14.setFont(font)
        self.labelTitle_14.setLayoutDirection(Qt.LeftToRight)
        self.labelTitle_14.setAutoFillBackground(False)
        self.labelTitle_14.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")
        self.labelTitle_14.setFrameShape(QFrame.NoFrame)
        self.labelTitle_14.setFrameShadow(QFrame.Plain)
        self.labelTitle_14.setScaledContents(False)
        self.labelTitle_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.labelTitle_14)

        self.label_43 = QLabel(self.frame_54)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")

        self.horizontalLayout_69.addWidget(self.label_43)

        self.labelTitle_15 = QLabel(self.frame_54)
        self.labelTitle_15.setObjectName(u"labelTitle_15")
        self.labelTitle_15.setFont(font)
        self.labelTitle_15.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")
        self.labelTitle_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.labelTitle_15)


        self.verticalLayout_55.addWidget(self.frame_54)


        self.verticalLayout_120.addWidget(self.frame_53)


        self.horizontalLayout_65.addWidget(self.frame_52)


        self.verticalLayout_108.addWidget(self.main_dasht_top_2)

        self.main_dash_midle_2 = QFrame(self.scrollAreaWidgetContents_9)
        self.main_dash_midle_2.setObjectName(u"main_dash_midle_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_dash_midle_2.sizePolicy().hasHeightForWidth())
        self.main_dash_midle_2.setSizePolicy(sizePolicy)
        self.main_dash_midle_2.setMinimumSize(QSize(0, 0))
        self.main_dash_midle_2.setMaximumSize(QSize(16777215, 10))
        self.main_dash_midle_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"\n"
"border-bottom: 0px;\n"
"border: 0px;")
        self.main_dash_midle_2.setFrameShape(QFrame.StyledPanel)
        self.main_dash_midle_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_124 = QVBoxLayout(self.main_dash_midle_2)
        self.verticalLayout_124.setSpacing(0)
        self.verticalLayout_124.setObjectName(u"verticalLayout_124")
        self.verticalLayout_124.setContentsMargins(10, 10, 10, 10)
        self.date_filters_fatura_5 = QFrame(self.main_dash_midle_2)
        self.date_filters_fatura_5.setObjectName(u"date_filters_fatura_5")
        self.date_filters_fatura_5.setMaximumSize(QSize(16777215, 50))
        self.date_filters_fatura_5.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px;\n"
"border-right: 0px;")
        self.date_filters_fatura_5.setFrameShape(QFrame.StyledPanel)
        self.date_filters_fatura_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.date_filters_fatura_5)
        self.horizontalLayout_71.setSpacing(0)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(30, 0, 30, 0)

        self.verticalLayout_124.addWidget(self.date_filters_fatura_5)

        self.datails_fatura_card_5 = QFrame(self.main_dash_midle_2)
        self.datails_fatura_card_5.setObjectName(u"datails_fatura_card_5")
        self.datails_fatura_card_5.setMaximumSize(QSize(16777215, 80))
        self.datails_fatura_card_5.setStyleSheet(u"border-radius:5px;\n"
" border-bottom-right-radius:0px;\n"
" border-bottom-left-radius:0px;\n"
"\n"
"background-color: rgba(255, 255, 255, 30); ")
        self.datails_fatura_card_5.setFrameShape(QFrame.StyledPanel)
        self.datails_fatura_card_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.datails_fatura_card_5)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.icon_5 = QFrame(self.datails_fatura_card_5)
        self.icon_5.setObjectName(u"icon_5")
        self.icon_5.setMaximumSize(QSize(48, 48))
        self.icon_5.setStyleSheet(u"border-bottom: 0px;\n"
"border-radius: 5px;\n"
"border-image: url();")
        self.icon_5.setFrameShape(QFrame.StyledPanel)
        self.icon_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_72.addWidget(self.icon_5)

        self.name_bank_5 = QLabel(self.datails_fatura_card_5)
        self.name_bank_5.setObjectName(u"name_bank_5")
        self.name_bank_5.setLayoutDirection(Qt.LeftToRight)
        self.name_bank_5.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"background-color: none; \n"
"color:rgb(255, 255, 255);\n"
"")
        self.name_bank_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.name_bank_5)

        self.set_limite_card_5 = QFrame(self.datails_fatura_card_5)
        self.set_limite_card_5.setObjectName(u"set_limite_card_5")
        self.set_limite_card_5.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 1px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"color:rgb(255, 255, 255);\n"
"background-color: none; \n"
"")
        self.set_limite_card_5.setFrameShape(QFrame.StyledPanel)
        self.set_limite_card_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_130 = QVBoxLayout(self.set_limite_card_5)
        self.verticalLayout_130.setObjectName(u"verticalLayout_130")
        self.label_51 = QLabel(self.set_limite_card_5)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font)
        self.label_51.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"\n"
"border-radius:3px;")
        self.label_51.setAlignment(Qt.AlignCenter)

        self.verticalLayout_130.addWidget(self.label_51)

        self.label_52 = QLabel(self.set_limite_card_5)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font)
        self.label_52.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"\n"
"border-radius:3px;")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.verticalLayout_130.addWidget(self.label_52)


        self.horizontalLayout_72.addWidget(self.set_limite_card_5)

        self.set_fechamento_5 = QFrame(self.datails_fatura_card_5)
        self.set_fechamento_5.setObjectName(u"set_fechamento_5")
        self.set_fechamento_5.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 1px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"color:rgb(255, 255, 255);\n"
"background-color: none; \n"
"")
        self.set_fechamento_5.setFrameShape(QFrame.StyledPanel)
        self.set_fechamento_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_137 = QVBoxLayout(self.set_fechamento_5)
        self.verticalLayout_137.setObjectName(u"verticalLayout_137")
        self.label_57 = QLabel(self.set_fechamento_5)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font)
        self.label_57.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"border-radius:3px;")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.verticalLayout_137.addWidget(self.label_57)

        self.label_58 = QLabel(self.set_fechamento_5)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font)
        self.label_58.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"\n"
"border-radius:3px;")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.verticalLayout_137.addWidget(self.label_58)


        self.horizontalLayout_72.addWidget(self.set_fechamento_5)

        self.set_vencimento_5 = QFrame(self.datails_fatura_card_5)
        self.set_vencimento_5.setObjectName(u"set_vencimento_5")
        self.set_vencimento_5.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 0px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"color:rgb(255, 255, 255);\n"
"background-color: none; \n"
"")
        self.set_vencimento_5.setFrameShape(QFrame.StyledPanel)
        self.set_vencimento_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_138 = QVBoxLayout(self.set_vencimento_5)
        self.verticalLayout_138.setObjectName(u"verticalLayout_138")
        self.label_59 = QLabel(self.set_vencimento_5)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font)
        self.label_59.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"border-radius:3px;")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.verticalLayout_138.addWidget(self.label_59)

        self.label_60 = QLabel(self.set_vencimento_5)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font)
        self.label_60.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"\n"
"border-radius:3px;")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.verticalLayout_138.addWidget(self.label_60)


        self.horizontalLayout_72.addWidget(self.set_vencimento_5)


        self.verticalLayout_124.addWidget(self.datails_fatura_card_5)

        self.datalhed_fatura_mother_5 = QFrame(self.main_dash_midle_2)
        self.datalhed_fatura_mother_5.setObjectName(u"datalhed_fatura_mother_5")
        self.datalhed_fatura_mother_5.setStyleSheet(u"border-bottom: 0px;\n"
"border-right: 0px;\n"
"")
        self.datalhed_fatura_mother_5.setFrameShape(QFrame.StyledPanel)
        self.datalhed_fatura_mother_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_139 = QVBoxLayout(self.datalhed_fatura_mother_5)
        self.verticalLayout_139.setSpacing(0)
        self.verticalLayout_139.setObjectName(u"verticalLayout_139")
        self.verticalLayout_139.setContentsMargins(0, 0, 0, 0)
        self.table_faturas_ind_4 = QTableWidget(self.datalhed_fatura_mother_5)
        if (self.table_faturas_ind_4.columnCount() < 4):
            self.table_faturas_ind_4.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind_4.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind_4.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind_4.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind_4.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_faturas_ind_4.setObjectName(u"table_faturas_ind_4")
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light Condensed")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(3)
        self.table_faturas_ind_4.setFont(font2)
        self.table_faturas_ind_4.setStyleSheet(u"QWidget {\n"
"	\n"
"    color: #fffff8;\n"
"	border-radius:0px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(53, 53, 53);\n"
"    font-size: 11;\n"
"	border:none;\n"
"	width:45px;\n"
"	height: 50px;\n"
"\n"
"	border-radius:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #fffff8;\n"
"    font-size: 11pt;\n"
"	border-radius:0px;\n"
"	border-radius:0px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"	border-radius:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableView:item {\n"
"  border-bottom: 0.5px solid qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:0.45677 rgba(0, 0, 0, 0), stop:0.479846 rgba(255, 255, 255, 255), stop:0.50571 rgba(239, 236, 55, 0), stop:1 rgba(239, 236, 55, 0));\n"
"	border-radius:0px;\n"
"\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	\n"
"	background-color: rgb(92, 155, 179);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.table_faturas_ind_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_faturas_ind_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_faturas_ind_4.setAlternatingRowColors(False)
        self.table_faturas_ind_4.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_faturas_ind_4.setIconSize(QSize(45, 40))
        self.table_faturas_ind_4.setTextElideMode(Qt.ElideLeft)
        self.table_faturas_ind_4.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_faturas_ind_4.setShowGrid(False)
        self.table_faturas_ind_4.setSortingEnabled(False)
        self.table_faturas_ind_4.horizontalHeader().setVisible(False)
        self.table_faturas_ind_4.horizontalHeader().setCascadingSectionResizes(True)
        self.table_faturas_ind_4.horizontalHeader().setDefaultSectionSize(230)
        self.table_faturas_ind_4.horizontalHeader().setHighlightSections(True)
        self.table_faturas_ind_4.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_faturas_ind_4.horizontalHeader().setStretchLastSection(True)
        self.table_faturas_ind_4.verticalHeader().setVisible(False)
        self.table_faturas_ind_4.verticalHeader().setCascadingSectionResizes(False)
        self.table_faturas_ind_4.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_139.addWidget(self.table_faturas_ind_4)


        self.verticalLayout_124.addWidget(self.datalhed_fatura_mother_5)


        self.verticalLayout_108.addWidget(self.main_dash_midle_2)

        self.extrat_meses_2 = QStackedWidget(self.scrollAreaWidgetContents_9)
        self.extrat_meses_2.setObjectName(u"extrat_meses_2")
        self.extrat_meses_2.setMaximumSize(QSize(16777215, 60))
        self.extrat_meses_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"border-radius:7px;\n"
"")
        self.extrat_meses_2.setFrameShape(QFrame.StyledPanel)
        self.extrat_meses_2.setFrameShadow(QFrame.Raised)
        self.extrat_mesesPage1_2 = QWidget()
        self.extrat_mesesPage1_2.setObjectName(u"extrat_mesesPage1_2")
        self.extrat_mesesPage1_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.verticalLayout_35 = QVBoxLayout(self.extrat_mesesPage1_2)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(10, 0, 10, 0)
        self.filter_dt_container_2 = QFrame(self.extrat_mesesPage1_2)
        self.filter_dt_container_2.setObjectName(u"filter_dt_container_2")
        self.filter_dt_container_2.setMinimumSize(QSize(0, 50))
        self.filter_dt_container_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.filter_dt_container_2.setFrameShape(QFrame.StyledPanel)
        self.filter_dt_container_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.filter_dt_container_2)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.frame_D_2 = QFrame(self.filter_dt_container_2)
        self.frame_D_2.setObjectName(u"frame_D_2")
        self.frame_D_2.setMinimumSize(QSize(0, 0))
        self.frame_D_2.setMaximumSize(QSize(60, 16777215))
        self.frame_D_2.setStyleSheet(u"	border: 1px solid rgb(253, 253, 253);\n"
"	border-radius: 10px;\n"
"background-color: rgba(0, 0, 0,0);")
        self.frame_D_2.setFrameShape(QFrame.StyledPanel)
        self.frame_D_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_103 = QVBoxLayout(self.frame_D_2)
        self.verticalLayout_103.setSpacing(0)
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.verticalLayout_103.setContentsMargins(0, 0, 0, 0)
        self.line_d_2 = QLineEdit(self.frame_D_2)
        self.line_d_2.setObjectName(u"line_d_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_d_2.sizePolicy().hasHeightForWidth())
        self.line_d_2.setSizePolicy(sizePolicy1)
        self.line_d_2.setMaximumSize(QSize(16777215, 90))
        self.line_d_2.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"background-color: rgba(255, 255, 255, 30);")
        self.line_d_2.setMaxLength(2)
        self.line_d_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_103.addWidget(self.line_d_2)


        self.horizontalLayout_59.addWidget(self.frame_D_2)

        self.frame_M_2 = QFrame(self.filter_dt_container_2)
        self.frame_M_2.setObjectName(u"frame_M_2")
        self.frame_M_2.setMinimumSize(QSize(0, 0))
        self.frame_M_2.setMaximumSize(QSize(60, 16777215))
        self.frame_M_2.setStyleSheet(u"	border: 1px solid rgb(253, 253, 253);\n"
"	border-radius: 10px;\n"
"background-color: rgba(0, 0, 0,0);")
        self.frame_M_2.setFrameShape(QFrame.StyledPanel)
        self.frame_M_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_M_2)
        self.verticalLayout_104.setSpacing(0)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.line_m_2 = QLineEdit(self.frame_M_2)
        self.line_m_2.setObjectName(u"line_m_2")
        sizePolicy1.setHeightForWidth(self.line_m_2.sizePolicy().hasHeightForWidth())
        self.line_m_2.setSizePolicy(sizePolicy1)
        self.line_m_2.setMaximumSize(QSize(16777215, 90))
        self.line_m_2.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"background-color: rgba(255, 255, 255, 30);")
        self.line_m_2.setMaxLength(2)
        self.line_m_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_104.addWidget(self.line_m_2)


        self.horizontalLayout_59.addWidget(self.frame_M_2)

        self.frame_A_2 = QFrame(self.filter_dt_container_2)
        self.frame_A_2.setObjectName(u"frame_A_2")
        self.frame_A_2.setMinimumSize(QSize(0, 0))
        self.frame_A_2.setMaximumSize(QSize(80, 16777215))
        self.frame_A_2.setStyleSheet(u"	border: 1px solid rgb(253, 253, 253);\n"
"	border-radius: 10px;\n"
"background-color: rgba(0, 0, 0,0);")
        self.frame_A_2.setFrameShape(QFrame.StyledPanel)
        self.frame_A_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_107 = QVBoxLayout(self.frame_A_2)
        self.verticalLayout_107.setSpacing(0)
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.verticalLayout_107.setContentsMargins(0, 0, 0, 0)
        self.line_y_2 = QLineEdit(self.frame_A_2)
        self.line_y_2.setObjectName(u"line_y_2")
        sizePolicy1.setHeightForWidth(self.line_y_2.sizePolicy().hasHeightForWidth())
        self.line_y_2.setSizePolicy(sizePolicy1)
        self.line_y_2.setMaximumSize(QSize(16777215, 90))
        self.line_y_2.setLayoutDirection(Qt.LeftToRight)
        self.line_y_2.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;\n"
"background-color: rgba(255, 255, 255, 30);")
        self.line_y_2.setMaxLength(4)
        self.line_y_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_107.addWidget(self.line_y_2)


        self.horizontalLayout_59.addWidget(self.frame_A_2)

        self.pushButton_27 = QPushButton(self.filter_dt_container_2)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMaximumSize(QSize(16777215, 90))
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet(u"\n"
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
        icon15 = QIcon()
        icon15.addFile(u":/backgroud/src-page-cartoes/lup.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_27.setIcon(icon15)
        self.pushButton_27.setIconSize(QSize(30, 30))

        self.horizontalLayout_59.addWidget(self.pushButton_27)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_21)

        self.pushButton_28 = QPushButton(self.filter_dt_container_2)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(80, 0))
        self.pushButton_28.setMaximumSize(QSize(16777214, 90))
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet(u"\n"
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
        icon16 = QIcon()
        icon16.addFile(u":/backgroud/src-page-cartoes/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_28.setIcon(icon16)
        self.pushButton_28.setIconSize(QSize(16, 16))

        self.horizontalLayout_59.addWidget(self.pushButton_28)


        self.verticalLayout_35.addWidget(self.filter_dt_container_2)

        self.extrat_meses_2.addWidget(self.extrat_mesesPage1_2)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.horizontalLayout_108 = QHBoxLayout(self.page_11)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_108.addItem(self.horizontalSpacer_27)

        self.previus_month_2 = QPushButton(self.page_11)
        self.previus_month_2.setObjectName(u"previus_month_2")
        self.previus_month_2.setMinimumSize(QSize(80, 0))
        self.previus_month_2.setMaximumSize(QSize(120, 50))
        self.previus_month_2.setTabletTracking(False)
        self.previus_month_2.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border:none;\n"
"\n"
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
        self.previus_month_2.setIcon(icon12)
        self.previus_month_2.setIconSize(QSize(20, 20))

        self.horizontalLayout_108.addWidget(self.previus_month_2)

        self.label_67 = QLabel(self.page_11)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(80, 0))
        self.label_67.setMaximumSize(QSize(80, 16777215))
        self.label_67.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")

        self.horizontalLayout_108.addWidget(self.label_67)

        self.label_71 = QLabel(self.page_11)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"\n"
"background-color: rgba(255, 255, 255, 0); ")

        self.horizontalLayout_108.addWidget(self.label_71)

        self.label_72 = QLabel(self.page_11)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")

        self.horizontalLayout_108.addWidget(self.label_72)

        self.next_month_2 = QPushButton(self.page_11)
        self.next_month_2.setObjectName(u"next_month_2")
        self.next_month_2.setMinimumSize(QSize(80, 0))
        self.next_month_2.setMaximumSize(QSize(120, 50))
        self.next_month_2.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border:none;\n"
"\n"
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
        self.next_month_2.setIcon(icon16)

        self.horizontalLayout_108.addWidget(self.next_month_2)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_108.addItem(self.horizontalSpacer_28)

        self.extrat_meses_2.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.horizontalLayout_109 = QHBoxLayout(self.page_12)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.previus_month_4 = QPushButton(self.page_12)
        self.previus_month_4.setObjectName(u"previus_month_4")
        self.previus_month_4.setMinimumSize(QSize(80, 0))
        self.previus_month_4.setMaximumSize(QSize(120, 50))
        self.previus_month_4.setTabletTracking(False)
        self.previus_month_4.setStyleSheet(u"\n"
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
        self.previus_month_4.setIcon(icon12)
        self.previus_month_4.setIconSize(QSize(20, 20))

        self.horizontalLayout_109.addWidget(self.previus_month_4)

        self.horizontalSpacer_29 = QSpacerItem(339, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_109.addItem(self.horizontalSpacer_29)

        self.label_73 = QLabel(self.page_12)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")

        self.horizontalLayout_109.addWidget(self.label_73)

        self.label_74 = QLabel(self.page_12)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0); ")

        self.horizontalLayout_109.addWidget(self.label_74)

        self.horizontalSpacer_30 = QSpacerItem(338, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_109.addItem(self.horizontalSpacer_30)

        self.next_month_4 = QPushButton(self.page_12)
        self.next_month_4.setObjectName(u"next_month_4")
        self.next_month_4.setMinimumSize(QSize(80, 0))
        self.next_month_4.setMaximumSize(QSize(120, 50))
        self.next_month_4.setStyleSheet(u"\n"
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
        self.next_month_4.setIcon(icon16)

        self.horizontalLayout_109.addWidget(self.next_month_4)

        self.extrat_meses_2.addWidget(self.page_12)

        self.verticalLayout_108.addWidget(self.extrat_meses_2)

        self.main_dash_bottom_2 = QFrame(self.scrollAreaWidgetContents_9)
        self.main_dash_bottom_2.setObjectName(u"main_dash_bottom_2")
        self.main_dash_bottom_2.setMinimumSize(QSize(0, 0))
        self.main_dash_bottom_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.main_dash_bottom_2.setFrameShape(QFrame.StyledPanel)
        self.main_dash_bottom_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.main_dash_bottom_2)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.chart_gastos_all_2 = QTabWidget(self.main_dash_bottom_2)
        self.chart_gastos_all_2.setObjectName(u"chart_gastos_all_2")
        self.chart_gastos_all_2.setMinimumSize(QSize(0, 650))
        self.chart_gastos_all_2.setMaximumSize(QSize(16777215, 16777215))
        self.chart_gastos_all_2.setFont(font)
        self.chart_gastos_all_2.setLayoutDirection(Qt.LeftToRight)
        self.chart_gastos_all_2.setStyleSheet(u"\n"
"\n"
"QTabWidget::tab-bar {\n"
"  background: rgba(255,255,255,0);\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"  background: rgb(46, 46, 46);\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 10px;\n"
"\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background:rgb(53, 53, 53);\n"
"  color: rgb(255, 255, 255);\n"
" }\n"
"\n"
"QTabWidget::pane { border-top-left-radius:0px; border-top-right-radius:0px;}\n"
"\n"
"")
        self.chart_gastos_all_2.setTabPosition(QTabWidget.North)
        self.chart_gastos_all_2.setTabShape(QTabWidget.Rounded)
        self.chart_gastos_all_2.setElideMode(Qt.ElideMiddle)
        self.chart_gastos_all_2.setDocumentMode(False)
        self.chart_gastos_all_2.setTabsClosable(False)
        self.chart_gastos_all_2.setMovable(True)
        self.chart_gastos_all_2.setTabBarAutoHide(True)
        self.page_Tabe_main1 = QWidget()
        self.page_Tabe_main1.setObjectName(u"page_Tabe_main1")
        self.page_Tabe_main1.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.verticalLayout_140 = QVBoxLayout(self.page_Tabe_main1)
        self.verticalLayout_140.setSpacing(0)
        self.verticalLayout_140.setObjectName(u"verticalLayout_140")
        self.verticalLayout_140.setContentsMargins(0, 0, 10, 0)
        self.chart_main_evolution_4 = QFrame(self.page_Tabe_main1)
        self.chart_main_evolution_4.setObjectName(u"chart_main_evolution_4")
        self.chart_main_evolution_4.setStyleSheet(u"")
        self.chart_main_evolution_4.setFrameShape(QFrame.StyledPanel)
        self.chart_main_evolution_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_141 = QVBoxLayout(self.chart_main_evolution_4)
        self.verticalLayout_141.setSpacing(0)
        self.verticalLayout_141.setObjectName(u"verticalLayout_141")
        self.verticalLayout_141.setContentsMargins(0, 0, 0, 0)
        self.frame_55 = QFrame(self.chart_main_evolution_4)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setStyleSheet(u"")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_55)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setStyleSheet(u"border:none;\n"
"")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_56)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_7 = QScrollArea(self.frame_56)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setMinimumSize(QSize(0, 0))
        self.scrollArea_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 1435, 607))
        self.scrollAreaWidgetContents_7.setStyleSheet(u"")
        self.verticalLayout_61 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_93 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setMinimumSize(QSize(0, 0))
        self.frame_93.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); ")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_93)
        self.verticalLayout_92.setSpacing(0)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.frame_93)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMaximumSize(QSize(16777215, 16777215))
        self.frame_57.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_57)
        self.verticalLayout_62.setSpacing(0)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.stacked_configcartao0_2 = QStackedWidget(self.frame_57)
        self.stacked_configcartao0_2.setObjectName(u"stacked_configcartao0_2")
        self.stacked_configcartao0_2.setMinimumSize(QSize(0, 90))
        self.stacked_configcartao0_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"")
        self.stacked_configcartao0_2.setFrameShape(QFrame.StyledPanel)
        self.stacked_configcartao0_2.setFrameShadow(QFrame.Raised)
        self.table_extrato_main_1 = QWidget()
        self.table_extrato_main_1.setObjectName(u"table_extrato_main_1")
        self.horizontalLayout_53 = QHBoxLayout(self.table_extrato_main_1)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.stack_extrato_pages_2 = QStackedWidget(self.table_extrato_main_1)
        self.stack_extrato_pages_2.setObjectName(u"stack_extrato_pages_2")
        self.stack_extrato_pages_2.setMinimumSize(QSize(0, 0))
        self.stack_extrato_pages_2.setMaximumSize(QSize(16777215, 16777215))
        self.stack_extrato_pages_2.setFrameShape(QFrame.StyledPanel)
        self.stack_extrato_pages_2.setFrameShadow(QFrame.Raised)
        self.extrato_cards_dbs_2 = QWidget()
        self.extrato_cards_dbs_2.setObjectName(u"extrato_cards_dbs_2")
        self.horizontalLayout_54 = QHBoxLayout(self.extrato_cards_dbs_2)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.extrato_cards_dbs_2)
        if (self.tableWidget.columnCount() < 12):
            self.tableWidget.setColumnCount(12)
        icon17 = QIcon()
        icon17.addFile(u":/main_menutable/main_page_tables/unchecked.png", QSize(), QIcon.Normal, QIcon.Off)
        font3 = QFont()
        font3.setStyleStrategy(QFont.PreferAntialias)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font3);
        __qtablewidgetitem4.setIcon(icon17);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        font4 = QFont()
        font4.setFamily(u"Yu Gothic")
        font4.setPointSize(12)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        icon18 = QIcon()
        icon18.addFile(u":/main_menutable/main_page_tables/decrecente.png", QSize(), QIcon.Normal, QIcon.Off)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font4);
        __qtablewidgetitem9.setIcon(icon18);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font4);
        __qtablewidgetitem10.setIcon(icon18);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font4);
        __qtablewidgetitem11.setIcon(icon18);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font4);
        __qtablewidgetitem12.setIcon(icon18);
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font4);
        __qtablewidgetitem13.setIcon(icon18);
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font4);
        __qtablewidgetitem14.setIcon(icon18);
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font4);
        __qtablewidgetitem15.setIcon(icon18);
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem15)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"QWidget {\n"
"	\n"
"    color: #fffff8;\n"
"	border-radius:0px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(53, 53, 53);\n"
"	border:none;\n"
"	width:45px;\n"
"	height: 50px;\n"
"	margin-left:1px;\n"
"\n"
"	border-radius:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #fffff8;\n"
"\n"
"	border-radius:0px;\n"
"	border-radius:0px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"	border-radius:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableView:item {\n"
"  border-bottom: 0.5px solid qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:0.45677 rgba(0, 0, 0, 0), stop:0.479846 rgba(255, 255, 255, 255), stop:0.50571 rgba(239, 236, 55, 0), stop:1 rgba(239, 236, 55, 0));\n"
"	border-radius:0px;\n"
"\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	\n"
"	border:1px solid rgb(92, 155, 179);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setIconSize(QSize(40, 40))
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(114)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.horizontalLayout_54.addWidget(self.tableWidget)

        self.stack_extrato_pages_2.addWidget(self.extrato_cards_dbs_2)
        self.page_not_found_2 = QWidget()
        self.page_not_found_2.setObjectName(u"page_not_found_2")
        self.verticalLayout_63 = QVBoxLayout(self.page_not_found_2)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacer_10)

        self.image_notfoud_2 = QFrame(self.page_not_found_2)
        self.image_notfoud_2.setObjectName(u"image_notfoud_2")
        self.image_notfoud_2.setMinimumSize(QSize(0, 300))
        self.image_notfoud_2.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/not-found.png);\n"
"background-position: center;\n"
"background-repeat:no-repeat;\n"
"")
        self.image_notfoud_2.setFrameShape(QFrame.StyledPanel)
        self.image_notfoud_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_63.addWidget(self.image_notfoud_2)

        self.frame_page_not_found_2 = QFrame(self.page_not_found_2)
        self.frame_page_not_found_2.setObjectName(u"frame_page_not_found_2")
        self.frame_page_not_found_2.setFrameShape(QFrame.StyledPanel)
        self.frame_page_not_found_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_page_not_found_2)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.text_page_notfound_2 = QLabel(self.frame_page_not_found_2)
        self.text_page_notfound_2.setObjectName(u"text_page_notfound_2")
        self.text_page_notfound_2.setMaximumSize(QSize(16777215, 20))
        self.text_page_notfound_2.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.text_page_notfound_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_64.addWidget(self.text_page_notfound_2)

        self.verticalSpacer_11 = QSpacerItem(20, 120, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_64.addItem(self.verticalSpacer_11)


        self.verticalLayout_63.addWidget(self.frame_page_not_found_2)

        self.stack_extrato_pages_2.addWidget(self.page_not_found_2)
        self.page_emdia_2 = QWidget()
        self.page_emdia_2.setObjectName(u"page_emdia_2")
        self.verticalLayout_65 = QVBoxLayout(self.page_emdia_2)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer_12)

        self.image_emdia_2 = QFrame(self.page_emdia_2)
        self.image_emdia_2.setObjectName(u"image_emdia_2")
        self.image_emdia_2.setMinimumSize(QSize(0, 300))
        self.image_emdia_2.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/payout.png);\n"
"background-position: center;\n"
"background-repeat:no-repeat;\n"
"")
        self.image_emdia_2.setFrameShape(QFrame.StyledPanel)
        self.image_emdia_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_65.addWidget(self.image_emdia_2)

        self.txt_pag_emdia_2 = QLabel(self.page_emdia_2)
        self.txt_pag_emdia_2.setObjectName(u"txt_pag_emdia_2")
        self.txt_pag_emdia_2.setStyleSheet(u"border: 0px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")
        self.txt_pag_emdia_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_65.addWidget(self.txt_pag_emdia_2)

        self.verticalSpacer_13 = QSpacerItem(20, 95, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_65.addItem(self.verticalSpacer_13)

        self.stack_extrato_pages_2.addWidget(self.page_emdia_2)

        self.horizontalLayout_53.addWidget(self.stack_extrato_pages_2)

        self.main_menu_extrato_page = QFrame(self.table_extrato_main_1)
        self.main_menu_extrato_page.setObjectName(u"main_menu_extrato_page")
        self.main_menu_extrato_page.setMinimumSize(QSize(0, 0))
        self.main_menu_extrato_page.setMaximumSize(QSize(400, 16777215))
        self.main_menu_extrato_page.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.main_menu_extrato_page.setFrameShape(QFrame.StyledPanel)
        self.main_menu_extrato_page.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.main_menu_extrato_page)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.frame_58 = QFrame(self.main_menu_extrato_page)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setStyleSheet(u"border-radius: 0px;\n"
"\n"
"	\n"
"\n"
"background-color: rgba(255, 255, 255,30);\n"
"\n"
"")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_58)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.scrollArea_10 = QScrollArea(self.frame_58)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea_10.sizePolicy().hasHeightForWidth())
        self.scrollArea_10.setSizePolicy(sizePolicy2)
        self.scrollArea_10.setFont(font)
        self.scrollArea_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border:0px;\n"
"background-color: rgba(255, 255, 255,0);")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 269, 657))
        self.verticalLayout_93 = QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.label_44 = QLabel(self.scrollAreaWidgetContents_10)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font)
        self.label_44.setStyleSheet(u"border:0px;\n"
"")

        self.verticalLayout_93.addWidget(self.label_44)

        self.textEdit = QTextEdit(self.scrollAreaWidgetContents_10)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 100))
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"border-radius:7px;")
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.verticalLayout_93.addWidget(self.textEdit)

        self.label_if_card = QLabel(self.scrollAreaWidgetContents_10)
        self.label_if_card.setObjectName(u"label_if_card")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_if_card.sizePolicy().hasHeightForWidth())
        self.label_if_card.setSizePolicy(sizePolicy3)
        self.label_if_card.setMaximumSize(QSize(16777215, 16777215))
        self.label_if_card.setFont(font)
        self.label_if_card.setStyleSheet(u"border:0px;\n"
"")

        self.verticalLayout_93.addWidget(self.label_if_card)

        self.verticalSpacer_3 = QSpacerItem(20, 247, QSizePolicy.Minimum, QSizePolicy.Ignored)

        self.verticalLayout_93.addItem(self.verticalSpacer_3)

        self.frame_if_card_main = QFrame(self.scrollAreaWidgetContents_10)
        self.frame_if_card_main.setObjectName(u"frame_if_card_main")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_if_card_main.sizePolicy().hasHeightForWidth())
        self.frame_if_card_main.setSizePolicy(sizePolicy4)
        self.frame_if_card_main.setMaximumSize(QSize(16777215, 16777215))
        self.frame_if_card_main.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"border-radius:7px;")
        self.frame_if_card_main.setFrameShape(QFrame.StyledPanel)
        self.frame_if_card_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_if_card_main)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.lauy_3 = QHBoxLayout()
        self.lauy_3.setObjectName(u"lauy_3")
        self.frame_59 = QFrame(self.frame_if_card_main)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMaximumSize(QSize(157, 16777215))
        self.frame_59.setStyleSheet(u"border: none;\n"
"border-radius:0px;")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_59)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.label_45 = QLabel(self.frame_59)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font)
        self.label_45.setAlignment(Qt.AlignCenter)

        self.verticalLayout_94.addWidget(self.label_45)

        self.btn_if_card_2 = QPushButton(self.frame_59)
        self.btn_if_card_2.setObjectName(u"btn_if_card_2")
        self.btn_if_card_2.setMinimumSize(QSize(0, 26))
        self.btn_if_card_2.setFont(font)
        self.btn_if_card_2.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"background-color:rgba(255,255,255,10);\n"
"\n"
"border: 1px solid rgba(255,255,255,20);\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"}")

        self.verticalLayout_94.addWidget(self.btn_if_card_2)


        self.lauy_3.addWidget(self.frame_59)

        self.icon_if_card = QFrame(self.frame_if_card_main)
        self.icon_if_card.setObjectName(u"icon_if_card")
        self.icon_if_card.setMinimumSize(QSize(40, 40))
        self.icon_if_card.setMaximumSize(QSize(40, 40))
        self.icon_if_card.setStyleSheet(u"background-color: rgb(255, 85, 255);\n"
"border-radius:20px;")
        self.icon_if_card.setFrameShape(QFrame.StyledPanel)
        self.icon_if_card.setFrameShadow(QFrame.Raised)

        self.lauy_3.addWidget(self.icon_if_card)


        self.horizontalLayout_55.addLayout(self.lauy_3)


        self.verticalLayout_93.addWidget(self.frame_if_card_main)

        self.frame_tools_nexo = QFrame(self.scrollAreaWidgetContents_10)
        self.frame_tools_nexo.setObjectName(u"frame_tools_nexo")
        self.frame_tools_nexo.setMinimumSize(QSize(0, 50))
        self.frame_tools_nexo.setFrameShape(QFrame.StyledPanel)
        self.frame_tools_nexo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_111 = QHBoxLayout(self.frame_tools_nexo)
        self.horizontalLayout_111.setSpacing(0)
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalLayout_111.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.frame_tools_nexo)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)

        self.horizontalLayout_111.addWidget(self.label_46)

        self.toolButton_pdf_opt = QToolButton(self.frame_tools_nexo)
        self.toolButton_pdf_opt.setObjectName(u"toolButton_pdf_opt")
        self.toolButton_pdf_opt.setPopupMode(QToolButton.InstantPopup)
        self.toolButton_pdf_opt.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.toolButton_pdf_opt.setAutoRaise(False)
        self.toolButton_pdf_opt.setArrowType(Qt.NoArrow)

        self.horizontalLayout_111.addWidget(self.toolButton_pdf_opt)


        self.verticalLayout_93.addWidget(self.frame_tools_nexo)

        self.listWidget_2 = QListWidget(self.scrollAreaWidgetContents_10)
        self.listWidget_2.setObjectName(u"listWidget_2")
        sizePolicy4.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy4)
        self.listWidget_2.setMinimumSize(QSize(0, 70))
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet(u"\n"
"\n"
"QListWidget{\n"
"border: 1px solid rgba(255,255,255,20);\n"
"border-radius:7px;\n"
"}\n"
"QScrollBar:horizontal { border: 1px solid #2A2929; background: #2A2929; height: 7px; margin: 0px 21px 0 21px; } QScrollBar::handle:horizontal { background: #646464; min-width: 5px; } \n"
"QScrollBar::add-line:horizontal { border: 1px solid #2A2929; background: #2A2929; width: 20px; subcontrol-position: right; subcontrol-origin: margin; } \n"
"QScrollBar::sub-line:horizontal { border: 1px solid #2A2929; background: #2A2929; width: 20px; subcontrol-position: left; subcontrol-origin: margin; }\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal { background: none; }")
        self.listWidget_2.setDragEnabled(True)
        self.listWidget_2.setDragDropOverwriteMode(False)
        self.listWidget_2.setDragDropMode(QAbstractItemView.DragOnly)
        self.listWidget_2.setDefaultDropAction(Qt.MoveAction)
        self.listWidget_2.setAlternatingRowColors(False)
        self.listWidget_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidget_2.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listWidget_2.setMovement(QListView.Free)
        self.listWidget_2.setFlow(QListView.TopToBottom)
        self.listWidget_2.setResizeMode(QListView.Fixed)
        self.listWidget_2.setLayoutMode(QListView.SinglePass)
        self.listWidget_2.setViewMode(QListView.ListMode)
        self.listWidget_2.setModelColumn(0)
        self.listWidget_2.setUniformItemSizes(False)
        self.listWidget_2.setSortingEnabled(False)

        self.verticalLayout_93.addWidget(self.listWidget_2)

        self.frame_options_pdf = QFrame(self.scrollAreaWidgetContents_10)
        self.frame_options_pdf.setObjectName(u"frame_options_pdf")
        self.frame_options_pdf.setMinimumSize(QSize(0, 50))
        self.frame_options_pdf.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border-radius:10px;")
        self.frame_options_pdf.setFrameShape(QFrame.StyledPanel)
        self.frame_options_pdf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_options_pdf)
        self.horizontalLayout_56.setSpacing(6)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.delet_pdf = QPushButton(self.frame_options_pdf)
        self.delet_pdf.setObjectName(u"delet_pdf")
        self.delet_pdf.setMinimumSize(QSize(0, 30))
        self.delet_pdf.setMaximumSize(QSize(113, 30))
        self.delet_pdf.setFont(font)
        self.delet_pdf.setLayoutDirection(Qt.LeftToRight)
        self.delet_pdf.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"background-color:rgba(255,255,255,10);\n"
"\n"
"border: 1px solid rgba(255,255,255,20);\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/icons-cards/src-page-cartoes/urgencia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delet_pdf.setIcon(icon19)

        self.horizontalLayout_56.addWidget(self.delet_pdf)

        self.download_pdf = QPushButton(self.frame_options_pdf)
        self.download_pdf.setObjectName(u"download_pdf")
        self.download_pdf.setMinimumSize(QSize(0, 30))
        self.download_pdf.setMaximumSize(QSize(113, 30))
        self.download_pdf.setFont(font)
        self.download_pdf.setLayoutDirection(Qt.LeftToRight)
        self.download_pdf.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"background-color:rgba(255,255,255,10);\n"
"\n"
"border: 1px solid rgba(255,255,255,20);\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"}")
        self.download_pdf.setIcon(icon19)

        self.horizontalLayout_56.addWidget(self.download_pdf)


        self.verticalLayout_93.addWidget(self.frame_options_pdf)

        self.paga_fatura_3 = QPushButton(self.scrollAreaWidgetContents_10)
        self.paga_fatura_3.setObjectName(u"paga_fatura_3")
        self.paga_fatura_3.setMinimumSize(QSize(0, 30))
        self.paga_fatura_3.setMaximumSize(QSize(16777215, 30))
        self.paga_fatura_3.setFont(font)
        self.paga_fatura_3.setLayoutDirection(Qt.LeftToRight)
        self.paga_fatura_3.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"background-color:rgba(255,255,255,10);\n"
"\n"
"border: 1px solid rgba(255,255,255,20);\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/icons-cards/src-page-cartoes/money.png", QSize(), QIcon.Normal, QIcon.Off)
        self.paga_fatura_3.setIcon(icon20)

        self.verticalLayout_93.addWidget(self.paga_fatura_3)

        self.edit_compra_3 = QPushButton(self.scrollAreaWidgetContents_10)
        self.edit_compra_3.setObjectName(u"edit_compra_3")
        self.edit_compra_3.setMinimumSize(QSize(0, 30))
        self.edit_compra_3.setMaximumSize(QSize(16777215, 30))
        self.edit_compra_3.setFont(font)
        self.edit_compra_3.setLayoutDirection(Qt.LeftToRight)
        self.edit_compra_3.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"background-color:rgba(255,255,255,10);\n"
"\n"
"border: 1px solid rgba(255,255,255,20);\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/icons-cards/src-page-cartoes/icons8-etiquetas-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_compra_3.setIcon(icon21)

        self.verticalLayout_93.addWidget(self.edit_compra_3)

        self.parcela_fatura_3 = QPushButton(self.scrollAreaWidgetContents_10)
        self.parcela_fatura_3.setObjectName(u"parcela_fatura_3")
        self.parcela_fatura_3.setMinimumSize(QSize(0, 30))
        self.parcela_fatura_3.setMaximumSize(QSize(16777215, 30))
        self.parcela_fatura_3.setFont(font)
        self.parcela_fatura_3.setLayoutDirection(Qt.LeftToRight)
        self.parcela_fatura_3.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"background-color:rgba(255,255,255,10);\n"
"\n"
"border: 1px solid rgba(255,255,255,20);\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u":/icons-cards/src-page-cartoes/parcelas.png", QSize(), QIcon.Normal, QIcon.Off)
        self.parcela_fatura_3.setIcon(icon22)

        self.verticalLayout_93.addWidget(self.parcela_fatura_3)

        self.apaga_compra_3 = QPushButton(self.scrollAreaWidgetContents_10)
        self.apaga_compra_3.setObjectName(u"apaga_compra_3")
        self.apaga_compra_3.setMinimumSize(QSize(0, 30))
        self.apaga_compra_3.setMaximumSize(QSize(16777215, 30))
        self.apaga_compra_3.setFont(font)
        self.apaga_compra_3.setLayoutDirection(Qt.LeftToRight)
        self.apaga_compra_3.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"background-color:rgba(255,255,255,10);\n"
"\n"
"border: 1px solid rgba(255,255,255,20);\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"}")
        self.apaga_compra_3.setIcon(icon19)

        self.verticalLayout_93.addWidget(self.apaga_compra_3)

        self.filter_dates_btn_3 = QPushButton(self.scrollAreaWidgetContents_10)
        self.filter_dates_btn_3.setObjectName(u"filter_dates_btn_3")
        self.filter_dates_btn_3.setMinimumSize(QSize(0, 30))
        self.filter_dates_btn_3.setFont(font)
        self.filter_dates_btn_3.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"background-color:rgba(255,255,255,10);\n"
"\n"
"border: 1px solid rgba(255,255,255,20);\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u":/icons-cards/src-page-cartoes/datase.png", QSize(), QIcon.Normal, QIcon.Off)
        self.filter_dates_btn_3.setIcon(icon23)

        self.verticalLayout_93.addWidget(self.filter_dates_btn_3)

        self.verticalSpacer_14 = QSpacerItem(20, 500, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_93.addItem(self.verticalSpacer_14)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_67.addWidget(self.scrollArea_10)


        self.verticalLayout_66.addWidget(self.frame_58)


        self.horizontalLayout_53.addWidget(self.main_menu_extrato_page)

        self.stacked_configcartao0_2.addWidget(self.table_extrato_main_1)

        self.verticalLayout_62.addWidget(self.stacked_configcartao0_2)


        self.verticalLayout_92.addWidget(self.frame_57)


        self.verticalLayout_61.addWidget(self.frame_93)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_60.addWidget(self.scrollArea_7)


        self.verticalLayout_59.addWidget(self.frame_56)


        self.verticalLayout_141.addWidget(self.frame_55)


        self.verticalLayout_140.addWidget(self.chart_main_evolution_4)

        icon24 = QIcon()
        icon24.addFile(u":/icons-cards/src-page-cartoes/null.png", QSize(), QIcon.Normal, QIcon.Off)
        self.chart_gastos_all_2.addTab(self.page_Tabe_main1, icon24, "")
        self.page_Tabe_main2 = QWidget()
        self.page_Tabe_main2.setObjectName(u"page_Tabe_main2")
        self.page_Tabe_main2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.verticalLayout_142 = QVBoxLayout(self.page_Tabe_main2)
        self.verticalLayout_142.setSpacing(0)
        self.verticalLayout_142.setObjectName(u"verticalLayout_142")
        self.verticalLayout_142.setContentsMargins(0, 0, 10, 0)
        self.chart_main_date_4 = QFrame(self.page_Tabe_main2)
        self.chart_main_date_4.setObjectName(u"chart_main_date_4")
        self.chart_main_date_4.setStyleSheet(u"border-radius:10px;")
        self.chart_main_date_4.setFrameShape(QFrame.StyledPanel)
        self.chart_main_date_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_143 = QVBoxLayout(self.chart_main_date_4)
        self.verticalLayout_143.setSpacing(0)
        self.verticalLayout_143.setObjectName(u"verticalLayout_143")
        self.verticalLayout_143.setContentsMargins(0, 0, 0, 0)
        self.frame_86 = QFrame(self.chart_main_date_4)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setStyleSheet(u"")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_11 = QScrollArea(self.frame_86)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setStyleSheet(u"	font: 25 14pt \"Bahnschrift Light Condensed\";")
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 1430, 644))
        self.horizontalLayout_58 = QHBoxLayout(self.scrollAreaWidgetContents_11)
        self.horizontalLayout_58.setSpacing(10)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.frame_87 = QFrame(self.scrollAreaWidgetContents_11)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:5px;")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_95 = QVBoxLayout(self.frame_87)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.label_47 = QLabel(self.frame_87)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(16777215, 40))
        self.label_47.setFont(font)
        self.label_47.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border-bottom: 1px solid rgba(255,255,255,30);\n"
"border-radius:0px;")
        self.label_47.setAlignment(Qt.AlignCenter)

        self.verticalLayout_95.addWidget(self.label_47)

        self.frame_209 = QFrame(self.frame_87)
        self.frame_209.setObjectName(u"frame_209")
        self.frame_209.setMinimumSize(QSize(120, 67))
        self.frame_209.setMaximumSize(QSize(16777215, 67))
        self.frame_209.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_209.setFrameShape(QFrame.StyledPanel)
        self.frame_209.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_209)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.frame_210 = QFrame(self.frame_209)
        self.frame_210.setObjectName(u"frame_210")
        self.frame_210.setMinimumSize(QSize(40, 0))
        self.frame_210.setMaximumSize(QSize(40, 40))
        self.frame_210.setStyleSheet(u"border-image: url(:/icons-cards/src-page-cartoes/nulsmal.png);\n"
"background-color:rgba(255,255,255,0);\n"
"")
        self.frame_210.setFrameShape(QFrame.StyledPanel)
        self.frame_210.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_81.addWidget(self.frame_210)

        self.frame_211 = QFrame(self.frame_209)
        self.frame_211.setObjectName(u"frame_211")
        self.frame_211.setMinimumSize(QSize(190, 40))
        self.frame_211.setMaximumSize(QSize(177, 40))
        self.frame_211.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_211.setFrameShape(QFrame.StyledPanel)
        self.frame_211.setFrameShadow(QFrame.Raised)
        self.verticalLayout_99 = QVBoxLayout(self.frame_211)
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.label_85 = QLabel(self.frame_211)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMinimumSize(QSize(0, 27))
        self.label_85.setMaximumSize(QSize(16777215, 18))
        font5 = QFont()
        font5.setFamily(u"Bahnschrift Light Condensed")
        font5.setPointSize(13)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(3)
        self.label_85.setFont(font5)
        self.label_85.setAutoFillBackground(False)
        self.label_85.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"font-size:13pt;")
        self.label_85.setAlignment(Qt.AlignCenter)

        self.verticalLayout_99.addWidget(self.label_85)


        self.horizontalLayout_81.addWidget(self.frame_211)

        self.frame_228 = QFrame(self.frame_209)
        self.frame_228.setObjectName(u"frame_228")
        self.frame_228.setMinimumSize(QSize(0, 0))
        self.frame_228.setMaximumSize(QSize(16777215, 16777215))
        self.frame_228.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_228.setFrameShape(QFrame.StyledPanel)
        self.frame_228.setFrameShadow(QFrame.Raised)
        self.verticalLayout_155 = QVBoxLayout(self.frame_228)
        self.verticalLayout_155.setObjectName(u"verticalLayout_155")
        self.comboBox_11 = QComboBox(self.frame_228)
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setMaximumSize(QSize(16777215, 90))
        self.comboBox_11.setStyleSheet(u"border: 0px;\n"
"font:11pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")
        self.comboBox_11.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBox_11.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.verticalLayout_155.addWidget(self.comboBox_11)


        self.horizontalLayout_81.addWidget(self.frame_228)


        self.verticalLayout_95.addWidget(self.frame_209)

        self.frame_269 = QFrame(self.frame_87)
        self.frame_269.setObjectName(u"frame_269")
        self.frame_269.setMinimumSize(QSize(120, 67))
        self.frame_269.setMaximumSize(QSize(16777215, 67))
        self.frame_269.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_269.setFrameShape(QFrame.StyledPanel)
        self.frame_269.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frame_269)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.frame_270 = QFrame(self.frame_269)
        self.frame_270.setObjectName(u"frame_270")
        self.frame_270.setMinimumSize(QSize(40, 0))
        self.frame_270.setMaximumSize(QSize(40, 40))
        self.frame_270.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/credt.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_270.setFrameShape(QFrame.StyledPanel)
        self.frame_270.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_105.addWidget(self.frame_270)

        self.frame_271 = QFrame(self.frame_269)
        self.frame_271.setObjectName(u"frame_271")
        self.frame_271.setMinimumSize(QSize(190, 0))
        self.frame_271.setMaximumSize(QSize(190, 16777215))
        self.frame_271.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_271.setFrameShape(QFrame.StyledPanel)
        self.frame_271.setFrameShadow(QFrame.Raised)
        self.verticalLayout_169 = QVBoxLayout(self.frame_271)
        self.verticalLayout_169.setObjectName(u"verticalLayout_169")
        self.label_100 = QLabel(self.frame_271)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setMinimumSize(QSize(0, 0))
        self.label_100.setMaximumSize(QSize(16777215, 28))
        self.label_100.setFont(font5)
        self.label_100.setLayoutDirection(Qt.LeftToRight)
        self.label_100.setAutoFillBackground(False)
        self.label_100.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"font-size:13pt;")
        self.label_100.setAlignment(Qt.AlignCenter)

        self.verticalLayout_169.addWidget(self.label_100)


        self.horizontalLayout_105.addWidget(self.frame_271)

        self.frame_272 = QFrame(self.frame_269)
        self.frame_272.setObjectName(u"frame_272")
        self.frame_272.setMinimumSize(QSize(0, 0))
        self.frame_272.setMaximumSize(QSize(16777215, 16777215))
        self.frame_272.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_272.setFrameShape(QFrame.StyledPanel)
        self.frame_272.setFrameShadow(QFrame.Raised)
        self.verticalLayout_174 = QVBoxLayout(self.frame_272)
        self.verticalLayout_174.setObjectName(u"verticalLayout_174")
        self.comboBox_25 = QComboBox(self.frame_272)
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.setObjectName(u"comboBox_25")
        self.comboBox_25.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_25.setStyleSheet(u"border: 0px;\n"
"font:11pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")

        self.verticalLayout_174.addWidget(self.comboBox_25)


        self.horizontalLayout_105.addWidget(self.frame_272)


        self.verticalLayout_95.addWidget(self.frame_269)

        self.frame_205 = QFrame(self.frame_87)
        self.frame_205.setObjectName(u"frame_205")
        self.frame_205.setMinimumSize(QSize(120, 67))
        self.frame_205.setMaximumSize(QSize(16777215, 67))
        self.frame_205.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_205.setFrameShape(QFrame.StyledPanel)
        self.frame_205.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_205)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.frame_219 = QFrame(self.frame_205)
        self.frame_219.setObjectName(u"frame_219")
        self.frame_219.setMinimumSize(QSize(40, 0))
        self.frame_219.setMaximumSize(QSize(40, 40))
        self.frame_219.setStyleSheet(u"border-image: url(:/icons-cards/src-page-cartoes/money.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_219.setFrameShape(QFrame.StyledPanel)
        self.frame_219.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_82.addWidget(self.frame_219)

        self.frame_223 = QFrame(self.frame_205)
        self.frame_223.setObjectName(u"frame_223")
        self.frame_223.setMinimumSize(QSize(0, 0))
        self.frame_223.setMaximumSize(QSize(190, 16777215))
        self.frame_223.setFont(font)
        self.frame_223.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_223.setFrameShape(QFrame.StyledPanel)
        self.frame_223.setFrameShadow(QFrame.Raised)
        self.verticalLayout_154 = QVBoxLayout(self.frame_223)
        self.verticalLayout_154.setObjectName(u"verticalLayout_154")
        self.label_90 = QLabel(self.frame_223)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setMinimumSize(QSize(177, 40))
        self.label_90.setMaximumSize(QSize(177, 40))
        self.label_90.setFont(font5)
        self.label_90.setAutoFillBackground(False)
        self.label_90.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"font-size:13pt;")
        self.label_90.setAlignment(Qt.AlignCenter)

        self.verticalLayout_154.addWidget(self.label_90)


        self.horizontalLayout_82.addWidget(self.frame_223)

        self.frame_227 = QFrame(self.frame_205)
        self.frame_227.setObjectName(u"frame_227")
        self.frame_227.setMinimumSize(QSize(0, 0))
        self.frame_227.setMaximumSize(QSize(16777215, 16777215))
        self.frame_227.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_227.setFrameShape(QFrame.StyledPanel)
        self.frame_227.setFrameShadow(QFrame.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_227)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.comboBox_27 = QComboBox(self.frame_227)
        self.comboBox_27.setObjectName(u"comboBox_27")
        self.comboBox_27.setMaximumSize(QSize(16777215, 90))
        self.comboBox_27.setStyleSheet(u"border: 0px;\n"
"font:11pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")

        self.verticalLayout_100.addWidget(self.comboBox_27)


        self.horizontalLayout_82.addWidget(self.frame_227)


        self.verticalLayout_95.addWidget(self.frame_205)

        self.frame_197 = QFrame(self.frame_87)
        self.frame_197.setObjectName(u"frame_197")
        self.frame_197.setMinimumSize(QSize(120, 67))
        self.frame_197.setMaximumSize(QSize(16777215, 67))
        self.frame_197.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_197.setFrameShape(QFrame.StyledPanel)
        self.frame_197.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_197)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.frame_198 = QFrame(self.frame_197)
        self.frame_198.setObjectName(u"frame_198")
        self.frame_198.setMinimumSize(QSize(40, 0))
        self.frame_198.setMaximumSize(QSize(40, 40))
        self.frame_198.setStyleSheet(u"border-image: url(:/icons-cards/src-page-cartoes/nulsmal.png);\n"
"background-color:rgba(255,255,255,0);\n"
"")
        self.frame_198.setFrameShape(QFrame.StyledPanel)
        self.frame_198.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_79.addWidget(self.frame_198)

        self.frame_199 = QFrame(self.frame_197)
        self.frame_199.setObjectName(u"frame_199")
        self.frame_199.setMinimumSize(QSize(190, 40))
        self.frame_199.setMaximumSize(QSize(177, 40))
        self.frame_199.setFont(font)
        self.frame_199.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_199.setFrameShape(QFrame.StyledPanel)
        self.frame_199.setFrameShadow(QFrame.Raised)
        self.verticalLayout_151 = QVBoxLayout(self.frame_199)
        self.verticalLayout_151.setObjectName(u"verticalLayout_151")
        self.label_82 = QLabel(self.frame_199)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMinimumSize(QSize(0, 0))
        self.label_82.setMaximumSize(QSize(16777215, 25))
        self.label_82.setFont(font5)
        self.label_82.setAutoFillBackground(False)
        self.label_82.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"font-size:13pt;")
        self.label_82.setAlignment(Qt.AlignCenter)

        self.verticalLayout_151.addWidget(self.label_82)


        self.horizontalLayout_79.addWidget(self.frame_199)

        self.frame_200 = QFrame(self.frame_197)
        self.frame_200.setObjectName(u"frame_200")
        self.frame_200.setMinimumSize(QSize(0, 0))
        self.frame_200.setMaximumSize(QSize(16777215, 16777215))
        self.frame_200.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_200.setFrameShape(QFrame.StyledPanel)
        self.frame_200.setFrameShadow(QFrame.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_200)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.comboBox_21 = QComboBox(self.frame_200)
        self.comboBox_21.setObjectName(u"comboBox_21")
        self.comboBox_21.setMaximumSize(QSize(16777215, 90))
        self.comboBox_21.setStyleSheet(u"border: 0px;\n"
"font:11pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")

        self.verticalLayout_96.addWidget(self.comboBox_21)


        self.horizontalLayout_79.addWidget(self.frame_200)


        self.verticalLayout_95.addWidget(self.frame_197)

        self.frame_185 = QFrame(self.frame_87)
        self.frame_185.setObjectName(u"frame_185")
        self.frame_185.setMinimumSize(QSize(120, 67))
        self.frame_185.setMaximumSize(QSize(16777215, 67))
        self.frame_185.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_185.setFrameShape(QFrame.StyledPanel)
        self.frame_185.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_185)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.frame_186 = QFrame(self.frame_185)
        self.frame_186.setObjectName(u"frame_186")
        self.frame_186.setMinimumSize(QSize(40, 0))
        self.frame_186.setMaximumSize(QSize(40, 40))
        self.frame_186.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/etiqueta.png);\n"
"background-color:rgba(255,255,255,0);\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;")
        self.frame_186.setFrameShape(QFrame.StyledPanel)
        self.frame_186.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_76.addWidget(self.frame_186)

        self.frame_187 = QFrame(self.frame_185)
        self.frame_187.setObjectName(u"frame_187")
        self.frame_187.setMinimumSize(QSize(190, 40))
        self.frame_187.setMaximumSize(QSize(177, 40))
        self.frame_187.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_187.setFrameShape(QFrame.StyledPanel)
        self.frame_187.setFrameShadow(QFrame.Raised)
        self.verticalLayout_146 = QVBoxLayout(self.frame_187)
        self.verticalLayout_146.setObjectName(u"verticalLayout_146")
        self.label_79 = QLabel(self.frame_187)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(0, 0))
        self.label_79.setMaximumSize(QSize(16777215, 18))
        self.label_79.setFont(font5)
        self.label_79.setAutoFillBackground(False)
        self.label_79.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"font-size:13pt;")
        self.label_79.setAlignment(Qt.AlignCenter)

        self.verticalLayout_146.addWidget(self.label_79)


        self.horizontalLayout_76.addWidget(self.frame_187)

        self.frame_188 = QFrame(self.frame_185)
        self.frame_188.setObjectName(u"frame_188")
        self.frame_188.setMinimumSize(QSize(0, 0))
        self.frame_188.setMaximumSize(QSize(16777215, 16777215))
        self.frame_188.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_188.setFrameShape(QFrame.StyledPanel)
        self.frame_188.setFrameShadow(QFrame.Raised)
        self.verticalLayout_147 = QVBoxLayout(self.frame_188)
        self.verticalLayout_147.setObjectName(u"verticalLayout_147")
        self.lineEdit_11 = QLineEdit(self.frame_188)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy1.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy1)
        self.lineEdit_11.setMaximumSize(QSize(16777215, 90))
        self.lineEdit_11.setStyleSheet(u"border: 0px;\n"
"font: 25 12pt \"Microsoft YaHei Light\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")

        self.verticalLayout_147.addWidget(self.lineEdit_11)


        self.horizontalLayout_76.addWidget(self.frame_188)


        self.verticalLayout_95.addWidget(self.frame_185)

        self.frame_189 = QFrame(self.frame_87)
        self.frame_189.setObjectName(u"frame_189")
        self.frame_189.setMinimumSize(QSize(120, 67))
        self.frame_189.setMaximumSize(QSize(16777215, 67))
        self.frame_189.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_189.setFrameShape(QFrame.StyledPanel)
        self.frame_189.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_189)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.frame_190 = QFrame(self.frame_189)
        self.frame_190.setObjectName(u"frame_190")
        self.frame_190.setMinimumSize(QSize(40, 0))
        self.frame_190.setMaximumSize(QSize(40, 40))
        self.frame_190.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/calendarios.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_190.setFrameShape(QFrame.StyledPanel)
        self.frame_190.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_77.addWidget(self.frame_190)

        self.frame_191 = QFrame(self.frame_189)
        self.frame_191.setObjectName(u"frame_191")
        self.frame_191.setMinimumSize(QSize(190, 40))
        self.frame_191.setMaximumSize(QSize(177, 40))
        self.frame_191.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_191.setFrameShape(QFrame.StyledPanel)
        self.frame_191.setFrameShadow(QFrame.Raised)
        self.verticalLayout_148 = QVBoxLayout(self.frame_191)
        self.verticalLayout_148.setObjectName(u"verticalLayout_148")
        self.label_80 = QLabel(self.frame_191)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(0, 0))
        self.label_80.setMaximumSize(QSize(16777215, 18))
        self.label_80.setFont(font5)
        self.label_80.setAutoFillBackground(False)
        self.label_80.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"font-size:13pt;")
        self.label_80.setAlignment(Qt.AlignCenter)

        self.verticalLayout_148.addWidget(self.label_80)


        self.horizontalLayout_77.addWidget(self.frame_191)

        self.frame_192 = QFrame(self.frame_189)
        self.frame_192.setObjectName(u"frame_192")
        self.frame_192.setMinimumSize(QSize(0, 0))
        self.frame_192.setMaximumSize(QSize(16777215, 16777215))
        self.frame_192.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_192.setFrameShape(QFrame.StyledPanel)
        self.frame_192.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_192)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.lancamento_programado_2 = QDateEdit(self.frame_192)
        self.lancamento_programado_2.setObjectName(u"lancamento_programado_2")
        self.lancamento_programado_2.setStyleSheet(u"QDateEdit{\n"
"	border:none;\n"
"	border-radius:0px;}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"  	height: 20px;\n"
"  	width: 80px;\n"
"	border:none;\n"
"	border-radius:0px;\n"
"  	color: white;\n"
"  	font-size: 18px;\n"
"  	icon-size: 20px, 20px;\n"
"  	background-color:rgb(0,0,0);\n"
"  }\n"
"  QCalendarWidget QMenu {\n"
"  	width: 100px;\n"
"  	left: 20px;\n"
"  	color: white;\n"
"  	font-size: 18px;\n"
"  	background-color:rgb(0,0,0);\n"
"  }\n"
"  QCalendarWidget QSpinBox { \n"
"  	width: 100px; \n"
"  	font-size: 18px;;\n"
"  	color: white; \n"
"  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); \n"
"  	selection-background-color: rgb(136, 136, 136);\n"
"  	selection-color: rgb(255, 255, 255);\n"
"  }\n"
"\n"
"  QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:20px; }\n"
"  QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:20px;}\n"
"  QCalendar"
                        "Widget QSpinBox::up-arrow { width:20px;  height:20px; }\n"
"  QCalendarWidget QSpinBox::down-arrow { width:20px;  height:20px; }\n"
"   \n"
"  /* header row */\n"
"  QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); }\n"
"   \n"
"  /* normal days */\n"
"  QCalendarWidget QAbstractItemView:enabled \n"
"  {\n"
"  	font-size: 18px;\n"
"  	background-color:rgb(0,0,0);\n"
"  	background-color: black;  \n"
"  	selection-background-color: rgb(0, 0, 0); \n"
"  	selection-color: rgb(0, 255, 0); \n"
"  }\n"
"   \n"
"  /* days in other months */\n"
"  /* navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar\n"
"{ \n"
"  	background-color:rgb(0,0,0);}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"color: rgb(64, 64, 64); \n"
"}")
        self.lancamento_programado_2.setAccelerated(True)
        self.lancamento_programado_2.setProperty("showGroupSeparator", True)
        self.lancamento_programado_2.setCalendarPopup(True)

        self.horizontalLayout_48.addWidget(self.lancamento_programado_2)

        self.pushButton_25 = QPushButton(self.frame_192)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setMinimumSize(QSize(48, 0))
        self.pushButton_25.setMaximumSize(QSize(48, 48))
        self.pushButton_25.setFont(font1)
        self.pushButton_25.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:5px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"	font-size:12pt;\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        self.pushButton_25.setCheckable(False)
        self.pushButton_25.setChecked(False)
        self.pushButton_25.setAutoExclusive(False)
        self.pushButton_25.setAutoDefault(False)
        self.pushButton_25.setFlat(False)

        self.horizontalLayout_48.addWidget(self.pushButton_25)


        self.horizontalLayout_77.addWidget(self.frame_192)


        self.verticalLayout_95.addWidget(self.frame_189)

        self.frame_193 = QFrame(self.frame_87)
        self.frame_193.setObjectName(u"frame_193")
        self.frame_193.setMinimumSize(QSize(120, 67))
        self.frame_193.setMaximumSize(QSize(16777215, 67))
        self.frame_193.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_193.setFrameShape(QFrame.StyledPanel)
        self.frame_193.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_193)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.frame_194 = QFrame(self.frame_193)
        self.frame_194.setObjectName(u"frame_194")
        self.frame_194.setMinimumSize(QSize(40, 0))
        self.frame_194.setMaximumSize(QSize(40, 40))
        self.frame_194.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/money2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_194.setFrameShape(QFrame.StyledPanel)
        self.frame_194.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_78.addWidget(self.frame_194)

        self.frame_195 = QFrame(self.frame_193)
        self.frame_195.setObjectName(u"frame_195")
        self.frame_195.setMinimumSize(QSize(190, 0))
        self.frame_195.setMaximumSize(QSize(190, 16777215))
        self.frame_195.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_195.setFrameShape(QFrame.StyledPanel)
        self.frame_195.setFrameShadow(QFrame.Raised)
        self.verticalLayout_149 = QVBoxLayout(self.frame_195)
        self.verticalLayout_149.setObjectName(u"verticalLayout_149")
        self.label_81 = QLabel(self.frame_195)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setMinimumSize(QSize(177, 40))
        self.label_81.setMaximumSize(QSize(177, 40))
        self.label_81.setFont(font5)
        self.label_81.setAutoFillBackground(False)
        self.label_81.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"font-size:13pt;")
        self.label_81.setAlignment(Qt.AlignCenter)

        self.verticalLayout_149.addWidget(self.label_81)


        self.horizontalLayout_78.addWidget(self.frame_195)

        self.frame_196 = QFrame(self.frame_193)
        self.frame_196.setObjectName(u"frame_196")
        self.frame_196.setMinimumSize(QSize(0, 0))
        self.frame_196.setMaximumSize(QSize(16777215, 16777215))
        self.frame_196.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_196.setFrameShape(QFrame.StyledPanel)
        self.frame_196.setFrameShadow(QFrame.Raised)
        self.verticalLayout_150 = QVBoxLayout(self.frame_196)
        self.verticalLayout_150.setObjectName(u"verticalLayout_150")
        self.lineEdit_13 = QLineEdit(self.frame_196)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMaximumSize(QSize(16777215, 90))
        self.lineEdit_13.setStyleSheet(u"border: 0px;\n"
"font: 25 12pt \"Microsoft YaHei Light\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:3px;")

        self.verticalLayout_150.addWidget(self.lineEdit_13)


        self.horizontalLayout_78.addWidget(self.frame_196)


        self.verticalLayout_95.addWidget(self.frame_193)

        self.frame_201 = QFrame(self.frame_87)
        self.frame_201.setObjectName(u"frame_201")
        self.frame_201.setMinimumSize(QSize(120, 67))
        self.frame_201.setMaximumSize(QSize(16777215, 67))
        self.frame_201.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_201.setFrameShape(QFrame.StyledPanel)
        self.frame_201.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_201)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.frame_202 = QFrame(self.frame_201)
        self.frame_202.setObjectName(u"frame_202")
        self.frame_202.setMinimumSize(QSize(40, 0))
        self.frame_202.setMaximumSize(QSize(40, 40))
        self.frame_202.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/parcelas2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_202.setFrameShape(QFrame.StyledPanel)
        self.frame_202.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_60.addWidget(self.frame_202)

        self.frame_203 = QFrame(self.frame_201)
        self.frame_203.setObjectName(u"frame_203")
        self.frame_203.setMinimumSize(QSize(190, 40))
        self.frame_203.setMaximumSize(QSize(177, 40))
        self.frame_203.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_203.setFrameShape(QFrame.StyledPanel)
        self.frame_203.setFrameShadow(QFrame.Raised)
        self.verticalLayout_152 = QVBoxLayout(self.frame_203)
        self.verticalLayout_152.setObjectName(u"verticalLayout_152")
        self.label_83 = QLabel(self.frame_203)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(0, 0))
        self.label_83.setMaximumSize(QSize(16777215, 28))
        self.label_83.setFont(font5)
        self.label_83.setLayoutDirection(Qt.LeftToRight)
        self.label_83.setAutoFillBackground(False)
        self.label_83.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"font-size:13pt;")
        self.label_83.setAlignment(Qt.AlignCenter)

        self.verticalLayout_152.addWidget(self.label_83)


        self.horizontalLayout_60.addWidget(self.frame_203)

        self.frame_204 = QFrame(self.frame_201)
        self.frame_204.setObjectName(u"frame_204")
        self.frame_204.setMinimumSize(QSize(0, 0))
        self.frame_204.setMaximumSize(QSize(16777215, 16777215))
        self.frame_204.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_204.setFrameShape(QFrame.StyledPanel)
        self.frame_204.setFrameShadow(QFrame.Raised)
        self.verticalLayout_153 = QVBoxLayout(self.frame_204)
        self.verticalLayout_153.setObjectName(u"verticalLayout_153")
        self.comboBox_22 = QComboBox(self.frame_204)
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.setObjectName(u"comboBox_22")
        self.comboBox_22.setMaximumSize(QSize(16777215, 90))
        self.comboBox_22.setStyleSheet(u"border: 0px;\n"
"font:11pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")

        self.verticalLayout_153.addWidget(self.comboBox_22)


        self.horizontalLayout_60.addWidget(self.frame_204)


        self.verticalLayout_95.addWidget(self.frame_201)


        self.horizontalLayout_58.addWidget(self.frame_87)

        self.config_new_lan_3 = QFrame(self.scrollAreaWidgetContents_11)
        self.config_new_lan_3.setObjectName(u"config_new_lan_3")
        self.config_new_lan_3.setMinimumSize(QSize(600, 0))
        self.config_new_lan_3.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:5px;")
        self.config_new_lan_3.setFrameShape(QFrame.StyledPanel)
        self.config_new_lan_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_97 = QVBoxLayout(self.config_new_lan_3)
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.label_48 = QLabel(self.config_new_lan_3)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(0, 40))
        self.label_48.setMaximumSize(QSize(16777215, 52))
        self.label_48.setFont(font)
        self.label_48.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border-bottom: 1px solid rgba(255,255,255,30);\n"
"border-radius:0px;")
        self.label_48.setAlignment(Qt.AlignCenter)

        self.verticalLayout_97.addWidget(self.label_48)

        self.frame_programar_data = QFrame(self.config_new_lan_3)
        self.frame_programar_data.setObjectName(u"frame_programar_data")
        self.frame_programar_data.setMinimumSize(QSize(120, 67))
        self.frame_programar_data.setMaximumSize(QSize(16777215, 67))
        self.frame_programar_data.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_programar_data.setFrameShape(QFrame.StyledPanel)
        self.frame_programar_data.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_programar_data)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.frame_274 = QFrame(self.frame_programar_data)
        self.frame_274.setObjectName(u"frame_274")
        self.frame_274.setMinimumSize(QSize(40, 0))
        self.frame_274.setMaximumSize(QSize(40, 40))
        self.frame_274.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/parcelas2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_274.setFrameShape(QFrame.StyledPanel)
        self.frame_274.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_75.addWidget(self.frame_274)

        self.frame_275 = QFrame(self.frame_programar_data)
        self.frame_275.setObjectName(u"frame_275")
        self.frame_275.setMinimumSize(QSize(190, 0))
        self.frame_275.setMaximumSize(QSize(190, 16777215))
        self.frame_275.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_275.setFrameShape(QFrame.StyledPanel)
        self.frame_275.setFrameShadow(QFrame.Raised)
        self.verticalLayout_175 = QVBoxLayout(self.frame_275)
        self.verticalLayout_175.setObjectName(u"verticalLayout_175")
        self.label_101 = QLabel(self.frame_275)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setMinimumSize(QSize(0, 0))
        self.label_101.setMaximumSize(QSize(16777215, 28))
        self.label_101.setFont(font5)
        self.label_101.setLayoutDirection(Qt.LeftToRight)
        self.label_101.setAutoFillBackground(False)
        self.label_101.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"font-size:13pt;")
        self.label_101.setAlignment(Qt.AlignCenter)

        self.verticalLayout_175.addWidget(self.label_101)


        self.horizontalLayout_75.addWidget(self.frame_275)

        self.frame_276 = QFrame(self.frame_programar_data)
        self.frame_276.setObjectName(u"frame_276")
        self.frame_276.setMinimumSize(QSize(0, 0))
        self.frame_276.setMaximumSize(QSize(16777215, 16777215))
        self.frame_276.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_276.setFrameShape(QFrame.StyledPanel)
        self.frame_276.setFrameShadow(QFrame.Raised)
        self.verticalLayout_176 = QVBoxLayout(self.frame_276)
        self.verticalLayout_176.setObjectName(u"verticalLayout_176")
        self.lancamento_programado = QDateEdit(self.frame_276)
        self.lancamento_programado.setObjectName(u"lancamento_programado")
        self.lancamento_programado.setStyleSheet(u"border:0px;")
        self.lancamento_programado.setAccelerated(True)
        self.lancamento_programado.setProperty("showGroupSeparator", True)
        self.lancamento_programado.setCalendarPopup(True)

        self.verticalLayout_176.addWidget(self.lancamento_programado)


        self.horizontalLayout_75.addWidget(self.frame_276)


        self.verticalLayout_97.addWidget(self.frame_programar_data)

        self.frame_recorrente = QFrame(self.config_new_lan_3)
        self.frame_recorrente.setObjectName(u"frame_recorrente")
        self.frame_recorrente.setMinimumSize(QSize(120, 67))
        self.frame_recorrente.setMaximumSize(QSize(16777215, 67))
        self.frame_recorrente.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_recorrente.setFrameShape(QFrame.StyledPanel)
        self.frame_recorrente.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_recorrente)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.frame_212 = QFrame(self.frame_recorrente)
        self.frame_212.setObjectName(u"frame_212")
        self.frame_212.setMinimumSize(QSize(40, 0))
        self.frame_212.setMaximumSize(QSize(40, 40))
        self.frame_212.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/parcelas2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_212.setFrameShape(QFrame.StyledPanel)
        self.frame_212.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_61.addWidget(self.frame_212)

        self.frame_213 = QFrame(self.frame_recorrente)
        self.frame_213.setObjectName(u"frame_213")
        self.frame_213.setMinimumSize(QSize(190, 0))
        self.frame_213.setMaximumSize(QSize(190, 16777215))
        self.frame_213.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_213.setFrameShape(QFrame.StyledPanel)
        self.frame_213.setFrameShadow(QFrame.Raised)
        self.verticalLayout_156 = QVBoxLayout(self.frame_213)
        self.verticalLayout_156.setObjectName(u"verticalLayout_156")
        self.label_86 = QLabel(self.frame_213)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setMinimumSize(QSize(0, 0))
        self.label_86.setMaximumSize(QSize(16777215, 28))
        self.label_86.setFont(font5)
        self.label_86.setLayoutDirection(Qt.LeftToRight)
        self.label_86.setAutoFillBackground(False)
        self.label_86.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"font-size:13pt;")
        self.label_86.setAlignment(Qt.AlignCenter)

        self.verticalLayout_156.addWidget(self.label_86)


        self.horizontalLayout_61.addWidget(self.frame_213)

        self.frame_214 = QFrame(self.frame_recorrente)
        self.frame_214.setObjectName(u"frame_214")
        self.frame_214.setMinimumSize(QSize(0, 0))
        self.frame_214.setMaximumSize(QSize(16777215, 16777215))
        self.frame_214.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_214.setFrameShape(QFrame.StyledPanel)
        self.frame_214.setFrameShadow(QFrame.Raised)
        self.verticalLayout_157 = QVBoxLayout(self.frame_214)
        self.verticalLayout_157.setObjectName(u"verticalLayout_157")
        self.comboBox_23 = QComboBox(self.frame_214)
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.setObjectName(u"comboBox_23")
        self.comboBox_23.setMaximumSize(QSize(16777215, 90))
        self.comboBox_23.setStyleSheet(u"border: 0px;\n"
"font:11pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")

        self.verticalLayout_157.addWidget(self.comboBox_23)


        self.horizontalLayout_61.addWidget(self.frame_214)


        self.verticalLayout_97.addWidget(self.frame_recorrente)

        self.frame_recorrente_config = QFrame(self.config_new_lan_3)
        self.frame_recorrente_config.setObjectName(u"frame_recorrente_config")
        self.frame_recorrente_config.setMinimumSize(QSize(120, 67))
        self.frame_recorrente_config.setMaximumSize(QSize(16777215, 67))
        self.frame_recorrente_config.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_recorrente_config.setFrameShape(QFrame.StyledPanel)
        self.frame_recorrente_config.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.frame_recorrente_config)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.frame_224 = QFrame(self.frame_recorrente_config)
        self.frame_224.setObjectName(u"frame_224")
        self.frame_224.setMinimumSize(QSize(40, 0))
        self.frame_224.setMaximumSize(QSize(40, 40))
        self.frame_224.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/parcelas2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_224.setFrameShape(QFrame.StyledPanel)
        self.frame_224.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_62.addWidget(self.frame_224)

        self.frame_225 = QFrame(self.frame_recorrente_config)
        self.frame_225.setObjectName(u"frame_225")
        self.frame_225.setMinimumSize(QSize(190, 0))
        self.frame_225.setMaximumSize(QSize(190, 16777215))
        self.frame_225.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_225.setFrameShape(QFrame.StyledPanel)
        self.frame_225.setFrameShadow(QFrame.Raised)
        self.verticalLayout_162 = QVBoxLayout(self.frame_225)
        self.verticalLayout_162.setObjectName(u"verticalLayout_162")
        self.label_89 = QLabel(self.frame_225)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(0, 0))
        self.label_89.setMaximumSize(QSize(16777215, 28))
        self.label_89.setFont(font5)
        self.label_89.setLayoutDirection(Qt.LeftToRight)
        self.label_89.setAutoFillBackground(False)
        self.label_89.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"font-size:13pt;")
        self.label_89.setAlignment(Qt.AlignCenter)

        self.verticalLayout_162.addWidget(self.label_89)


        self.horizontalLayout_62.addWidget(self.frame_225)

        self.frame_226 = QFrame(self.frame_recorrente_config)
        self.frame_226.setObjectName(u"frame_226")
        self.frame_226.setMinimumSize(QSize(0, 0))
        self.frame_226.setMaximumSize(QSize(16777215, 16777215))
        self.frame_226.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_226.setFrameShape(QFrame.StyledPanel)
        self.frame_226.setFrameShadow(QFrame.Raised)
        self.verticalLayout_163 = QVBoxLayout(self.frame_226)
        self.verticalLayout_163.setObjectName(u"verticalLayout_163")
        self.comboBox_26 = QComboBox(self.frame_226)
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.setObjectName(u"comboBox_26")
        self.comboBox_26.setMaximumSize(QSize(16777215, 90))
        self.comboBox_26.setStyleSheet(u"border: 0px;\n"
"font:11pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")

        self.verticalLayout_163.addWidget(self.comboBox_26)


        self.horizontalLayout_62.addWidget(self.frame_226)


        self.verticalLayout_97.addWidget(self.frame_recorrente_config)

        self.frame_recorrente_config_date = QFrame(self.config_new_lan_3)
        self.frame_recorrente_config_date.setObjectName(u"frame_recorrente_config_date")
        self.frame_recorrente_config_date.setMinimumSize(QSize(120, 67))
        self.frame_recorrente_config_date.setMaximumSize(QSize(16777215, 67))
        self.frame_recorrente_config_date.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_recorrente_config_date.setFrameShape(QFrame.StyledPanel)
        self.frame_recorrente_config_date.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_recorrente_config_date)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.frame_220 = QFrame(self.frame_recorrente_config_date)
        self.frame_220.setObjectName(u"frame_220")
        self.frame_220.setMinimumSize(QSize(40, 0))
        self.frame_220.setMaximumSize(QSize(40, 40))
        self.frame_220.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/parcelas2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_220.setFrameShape(QFrame.StyledPanel)
        self.frame_220.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_63.addWidget(self.frame_220)

        self.frame_221 = QFrame(self.frame_recorrente_config_date)
        self.frame_221.setObjectName(u"frame_221")
        self.frame_221.setMinimumSize(QSize(190, 0))
        self.frame_221.setMaximumSize(QSize(190, 16777215))
        self.frame_221.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_221.setFrameShape(QFrame.StyledPanel)
        self.frame_221.setFrameShadow(QFrame.Raised)
        self.verticalLayout_160 = QVBoxLayout(self.frame_221)
        self.verticalLayout_160.setObjectName(u"verticalLayout_160")
        self.label_88 = QLabel(self.frame_221)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(0, 0))
        self.label_88.setMaximumSize(QSize(16777215, 28))
        self.label_88.setFont(font5)
        self.label_88.setLayoutDirection(Qt.LeftToRight)
        self.label_88.setAutoFillBackground(False)
        self.label_88.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"font-size:13pt;")
        self.label_88.setAlignment(Qt.AlignCenter)

        self.verticalLayout_160.addWidget(self.label_88)


        self.horizontalLayout_63.addWidget(self.frame_221)

        self.frame_222 = QFrame(self.frame_recorrente_config_date)
        self.frame_222.setObjectName(u"frame_222")
        self.frame_222.setMinimumSize(QSize(0, 0))
        self.frame_222.setMaximumSize(QSize(16777215, 16777215))
        self.frame_222.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_222.setFrameShape(QFrame.StyledPanel)
        self.frame_222.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_222)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.lineEdit_14 = QLineEdit(self.frame_222)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setMaximumSize(QSize(16777215, 90))
        self.lineEdit_14.setStyleSheet(u"border: 0px;\n"
"font: 25 12pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")

        self.horizontalLayout_73.addWidget(self.lineEdit_14)

        self.pushButton_26 = QPushButton(self.frame_222)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(48, 0))
        self.pushButton_26.setMaximumSize(QSize(48, 48))
        self.pushButton_26.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        self.pushButton_26.setCheckable(False)
        self.pushButton_26.setChecked(False)
        self.pushButton_26.setAutoExclusive(False)
        self.pushButton_26.setAutoDefault(False)
        self.pushButton_26.setFlat(False)

        self.horizontalLayout_73.addWidget(self.pushButton_26)


        self.horizontalLayout_63.addWidget(self.frame_222)


        self.verticalLayout_97.addWidget(self.frame_recorrente_config_date)

        self.frame_215 = QFrame(self.config_new_lan_3)
        self.frame_215.setObjectName(u"frame_215")
        self.frame_215.setMinimumSize(QSize(120, 67))
        self.frame_215.setMaximumSize(QSize(16777215, 67))
        self.frame_215.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_215.setFrameShape(QFrame.StyledPanel)
        self.frame_215.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_215)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.frame_216 = QFrame(self.frame_215)
        self.frame_216.setObjectName(u"frame_216")
        self.frame_216.setMinimumSize(QSize(40, 0))
        self.frame_216.setMaximumSize(QSize(40, 40))
        self.frame_216.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/parcelas2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_216.setFrameShape(QFrame.StyledPanel)
        self.frame_216.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_74.addWidget(self.frame_216)

        self.frame_217 = QFrame(self.frame_215)
        self.frame_217.setObjectName(u"frame_217")
        self.frame_217.setMinimumSize(QSize(190, 0))
        self.frame_217.setMaximumSize(QSize(190, 16777215))
        self.frame_217.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_217.setFrameShape(QFrame.StyledPanel)
        self.frame_217.setFrameShadow(QFrame.Raised)
        self.verticalLayout_158 = QVBoxLayout(self.frame_217)
        self.verticalLayout_158.setObjectName(u"verticalLayout_158")
        self.label_87 = QLabel(self.frame_217)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(0, 0))
        self.label_87.setMaximumSize(QSize(16777215, 28))
        self.label_87.setFont(font5)
        self.label_87.setLayoutDirection(Qt.LeftToRight)
        self.label_87.setAutoFillBackground(False)
        self.label_87.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"font-size:13pt;")
        self.label_87.setAlignment(Qt.AlignCenter)

        self.verticalLayout_158.addWidget(self.label_87)


        self.horizontalLayout_74.addWidget(self.frame_217)

        self.frame_218 = QFrame(self.frame_215)
        self.frame_218.setObjectName(u"frame_218")
        self.frame_218.setMinimumSize(QSize(0, 0))
        self.frame_218.setMaximumSize(QSize(16777215, 16777215))
        self.frame_218.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_218.setFrameShape(QFrame.StyledPanel)
        self.frame_218.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_218)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalSpacer_24 = QSpacerItem(67, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_24)

        self.download_pdf_2 = QPushButton(self.frame_218)
        self.download_pdf_2.setObjectName(u"download_pdf_2")
        self.download_pdf_2.setMinimumSize(QSize(150, 30))
        self.download_pdf_2.setMaximumSize(QSize(16777215, 30))
        self.download_pdf_2.setFont(font)
        self.download_pdf_2.setLayoutDirection(Qt.LeftToRight)
        self.download_pdf_2.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"\n"
"\n"
"\n"
"	\n"
"background-color:rgba(255,255,255,10);\n"
"\n"
"border: 1px solid rgba(255,255,255,20);\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"}")
        self.download_pdf_2.setIcon(icon19)

        self.horizontalLayout_80.addWidget(self.download_pdf_2)

        self.horizontalSpacer_25 = QSpacerItem(67, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_25)


        self.horizontalLayout_74.addWidget(self.frame_218)


        self.verticalLayout_97.addWidget(self.frame_215)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_97.addItem(self.verticalSpacer_15)


        self.horizontalLayout_58.addWidget(self.config_new_lan_3)

        self.frame_88 = QFrame(self.scrollAreaWidgetContents_11)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(250, 0))
        self.frame_88.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:5px;")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_88)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.label_61 = QLabel(self.frame_88)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMaximumSize(QSize(16777215, 40))
        self.label_61.setFont(font)
        self.label_61.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border-bottom: 1px solid rgba(255,255,255,30);\n"
"border-radius:0px;")
        self.label_61.setAlignment(Qt.AlignCenter)

        self.verticalLayout_98.addWidget(self.label_61)

        self.listWidget_3 = QListWidget(self.frame_88)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(255, 255, 255);")
        self.listWidget_3.setTabKeyNavigation(True)
        self.listWidget_3.setDragEnabled(True)
        self.listWidget_3.setDragDropOverwriteMode(True)
        self.listWidget_3.setDragDropMode(QAbstractItemView.DragDrop)
        self.listWidget_3.setDefaultDropAction(Qt.ActionMask)

        self.verticalLayout_98.addWidget(self.listWidget_3)

        self.frame_95 = QFrame(self.frame_88)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMaximumSize(QSize(16777215, 50))
        self.frame_95.setStyleSheet(u"color: rgb(0, 0, 0);background-color:none;")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.frame_95)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.add_lancamento_btn = QPushButton(self.frame_95)
        self.add_lancamento_btn.setObjectName(u"add_lancamento_btn")
        self.add_lancamento_btn.setMinimumSize(QSize(110, 30))
        self.add_lancamento_btn.setMaximumSize(QSize(110, 25))
        self.add_lancamento_btn.setFont(font)
        self.add_lancamento_btn.setStyleSheet(u"\n"
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

        self.horizontalLayout_106.addWidget(self.add_lancamento_btn)

        self.update_bank_2 = QPushButton(self.frame_95)
        self.update_bank_2.setObjectName(u"update_bank_2")
        self.update_bank_2.setMinimumSize(QSize(0, 30))
        self.update_bank_2.setMaximumSize(QSize(110, 25))
        self.update_bank_2.setStyleSheet(u"\n"
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

        self.horizontalLayout_106.addWidget(self.update_bank_2)


        self.verticalLayout_98.addWidget(self.frame_95)


        self.horizontalLayout_58.addWidget(self.frame_88)

        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)

        self.horizontalLayout_57.addWidget(self.scrollArea_11)


        self.verticalLayout_143.addWidget(self.frame_86)


        self.verticalLayout_142.addWidget(self.chart_main_date_4)

        self.chart_gastos_all_2.addTab(self.page_Tabe_main2, icon23, "")
        self.page_Tabe_main3 = QWidget()
        self.page_Tabe_main3.setObjectName(u"page_Tabe_main3")
        self.page_Tabe_main3.setMaximumSize(QSize(16777215, 16777215))
        self.page_Tabe_main3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
"")
        self.horizontalLayout_83 = QHBoxLayout(self.page_Tabe_main3)
        self.horizontalLayout_83.setSpacing(11)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.frame_89 = QFrame(self.page_Tabe_main3)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setMaximumSize(QSize(16777215, 16777215))
        self.frame_89.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:5px;")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.verticalLayout_101 = QVBoxLayout(self.frame_89)
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.label_65 = QLabel(self.frame_89)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(16777215, 40))
        self.label_65.setFont(font)
        self.label_65.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border-bottom: 1px solid rgba(255,255,255,30);\n"
"border-radius:0px;")
        self.label_65.setAlignment(Qt.AlignCenter)

        self.verticalLayout_101.addWidget(self.label_65)

        self.select_conta_bancaria = QComboBox(self.frame_89)
        self.select_conta_bancaria.addItem("")
        self.select_conta_bancaria.addItem("")
        self.select_conta_bancaria.addItem("")
        self.select_conta_bancaria.addItem("")
        self.select_conta_bancaria.addItem("")
        self.select_conta_bancaria.addItem("")
        self.select_conta_bancaria.addItem("")
        self.select_conta_bancaria.setObjectName(u"select_conta_bancaria")
        self.select_conta_bancaria.setMinimumSize(QSize(0, 30))
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
        self.select_conta_bancaria.setFont(font6)
        self.select_conta_bancaria.setLayoutDirection(Qt.LeftToRight)
        self.select_conta_bancaria.setStyleSheet(u"")

        self.verticalLayout_101.addWidget(self.select_conta_bancaria)

        self.frame_bank_padrao = QFrame(self.frame_89)
        self.frame_bank_padrao.setObjectName(u"frame_bank_padrao")
        self.frame_bank_padrao.setMinimumSize(QSize(120, 67))
        self.frame_bank_padrao.setMaximumSize(QSize(16777215, 67))
        self.frame_bank_padrao.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_bank_padrao.setFrameShape(QFrame.StyledPanel)
        self.frame_bank_padrao.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_bank_padrao)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.frame_277 = QFrame(self.frame_bank_padrao)
        self.frame_277.setObjectName(u"frame_277")
        self.frame_277.setMinimumSize(QSize(40, 0))
        self.frame_277.setMaximumSize(QSize(40, 40))
        self.frame_277.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/parcelas2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_277.setFrameShape(QFrame.StyledPanel)
        self.frame_277.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_107.addWidget(self.frame_277)

        self.frame_278 = QFrame(self.frame_bank_padrao)
        self.frame_278.setObjectName(u"frame_278")
        self.frame_278.setMinimumSize(QSize(190, 0))
        self.frame_278.setMaximumSize(QSize(190, 16777215))
        self.frame_278.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_278.setFrameShape(QFrame.StyledPanel)
        self.frame_278.setFrameShadow(QFrame.Raised)
        self.verticalLayout_164 = QVBoxLayout(self.frame_278)
        self.verticalLayout_164.setObjectName(u"verticalLayout_164")
        self.label_102 = QLabel(self.frame_278)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setMinimumSize(QSize(0, 0))
        self.label_102.setMaximumSize(QSize(16777215, 28))
        self.label_102.setFont(font)
        self.label_102.setLayoutDirection(Qt.LeftToRight)
        self.label_102.setAutoFillBackground(False)
        self.label_102.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;")
        self.label_102.setAlignment(Qt.AlignCenter)

        self.verticalLayout_164.addWidget(self.label_102)


        self.horizontalLayout_107.addWidget(self.frame_278)

        self.frame_279 = QFrame(self.frame_bank_padrao)
        self.frame_279.setObjectName(u"frame_279")
        self.frame_279.setMinimumSize(QSize(0, 0))
        self.frame_279.setMaximumSize(QSize(16777215, 16777215))
        self.frame_279.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_279.setFrameShape(QFrame.StyledPanel)
        self.frame_279.setFrameShadow(QFrame.Raised)
        self.verticalLayout_177 = QVBoxLayout(self.frame_279)
        self.verticalLayout_177.setObjectName(u"verticalLayout_177")
        self.combo_bank_padrao = QComboBox(self.frame_279)
        self.combo_bank_padrao.addItem("")
        self.combo_bank_padrao.addItem("")
        self.combo_bank_padrao.addItem("")
        self.combo_bank_padrao.setObjectName(u"combo_bank_padrao")
        self.combo_bank_padrao.setMaximumSize(QSize(16777215, 90))
        self.combo_bank_padrao.setStyleSheet(u"border: 0px;\n"
"font: 25 12pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")

        self.verticalLayout_177.addWidget(self.combo_bank_padrao)


        self.horizontalLayout_107.addWidget(self.frame_279)


        self.verticalLayout_101.addWidget(self.frame_bank_padrao)

        self.frame_90 = QFrame(self.frame_89)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMaximumSize(QSize(16777215, 262))
        self.frame_90.setStyleSheet(u"")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.stackedWidgetadc_2 = QStackedWidget(self.frame_90)
        self.stackedWidgetadc_2.setObjectName(u"stackedWidgetadc_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(65)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.stackedWidgetadc_2.sizePolicy().hasHeightForWidth())
        self.stackedWidgetadc_2.setSizePolicy(sizePolicy5)
        self.stackedWidgetadc_2.setMinimumSize(QSize(0, 0))
        self.stackedWidgetadc_2.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidgetadc_2.setStyleSheet(u"QFrame{\n"
"background-color:rgba(255,255,255,0);\n"
"border-radius: 10px;\n"
"border: 3px solid  rgb(0, 0, 0);\n"
"border:0px;\n"
"\n"
"}\n"
"\n"
"QFrame:hover{\n"
"border: 3px solid  rgb(55, 50,5 0);\n"
"\n"
"}")
        self.stackedWidgetadc_2.setFrameShape(QFrame.StyledPanel)
        self.stackedWidgetadc_2.setFrameShadow(QFrame.Raised)
        self.stackedWidgetadc_2Page1 = QWidget()
        self.stackedWidgetadc_2Page1.setObjectName(u"stackedWidgetadc_2Page1")
        self.gridLayout_4 = QGridLayout(self.stackedWidgetadc_2Page1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_91 = QFrame(self.stackedWidgetadc_2Page1)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(0, 142))
        self.frame_91.setStyleSheet(u"border:none;\n"
"background-color: rgba(255, 255, 255, 0); color: rgb(0, 0, 0);")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_91)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.adcagencia_conta = QLineEdit(self.frame_91)
        self.adcagencia_conta.setObjectName(u"adcagencia_conta")
        self.adcagencia_conta.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adcagencia_conta.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.adcagencia_conta, 2, 1, 1, 1)

        self.adctitular_conta = QLineEdit(self.frame_91)
        self.adctitular_conta.setObjectName(u"adctitular_conta")
        self.adctitular_conta.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adctitular_conta.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.adctitular_conta, 0, 1, 1, 1)

        self.adc_saldo_conta = QLineEdit(self.frame_91)
        self.adc_saldo_conta.setObjectName(u"adc_saldo_conta")
        self.adc_saldo_conta.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adc_saldo_conta.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.adc_saldo_conta, 5, 1, 1, 1)

        self.label_62 = QLabel(self.frame_91)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label_62, 5, 0, 1, 1)

        self.textcard_5 = QLabel(self.frame_91)
        self.textcard_5.setObjectName(u"textcard_5")
        self.textcard_5.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard_5.setTextFormat(Qt.AutoText)
        self.textcard_5.setScaledContents(False)
        self.textcard_5.setAlignment(Qt.AlignCenter)
        self.textcard_5.setWordWrap(False)

        self.gridLayout_3.addWidget(self.textcard_5, 0, 0, 1, 1)

        self.textcard_6 = QLabel(self.frame_91)
        self.textcard_6.setObjectName(u"textcard_6")
        self.textcard_6.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard_6.setTextFormat(Qt.AutoText)
        self.textcard_6.setScaledContents(False)
        self.textcard_6.setAlignment(Qt.AlignCenter)
        self.textcard_6.setWordWrap(False)

        self.gridLayout_3.addWidget(self.textcard_6, 2, 0, 1, 1)

        self.adc_conta_conta = QLineEdit(self.frame_91)
        self.adc_conta_conta.setObjectName(u"adc_conta_conta")
        self.adc_conta_conta.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adc_conta_conta.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.adc_conta_conta, 3, 1, 1, 1)

        self.textcard_7 = QLabel(self.frame_91)
        self.textcard_7.setObjectName(u"textcard_7")
        self.textcard_7.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard_7.setTextFormat(Qt.AutoText)
        self.textcard_7.setScaledContents(False)
        self.textcard_7.setAlignment(Qt.AlignCenter)
        self.textcard_7.setWordWrap(False)

        self.gridLayout_3.addWidget(self.textcard_7, 3, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_91, 2, 0, 1, 1)

        self.hide_cards_main_3 = QPushButton(self.stackedWidgetadc_2Page1)
        self.hide_cards_main_3.setObjectName(u"hide_cards_main_3")
        self.hide_cards_main_3.setMinimumSize(QSize(40, 53))
        self.hide_cards_main_3.setMaximumSize(QSize(16777215, 16777215))
        self.hide_cards_main_3.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        self.hide_cards_main_3.setIcon(icon12)
        self.hide_cards_main_3.setIconSize(QSize(40, 40))

        self.gridLayout_4.addWidget(self.hide_cards_main_3, 0, 1, 1, 1)

        self.logoadc_2 = QFrame(self.stackedWidgetadc_2Page1)
        self.logoadc_2.setObjectName(u"logoadc_2")
        self.logoadc_2.setMinimumSize(QSize(0, 40))
        self.logoadc_2.setMaximumSize(QSize(40, 40))
        self.logoadc_2.setStyleSheet(u"border: 0px;\n"
"\n"
"")
        self.logoadc_2.setFrameShape(QFrame.StyledPanel)
        self.logoadc_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.logoadc_2, 0, 0, 1, 1)

        self.stackedWidgetadc_2.addWidget(self.stackedWidgetadc_2Page1)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.gridLayout_6 = QGridLayout(self.page_10)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.logoadc_3 = QFrame(self.page_10)
        self.logoadc_3.setObjectName(u"logoadc_3")
        self.logoadc_3.setMinimumSize(QSize(40, 40))
        self.logoadc_3.setMaximumSize(QSize(40, 40))
        self.logoadc_3.setStyleSheet(u"border: 0px;\n"
"\n"
"")
        self.logoadc_3.setFrameShape(QFrame.StyledPanel)
        self.logoadc_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.logoadc_3, 0, 0, 1, 1)

        self.hide_cards_main_4 = QPushButton(self.page_10)
        self.hide_cards_main_4.setObjectName(u"hide_cards_main_4")
        self.hide_cards_main_4.setMinimumSize(QSize(40, 53))
        self.hide_cards_main_4.setMaximumSize(QSize(16777215, 16777215))
        self.hide_cards_main_4.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        self.hide_cards_main_4.setIcon(icon12)
        self.hide_cards_main_4.setIconSize(QSize(40, 40))

        self.gridLayout_6.addWidget(self.hide_cards_main_4, 0, 2, 1, 1)

        self.frame_94 = QFrame(self.page_10)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(0, 142))
        self.frame_94.setStyleSheet(u"border:none;\n"
"background-color: rgba(255, 255, 255, 0); \n"
"color: rgb(0, 0, 0);")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_94)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_66 = QLabel(self.frame_94)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_66, 6, 0, 1, 1)

        self.adclimite_2 = QLineEdit(self.frame_94)
        self.adclimite_2.setObjectName(u"adclimite_2")
        self.adclimite_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adclimite_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.adclimite_2, 0, 1, 1, 1)

        self.adctitular_2 = QLineEdit(self.frame_94)
        self.adctitular_2.setObjectName(u"adctitular_2")
        self.adctitular_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adctitular_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.adctitular_2, 1, 1, 1, 1)

        self.textcard_8 = QLabel(self.frame_94)
        self.textcard_8.setObjectName(u"textcard_8")
        self.textcard_8.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard_8.setTextFormat(Qt.AutoText)
        self.textcard_8.setScaledContents(False)
        self.textcard_8.setAlignment(Qt.AlignCenter)
        self.textcard_8.setWordWrap(False)

        self.gridLayout_5.addWidget(self.textcard_8, 3, 0, 1, 1)

        self.adcfechamento_2 = QLineEdit(self.frame_94)
        self.adcfechamento_2.setObjectName(u"adcfechamento_2")
        self.adcfechamento_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adcfechamento_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.adcfechamento_2, 6, 1, 1, 1)

        self.textcard_9 = QLabel(self.frame_94)
        self.textcard_9.setObjectName(u"textcard_9")
        self.textcard_9.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard_9.setTextFormat(Qt.AutoText)
        self.textcard_9.setScaledContents(False)
        self.textcard_9.setAlignment(Qt.AlignCenter)
        self.textcard_9.setWordWrap(False)

        self.gridLayout_5.addWidget(self.textcard_9, 1, 0, 1, 1)

        self.textcard_10 = QLabel(self.frame_94)
        self.textcard_10.setObjectName(u"textcard_10")
        self.textcard_10.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard_10.setTextFormat(Qt.AutoText)
        self.textcard_10.setScaledContents(False)
        self.textcard_10.setAlignment(Qt.AlignCenter)
        self.textcard_10.setWordWrap(False)

        self.gridLayout_5.addWidget(self.textcard_10, 0, 0, 1, 1)

        self.textcard_11 = QLabel(self.frame_94)
        self.textcard_11.setObjectName(u"textcard_11")
        self.textcard_11.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard_11.setTextFormat(Qt.AutoText)
        self.textcard_11.setScaledContents(False)
        self.textcard_11.setAlignment(Qt.AlignCenter)
        self.textcard_11.setWordWrap(False)

        self.gridLayout_5.addWidget(self.textcard_11, 4, 0, 1, 1)

        self.adcfinal_2 = QLineEdit(self.frame_94)
        self.adcfinal_2.setObjectName(u"adcfinal_2")
        self.adcfinal_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adcfinal_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.adcfinal_2, 3, 1, 1, 1)

        self.adcvencimento_2 = QLineEdit(self.frame_94)
        self.adcvencimento_2.setObjectName(u"adcvencimento_2")
        self.adcvencimento_2.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adcvencimento_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.adcvencimento_2, 4, 1, 1, 1)


        self.gridLayout_6.addWidget(self.frame_94, 1, 0, 1, 3)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_26, 0, 1, 1, 1)

        self.stackedWidgetadc_2.addWidget(self.page_10)

        self.horizontalLayout_84.addWidget(self.stackedWidgetadc_2)


        self.verticalLayout_101.addWidget(self.frame_90)

        self.frame_257 = QFrame(self.frame_89)
        self.frame_257.setObjectName(u"frame_257")
        self.frame_257.setMinimumSize(QSize(120, 67))
        self.frame_257.setMaximumSize(QSize(16777215, 67))
        self.frame_257.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_257.setFrameShape(QFrame.StyledPanel)
        self.frame_257.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_257)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.frame_258 = QFrame(self.frame_257)
        self.frame_258.setObjectName(u"frame_258")
        self.frame_258.setMinimumSize(QSize(40, 0))
        self.frame_258.setMaximumSize(QSize(40, 40))
        self.frame_258.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/parcelas2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_258.setFrameShape(QFrame.StyledPanel)
        self.frame_258.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_100.addWidget(self.frame_258)

        self.frame_259 = QFrame(self.frame_257)
        self.frame_259.setObjectName(u"frame_259")
        self.frame_259.setMinimumSize(QSize(190, 0))
        self.frame_259.setMaximumSize(QSize(190, 16777215))
        self.frame_259.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_259.setFrameShape(QFrame.StyledPanel)
        self.frame_259.setFrameShadow(QFrame.Raised)
        self.verticalLayout_159 = QVBoxLayout(self.frame_259)
        self.verticalLayout_159.setObjectName(u"verticalLayout_159")
        self.label_97 = QLabel(self.frame_259)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setMinimumSize(QSize(0, 0))
        self.label_97.setMaximumSize(QSize(16777215, 28))
        self.label_97.setFont(font)
        self.label_97.setLayoutDirection(Qt.LeftToRight)
        self.label_97.setAutoFillBackground(False)
        self.label_97.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;")
        self.label_97.setAlignment(Qt.AlignCenter)

        self.verticalLayout_159.addWidget(self.label_97)


        self.horizontalLayout_100.addWidget(self.frame_259)

        self.frame_260 = QFrame(self.frame_257)
        self.frame_260.setObjectName(u"frame_260")
        self.frame_260.setMinimumSize(QSize(0, 0))
        self.frame_260.setMaximumSize(QSize(16777215, 16777215))
        self.frame_260.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_260.setFrameShape(QFrame.StyledPanel)
        self.frame_260.setFrameShadow(QFrame.Raised)
        self.verticalLayout_166 = QVBoxLayout(self.frame_260)
        self.verticalLayout_166.setObjectName(u"verticalLayout_166")
        self.comboBox_24 = QComboBox(self.frame_260)
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.setObjectName(u"comboBox_24")
        self.comboBox_24.setMaximumSize(QSize(16777215, 90))
        self.comboBox_24.setStyleSheet(u"border: 0px;\n"
"font: 25 12pt \"Microsoft YaHei Light\";\n"
"border-radius:3px;")

        self.verticalLayout_166.addWidget(self.comboBox_24)


        self.horizontalLayout_100.addWidget(self.frame_260)


        self.verticalLayout_101.addWidget(self.frame_257)

        self.frame_92 = QFrame(self.frame_89)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMaximumSize(QSize(16777215, 50))
        self.frame_92.setStyleSheet(u"background-color:none;\n"
"color: rgb(0, 0, 0);")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.add_bank = QPushButton(self.frame_92)
        self.add_bank.setObjectName(u"add_bank")
        self.add_bank.setMinimumSize(QSize(110, 30))
        self.add_bank.setMaximumSize(QSize(110, 25))
        self.add_bank.setFont(font)
        self.add_bank.setStyleSheet(u"\n"
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

        self.horizontalLayout_85.addWidget(self.add_bank)

        self.remover_bank = QPushButton(self.frame_92)
        self.remover_bank.setObjectName(u"remover_bank")
        self.remover_bank.setMinimumSize(QSize(110, 30))
        self.remover_bank.setMaximumSize(QSize(110, 25))
        self.remover_bank.setFont(font)
        self.remover_bank.setStyleSheet(u"\n"
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

        self.horizontalLayout_85.addWidget(self.remover_bank)

        self.update_bank = QPushButton(self.frame_92)
        self.update_bank.setObjectName(u"update_bank")
        self.update_bank.setMinimumSize(QSize(0, 30))
        self.update_bank.setMaximumSize(QSize(110, 25))
        self.update_bank.setStyleSheet(u"\n"
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

        self.horizontalLayout_85.addWidget(self.update_bank)


        self.verticalLayout_101.addWidget(self.frame_92)


        self.horizontalLayout_83.addWidget(self.frame_89)

        self.frame_96 = QFrame(self.page_Tabe_main3)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"border-radius:5px;")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_96)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.label_63 = QLabel(self.frame_96)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(0, 47))
        self.label_63.setMaximumSize(QSize(16777215, 40))
        self.label_63.setFont(font)
        self.label_63.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border-bottom: 1px solid rgba(255,255,255,30);\n"
"border-radius:0px;")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.verticalLayout_102.addWidget(self.label_63)

        self.frame_232 = QFrame(self.frame_96)
        self.frame_232.setObjectName(u"frame_232")
        self.frame_232.setMinimumSize(QSize(120, 0))
        self.frame_232.setMaximumSize(QSize(16777215, 67))
        self.frame_232.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;\n"
"font: 25 13pt \"Bahnschrift Light Condensed\";")
        self.frame_232.setFrameShape(QFrame.StyledPanel)
        self.frame_232.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_232)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.frame_233 = QFrame(self.frame_232)
        self.frame_233.setObjectName(u"frame_233")
        self.frame_233.setMinimumSize(QSize(40, 0))
        self.frame_233.setMaximumSize(QSize(40, 40))
        self.frame_233.setStyleSheet(u"border-image: url(:/icons-cards/src-page-cartoes/nulsmal.png);\n"
"background-color:rgba(255,255,255,0);\n"
"")
        self.frame_233.setFrameShape(QFrame.StyledPanel)
        self.frame_233.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_86.addWidget(self.frame_233)

        self.frame_234 = QFrame(self.frame_232)
        self.frame_234.setObjectName(u"frame_234")
        self.frame_234.setMinimumSize(QSize(190, 0))
        self.frame_234.setMaximumSize(QSize(190, 40))
        self.frame_234.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_234.setFrameShape(QFrame.StyledPanel)
        self.frame_234.setFrameShadow(QFrame.Raised)
        self.verticalLayout_105 = QVBoxLayout(self.frame_234)
        self.verticalLayout_105.setSpacing(0)
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.verticalLayout_105.setContentsMargins(0, 0, 0, 0)
        self.label_91 = QLabel(self.frame_234)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setMinimumSize(QSize(0, 27))
        self.label_91.setMaximumSize(QSize(16777215, 16777215))
        self.label_91.setFont(font5)
        self.label_91.setAutoFillBackground(False)
        self.label_91.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;")
        self.label_91.setAlignment(Qt.AlignCenter)

        self.verticalLayout_105.addWidget(self.label_91)


        self.horizontalLayout_86.addWidget(self.frame_234)

        self.frame_235 = QFrame(self.frame_232)
        self.frame_235.setObjectName(u"frame_235")
        self.frame_235.setMinimumSize(QSize(200, 0))
        self.frame_235.setMaximumSize(QSize(16777215, 16777215))
        self.frame_235.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_235.setFrameShape(QFrame.StyledPanel)
        self.frame_235.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.frame_235)
        self.horizontalLayout_99.setSpacing(0)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.frame_235)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setStyleSheet(u"border:none;")
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setReadOnly(True)

        self.horizontalLayout_99.addWidget(self.plainTextEdit)


        self.horizontalLayout_86.addWidget(self.frame_235)


        self.verticalLayout_102.addWidget(self.frame_232)

        self.frame_206 = QFrame(self.frame_96)
        self.frame_206.setObjectName(u"frame_206")
        self.frame_206.setMinimumSize(QSize(120, 0))
        self.frame_206.setMaximumSize(QSize(16777215, 67))
        self.frame_206.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_206.setFrameShape(QFrame.StyledPanel)
        self.frame_206.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_206)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.frame_207 = QFrame(self.frame_206)
        self.frame_207.setObjectName(u"frame_207")
        self.frame_207.setMinimumSize(QSize(40, 0))
        self.frame_207.setMaximumSize(QSize(40, 40))
        self.frame_207.setStyleSheet(u"border-image: url(:/icons-cards/src-page-cartoes/nulsmal.png);\n"
"background-color:rgba(255,255,255,0);\n"
"")
        self.frame_207.setFrameShape(QFrame.StyledPanel)
        self.frame_207.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_87.addWidget(self.frame_207)

        self.frame_208 = QFrame(self.frame_206)
        self.frame_208.setObjectName(u"frame_208")
        self.frame_208.setMinimumSize(QSize(190, 0))
        self.frame_208.setMaximumSize(QSize(190, 16777215))
        self.frame_208.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_208.setFrameShape(QFrame.StyledPanel)
        self.frame_208.setFrameShadow(QFrame.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_208)
        self.verticalLayout_106.setSpacing(0)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_106.setContentsMargins(0, 0, 0, 0)
        self.label_84 = QLabel(self.frame_208)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(0, 27))
        self.label_84.setMaximumSize(QSize(16777215, 18))
        self.label_84.setFont(font)
        self.label_84.setAutoFillBackground(False)
        self.label_84.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;")
        self.label_84.setAlignment(Qt.AlignCenter)

        self.verticalLayout_106.addWidget(self.label_84)


        self.horizontalLayout_87.addWidget(self.frame_208)

        self.frame_236 = QFrame(self.frame_206)
        self.frame_236.setObjectName(u"frame_236")
        self.frame_236.setMinimumSize(QSize(200, 0))
        self.frame_236.setMaximumSize(QSize(16777215, 16777215))
        self.frame_236.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_236.setFrameShape(QFrame.StyledPanel)
        self.frame_236.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame_236)
        self.horizontalLayout_98.setSpacing(0)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_2 = QPlainTextEdit(self.frame_236)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setStyleSheet(u"border:none;")
        self.plainTextEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_2.setReadOnly(True)

        self.horizontalLayout_98.addWidget(self.plainTextEdit_2)


        self.horizontalLayout_87.addWidget(self.frame_236)


        self.verticalLayout_102.addWidget(self.frame_206)

        self.frame_237 = QFrame(self.frame_96)
        self.frame_237.setObjectName(u"frame_237")
        self.frame_237.setMinimumSize(QSize(120, 0))
        self.frame_237.setMaximumSize(QSize(16777215, 67))
        self.frame_237.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_237.setFrameShape(QFrame.StyledPanel)
        self.frame_237.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_237)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.frame_238 = QFrame(self.frame_237)
        self.frame_238.setObjectName(u"frame_238")
        self.frame_238.setMinimumSize(QSize(40, 0))
        self.frame_238.setMaximumSize(QSize(40, 40))
        self.frame_238.setStyleSheet(u"border-image: url(:/backgroud/src-page-cartoes/etiqueta.png);\n"
"background-color:rgba(255,255,255,0);\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;")
        self.frame_238.setFrameShape(QFrame.StyledPanel)
        self.frame_238.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_88.addWidget(self.frame_238)

        self.frame_239 = QFrame(self.frame_237)
        self.frame_239.setObjectName(u"frame_239")
        self.frame_239.setMinimumSize(QSize(190, 0))
        self.frame_239.setMaximumSize(QSize(190, 16777215))
        self.frame_239.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_239.setFrameShape(QFrame.StyledPanel)
        self.frame_239.setFrameShadow(QFrame.Raised)
        self.verticalLayout_161 = QVBoxLayout(self.frame_239)
        self.verticalLayout_161.setSpacing(0)
        self.verticalLayout_161.setObjectName(u"verticalLayout_161")
        self.verticalLayout_161.setContentsMargins(0, 0, 0, 0)
        self.label_92 = QLabel(self.frame_239)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setMinimumSize(QSize(0, 0))
        self.label_92.setMaximumSize(QSize(16777215, 18))
        self.label_92.setFont(font)
        self.label_92.setAutoFillBackground(False)
        self.label_92.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;")
        self.label_92.setAlignment(Qt.AlignCenter)

        self.verticalLayout_161.addWidget(self.label_92)


        self.horizontalLayout_88.addWidget(self.frame_239)

        self.frame_240 = QFrame(self.frame_237)
        self.frame_240.setObjectName(u"frame_240")
        self.frame_240.setMinimumSize(QSize(0, 0))
        self.frame_240.setMaximumSize(QSize(16777215, 16777215))
        self.frame_240.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_240.setFrameShape(QFrame.StyledPanel)
        self.frame_240.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_240)
        self.horizontalLayout_97.setSpacing(0)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_3 = QPlainTextEdit(self.frame_240)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setStyleSheet(u"border:none;")
        self.plainTextEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_3.setReadOnly(True)

        self.horizontalLayout_97.addWidget(self.plainTextEdit_3)


        self.horizontalLayout_88.addWidget(self.frame_240)


        self.verticalLayout_102.addWidget(self.frame_237)

        self.frame_241 = QFrame(self.frame_96)
        self.frame_241.setObjectName(u"frame_241")
        self.frame_241.setMinimumSize(QSize(120, 0))
        self.frame_241.setMaximumSize(QSize(16777215, 67))
        self.frame_241.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_241.setFrameShape(QFrame.StyledPanel)
        self.frame_241.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_241)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.frame_242 = QFrame(self.frame_241)
        self.frame_242.setObjectName(u"frame_242")
        self.frame_242.setMinimumSize(QSize(40, 0))
        self.frame_242.setMaximumSize(QSize(40, 40))
        self.frame_242.setStyleSheet(u"border-image: url(:/backgroud/src-page-cartoes/calendarios.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_242.setFrameShape(QFrame.StyledPanel)
        self.frame_242.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_89.addWidget(self.frame_242)

        self.frame_243 = QFrame(self.frame_241)
        self.frame_243.setObjectName(u"frame_243")
        self.frame_243.setMinimumSize(QSize(190, 0))
        self.frame_243.setMaximumSize(QSize(190, 16777215))
        self.frame_243.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_243.setFrameShape(QFrame.StyledPanel)
        self.frame_243.setFrameShadow(QFrame.Raised)
        self.verticalLayout_167 = QVBoxLayout(self.frame_243)
        self.verticalLayout_167.setSpacing(0)
        self.verticalLayout_167.setObjectName(u"verticalLayout_167")
        self.verticalLayout_167.setContentsMargins(0, 0, 0, 0)
        self.label_93 = QLabel(self.frame_243)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setMinimumSize(QSize(0, 0))
        self.label_93.setMaximumSize(QSize(16777215, 18))
        self.label_93.setFont(font)
        self.label_93.setAutoFillBackground(False)
        self.label_93.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;")
        self.label_93.setAlignment(Qt.AlignCenter)

        self.verticalLayout_167.addWidget(self.label_93)


        self.horizontalLayout_89.addWidget(self.frame_243)

        self.frame_244 = QFrame(self.frame_241)
        self.frame_244.setObjectName(u"frame_244")
        self.frame_244.setMinimumSize(QSize(0, 0))
        self.frame_244.setMaximumSize(QSize(16777215, 16777215))
        self.frame_244.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_244.setFrameShape(QFrame.StyledPanel)
        self.frame_244.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_244)
        self.horizontalLayout_96.setSpacing(0)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_4 = QPlainTextEdit(self.frame_244)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setStyleSheet(u"border:none;")
        self.plainTextEdit_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_4.setReadOnly(True)

        self.horizontalLayout_96.addWidget(self.plainTextEdit_4)


        self.horizontalLayout_89.addWidget(self.frame_244)


        self.verticalLayout_102.addWidget(self.frame_241)

        self.label_64 = QLabel(self.frame_96)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(0, 47))
        self.label_64.setMaximumSize(QSize(16777215, 16777215))
        self.label_64.setFont(font)
        self.label_64.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border-bottom: 1px solid rgba(255,255,255,30);\n"
"border-radius:0px;")
        self.label_64.setAlignment(Qt.AlignCenter)

        self.verticalLayout_102.addWidget(self.label_64)

        self.frame_245 = QFrame(self.frame_96)
        self.frame_245.setObjectName(u"frame_245")
        self.frame_245.setMinimumSize(QSize(120, 0))
        self.frame_245.setMaximumSize(QSize(16777215, 67))
        self.frame_245.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_245.setFrameShape(QFrame.StyledPanel)
        self.frame_245.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_245)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.frame_246 = QFrame(self.frame_245)
        self.frame_246.setObjectName(u"frame_246")
        self.frame_246.setMinimumSize(QSize(40, 0))
        self.frame_246.setMaximumSize(QSize(40, 40))
        self.frame_246.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/money2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_246.setFrameShape(QFrame.StyledPanel)
        self.frame_246.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_91.addWidget(self.frame_246)

        self.frame_247 = QFrame(self.frame_245)
        self.frame_247.setObjectName(u"frame_247")
        self.frame_247.setMinimumSize(QSize(190, 0))
        self.frame_247.setMaximumSize(QSize(190, 16777215))
        self.frame_247.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_247.setFrameShape(QFrame.StyledPanel)
        self.frame_247.setFrameShadow(QFrame.Raised)
        self.verticalLayout_168 = QVBoxLayout(self.frame_247)
        self.verticalLayout_168.setSpacing(0)
        self.verticalLayout_168.setObjectName(u"verticalLayout_168")
        self.verticalLayout_168.setContentsMargins(0, 0, 0, 0)
        self.label_94 = QLabel(self.frame_247)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setMinimumSize(QSize(0, 0))
        self.label_94.setMaximumSize(QSize(16777215, 16777215))
        self.label_94.setFont(font)
        self.label_94.setAutoFillBackground(False)
        self.label_94.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;")
        self.label_94.setAlignment(Qt.AlignCenter)

        self.verticalLayout_168.addWidget(self.label_94)


        self.horizontalLayout_91.addWidget(self.frame_247)

        self.frame_248 = QFrame(self.frame_245)
        self.frame_248.setObjectName(u"frame_248")
        self.frame_248.setMinimumSize(QSize(0, 0))
        self.frame_248.setMaximumSize(QSize(16777215, 16777215))
        self.frame_248.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_248.setFrameShape(QFrame.StyledPanel)
        self.frame_248.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_248)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_5 = QPlainTextEdit(self.frame_248)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setStyleSheet(u"border:none;")
        self.plainTextEdit_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_5.setReadOnly(True)

        self.horizontalLayout_95.addWidget(self.plainTextEdit_5)


        self.horizontalLayout_91.addWidget(self.frame_248)


        self.verticalLayout_102.addWidget(self.frame_245)

        self.frame_265 = QFrame(self.frame_96)
        self.frame_265.setObjectName(u"frame_265")
        self.frame_265.setMinimumSize(QSize(120, 0))
        self.frame_265.setMaximumSize(QSize(16777215, 67))
        self.frame_265.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_265.setFrameShape(QFrame.StyledPanel)
        self.frame_265.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.frame_265)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.frame_266 = QFrame(self.frame_265)
        self.frame_266.setObjectName(u"frame_266")
        self.frame_266.setMinimumSize(QSize(40, 0))
        self.frame_266.setMaximumSize(QSize(40, 40))
        self.frame_266.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/parcelas2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_266.setFrameShape(QFrame.StyledPanel)
        self.frame_266.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_103.addWidget(self.frame_266)

        self.frame_267 = QFrame(self.frame_265)
        self.frame_267.setObjectName(u"frame_267")
        self.frame_267.setMinimumSize(QSize(190, 0))
        self.frame_267.setMaximumSize(QSize(190, 16777215))
        self.frame_267.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_267.setFrameShape(QFrame.StyledPanel)
        self.frame_267.setFrameShadow(QFrame.Raised)
        self.verticalLayout_173 = QVBoxLayout(self.frame_267)
        self.verticalLayout_173.setSpacing(0)
        self.verticalLayout_173.setObjectName(u"verticalLayout_173")
        self.verticalLayout_173.setContentsMargins(0, 0, 0, 0)
        self.label_99 = QLabel(self.frame_267)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setMinimumSize(QSize(0, 0))
        self.label_99.setMaximumSize(QSize(16777215, 16777215))
        self.label_99.setFont(font)
        self.label_99.setLayoutDirection(Qt.LeftToRight)
        self.label_99.setAutoFillBackground(False)
        self.label_99.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;")
        self.label_99.setAlignment(Qt.AlignCenter)

        self.verticalLayout_173.addWidget(self.label_99)


        self.horizontalLayout_103.addWidget(self.frame_267)

        self.frame_268 = QFrame(self.frame_265)
        self.frame_268.setObjectName(u"frame_268")
        self.frame_268.setMinimumSize(QSize(0, 0))
        self.frame_268.setMaximumSize(QSize(16777215, 16777215))
        self.frame_268.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_268.setFrameShape(QFrame.StyledPanel)
        self.frame_268.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.frame_268)
        self.horizontalLayout_104.setSpacing(0)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_9 = QPlainTextEdit(self.frame_268)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")
        self.plainTextEdit_9.setStyleSheet(u"border:none;")
        self.plainTextEdit_9.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_9.setReadOnly(True)

        self.horizontalLayout_104.addWidget(self.plainTextEdit_9)


        self.horizontalLayout_103.addWidget(self.frame_268)


        self.verticalLayout_102.addWidget(self.frame_265)

        self.frame_249 = QFrame(self.frame_96)
        self.frame_249.setObjectName(u"frame_249")
        self.frame_249.setMinimumSize(QSize(120, 0))
        self.frame_249.setMaximumSize(QSize(16777215, 67))
        self.frame_249.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_249.setFrameShape(QFrame.StyledPanel)
        self.frame_249.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_249)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.frame_250 = QFrame(self.frame_249)
        self.frame_250.setObjectName(u"frame_250")
        self.frame_250.setMinimumSize(QSize(40, 0))
        self.frame_250.setMaximumSize(QSize(40, 40))
        self.frame_250.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/credt.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_250.setFrameShape(QFrame.StyledPanel)
        self.frame_250.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_92.addWidget(self.frame_250)

        self.frame_251 = QFrame(self.frame_249)
        self.frame_251.setObjectName(u"frame_251")
        self.frame_251.setMinimumSize(QSize(190, 0))
        self.frame_251.setMaximumSize(QSize(190, 16777215))
        self.frame_251.setFont(font)
        self.frame_251.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_251.setFrameShape(QFrame.StyledPanel)
        self.frame_251.setFrameShadow(QFrame.Raised)
        self.verticalLayout_170 = QVBoxLayout(self.frame_251)
        self.verticalLayout_170.setSpacing(0)
        self.verticalLayout_170.setObjectName(u"verticalLayout_170")
        self.verticalLayout_170.setContentsMargins(0, 0, 0, 0)
        self.label_95 = QLabel(self.frame_251)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setMinimumSize(QSize(0, 0))
        self.label_95.setMaximumSize(QSize(16777215, 16777215))
        self.label_95.setFont(font)
        self.label_95.setAutoFillBackground(False)
        self.label_95.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;")
        self.label_95.setAlignment(Qt.AlignCenter)

        self.verticalLayout_170.addWidget(self.label_95)


        self.horizontalLayout_92.addWidget(self.frame_251)

        self.frame_252 = QFrame(self.frame_249)
        self.frame_252.setObjectName(u"frame_252")
        self.frame_252.setMinimumSize(QSize(0, 0))
        self.frame_252.setMaximumSize(QSize(16777215, 16777215))
        self.frame_252.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_252.setFrameShape(QFrame.StyledPanel)
        self.frame_252.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_252)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_6 = QPlainTextEdit(self.frame_252)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setStyleSheet(u"border:none;")
        self.plainTextEdit_6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_6.setReadOnly(True)

        self.horizontalLayout_90.addWidget(self.plainTextEdit_6)


        self.horizontalLayout_92.addWidget(self.frame_252)


        self.verticalLayout_102.addWidget(self.frame_249)

        self.frame_261 = QFrame(self.frame_96)
        self.frame_261.setObjectName(u"frame_261")
        self.frame_261.setMinimumSize(QSize(120, 0))
        self.frame_261.setMaximumSize(QSize(16777215, 67))
        self.frame_261.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_261.setFrameShape(QFrame.StyledPanel)
        self.frame_261.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_261)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.frame_262 = QFrame(self.frame_261)
        self.frame_262.setObjectName(u"frame_262")
        self.frame_262.setMinimumSize(QSize(40, 0))
        self.frame_262.setMaximumSize(QSize(40, 40))
        self.frame_262.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/parcelas2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_262.setFrameShape(QFrame.StyledPanel)
        self.frame_262.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_101.addWidget(self.frame_262)

        self.frame_263 = QFrame(self.frame_261)
        self.frame_263.setObjectName(u"frame_263")
        self.frame_263.setMinimumSize(QSize(190, 0))
        self.frame_263.setMaximumSize(QSize(190, 16777215))
        self.frame_263.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_263.setFrameShape(QFrame.StyledPanel)
        self.frame_263.setFrameShadow(QFrame.Raised)
        self.verticalLayout_172 = QVBoxLayout(self.frame_263)
        self.verticalLayout_172.setSpacing(0)
        self.verticalLayout_172.setObjectName(u"verticalLayout_172")
        self.verticalLayout_172.setContentsMargins(0, 0, 0, 0)
        self.label_98 = QLabel(self.frame_263)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setMinimumSize(QSize(0, 0))
        self.label_98.setMaximumSize(QSize(16777215, 16777215))
        self.label_98.setFont(font)
        self.label_98.setLayoutDirection(Qt.LeftToRight)
        self.label_98.setAutoFillBackground(False)
        self.label_98.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;")
        self.label_98.setAlignment(Qt.AlignCenter)

        self.verticalLayout_172.addWidget(self.label_98)


        self.horizontalLayout_101.addWidget(self.frame_263)

        self.frame_264 = QFrame(self.frame_261)
        self.frame_264.setObjectName(u"frame_264")
        self.frame_264.setMinimumSize(QSize(0, 0))
        self.frame_264.setMaximumSize(QSize(16777215, 16777215))
        self.frame_264.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_264.setFrameShape(QFrame.StyledPanel)
        self.frame_264.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_102 = QHBoxLayout(self.frame_264)
        self.horizontalLayout_102.setSpacing(0)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalLayout_102.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_8 = QPlainTextEdit(self.frame_264)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setStyleSheet(u"border:none;")
        self.plainTextEdit_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_8.setReadOnly(True)

        self.horizontalLayout_102.addWidget(self.plainTextEdit_8)


        self.horizontalLayout_101.addWidget(self.frame_264)


        self.verticalLayout_102.addWidget(self.frame_261)

        self.frame_253 = QFrame(self.frame_96)
        self.frame_253.setObjectName(u"frame_253")
        self.frame_253.setMinimumSize(QSize(120, 0))
        self.frame_253.setMaximumSize(QSize(16777215, 67))
        self.frame_253.setStyleSheet(u"background-color:rgba(255,255,255,10);\n"
"border-radius:5px;")
        self.frame_253.setFrameShape(QFrame.StyledPanel)
        self.frame_253.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_253)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.frame_254 = QFrame(self.frame_253)
        self.frame_254.setObjectName(u"frame_254")
        self.frame_254.setMinimumSize(QSize(40, 0))
        self.frame_254.setMaximumSize(QSize(40, 40))
        self.frame_254.setStyleSheet(u"background-image: url(:/backgroud/src-page-cartoes/parcelas2.png);\n"
"\n"
"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_254.setFrameShape(QFrame.StyledPanel)
        self.frame_254.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_93.addWidget(self.frame_254)

        self.frame_255 = QFrame(self.frame_253)
        self.frame_255.setObjectName(u"frame_255")
        self.frame_255.setMinimumSize(QSize(190, 0))
        self.frame_255.setMaximumSize(QSize(190, 16777215))
        self.frame_255.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_255.setFrameShape(QFrame.StyledPanel)
        self.frame_255.setFrameShadow(QFrame.Raised)
        self.verticalLayout_171 = QVBoxLayout(self.frame_255)
        self.verticalLayout_171.setSpacing(0)
        self.verticalLayout_171.setObjectName(u"verticalLayout_171")
        self.verticalLayout_171.setContentsMargins(0, 0, 0, 0)
        self.label_96 = QLabel(self.frame_255)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setMinimumSize(QSize(0, 0))
        self.label_96.setMaximumSize(QSize(16777215, 16777215))
        self.label_96.setFont(font)
        self.label_96.setLayoutDirection(Qt.LeftToRight)
        self.label_96.setAutoFillBackground(False)
        self.label_96.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;")
        self.label_96.setAlignment(Qt.AlignCenter)

        self.verticalLayout_171.addWidget(self.label_96)


        self.horizontalLayout_93.addWidget(self.frame_255)

        self.frame_256 = QFrame(self.frame_253)
        self.frame_256.setObjectName(u"frame_256")
        self.frame_256.setMinimumSize(QSize(0, 0))
        self.frame_256.setMaximumSize(QSize(16777215, 16777215))
        self.frame_256.setStyleSheet(u"border: 1px solid rgba(255,255,255,20);\n"
"\n"
"background-color:rgba(255,255,255,0);")
        self.frame_256.setFrameShape(QFrame.StyledPanel)
        self.frame_256.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_256)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit_7 = QPlainTextEdit(self.frame_256)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setStyleSheet(u"border:none;")
        self.plainTextEdit_7.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_7.setReadOnly(True)

        self.horizontalLayout_94.addWidget(self.plainTextEdit_7)


        self.horizontalLayout_93.addWidget(self.frame_256)


        self.verticalLayout_102.addWidget(self.frame_253)


        self.horizontalLayout_83.addWidget(self.frame_96)

        self.table_active_banks = QTableWidget(self.page_Tabe_main3)
        if (self.table_active_banks.columnCount() < 7):
            self.table_active_banks.setColumnCount(7)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_active_banks.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_active_banks.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_active_banks.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_active_banks.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_active_banks.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_active_banks.setHorizontalHeaderItem(5, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_active_banks.setHorizontalHeaderItem(6, __qtablewidgetitem22)
        self.table_active_banks.setObjectName(u"table_active_banks")
        self.table_active_banks.setMinimumSize(QSize(0, 0))
        self.table_active_banks.setMaximumSize(QSize(16777215, 16777215))
        self.table_active_banks.setTabletTracking(False)
        self.table_active_banks.setStyleSheet(u"QWidget {\n"
"	\n"
"\n"
"	border-radius:0px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(53, 53, 53);\n"
"    font-size: 11;\n"
"	border:none;\n"
"	width:45px;\n"
"	height: 50px;\n"
"\n"
"	border-radius:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #fffff8;\n"
"    font-size: 11pt;\n"
"	border-radius:0px;\n"
"	border-radius:0px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"	border-radius:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableView:item {\n"
"  border-bottom: 0.5px solid qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:0.45677 rgba(0, 0, 0, 0), stop:0.479846 rgba(255, 255, 255, 255), stop:0.50571 rgba(239, 236, 55, 0), stop:1 rgba(239, 236, 55, 0));\n"
"	border-radius:0px;\n"
"\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	\n"
"	background-color: rgb(92, 155, 179);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.table_active_banks.setFrameShape(QFrame.StyledPanel)
        self.table_active_banks.setFrameShadow(QFrame.Plain)
        self.table_active_banks.setAutoScroll(True)
        self.table_active_banks.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_active_banks.setTabKeyNavigation(True)
        self.table_active_banks.setDragDropOverwriteMode(True)
        self.table_active_banks.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.table_active_banks.setAlternatingRowColors(False)
        self.table_active_banks.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table_active_banks.setShowGrid(False)
        self.table_active_banks.setGridStyle(Qt.DashLine)
        self.table_active_banks.setSortingEnabled(False)
        self.table_active_banks.setWordWrap(True)
        self.table_active_banks.horizontalHeader().setVisible(False)
        self.table_active_banks.horizontalHeader().setCascadingSectionResizes(True)
        self.table_active_banks.horizontalHeader().setDefaultSectionSize(113)
        self.table_active_banks.horizontalHeader().setHighlightSections(True)
        self.table_active_banks.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_active_banks.horizontalHeader().setStretchLastSection(False)
        self.table_active_banks.verticalHeader().setVisible(False)
        self.table_active_banks.verticalHeader().setCascadingSectionResizes(False)
        self.table_active_banks.verticalHeader().setMinimumSectionSize(23)
        self.table_active_banks.verticalHeader().setDefaultSectionSize(30)
        self.table_active_banks.verticalHeader().setHighlightSections(True)
        self.table_active_banks.verticalHeader().setProperty("showSortIndicator", False)
        self.table_active_banks.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_83.addWidget(self.table_active_banks)

        self.chart_gastos_all_2.addTab(self.page_Tabe_main3, icon21, "")
        self.page_Tabe_main4 = QWidget()
        self.page_Tabe_main4.setObjectName(u"page_Tabe_main4")
        self.page_Tabe_main4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.chart_gastos_all_2.addTab(self.page_Tabe_main4, icon19, "")

        self.verticalLayout_56.addWidget(self.chart_gastos_all_2)


        self.verticalLayout_108.addWidget(self.main_dash_bottom_2)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)

        self.verticalLayout_34.addWidget(self.scrollArea_9)

        self.detalhes_cartao_2.addWidget(self.dashboard_cards_2)

        self.horizontalLayout_51.addWidget(self.detalhes_cartao_2)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.horizontalLayout_50.addWidget(self.scrollArea_6)


        self.verticalLayout_33.addWidget(self.frame_42)


        self.verticalLayout_2.addWidget(self.frame_40)

        self.stackedWidget_2.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.verticalLayout_38 = QVBoxLayout(self.page_3)
        self.verticalLayout_38.setSpacing(30)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.backgroud_cartao = QFrame(self.page_3)
        self.backgroud_cartao.setObjectName(u"backgroud_cartao")
        self.backgroud_cartao.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
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
        self.cartao_options.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
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
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px;	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"}")
        icon25 = QIcon()
        icon25.addFile(u":/backgroud/src-page-cartoes/cards.png", QSize(), QIcon.Normal, QIcon.Off)
        self.grid.setIcon(icon25)
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
"	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px;	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"}")
        icon26 = QIcon()
        icon26.addFile(u":/backgroud/src-page-cartoes/card_config.png", QSize(), QIcon.Normal, QIcon.Off)
        self.grid_2.setIcon(icon26)
        self.grid_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.grid_2)

        self.horizontalSpacer_4 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout_39.addWidget(self.cartao_options)

        self.stackedWidget_3 = QStackedWidget(self.backgroud_cartao)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMinimumSize(QSize(0, 0))
        self.stackedWidget_3.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color:rgba(255,255,255,0);")
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
"    width: 5px;\n"
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
"/* BTN BOTTOM -"
                        " SCROLLBAR */\n"
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
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.content_cartao = QFrame(self.scrollAreaWidgetContents_2)
        self.content_cartao.setObjectName(u"content_cartao")
        self.content_cartao.setMinimumSize(QSize(0, 0))
        self.content_cartao.setMaximumSize(QSize(440, 16777215))
        self.content_cartao.setStyleSheet(u"background-color:rgba(255,255,255,0);")
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
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 440, 870))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setSpacing(20)
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
        self.detalhes_cartaoPage1.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.verticalLayout_40 = QVBoxLayout(self.detalhes_cartaoPage1)
        self.verticalLayout_40.setSpacing(30)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 10, 0, 0)
        self.CONTAINER_geral = QFrame(self.detalhes_cartaoPage1)
        self.CONTAINER_geral.setObjectName(u"CONTAINER_geral")
        self.CONTAINER_geral.setMinimumSize(QSize(0, 0))
        self.CONTAINER_geral.setStyleSheet(u"QFrame{\n"
"	background-color:rgba(255,255,255,0);\n"
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy6)
        self.frame_29.setMinimumSize(QSize(0, 0))
        self.frame_29.setToolTipDuration(0)
        self.frame_29.setAutoFillBackground(False)
        self.frame_29.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_29)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(9, -1, 9, -1)
        self.frame_12 = QFrame(self.frame_29)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(200, 200))
        self.frame_12.setMaximumSize(QSize(16777215, 16777215))
        self.frame_12.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, 9, 0)
        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(80, 0))
        self.frame_15.setMaximumSize(QSize(80, 16777215))
        self.frame_15.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border:1px solid rgba(255,255,255,40);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_15)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.hide_cards_det = QPushButton(self.frame_15)
        self.hide_cards_det.setObjectName(u"hide_cards_det")
        self.hide_cards_det.setMinimumSize(QSize(40, 53))
        self.hide_cards_det.setMaximumSize(QSize(16777215, 16777215))
        self.hide_cards_det.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        self.hide_cards_det.setIcon(icon12)
        self.hide_cards_det.setIconSize(QSize(40, 40))

        self.verticalLayout_17.addWidget(self.hide_cards_det)

        self.show_cards_det = QPushButton(self.frame_15)
        self.show_cards_det.setObjectName(u"show_cards_det")
        self.show_cards_det.setMinimumSize(QSize(40, 53))
        self.show_cards_det.setMaximumSize(QSize(16777215, 16777215))
        self.show_cards_det.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        self.show_cards_det.setIcon(icon13)
        self.show_cards_det.setIconSize(QSize(40, 40))

        self.verticalLayout_17.addWidget(self.show_cards_det)

        self.back_main_dash = QPushButton(self.frame_15)
        self.back_main_dash.setObjectName(u"back_main_dash")
        self.back_main_dash.setMinimumSize(QSize(40, 53))
        self.back_main_dash.setMaximumSize(QSize(16777215, 16777215))
        self.back_main_dash.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        icon27 = QIcon()
        icon27.addFile(u":/menu/home-card.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_main_dash.setIcon(icon27)
        self.back_main_dash.setIconSize(QSize(35, 35))

        self.verticalLayout_17.addWidget(self.back_main_dash)


        self.horizontalLayout_11.addWidget(self.frame_15)

        self.circularProgressBarBase_2 = QFrame(self.frame_12)
        self.circularProgressBarBase_2.setObjectName(u"circularProgressBarBase_2")
        self.circularProgressBarBase_2.setMinimumSize(QSize(200, 200))
        self.circularProgressBarBase_2.setMaximumSize(QSize(200, 200))
        self.circularProgressBarBase_2.setStyleSheet(u"border:none;\n"
"border-image:none;\n"
"background-color: rgba(255, 255, 255,30);\n"
"border:1px solid rgba(255,255,255,40);")
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
"	background-color: rgb(54, 54, 54);\n"
"border:none;\n"
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
        sizePolicy4.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy4)
        self.frame_30.setMinimumSize(QSize(666, 100))
        self.frame_30.setMaximumSize(QSize(16777215, 16777215))
        self.frame_30.setStyleSheet(u"border:none;\n"
"border-image:none;\n"
"")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_30)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.date_gui_4 = QFrame(self.frame_30)
        self.date_gui_4.setObjectName(u"date_gui_4")
        self.date_gui_4.setMinimumSize(QSize(0, 20))
        self.date_gui_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")
        self.date_gui_4.setFrameShape(QFrame.StyledPanel)
        self.date_gui_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.date_gui_4)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(9, 9, 9, 9)
        self.progressbar_indvidual = QProgressBar(self.date_gui_4)
        self.progressbar_indvidual.setObjectName(u"progressbar_indvidual")
        self.progressbar_indvidual.setMaximumSize(QSize(16777215, 30))
        self.progressbar_indvidual.setStyleSheet(u"QProgressBar\n"
"{\n"
"    background: green;\n"
"    color: black;\n"
"    border-style: outset;\n"
"    border-color:  black;\n"
"    border-radius: 7px;\n"
"	border:none;\n"
"\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"   		\n"
"	background-color: rgb(92, 155, 179);\n"
"	border-top-left-radius:7px;\n"
"	 border-bottom-left-radius:7px;\n"
"\n"
"}")
        self.progressbar_indvidual.setValue(90)
        self.progressbar_indvidual.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.progressbar_indvidual)


        self.verticalLayout_21.addWidget(self.date_gui_4)

        self.frame_50 = QFrame(self.frame_30)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(1000, 16777215))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_50)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_50)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 0))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_70.setSpacing(10)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 10, 0, 0)
        self.labelTitle_8 = QLabel(self.frame_16)
        self.labelTitle_8.setObjectName(u"labelTitle_8")
        self.labelTitle_8.setFont(font)
        self.labelTitle_8.setLayoutDirection(Qt.LeftToRight)
        self.labelTitle_8.setAutoFillBackground(False)
        self.labelTitle_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")
        self.labelTitle_8.setFrameShape(QFrame.NoFrame)
        self.labelTitle_8.setFrameShadow(QFrame.Plain)
        self.labelTitle_8.setScaledContents(False)
        self.labelTitle_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_70.addWidget(self.labelTitle_8)

        self.labelTitle_10 = QLabel(self.frame_16)
        self.labelTitle_10.setObjectName(u"labelTitle_10")
        self.labelTitle_10.setFont(font)
        self.labelTitle_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")
        self.labelTitle_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_70.addWidget(self.labelTitle_10)


        self.verticalLayout_20.addWidget(self.frame_16)


        self.verticalLayout_21.addWidget(self.frame_50)


        self.horizontalLayout_11.addWidget(self.frame_30)


        self.verticalLayout_46.addWidget(self.frame_12)

        self.frame_60 = QFrame(self.frame_29)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMinimumSize(QSize(0, 0))
        self.frame_60.setMaximumSize(QSize(16777215, 90))
        self.frame_60.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 6, 10, 6)
        self.compras = QPushButton(self.frame_60)
        self.compras.setObjectName(u"compras")
        self.compras.setMinimumSize(QSize(0, 50))
        self.compras.setMaximumSize(QSize(16777215, 16777215))
        self.compras.setTabletTracking(False)
        self.compras.setStyleSheet(u"QPushButton{\n"
"	\n"
"\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	border-top-right-radius:0px;\n"
"	border-bottom-right-radius:0px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        icon28 = QIcon()
        icon28.addFile(u":/backgroud/src-page-cartoes/shoop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.compras.setIcon(icon28)
        self.compras.setIconSize(QSize(35, 35))

        self.horizontalLayout_17.addWidget(self.compras)

        self.nova_despesa = QPushButton(self.frame_60)
        self.nova_despesa.setObjectName(u"nova_despesa")
        self.nova_despesa.setMinimumSize(QSize(0, 0))
        self.nova_despesa.setMaximumSize(QSize(16777215, 50))
        self.nova_despesa.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(46, 46, 46);\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"	 border-bottom-right-radius:0px;\n"
"	 border-top-right-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        icon29 = QIcon()
        icon29.addFile(u":/backgroud/src-page-cartoes/cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nova_despesa.setIcon(icon29)
        self.nova_despesa.setIconSize(QSize(35, 35))

        self.horizontalLayout_17.addWidget(self.nova_despesa)

        self.pushButton_14 = QPushButton(self.frame_60)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(0, 0))
        self.pushButton_14.setMaximumSize(QSize(16777215, 50))
        self.pushButton_14.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(46, 46, 46);\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"	 border-bottom-right-radius:0px;\n"
"	 border-top-right-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        icon30 = QIcon()
        icon30.addFile(u":/backgroud/src-page-cartoes/grafic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon30)
        self.pushButton_14.setIconSize(QSize(35, 35))

        self.horizontalLayout_17.addWidget(self.pushButton_14)

        self.faturas = QPushButton(self.frame_60)
        self.faturas.setObjectName(u"faturas")
        self.faturas.setMinimumSize(QSize(0, 0))
        self.faturas.setMaximumSize(QSize(16777215, 50))
        self.faturas.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(46, 46, 46);\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"	 border-bottom-right-radius:0px;\n"
"	 border-top-right-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        icon31 = QIcon()
        icon31.addFile(u":/backgroud/src-page-cartoes/calendarios.png", QSize(), QIcon.Normal, QIcon.Off)
        self.faturas.setIcon(icon31)
        self.faturas.setIconSize(QSize(30, 30))

        self.horizontalLayout_17.addWidget(self.faturas)

        self.pushButton_12 = QPushButton(self.frame_60)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(0, 0))
        self.pushButton_12.setMaximumSize(QSize(16777215, 50))
        self.pushButton_12.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        self.pushButton_12.setIconSize(QSize(30, 30))

        self.horizontalLayout_17.addWidget(self.pushButton_12)


        self.verticalLayout_46.addWidget(self.frame_60)

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
        self.verticalLayout_28.setContentsMargins(10, 0, 10, 0)
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
        sizePolicy1.setHeightForWidth(self.line_d.sizePolicy().hasHeightForWidth())
        self.line_d.setSizePolicy(sizePolicy1)
        self.line_d.setMaximumSize(QSize(16777215, 90))
        self.line_d.setStyleSheet(u"border: 0px;\n"
"border-radius:3px;\n"
"background-color: rgba(255, 255, 255, 30);")
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
"border-radius:3px;\n"
"background-color: rgba(255, 255, 255, 30);")
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
"border-radius:3px;\n"
"background-color: rgba(255, 255, 255, 30);")
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
        self.pushButton_2.setIcon(icon15)
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
        self.pushButton_3.setIcon(icon16)
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
        self.previus_month.setIcon(icon12)
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
        self.next_month.setIcon(icon16)

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
        self.previus_month_3.setIcon(icon12)
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
        self.next_month_3.setIcon(icon16)

        self.horizontalLayout_39.addWidget(self.next_month_3)

        self.extrat_meses.addWidget(self.page_8)

        self.verticalLayout_46.addWidget(self.extrat_meses)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"border:none;\n"
"background-color:rgba(255,255,255,0);")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_31)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(10, 0, 10, 0)
        self.scrollArea_2 = QScrollArea(self.frame_31)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); ")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1008, 512))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.verticalLayout_53 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.frame_62 = QFrame(self.scrollAreaWidgetContents)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setMinimumSize(QSize(0, 0))
        self.frame_62.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); ")
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
        __qtablewidgetitem23 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(3, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(4, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(5, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(6, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(7, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(8, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.extrato_cartao_0.setHorizontalHeaderItem(9, __qtablewidgetitem32)
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
"	background-color:rgb(53, 53, 53);\n"
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
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"}")
        self.apaga_compra.setIcon(icon19)

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
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"}")
        self.edit_compra.setIcon(icon21)

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
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"}")
        self.paga_fatura.setIcon(icon20)

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
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"}")
        self.parcela_fatura.setIcon(icon22)

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
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(33, 33, 33);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"}")
        self.filter_dates_btn.setIcon(icon23)

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

        self.datails_fatura_card_2 = QFrame(self.central_cards_main_2)
        self.datails_fatura_card_2.setObjectName(u"datails_fatura_card_2")
        self.datails_fatura_card_2.setMaximumSize(QSize(16777215, 80))
        self.datails_fatura_card_2.setStyleSheet(u"\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border-bottom-right-radius:0px;\n"
" border-bottom-left-radius:0px;")
        self.datails_fatura_card_2.setFrameShape(QFrame.StyledPanel)
        self.datails_fatura_card_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.datails_fatura_card_2)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.icon_2 = QFrame(self.datails_fatura_card_2)
        self.icon_2.setObjectName(u"icon_2")
        self.icon_2.setMaximumSize(QSize(48, 48))
        self.icon_2.setStyleSheet(u"border-bottom: 0px;\n"
"border-radius: 5px;\n"
"border-image: url();")
        self.icon_2.setFrameShape(QFrame.StyledPanel)
        self.icon_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_40.addWidget(self.icon_2)

        self.name_bank_2 = QLabel(self.datails_fatura_card_2)
        self.name_bank_2.setObjectName(u"name_bank_2")
        self.name_bank_2.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"background-color: none; \n"
"")
        self.name_bank_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.name_bank_2)

        self.set_limite_card_2 = QFrame(self.datails_fatura_card_2)
        self.set_limite_card_2.setObjectName(u"set_limite_card_2")
        self.set_limite_card_2.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 1px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"background-color: none; \n"
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
"\n"
"\n"
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
"background-color: none; \n"
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
"\n"
"\n"
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
"background-color: none; \n"
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
"\n"
"\n"
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
"background-color: none; \n"
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
"\n"
"\n"
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
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind.setHorizontalHeaderItem(4, __qtablewidgetitem37)
        self.table_faturas_ind.setObjectName(u"table_faturas_ind")
        self.table_faturas_ind.setFont(font2)
        self.table_faturas_ind.setStyleSheet(u"QWidget {\n"
"	\n"
"    color: #fffff8;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(53, 53, 53);\n"
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
        self.table_faturas_ind.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_faturas_ind.setIconSize(QSize(45, 40))
        self.table_faturas_ind.setTextElideMode(Qt.ElideLeft)
        self.table_faturas_ind.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_faturas_ind.setShowGrid(False)
        self.table_faturas_ind.setSortingEnabled(False)
        self.table_faturas_ind.horizontalHeader().setVisible(False)
        self.table_faturas_ind.horizontalHeader().setCascadingSectionResizes(True)
        self.table_faturas_ind.horizontalHeader().setDefaultSectionSize(189)
        self.table_faturas_ind.horizontalHeader().setHighlightSections(True)
        self.table_faturas_ind.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_faturas_ind.horizontalHeader().setStretchLastSection(True)
        self.table_faturas_ind.verticalHeader().setVisible(False)
        self.table_faturas_ind.verticalHeader().setCascadingSectionResizes(False)
        self.table_faturas_ind.verticalHeader().setStretchLastSection(False)

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
"border-radius:3px;")
        self.comboBox_2.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBox_2.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

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
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        self.pushButton_17.setCheckable(False)
        self.pushButton_17.setChecked(False)
        self.pushButton_17.setAutoExclusive(False)
        self.pushButton_17.setAutoDefault(False)
        self.pushButton_17.setFlat(False)

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
"border-radius:3px;")

        self.verticalLayout_68.addWidget(self.comboBox_3)


        self.horizontalLayout_19.addWidget(self.frame_85)


        self.verticalLayout_72.addWidget(self.frame_67)

        self.frame_18 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(120, 67))
        self.frame_18.setMaximumSize(QSize(16777215, 67))
        self.frame_18.setStyleSheet(u"\n"
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
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
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
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
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
        self.horizontalLayout_24 = QHBoxLayout(self.charts_indvidual)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.tabWidget = QTabWidget(self.charts_indvidual)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet(u"QTabWidget::tab-bar {\n"
"  background: gray;\n"
"\n"
"\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  background: rgb(46, 46, 46);\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 10px;\n"
"\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background:rgb(53, 53, 53);\n"
"  color: rgb(255, 255, 255);\n"
" }\n"
"\n"
"QTabWidget::pane { border-top-left-radius:0px; border-top-right-radius:0px;}")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideMiddle)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(True)
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tab_7.setMaximumSize(QSize(16777215, 16777215))
        self.tab_7.setStyleSheet(u"")
        self.verticalLayout_69 = QVBoxLayout(self.tab_7)
        self.verticalLayout_69.setSpacing(0)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(0, 0, 10, 0)
        self.chart_main_category = QFrame(self.tab_7)
        self.chart_main_category.setObjectName(u"chart_main_category")
        self.chart_main_category.setStyleSheet(u"border-radius:10px;")
        self.chart_main_category.setFrameShape(QFrame.StyledPanel)
        self.chart_main_category.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.chart_main_category)
        self.verticalLayout_70.setSpacing(0)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.verticalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.chart_main_category)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"background-color: ")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.frame_28)
        self.verticalLayout_74.setSpacing(0)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.verticalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.frame_chart_category = QVBoxLayout()
        self.frame_chart_category.setObjectName(u"frame_chart_category")

        self.verticalLayout_74.addLayout(self.frame_chart_category)


        self.verticalLayout_70.addWidget(self.frame_28)


        self.verticalLayout_69.addWidget(self.chart_main_category)

        self.tabWidget.addTab(self.tab_7, icon21, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_86 = QVBoxLayout(self.tab_8)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 10, 0)
        self.chart_main_evolution = QFrame(self.tab_8)
        self.chart_main_evolution.setObjectName(u"chart_main_evolution")
        self.chart_main_evolution.setStyleSheet(u"border-radius:10px;")
        self.chart_main_evolution.setFrameShape(QFrame.StyledPanel)
        self.chart_main_evolution.setFrameShadow(QFrame.Raised)
        self.verticalLayout_87 = QVBoxLayout(self.chart_main_evolution)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.frame_33 = QFrame(self.chart_main_evolution)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_33)
        self.verticalLayout_88.setSpacing(0)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.frame_chart_evolution_fat = QVBoxLayout()
        self.frame_chart_evolution_fat.setObjectName(u"frame_chart_evolution_fat")

        self.verticalLayout_88.addLayout(self.frame_chart_evolution_fat)


        self.verticalLayout_87.addWidget(self.frame_33)


        self.verticalLayout_86.addWidget(self.chart_main_evolution)

        self.tabWidget.addTab(self.tab_8, icon24, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.tab_9.setStyleSheet(u"")
        self.verticalLayout_89 = QVBoxLayout(self.tab_9)
        self.verticalLayout_89.setSpacing(0)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.verticalLayout_89.setContentsMargins(0, 0, 10, 0)
        self.chart_main_date = QFrame(self.tab_9)
        self.chart_main_date.setObjectName(u"chart_main_date")
        self.chart_main_date.setStyleSheet(u"border-radius:10px;")
        self.chart_main_date.setFrameShape(QFrame.StyledPanel)
        self.chart_main_date.setFrameShadow(QFrame.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.chart_main_date)
        self.verticalLayout_90.setSpacing(0)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.frame_36 = QFrame(self.chart_main_date)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;\n"
"")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_91 = QVBoxLayout(self.frame_36)
        self.verticalLayout_91.setSpacing(0)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.verticalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.frame_chart_date_day = QVBoxLayout()
        self.frame_chart_date_day.setObjectName(u"frame_chart_date_day")

        self.verticalLayout_91.addLayout(self.frame_chart_date_day)


        self.verticalLayout_90.addWidget(self.frame_36)


        self.verticalLayout_89.addWidget(self.chart_main_date)

        self.tabWidget.addTab(self.tab_9, icon23, "")

        self.horizontalLayout_24.addWidget(self.tabWidget)

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
        self.dashboard_cards.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.verticalLayout_32 = QVBoxLayout(self.dashboard_cards)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.scrollArea_8 = QScrollArea(self.dashboard_cards)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setStyleSheet(u"")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 1023, 875))
        self.scrollAreaWidgetContents_8.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.main_dasht_top = QFrame(self.scrollAreaWidgetContents_8)
        self.main_dasht_top.setObjectName(u"main_dasht_top")
        self.main_dasht_top.setMinimumSize(QSize(200, 200))
        self.main_dasht_top.setMaximumSize(QSize(16777215, 16777215))
        self.main_dasht_top.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.main_dasht_top.setFrameShape(QFrame.StyledPanel)
        self.main_dasht_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.main_dasht_top)
        self.horizontalLayout_64.setSpacing(10)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_64.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.main_dasht_top)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(80, 0))
        self.frame_2.setMaximumSize(QSize(80, 16777215))
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.hide_cards_main = QPushButton(self.frame_2)
        self.hide_cards_main.setObjectName(u"hide_cards_main")
        self.hide_cards_main.setMinimumSize(QSize(40, 53))
        self.hide_cards_main.setMaximumSize(QSize(16777215, 16777215))
        self.hide_cards_main.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        self.hide_cards_main.setIcon(icon12)
        self.hide_cards_main.setIconSize(QSize(40, 40))

        self.verticalLayout_16.addWidget(self.hide_cards_main)

        self.show_cards_main = QPushButton(self.frame_2)
        self.show_cards_main.setObjectName(u"show_cards_main")
        self.show_cards_main.setMinimumSize(QSize(40, 53))
        self.show_cards_main.setMaximumSize(QSize(16777215, 16777215))
        self.show_cards_main.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        self.show_cards_main.setIcon(icon13)
        self.show_cards_main.setIconSize(QSize(40, 40))

        self.verticalLayout_16.addWidget(self.show_cards_main)

        self.pushButton_20 = QPushButton(self.frame_2)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(40, 53))
        self.pushButton_20.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_20.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"	\n"
"	background-color: rgb(46, 46, 46);\n"
"\n"
"	border: 1px solid  rgb(55, 55, 55);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(53, 53, 53);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	background-color: rgb(31, 31, 31);\n"
"\n"
"}")
        self.pushButton_20.setIcon(icon14)
        self.pushButton_20.setIconSize(QSize(40, 40))

        self.verticalLayout_16.addWidget(self.pushButton_20)


        self.horizontalLayout_64.addWidget(self.frame_2)

        self.welcome = QFrame(self.main_dasht_top)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setMinimumSize(QSize(200, 200))
        self.welcome.setMaximumSize(QSize(200, 200))
        self.welcome.setStyleSheet(u"border:none;\n"
"border-image:none;\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")
        self.welcome.setFrameShape(QFrame.NoFrame)
        self.welcome.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.welcome)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_25 = QFrame(self.welcome)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 60))
        self.frame_25.setStyleSheet(u"background-color:none;\n"
"border:none;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_17 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_17)

        self.frame_34 = QFrame(self.frame_25)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMinimumSize(QSize(60, 0))
        self.frame_34.setStyleSheet(u"background-image: url(:/time/menu/night.png);\n"
"background-repeat:no-repeat;\n"
"background-position:center;\n"
"")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_46.addWidget(self.frame_34)

        self.horizontalSpacer_18 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_18)


        self.verticalLayout_18.addWidget(self.frame_25)

        self.label_36 = QLabel(self.welcome)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border:none;")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_36)

        self.label_38 = QLabel(self.welcome)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border:none;")
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_38)


        self.horizontalLayout_64.addWidget(self.welcome)

        self.frame_37 = QFrame(self.main_dasht_top)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMinimumSize(QSize(38, 100))
        self.frame_37.setMaximumSize(QSize(16777215, 16777215))
        self.frame_37.setStyleSheet(u"border:none;\n"
"border-image:none;")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_119 = QVBoxLayout(self.frame_37)
        self.verticalLayout_119.setSpacing(0)
        self.verticalLayout_119.setObjectName(u"verticalLayout_119")
        self.verticalLayout_119.setContentsMargins(0, 0, 0, 0)
        self.date_gui_3 = QFrame(self.frame_37)
        self.date_gui_3.setObjectName(u"date_gui_3")
        self.date_gui_3.setMinimumSize(QSize(0, 20))
        self.date_gui_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")
        self.date_gui_3.setFrameShape(QFrame.StyledPanel)
        self.date_gui_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.date_gui_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.progressBar = QProgressBar(self.date_gui_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 30))
        self.progressBar.setStyleSheet(u"QProgressBar\n"
"{\n"
"    background: green;\n"
"    color: black;\n"
"    border-style: outset;\n"
"	border:none;\n"
"    border-color:  black;\n"
"    border-radius: 7px;\n"
"\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"   		\n"
"	background-color: rgb(92, 155, 179);\n"
"	border-top-left-radius:7px;\n"
"	 border-bottom-left-radius:7px;\n"
"\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.progressBar)


        self.verticalLayout_119.addWidget(self.date_gui_3)

        self.frame_46 = QFrame(self.frame_37)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMaximumSize(QSize(1000, 16777215))
        self.frame_46.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_46)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.frame_46)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_66.setSpacing(10)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 10, 0, 0)
        self.labelTitle_12 = QLabel(self.frame_11)
        self.labelTitle_12.setObjectName(u"labelTitle_12")
        self.labelTitle_12.setFont(font)
        self.labelTitle_12.setLayoutDirection(Qt.LeftToRight)
        self.labelTitle_12.setAutoFillBackground(False)
        self.labelTitle_12.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")
        self.labelTitle_12.setFrameShape(QFrame.NoFrame)
        self.labelTitle_12.setFrameShadow(QFrame.Plain)
        self.labelTitle_12.setScaledContents(False)
        self.labelTitle_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.labelTitle_12)

        self.label_39 = QLabel(self.frame_11)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")

        self.horizontalLayout_66.addWidget(self.label_39)

        self.labelTitle_13 = QLabel(self.frame_11)
        self.labelTitle_13.setObjectName(u"labelTitle_13")
        self.labelTitle_13.setFont(font)
        self.labelTitle_13.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:1px solid rgba(255,255,255,40);")
        self.labelTitle_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.labelTitle_13)


        self.verticalLayout_15.addWidget(self.frame_11)


        self.verticalLayout_119.addWidget(self.frame_46)


        self.horizontalLayout_64.addWidget(self.frame_37)


        self.verticalLayout_14.addWidget(self.main_dasht_top)

        self.main_dash_midle = QFrame(self.scrollAreaWidgetContents_8)
        self.main_dash_midle.setObjectName(u"main_dash_midle")
        sizePolicy.setHeightForWidth(self.main_dash_midle.sizePolicy().hasHeightForWidth())
        self.main_dash_midle.setSizePolicy(sizePolicy)
        self.main_dash_midle.setMinimumSize(QSize(0, 0))
        self.main_dash_midle.setMaximumSize(QSize(16777215, 16777215))
        self.main_dash_midle.setStyleSheet(u"background-color: rgba(255, 255, 255, 10); \n"
"\n"
"border-bottom: 0px;\n"
"")
        self.main_dash_midle.setFrameShape(QFrame.StyledPanel)
        self.main_dash_midle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_122 = QVBoxLayout(self.main_dash_midle)
        self.verticalLayout_122.setSpacing(0)
        self.verticalLayout_122.setObjectName(u"verticalLayout_122")
        self.verticalLayout_122.setContentsMargins(0, 0, 0, 0)
        self.date_filters_fatura_4 = QFrame(self.main_dash_midle)
        self.date_filters_fatura_4.setObjectName(u"date_filters_fatura_4")
        self.date_filters_fatura_4.setMaximumSize(QSize(16777215, 50))
        self.date_filters_fatura_4.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px;\n"
"border-right: 0px;")
        self.date_filters_fatura_4.setFrameShape(QFrame.StyledPanel)
        self.date_filters_fatura_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.date_filters_fatura_4)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(30, 0, 30, 0)

        self.verticalLayout_122.addWidget(self.date_filters_fatura_4)

        self.datails_fatura_card_4 = QFrame(self.main_dash_midle)
        self.datails_fatura_card_4.setObjectName(u"datails_fatura_card_4")
        self.datails_fatura_card_4.setMaximumSize(QSize(16777215, 80))
        self.datails_fatura_card_4.setStyleSheet(u"border-radius:5px;\n"
" border-bottom-right-radius:0px;\n"
" border-bottom-left-radius:0px;\n"
"\n"
"background-color: rgba(255, 255, 255, 30); ")
        self.datails_fatura_card_4.setFrameShape(QFrame.StyledPanel)
        self.datails_fatura_card_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.datails_fatura_card_4)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.icon_4 = QFrame(self.datails_fatura_card_4)
        self.icon_4.setObjectName(u"icon_4")
        self.icon_4.setMaximumSize(QSize(48, 48))
        self.icon_4.setStyleSheet(u"border-bottom: 0px;\n"
"border-radius: 5px;\n"
"border-image: url();")
        self.icon_4.setFrameShape(QFrame.StyledPanel)
        self.icon_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_68.addWidget(self.icon_4)

        self.name_bank_4 = QLabel(self.datails_fatura_card_4)
        self.name_bank_4.setObjectName(u"name_bank_4")
        self.name_bank_4.setLayoutDirection(Qt.LeftToRight)
        self.name_bank_4.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"background-color: none; \n"
"\n"
"")
        self.name_bank_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.name_bank_4)

        self.set_limite_card_4 = QFrame(self.datails_fatura_card_4)
        self.set_limite_card_4.setObjectName(u"set_limite_card_4")
        self.set_limite_card_4.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 1px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"background-color: none; \n"
"")
        self.set_limite_card_4.setFrameShape(QFrame.StyledPanel)
        self.set_limite_card_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_123 = QVBoxLayout(self.set_limite_card_4)
        self.verticalLayout_123.setObjectName(u"verticalLayout_123")
        self.label_49 = QLabel(self.set_limite_card_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)
        self.label_49.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"\n"
"border-radius:3px;")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.verticalLayout_123.addWidget(self.label_49)

        self.label_50 = QLabel(self.set_limite_card_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)
        self.label_50.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"\n"
"border-radius:3px;")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.verticalLayout_123.addWidget(self.label_50)


        self.horizontalLayout_68.addWidget(self.set_limite_card_4)

        self.set_fechamento_4 = QFrame(self.datails_fatura_card_4)
        self.set_fechamento_4.setObjectName(u"set_fechamento_4")
        self.set_fechamento_4.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 1px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"background-color: none; \n"
"")
        self.set_fechamento_4.setFrameShape(QFrame.StyledPanel)
        self.set_fechamento_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_125 = QVBoxLayout(self.set_fechamento_4)
        self.verticalLayout_125.setObjectName(u"verticalLayout_125")
        self.label_53 = QLabel(self.set_fechamento_4)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font)
        self.label_53.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"border-radius:3px;")
        self.label_53.setAlignment(Qt.AlignCenter)

        self.verticalLayout_125.addWidget(self.label_53)

        self.label_54 = QLabel(self.set_fechamento_4)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)
        self.label_54.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"\n"
"border-radius:3px;")
        self.label_54.setAlignment(Qt.AlignCenter)

        self.verticalLayout_125.addWidget(self.label_54)


        self.horizontalLayout_68.addWidget(self.set_fechamento_4)

        self.set_vencimento_4 = QFrame(self.datails_fatura_card_4)
        self.set_vencimento_4.setObjectName(u"set_vencimento_4")
        self.set_vencimento_4.setStyleSheet(u"border-radius: 0px;\n"
"border-bottom: 0px solid rgb(45, 45, 68);\n"
"border-right: 0px solid rgb(45, 45, 68);\n"
"border-left: 0px solid rgb(45, 45, 68);\n"
"background-color: none; \n"
"")
        self.set_vencimento_4.setFrameShape(QFrame.StyledPanel)
        self.set_vencimento_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_126 = QVBoxLayout(self.set_vencimento_4)
        self.verticalLayout_126.setObjectName(u"verticalLayout_126")
        self.label_55 = QLabel(self.set_vencimento_4)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)
        self.label_55.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"border-radius:3px;")
        self.label_55.setAlignment(Qt.AlignCenter)

        self.verticalLayout_126.addWidget(self.label_55)

        self.label_56 = QLabel(self.set_vencimento_4)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font)
        self.label_56.setStyleSheet(u"border-bottom: 0px;\n"
"border: 0px;\n"
"\n"
"\n"
"border-radius:3px;")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.verticalLayout_126.addWidget(self.label_56)


        self.horizontalLayout_68.addWidget(self.set_vencimento_4)


        self.verticalLayout_122.addWidget(self.datails_fatura_card_4)

        self.datalhed_fatura_mother_4 = QFrame(self.main_dash_midle)
        self.datalhed_fatura_mother_4.setObjectName(u"datalhed_fatura_mother_4")
        self.datalhed_fatura_mother_4.setStyleSheet(u"border-bottom: 0px;\n"
"border-right: 0px;\n"
"")
        self.datalhed_fatura_mother_4.setFrameShape(QFrame.StyledPanel)
        self.datalhed_fatura_mother_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_127 = QVBoxLayout(self.datalhed_fatura_mother_4)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName(u"verticalLayout_127")
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.table_faturas_ind_3 = QTableWidget(self.datalhed_fatura_mother_4)
        if (self.table_faturas_ind_3.columnCount() < 4):
            self.table_faturas_ind_3.setColumnCount(4)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind_3.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind_3.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind_3.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.table_faturas_ind_3.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        self.table_faturas_ind_3.setObjectName(u"table_faturas_ind_3")
        self.table_faturas_ind_3.setFont(font2)
        self.table_faturas_ind_3.setStyleSheet(u"QWidget {\n"
"    color: #fffff8;\n"
"\n"
"	border-radius:0px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(53, 53, 53);\n"
"    font-size: 11;\n"
"	border:none;\n"
"	width:45px;\n"
"	height: 50px;\n"
"\n"
"	border-radius:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #fffff8;\n"
"    font-size: 11pt;\n"
"	border-radius:0px;\n"
"	border-radius:0px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"	border-radius:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableView:item {\n"
"  border-bottom: 0.5px solid qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:0.45677 rgba(0, 0, 0, 0), stop:0.479846 rgba(255, 255, 255, 255), stop:0.50571 rgba(239, 236, 55, 0), stop:1 rgba(239, 236, 55, 0));\n"
"	border-radius:0px;\n"
"\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	\n"
"	background-color: rgb(92, 155, 179);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")
        self.table_faturas_ind_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_faturas_ind_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table_faturas_ind_3.setAlternatingRowColors(False)
        self.table_faturas_ind_3.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_faturas_ind_3.setIconSize(QSize(45, 40))
        self.table_faturas_ind_3.setTextElideMode(Qt.ElideLeft)
        self.table_faturas_ind_3.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_faturas_ind_3.setShowGrid(False)
        self.table_faturas_ind_3.setSortingEnabled(False)
        self.table_faturas_ind_3.horizontalHeader().setVisible(False)
        self.table_faturas_ind_3.horizontalHeader().setCascadingSectionResizes(True)
        self.table_faturas_ind_3.horizontalHeader().setDefaultSectionSize(230)
        self.table_faturas_ind_3.horizontalHeader().setHighlightSections(True)
        self.table_faturas_ind_3.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_faturas_ind_3.horizontalHeader().setStretchLastSection(True)
        self.table_faturas_ind_3.verticalHeader().setVisible(False)
        self.table_faturas_ind_3.verticalHeader().setCascadingSectionResizes(False)
        self.table_faturas_ind_3.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_127.addWidget(self.table_faturas_ind_3)


        self.verticalLayout_122.addWidget(self.datalhed_fatura_mother_4)


        self.verticalLayout_14.addWidget(self.main_dash_midle)

        self.main_dash_bottom = QFrame(self.scrollAreaWidgetContents_8)
        self.main_dash_bottom.setObjectName(u"main_dash_bottom")
        self.main_dash_bottom.setMinimumSize(QSize(0, 500))
        self.main_dash_bottom.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.main_dash_bottom.setFrameShape(QFrame.StyledPanel)
        self.main_dash_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.main_dash_bottom)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.chart_gastos_all = QTabWidget(self.main_dash_bottom)
        self.chart_gastos_all.setObjectName(u"chart_gastos_all")
        self.chart_gastos_all.setMinimumSize(QSize(0, 0))
        self.chart_gastos_all.setMaximumSize(QSize(16777215, 16777215))
        self.chart_gastos_all.setFont(font)
        self.chart_gastos_all.setLayoutDirection(Qt.LeftToRight)
        self.chart_gastos_all.setStyleSheet(u"\n"
"\n"
"QTabWidget::tab-bar {\n"
"  background: gray;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"  background: rgb(46, 46, 46);\n"
"  padding: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"  background:rgb(53, 53, 53);\n"
"  color: rgb(255, 255, 255);\n"
" }\n"
"\n"
"QTabWidget::pane { border-top-left-radius:0px; border-top-right-radius:0px;}\n"
"\n"
"")
        self.chart_gastos_all.setTabPosition(QTabWidget.North)
        self.chart_gastos_all.setTabShape(QTabWidget.Rounded)
        self.chart_gastos_all.setElideMode(Qt.ElideMiddle)
        self.chart_gastos_all.setDocumentMode(False)
        self.chart_gastos_all.setTabsClosable(False)
        self.chart_gastos_all.setMovable(True)
        self.chart_gastos_all.setTabBarAutoHide(True)
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.tab_14.setStyleSheet(u"")
        self.verticalLayout_131 = QVBoxLayout(self.tab_14)
        self.verticalLayout_131.setSpacing(0)
        self.verticalLayout_131.setObjectName(u"verticalLayout_131")
        self.verticalLayout_131.setContentsMargins(0, 0, 10, 0)
        self.chart_main_evolution_3 = QFrame(self.tab_14)
        self.chart_main_evolution_3.setObjectName(u"chart_main_evolution_3")
        self.chart_main_evolution_3.setStyleSheet(u"")
        self.chart_main_evolution_3.setFrameShape(QFrame.StyledPanel)
        self.chart_main_evolution_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_132 = QVBoxLayout(self.chart_main_evolution_3)
        self.verticalLayout_132.setSpacing(0)
        self.verticalLayout_132.setObjectName(u"verticalLayout_132")
        self.verticalLayout_132.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QFrame(self.chart_main_evolution_3)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_133 = QVBoxLayout(self.frame_48)
        self.verticalLayout_133.setSpacing(0)
        self.verticalLayout_133.setObjectName(u"verticalLayout_133")
        self.verticalLayout_133.setContentsMargins(0, 0, 0, 0)
        self.chart_evolution_all = QVBoxLayout()
        self.chart_evolution_all.setObjectName(u"chart_evolution_all")

        self.verticalLayout_133.addLayout(self.chart_evolution_all)


        self.verticalLayout_132.addWidget(self.frame_48)


        self.verticalLayout_131.addWidget(self.chart_main_evolution_3)

        self.chart_gastos_all.addTab(self.tab_14, icon24, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.tab_15.setStyleSheet(u"")
        self.verticalLayout_134 = QVBoxLayout(self.tab_15)
        self.verticalLayout_134.setSpacing(0)
        self.verticalLayout_134.setObjectName(u"verticalLayout_134")
        self.verticalLayout_134.setContentsMargins(0, 0, 10, 0)
        self.chart_main_date_3 = QFrame(self.tab_15)
        self.chart_main_date_3.setObjectName(u"chart_main_date_3")
        self.chart_main_date_3.setStyleSheet(u"border-radius:10px;")
        self.chart_main_date_3.setFrameShape(QFrame.StyledPanel)
        self.chart_main_date_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_135 = QVBoxLayout(self.chart_main_date_3)
        self.verticalLayout_135.setSpacing(0)
        self.verticalLayout_135.setObjectName(u"verticalLayout_135")
        self.verticalLayout_135.setContentsMargins(0, 0, 0, 0)
        self.frame_49 = QFrame(self.chart_main_date_3)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_136 = QVBoxLayout(self.frame_49)
        self.verticalLayout_136.setSpacing(0)
        self.verticalLayout_136.setObjectName(u"verticalLayout_136")
        self.verticalLayout_136.setContentsMargins(0, 0, 0, 0)
        self.frame_chart_date_day_3 = QVBoxLayout()
        self.frame_chart_date_day_3.setObjectName(u"frame_chart_date_day_3")

        self.verticalLayout_136.addLayout(self.frame_chart_date_day_3)


        self.verticalLayout_135.addWidget(self.frame_49)


        self.verticalLayout_134.addWidget(self.chart_main_date_3)

        self.chart_gastos_all.addTab(self.tab_15, icon23, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.tab_13.setMaximumSize(QSize(16777215, 16777215))
        self.tab_13.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"")
        self.verticalLayout_128 = QVBoxLayout(self.tab_13)
        self.verticalLayout_128.setSpacing(0)
        self.verticalLayout_128.setObjectName(u"verticalLayout_128")
        self.verticalLayout_128.setContentsMargins(0, 0, 0, 0)
        self.chart_main_category_3 = QFrame(self.tab_13)
        self.chart_main_category_3.setObjectName(u"chart_main_category_3")
        self.chart_main_category_3.setStyleSheet(u"background-color: none;\n"
"\n"
"")
        self.chart_main_category_3.setFrameShape(QFrame.StyledPanel)
        self.chart_main_category_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_129 = QVBoxLayout(self.chart_main_category_3)
        self.verticalLayout_129.setSpacing(0)
        self.verticalLayout_129.setObjectName(u"verticalLayout_129")
        self.verticalLayout_129.setContentsMargins(0, 0, 0, 0)
        self.frame_47 = QFrame(self.chart_main_category_3)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setStyleSheet(u"border-radius:0px;")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_35.setSpacing(10)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(10, 10, 10, 10)
        self.listWidget = QListWidget(self.frame_47)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(200, 0))
        self.listWidget.setMaximumSize(QSize(200, 16777215))
        self.listWidget.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_35.addWidget(self.listWidget)

        self.limit_dash_gastos = QFrame(self.frame_47)
        self.limit_dash_gastos.setObjectName(u"limit_dash_gastos")
        self.limit_dash_gastos.setMinimumSize(QSize(200, 0))
        self.limit_dash_gastos.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"")
        self.limit_dash_gastos.setFrameShape(QFrame.StyledPanel)
        self.limit_dash_gastos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.limit_dash_gastos)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.label_40 = QLabel(self.limit_dash_gastos)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_40)

        self.icon_met = QFrame(self.limit_dash_gastos)
        self.icon_met.setObjectName(u"icon_met")
        self.icon_met.setMaximumSize(QSize(16777215, 100))
        self.icon_met.setStyleSheet(u"background-color: none;\n"
"")
        self.icon_met.setFrameShape(QFrame.StyledPanel)
        self.icon_met.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.icon_met)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_9 = QSpacerItem(289, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_9)

        self.frame = QFrame(self.icon_met)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 0))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_30.addWidget(self.frame)

        self.horizontalSpacer_10 = QSpacerItem(289, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_10)


        self.verticalLayout_13.addWidget(self.icon_met)

        self.label = QLabel(self.limit_dash_gastos)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 40))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border-radius:5px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label)

        self.stackedWidget_25 = QStackedWidget(self.limit_dash_gastos)
        self.stackedWidget_25.setObjectName(u"stackedWidget_25")
        self.stackedWidget_25.setMaximumSize(QSize(16777215, 50))
        self.stackedWidget_25.setStyleSheet(u"background-color: none;\n"
"\n"
"border-radius:0px;")
        self.stackedWidget_25.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget_25.setFrameShadow(QFrame.Raised)
        self.stackedWidget_25Page1 = QWidget()
        self.stackedWidget_25Page1.setObjectName(u"stackedWidget_25Page1")
        self.stackedWidget_25Page1.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border-radius:5px;")
        self.horizontalLayout_32 = QHBoxLayout(self.stackedWidget_25Page1)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_11)

        self.label_8 = QLabel(self.stackedWidget_25Page1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color: none;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_8)

        self.label_11 = QLabel(self.stackedWidget_25Page1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background-color: none;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_11)

        self.label_12 = QLabel(self.stackedWidget_25Page1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background-color: none;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_12)

        self.pushButton_21 = QPushButton(self.stackedWidget_25Page1)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"background-color: none;\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"\n"
"	\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	color: rgb(170, 170, 0);\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        icon32 = QIcon()
        icon32.addFile(u":/menu/menu/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_21.setIcon(icon32)
        self.pushButton_21.setIconSize(QSize(20, 30))

        self.horizontalLayout_32.addWidget(self.pushButton_21)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_12)

        self.stackedWidget_25.addWidget(self.stackedWidget_25Page1)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.page_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border-radius:5px;")
        self.horizontalLayout_45 = QHBoxLayout(self.page_9)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalSpacer_13 = QSpacerItem(185, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_13)

        self.label_23 = QLabel(self.page_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"background-color: none;")

        self.horizontalLayout_45.addWidget(self.label_23)

        self.lineEdit_4 = QLineEdit(self.page_9)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"border-bottom:1px solid black;\n"
"border-radius:0px;\n"
"\n"
"background-color: rgba(255, 255, 255, 0); ")
        self.lineEdit_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.lineEdit_4)

        self.pushButton_22 = QPushButton(self.page_9)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	background-color: none;\n"
"\n"
"	border-radius:10px;\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"\n"
"	\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	color: rgb(170, 170, 0);\n"
"	\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.pushButton_22.setIcon(icon32)
        self.pushButton_22.setIconSize(QSize(20, 30))

        self.horizontalLayout_45.addWidget(self.pushButton_22)

        self.horizontalSpacer_16 = QSpacerItem(185, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_16)

        self.stackedWidget_25.addWidget(self.page_9)

        self.verticalLayout_13.addWidget(self.stackedWidget_25)

        self.frame_19 = QFrame(self.limit_dash_gastos)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(16777215, 200))
        self.frame_19.setStyleSheet(u"background-color: none;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_19)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_19)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 40))
        self.label_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border-radius:5px;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_9)

        self.frame_26 = QFrame(self.frame_19)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(16777215, 40))
        self.frame_26.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border-radius:5px;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_13 = QLabel(self.frame_26)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background-color: none;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_26)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"background-color: none;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_26)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color: none;")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_15)


        self.verticalLayout_22.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_19)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(16777215, 40))
        self.frame_27.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border-radius:5px;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_16 = QLabel(self.frame_27)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background-color: none;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_16)

        self.label_18 = QLabel(self.frame_27)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"background-color: none;")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_18)

        self.label_21 = QLabel(self.frame_27)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"background-color: none;")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.label_21)


        self.verticalLayout_22.addWidget(self.frame_27)


        self.verticalLayout_13.addWidget(self.frame_19)


        self.horizontalLayout_35.addWidget(self.limit_dash_gastos)


        self.verticalLayout_129.addWidget(self.frame_47)


        self.verticalLayout_128.addWidget(self.chart_main_category_3)

        self.chart_gastos_all.addTab(self.tab_13, icon21, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.chart_gastos_all.addTab(self.tab, icon19, "")

        self.verticalLayout_8.addWidget(self.chart_gastos_all)


        self.verticalLayout_14.addWidget(self.main_dash_bottom)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_32.addWidget(self.scrollArea_8)

        self.detalhes_cartao.addWidget(self.dashboard_cards)

        self.horizontalLayout_15.addWidget(self.detalhes_cartao)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_9.addWidget(self.scrollArea)

        self.stackedWidget_3.addWidget(self.page)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.page2.setStyleSheet(u"background-color:rgba(255,255,255,0);")
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
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 520, 318))
        self.horizontalLayout_20 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_20.setSpacing(10)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_9 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(502, 300))
        self.frame_9.setMaximumSize(QSize(900, 16777215))
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	background-color: rgba(255, 255, 255, 30); \n"
"\n"
"	border-radius: 10px;\n"
"	border-bottom: 4px solid rgb(45, 45, 45);\n"
"	border-right: 4px solid rgb(45, 45, 45);\n"
"\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.table_active_cards = QTableWidget(self.frame_9)
        if (self.table_active_cards.columnCount() < 7):
            self.table_active_cards.setColumnCount(7)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_active_cards.setHorizontalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_active_cards.setHorizontalHeaderItem(1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_active_cards.setHorizontalHeaderItem(2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_active_cards.setHorizontalHeaderItem(3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.table_active_cards.setHorizontalHeaderItem(4, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.table_active_cards.setHorizontalHeaderItem(5, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.table_active_cards.setHorizontalHeaderItem(6, __qtablewidgetitem48)
        self.table_active_cards.setObjectName(u"table_active_cards")
        self.table_active_cards.setMinimumSize(QSize(0, 0))
        self.table_active_cards.setMaximumSize(QSize(16777215, 16777215))
        self.table_active_cards.setTabletTracking(False)
        self.table_active_cards.setStyleSheet(u"QWidget {\n"
"	\n"
"    color: #fffff8;\n"
"	border-radius:0px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgb(53, 53, 53);\n"
"    font-size: 11;\n"
"	border:none;\n"
"	width:45px;\n"
"	height: 50px;\n"
"\n"
"	border-radius:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget {\n"
"    gridline-color: #fffff8;\n"
"    font-size: 11pt;\n"
"	border-radius:0px;\n"
"	border-radius:0px;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background-color: #646464;\n"
"	border-radius:0px;\n"
"\n"
"\n"
"}\n"
"\n"
"QTableView:item {\n"
"  border-bottom: 0.5px solid qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:0.45677 rgba(0, 0, 0, 0), stop:0.479846 rgba(255, 255, 255, 255), stop:0.50571 rgba(239, 236, 55, 0), stop:1 rgba(239, 236, 55, 0));\n"
"	border-radius:0px;\n"
"\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	\n"
"	background-color: rgb(92, 155, 179);\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
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
        self.table_active_cards.horizontalHeader().setDefaultSectionSize(113)
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

        self.verticalLayout_23.addWidget(self.table_active_cards)

        self.frame_35 = QFrame(self.frame_9)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMaximumSize(QSize(16777215, 500))
        self.frame_35.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border:none;")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_35)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.select_card = QComboBox(self.frame_35)
        self.select_card.addItem("")
        self.select_card.addItem("")
        self.select_card.addItem("")
        self.select_card.addItem("")
        self.select_card.addItem("")
        self.select_card.addItem("")
        self.select_card.addItem("")
        self.select_card.setObjectName(u"select_card")
        self.select_card.setMinimumSize(QSize(0, 30))
        self.select_card.setFont(font6)
        self.select_card.setLayoutDirection(Qt.LeftToRight)
        self.select_card.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")

        self.verticalLayout_10.addWidget(self.select_card)

        self.frame_39 = QFrame(self.frame_35)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalSpacer_19 = QSpacerItem(212, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_19)

        self.frameadc = QFrame(self.frame_39)
        self.frameadc.setObjectName(u"frameadc")
        sizePolicy5.setHeightForWidth(self.frameadc.sizePolicy().hasHeightForWidth())
        self.frameadc.setSizePolicy(sizePolicy5)
        self.frameadc.setMinimumSize(QSize(0, 0))
        self.frameadc.setMaximumSize(QSize(400, 230))
        self.frameadc.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"border: 3px solid  rgb(0, 0, 0);\n"
"border:0px;\n"
"}\n"
"\n"
"QFrame:hover{\n"
"border: 3px solid  rgb(55, 50,5 0);\n"
"\n"
"}")
        self.frameadc.setFrameShape(QFrame.StyledPanel)
        self.frameadc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frameadc)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.logoadc = QFrame(self.frameadc)
        self.logoadc.setObjectName(u"logoadc")
        self.logoadc.setMinimumSize(QSize(0, 40))
        self.logoadc.setMaximumSize(QSize(40, 40))
        self.logoadc.setStyleSheet(u"border: 0px;\n"
"\n"
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
        self.label_37 = QLabel(self.frame_10)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_37, 6, 0, 1, 1)

        self.adclimite = QLineEdit(self.frame_10)
        self.adclimite.setObjectName(u"adclimite")
        self.adclimite.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adclimite.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.adclimite, 0, 1, 1, 1)

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

        self.gridLayout.addWidget(self.textcard_3, 3, 0, 1, 1)

        self.adcfechamento = QLineEdit(self.frame_10)
        self.adcfechamento.setObjectName(u"adcfechamento")
        self.adcfechamento.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adcfechamento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.adcfechamento, 6, 1, 1, 1)

        self.textcard_2 = QLabel(self.frame_10)
        self.textcard_2.setObjectName(u"textcard_2")
        self.textcard_2.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard_2.setTextFormat(Qt.AutoText)
        self.textcard_2.setScaledContents(False)
        self.textcard_2.setAlignment(Qt.AlignCenter)
        self.textcard_2.setWordWrap(False)

        self.gridLayout.addWidget(self.textcard_2, 1, 0, 1, 1)

        self.textcard = QLabel(self.frame_10)
        self.textcard.setObjectName(u"textcard")
        self.textcard.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard.setTextFormat(Qt.AutoText)
        self.textcard.setScaledContents(False)
        self.textcard.setAlignment(Qt.AlignCenter)
        self.textcard.setWordWrap(False)

        self.gridLayout.addWidget(self.textcard, 0, 0, 1, 1)

        self.textcard_4 = QLabel(self.frame_10)
        self.textcard_4.setObjectName(u"textcard_4")
        self.textcard_4.setStyleSheet(u"border: 0px;\n"
"")
        self.textcard_4.setTextFormat(Qt.AutoText)
        self.textcard_4.setScaledContents(False)
        self.textcard_4.setAlignment(Qt.AlignCenter)
        self.textcard_4.setWordWrap(False)

        self.gridLayout.addWidget(self.textcard_4, 4, 0, 1, 1)

        self.adcfinal = QLineEdit(self.frame_10)
        self.adcfinal.setObjectName(u"adcfinal")
        self.adcfinal.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adcfinal.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.adcfinal, 3, 1, 1, 1)

        self.adcvencimento = QLineEdit(self.frame_10)
        self.adcvencimento.setObjectName(u"adcvencimento")
        self.adcvencimento.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgb(238, 238, 238);\n"
"border: 1px solid  rgb(55, 55, 55);")
        self.adcvencimento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.adcvencimento, 4, 1, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_10)


        self.horizontalLayout_49.addWidget(self.frameadc)

        self.horizontalSpacer_20 = QSpacerItem(212, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_20)


        self.verticalLayout_10.addWidget(self.frame_39)

        self.frame_38 = QFrame(self.frame_35)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMaximumSize(QSize(16777215, 50))
        self.frame_38.setStyleSheet(u"")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.add_card_3 = QPushButton(self.frame_38)
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

        self.horizontalLayout_47.addWidget(self.add_card_3)

        self.remover_card_3 = QPushButton(self.frame_38)
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

        self.horizontalLayout_47.addWidget(self.remover_card_3)

        self.pushButton_23 = QPushButton(self.frame_38)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setMinimumSize(QSize(0, 30))
        self.pushButton_23.setMaximumSize(QSize(110, 25))
        self.pushButton_23.setStyleSheet(u"\n"
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

        self.horizontalLayout_47.addWidget(self.pushButton_23)


        self.verticalLayout_10.addWidget(self.frame_38)


        self.verticalLayout_23.addWidget(self.frame_35)

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

        self.verticalLayout_23.addWidget(self.menu_option_3)


        self.horizontalLayout_20.addWidget(self.frame_9)

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
        self.frame_41 = QFrame(self.page_6)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setGeometry(QRect(30, 30, 451, 171))
        self.frame_41.setStyleSheet(u"background-color:rgba(255,255,255,30);")
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_109 = QVBoxLayout(self.frame_41)
        self.verticalLayout_109.setSpacing(10)
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.label_6 = QLabel(self.frame_41)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_109.addWidget(self.label_6)

        self.frame_98 = QFrame(self.frame_41)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_98)
        self.verticalLayout_110.setSpacing(0)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.label_76 = QLabel(self.frame_98)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setStyleSheet(u"background-color:rgba(255,255,255,30);")

        self.verticalLayout_110.addWidget(self.label_76)

        self.frame_99 = QFrame(self.frame_98)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_110.setSpacing(0)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalLayout_110.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_32 = QSpacerItem(70, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_110.addItem(self.horizontalSpacer_32)

        self.hidden_saldo_fat0_true = QRadioButton(self.frame_99)
        self.hidden_saldo_fat0_true.setObjectName(u"hidden_saldo_fat0_true")
        font7 = QFont()
        font7.setFamily(u"Bahnschrift Light Condensed")
        font7.setPointSize(14)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(3)
        font7.setStyleStrategy(QFont.PreferDefault)
        self.hidden_saldo_fat0_true.setFont(font7)
        self.hidden_saldo_fat0_true.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.hidden_saldo_fat0_true.setLayoutDirection(Qt.LeftToRight)
        self.hidden_saldo_fat0_true.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_110.addWidget(self.hidden_saldo_fat0_true)

        self.horizontalSpacer_31 = QSpacerItem(70, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_110.addItem(self.horizontalSpacer_31)

        self.hidden_saldo_fat0_false = QRadioButton(self.frame_99)
        self.hidden_saldo_fat0_false.setObjectName(u"hidden_saldo_fat0_false")
        self.hidden_saldo_fat0_false.setStyleSheet(u"background-color:rgba(255,255,255,30);\n"
"color: rgb(255, 255, 255);")
        self.hidden_saldo_fat0_false.setChecked(True)

        self.horizontalLayout_110.addWidget(self.hidden_saldo_fat0_false)

        self.horizontalSpacer_33 = QSpacerItem(70, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_110.addItem(self.horizontalSpacer_33)


        self.verticalLayout_110.addWidget(self.frame_99)


        self.verticalLayout_109.addWidget(self.frame_98)

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
        icon33 = QIcon()
        icon33.addFile(u":/dev/dev/devs.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon33)
        self.pushButton_4.setIconSize(QSize(40, 40))

        self.verticalLayout_58.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_23)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon34 = QIcon()
        icon34.addFile(u":/dev/dev/academy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon34)
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
        icon35 = QIcon()
        icon35.addFile(u":/dev/dev/git.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon35)
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

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.detalhes_cartao_2.setCurrentIndex(0)
        self.extrat_meses_2.setCurrentIndex(1)
        self.chart_gastos_all_2.setCurrentIndex(0)
        self.stacked_configcartao0_2.setCurrentIndex(0)
        self.stack_extrato_pages_2.setCurrentIndex(0)
        self.pushButton_25.setDefault(False)
        self.pushButton_26.setDefault(False)
        self.stackedWidgetadc_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.detalhes_cartao.setCurrentIndex(1)
        self.extrat_meses.setCurrentIndex(1)
        self.stacked_configcartao0.setCurrentIndex(0)
        self.stack_extrato_pages.setCurrentIndex(0)
        self.pushButton_17.setDefault(False)
        self.tabWidget.setCurrentIndex(2)
        self.chart_gastos_all.setCurrentIndex(0)
        self.stackedWidget_25.setCurrentIndex(0)


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
        self.credits.setText(QCoreApplication.translate("MainWindow", u"   Home Application Ver: 1.06", None))
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
        self.hide_cards_main_2.setText("")
        self.show_cards_main_2.setText("")
        self.pushButton_24.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, Boa Tarde.", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"15:23", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Conta:", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Saldo em Reais", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"R$ 0,00", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Cart\u00f5es de Creditos</span></p></body></html>", None))
        self.labelTitle_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Limites Utilizados:</span></p><p><span style=\" color:#ffffff;\">R$0,00</span></p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\"> Faturas de: </span></p><p align=\"center\"><span style=\" color:#ffffff;\">R$0,00</span></p></body></html>", None))
        self.labelTitle_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Limites Disponiveis</span></p><p><span style=\" color:#ffffff;\">R$0,00</span></p></body></html>", None))
        self.name_bank_5.setText(QCoreApplication.translate("MainWindow", u"Selecione um Cart\u00e3o", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Limite", None))
        self.label_52.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Fechamento", None))
        self.label_58.setText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Vencimento", None))
        self.label_60.setText("")
        ___qtablewidgetitem = self.table_faturas_ind_4.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Cartao", None));
        ___qtablewidgetitem1 = self.table_faturas_ind_4.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o da fatura", None));
        ___qtablewidgetitem2 = self.table_faturas_ind_4.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Valor da fatura", None));
        ___qtablewidgetitem3 = self.table_faturas_ind_4.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ir para", None));
        self.line_d_2.setInputMask("")
        self.line_d_2.setText("")
        self.line_d_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Dia", None))
        self.line_m_2.setText("")
        self.line_m_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"M\u00eas", None))
        self.line_y_2.setText("")
        self.line_y_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  Ano", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Procurar  ", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.previus_month_2.setText(QCoreApplication.translate("MainWindow", u" Previus ", None))
#if QT_CONFIG(shortcut)
        self.previus_month_2.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Novembro", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"de", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"2022", None))
        self.next_month_2.setText(QCoreApplication.translate("MainWindow", u" Next", None))
#if QT_CONFIG(shortcut)
        self.next_month_2.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.previus_month_4.setText(QCoreApplication.translate("MainWindow", u" Previus ", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Ano", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"2022", None))
        self.next_month_4.setText(QCoreApplication.translate("MainWindow", u" Next", None))
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Chk", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"id_compra", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"id_bank", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Banco", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"tipo_e_s", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Prioridade", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Categoria", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Pagamento", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem15 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Saldo", None));
        self.text_page_notfound_2.setText(QCoreApplication.translate("MainWindow", u"Compra n\u00e3o localizada", None))
        self.txt_pag_emdia_2.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o h\u00e1 despesas este mes!", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o:", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Bahnschrift Light Condensed'; font-size:14pt; font-weight:24; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"KCA1_48\"></a><span style=\" font-size:12pt; font-weight:400;\">O</span><span style=\" font-size:12pt; font-weight:400;\"> Texas \u00e9 um dos 50 estados dos Estados Unidos, localizado na regi\u00e3o sul do pa\u00eds. Possui como limites o estado de Oklahoma ao norte, Novo M\u00e9xico ao oeste, \u2026</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:400;\"><br /></p></body></html>", None))
        self.label_if_card.setText(QCoreApplication.translate("MainWindow", u"Cartao:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Fatura de ", None))
        self.btn_if_card_2.setText(QCoreApplication.translate("MainWindow", u"Ver cartao", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Anexos:", None))
        self.toolButton_pdf_opt.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.delet_pdf.setText(QCoreApplication.translate("MainWindow", u"Apagar Anexo", None))
        self.download_pdf.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.paga_fatura_3.setText(QCoreApplication.translate("MainWindow", u"Pagar", None))
        self.edit_compra_3.setText(QCoreApplication.translate("MainWindow", u"Editar Lan\u00e7amento", None))
        self.parcela_fatura_3.setText(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00f5es", None))
        self.apaga_compra_3.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.filter_dates_btn_3.setText(QCoreApplication.translate("MainWindow", u"Filtrar por Data  ", None))
        self.chart_gastos_all_2.setTabText(self.chart_gastos_all_2.indexOf(self.page_Tabe_main1), QCoreApplication.translate("MainWindow", u"Fluxo de Caixa", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Lan\u00e7amento", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Conta", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Opera\u00e7\u00e3o", None))
        self.comboBox_25.setItemText(0, "")
        self.comboBox_25.setItemText(1, QCoreApplication.translate("MainWindow", u"Entrada", None))
        self.comboBox_25.setItemText(2, QCoreApplication.translate("MainWindow", u"Saida", None))

        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Pagamento", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Selecione a Categoria", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setPlaceholderText("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Data da Transa\u00e7\u00e3o", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Hoje", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Valor do Lan\u00e7amento", None))
        self.lineEdit_13.setText("")
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"J\u00e1 pago/recebido?", None))
        self.comboBox_22.setItemText(0, "")
        self.comboBox_22.setItemText(1, QCoreApplication.translate("MainWindow", u"Sim", None))
        self.comboBox_22.setItemText(2, QCoreApplication.translate("MainWindow", u"N\u00e3o", None))

        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Configurar Lan\u00e7amento", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Programar data", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Recorrente?", None))
        self.comboBox_23.setItemText(0, "")
        self.comboBox_23.setItemText(1, QCoreApplication.translate("MainWindow", u"Sim", None))
        self.comboBox_23.setItemText(2, QCoreApplication.translate("MainWindow", u"N\u00e3o", None))

        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Configurar recorrencia", None))
        self.comboBox_26.setItemText(0, "")
        self.comboBox_26.setItemText(1, QCoreApplication.translate("MainWindow", u"Mes", None))

        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Data todo dia", None))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Exemplo: 09", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Hoje", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Anexos:", None))
        self.download_pdf_2.setText(QCoreApplication.translate("MainWindow", u"Selecionar", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Anexos", None))
        self.add_lancamento_btn.setText(QCoreApplication.translate("MainWindow", u"Lan\u00e7ar", None))
        self.update_bank_2.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
        self.chart_gastos_all_2.setTabText(self.chart_gastos_all_2.indexOf(self.page_Tabe_main2), QCoreApplication.translate("MainWindow", u"Novo Lan\u00e7amento", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Adicionar novo", None))
        self.select_conta_bancaria.setItemText(0, QCoreApplication.translate("MainWindow", u"C6", None))
        self.select_conta_bancaria.setItemText(1, QCoreApplication.translate("MainWindow", u"NUBANK", None))
        self.select_conta_bancaria.setItemText(2, QCoreApplication.translate("MainWindow", u"BTG", None))
        self.select_conta_bancaria.setItemText(3, QCoreApplication.translate("MainWindow", u"SANTANDER", None))
        self.select_conta_bancaria.setItemText(4, QCoreApplication.translate("MainWindow", u"ITAU", None))
        self.select_conta_bancaria.setItemText(5, QCoreApplication.translate("MainWindow", u"BRADESCO", None))
        self.select_conta_bancaria.setItemText(6, QCoreApplication.translate("MainWindow", u"CAIXA ECONOMICA", None))

        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Definir como padrao?", None))
        self.combo_bank_padrao.setItemText(0, "")
        self.combo_bank_padrao.setItemText(1, QCoreApplication.translate("MainWindow", u"Sim", None))
        self.combo_bank_padrao.setItemText(2, QCoreApplication.translate("MainWindow", u"N\u00e3o", None))

        self.adcagencia_conta.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXX", None))
        self.adctitular_conta.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.adc_saldo_conta.setPlaceholderText(QCoreApplication.translate("MainWindow", u"01", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Saldo Inicial</span></p></body></html>", None))
        self.textcard_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Titular</span></p></body></html>", None))
        self.textcard_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Agencia</span></p></body></html>", None))
        self.adc_conta_conta.setPlaceholderText(QCoreApplication.translate("MainWindow", u"01", None))
        self.textcard_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Conta</span></p></body></html>", None))
        self.hide_cards_main_3.setText("")
        self.hide_cards_main_4.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Fechamento da Fatura:</span></p></body></html>", None))
        self.adclimite_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.adctitular_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.textcard_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Final do Cart\u00e3o</span></p></body></html>", None))
        self.adcfechamento_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"01", None))
        self.textcard_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Titular</span></p></body></html>", None))
        self.textcard_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Limite Total do Cartao</span></p></body></html>", None))
        self.textcard_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Vencimento</span></p></body></html>", None))
        self.adcfinal_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXX", None))
        self.adcvencimento_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"01", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Possui carao de credito?", None))
        self.comboBox_24.setItemText(0, "")
        self.comboBox_24.setItemText(1, QCoreApplication.translate("MainWindow", u"Sim", None))
        self.comboBox_24.setItemText(2, QCoreApplication.translate("MainWindow", u"N\u00e3o", None))

        self.add_bank.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.remover_bank.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.update_bank.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Revisao", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Banco", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"asdasdasd", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Agencia", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"asdasdasd", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Conta", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("MainWindow", u"asdasdasd", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Saldo", None))
        self.plainTextEdit_4.setPlainText(QCoreApplication.translate("MainWindow", u"asdasdasd", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Cartao de credito", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Limite", None))
        self.plainTextEdit_5.setPlainText(QCoreApplication.translate("MainWindow", u"asdasdasd", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Final do cartao", None))
        self.plainTextEdit_9.setPlainText(QCoreApplication.translate("MainWindow", u"asdasdasd", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Titular", None))
        self.plainTextEdit_6.setPlainText(QCoreApplication.translate("MainWindow", u"asdasdasd", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Vencimento", None))
        self.plainTextEdit_8.setPlainText(QCoreApplication.translate("MainWindow", u"asdasdasd", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Fechamento", None))
        self.plainTextEdit_7.setPlainText(QCoreApplication.translate("MainWindow", u"asdasdasd", None))
        ___qtablewidgetitem16 = self.table_active_banks.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem17 = self.table_active_banks.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"saldo_inicial", None));
        ___qtablewidgetitem18 = self.table_active_banks.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Banco", None));
        ___qtablewidgetitem19 = self.table_active_banks.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Agencia", None));
        ___qtablewidgetitem20 = self.table_active_banks.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Conta", None));
        ___qtablewidgetitem21 = self.table_active_banks.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Titular", None));
        ___qtablewidgetitem22 = self.table_active_banks.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"id_credit_Card", None));
        self.chart_gastos_all_2.setTabText(self.chart_gastos_all_2.indexOf(self.page_Tabe_main3), QCoreApplication.translate("MainWindow", u"Contas Bancarias", None))
        self.chart_gastos_all_2.setTabText(self.chart_gastos_all_2.indexOf(self.page_Tabe_main4), QCoreApplication.translate("MainWindow", u"Alertas", None))
        self.grid.setText(QCoreApplication.translate("MainWindow", u"    Meus Cart\u00f5es", None))
        self.grid_2.setText(QCoreApplication.translate("MainWindow", u"   Configurar Cart\u00f5es", None))
        self.hide_cards_det.setText("")
        self.show_cards_det.setText("")
        self.back_main_dash.setText("")
        self.labelCredits_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Uso de limte</span></p></body></html>", None))
        self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\"></span></p></body></html>", None))
        self.labelPercentage_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">0</span><span style=\" font-size:20pt; vertical-align:super;\">%</span></p></body></html>", None))
        self.frame_50.setStyleSheet(QCoreApplication.translate("MainWindow", u"background-color: rgba(255, 255, 255, 0);", None))
        self.labelTitle_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Limite Utilizado:</span></p><p><span style=\" font-size:20pt; color:#ffffff;\">R$0,00</span></p></body></html>", None))
        self.labelTitle_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Limite Disponivel</span></p><p><span style=\" font-size:20pt; color:#ffffff;\">R$0,00</span></p></body></html>", None))
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
#if QT_CONFIG(shortcut)
        self.previus_month.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Novembro", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"de", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"2022", None))
        self.next_month.setText(QCoreApplication.translate("MainWindow", u" Next", None))
#if QT_CONFIG(shortcut)
        self.next_month.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.previus_month_3.setText(QCoreApplication.translate("MainWindow", u" Previus ", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Ano", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"2022", None))
        self.next_month_3.setText(QCoreApplication.translate("MainWindow", u" Next", None))
        ___qtablewidgetitem23 = self.extrato_cartao_0.horizontalHeaderItem(0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"icon_cartegori", None));
        ___qtablewidgetitem24 = self.extrato_cartao_0.horizontalHeaderItem(1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Categoria", None));
        ___qtablewidgetitem25 = self.extrato_cartao_0.horizontalHeaderItem(2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Transa\u00e7\u00e3o", None));
        ___qtablewidgetitem26 = self.extrato_cartao_0.horizontalHeaderItem(3)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem27 = self.extrato_cartao_0.horizontalHeaderItem(4)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Opera\u00e7\u00e3o", None));
        ___qtablewidgetitem28 = self.extrato_cartao_0.horizontalHeaderItem(5)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Parcela", None));
        ___qtablewidgetitem29 = self.extrato_cartao_0.horizontalHeaderItem(6)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem30 = self.extrato_cartao_0.horizontalHeaderItem(7)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem31 = self.extrato_cartao_0.horizontalHeaderItem(8)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"data_filter", None));
        ___qtablewidgetitem32 = self.extrato_cartao_0.horizontalHeaderItem(9)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"status_payment", None));
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
        self.name_bank_2.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Limite", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Disponivel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Fechamento", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Vencimento", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"5000", None))
        ___qtablewidgetitem33 = self.table_faturas_ind.horizontalHeaderItem(0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"M\u00eas", None));
        ___qtablewidgetitem34 = self.table_faturas_ind.horizontalHeaderItem(1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o da fatura", None));
        ___qtablewidgetitem35 = self.table_faturas_ind.horizontalHeaderItem(2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Valor da fatura", None));
        ___qtablewidgetitem36 = self.table_faturas_ind.horizontalHeaderItem(3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Valor pago", None));
        ___qtablewidgetitem37 = self.table_faturas_ind.horizontalHeaderItem(4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Pagamento", None));
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Grafico de gastos neste cart\u00e3o por Categoria", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Evolu\u00e7\u00e3o de faturas", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Grafico de gastos neste cart\u00e3o por Data", None))
        self.hide_cards_main.setText("")
        self.show_cards_main.setText("")
        self.pushButton_20.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Ol\u00e1, Boa Tarde.", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"15:23", None))
        self.labelTitle_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Limites Utilizados:</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">R$0,00</span></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Faturas de: </span></p><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">R$0,00</span></p></body></html>", None))
        self.labelTitle_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Limites Disponiveis</span></p><p><span style=\" font-size:20pt; color:#ffffff;\">R$0,00</span></p></body></html>", None))
        self.name_bank_4.setText(QCoreApplication.translate("MainWindow", u"Selecione um Cart\u00e3o", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Limite", None))
        self.label_50.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Fechamento", None))
        self.label_54.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Vencimento", None))
        self.label_56.setText("")
        ___qtablewidgetitem38 = self.table_faturas_ind_3.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Cartao", None));
        ___qtablewidgetitem39 = self.table_faturas_ind_3.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Situa\u00e7\u00e3o da fatura", None));
        ___qtablewidgetitem40 = self.table_faturas_ind_3.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Valor da fatura", None));
        ___qtablewidgetitem41 = self.table_faturas_ind_3.horizontalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Ir para", None));
        self.chart_gastos_all.setTabText(self.chart_gastos_all.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Evolu\u00e7\u00e3o de faturas", None))
        self.chart_gastos_all.setTabText(self.chart_gastos_all.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Maiores gastos", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00e3o em desenvolvimento", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Limite de gastos em:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"0,00", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"de", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"700,00", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Limite:", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Inisira o limite desejavel", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Disponivel para gastar", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"por dia", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"por semana", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"total", None))
        self.chart_gastos_all.setTabText(self.chart_gastos_all.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Limite de Gastos", None))
        self.chart_gastos_all.setTabText(self.chart_gastos_all.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Alertas", None))
        ___qtablewidgetitem42 = self.table_active_cards.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Cartao", None));
        ___qtablewidgetitem43 = self.table_active_cards.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Titular", None));
        ___qtablewidgetitem44 = self.table_active_cards.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Limite", None));
        ___qtablewidgetitem45 = self.table_active_cards.horizontalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Final do cartao", None));
        ___qtablewidgetitem46 = self.table_active_cards.horizontalHeaderItem(4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Vencimento", None));
        ___qtablewidgetitem47 = self.table_active_cards.horizontalHeaderItem(5)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Fechamento", None));
        ___qtablewidgetitem48 = self.table_active_cards.horizontalHeaderItem(6)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"id", None));
        self.select_card.setItemText(0, QCoreApplication.translate("MainWindow", u"C6", None))
        self.select_card.setItemText(1, QCoreApplication.translate("MainWindow", u"NUBANK", None))
        self.select_card.setItemText(2, QCoreApplication.translate("MainWindow", u"BTG", None))
        self.select_card.setItemText(3, QCoreApplication.translate("MainWindow", u"SANTANDER", None))
        self.select_card.setItemText(4, QCoreApplication.translate("MainWindow", u"ITAU", None))
        self.select_card.setItemText(5, QCoreApplication.translate("MainWindow", u"BRADESCO", None))
        self.select_card.setItemText(6, QCoreApplication.translate("MainWindow", u"CAIXA ECONOMICA", None))

        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Fechamento da Fatura:</span></p></body></html>", None))
        self.adclimite.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$", None))
        self.adctitular.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.textcard_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Final do Cart\u00e3o</span></p></body></html>", None))
        self.adcfechamento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"01", None))
        self.textcard_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Titular</span></p></body></html>", None))
        self.textcard.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Limite Total do Cartao</span></p></body></html>", None))
        self.textcard_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Vencimento</span></p></body></html>", None))
        self.adcfinal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXX", None))
        self.adcvencimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"01", None))
        self.add_card_3.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.remover_card_3.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"PAGE3", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PAGE4", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Configura\u00e7\u00f5es da Tabela de Extrato de Lan\u00e7amentos</span></p></body></html>", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#ffffff;\">Ocultar Faturas com valores zerados:</span></p></body></html>", None))
        self.hidden_saldo_fat0_true.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.hidden_saldo_fat0_false.setText(QCoreApplication.translate("MainWindow", u"Nao", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Desenvolvido por Jhonatan Deni", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Estudante de Analise e desenvolvimento de Sistemas", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Meu primeiro projetinho de Finan\u00e7as, inicialmente apenas com uma pagina</p><p align=\"center\">Com intuito de organiza\u00e7\u00e3o e controle de Cartoes de Credito</p><p align=\"center\">Demais op\u00e7oes ainda serao implementadas</p><p align=\"center\">Obrigado :)</p><p align=\"center\"><br/></p><p align=\"justify\"><br/></p></body></html>", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Doa\u00e7\u00e3o para pagar as parcelas da faculdade :)", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"PicPay: @jhonatan.deni", None))
    # retranslateUi

