from pickle import GLOBAL
from re import S
import numpy as np
from PySide2.QtCore import *
from PySide2 import QtWidgets
from PySide2.QtGui import *
import pyautogui
import os.path
from threading import Timer
import threading
from time import sleep
import effects
from datetime import date


class funcoes_geral():
    def parcelado(self):
        
        if self.tablejaneiro_4.item(0,4).text() == 'PARCELADO':
            pyautogui.alert('DESEJA PARCELAR EM QUANTAS VEZES?')

    
    def data_e_hora(self):
        
        data_atual = date.today()
        data_em_texto = data_atual.strftime('%m/%Y')
