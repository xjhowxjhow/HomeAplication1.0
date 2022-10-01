
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
        self.scrollArea_9
        self.scrollAreaWidgetContents_2
        
        
        #SETA A SOMBRAS
        self.applyShadow(self.scrollArea_9)
        self.applyShadow(self.scrollAreaWidgetContents_2)
        