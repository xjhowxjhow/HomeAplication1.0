
from PySide2.QtCore import *
from PySide2 import QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
from login_pyside24 import Ui_MainWindow





#RECEBE O FRAME PARA APLICAR O EFEITO DE SOMBRA
class InitShadow(QtWidgets.QGraphicsDropShadowEffect):
    def __init__(self, frame):
        super().__init__(frame)
        self.frame = frame
        self.setBlurRadius(20)
        self.setColor(QColor(0, 0, 0, 60))
        self.frame.setGraphicsEffect(self)
        




class set_shadow(Ui_MainWindow):
    
    def sets(self):
        self.applyShadow = InitShadow
        #FRAMES:
        #SETA A SOMBRAS
        self.applyShadow(self.frame_43)
        self.applyShadow(self.welcome_2)
        self.applyShadow(self.frame_51)
        self.applyShadow(self.tableWidget)
        self.applyShadow(self.extrat_meses_2)
        self.applyShadow(self.frame_87)
        self.applyShadow(self.config_new_lan_3)
        self.applyShadow(self.frame_88)
        self.applyShadow(self.scrollArea_13)
        self.applyShadow(self.frame_89)
        self.applyShadow(self.frame_96)
        self.applyShadow(self.scrollArea_4)
        self.applyShadow(self.main_dasht_top)
        self.applyShadow(self.datails_fatura_card_4)
        self.applyShadow(self.frame_12)
        self.applyShadow(self.frame_60)
        self.applyShadow(self.frame_31)
        self.applyShadow(self.stackedWidget_58)