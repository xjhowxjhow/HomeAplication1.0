
import sqlite3
import os.path
import effects
import os
import sys
import re
import threading
import card_db_test
import card_db_fun
from threading import Thread
import calendar
from frame_bank.card_frame_bank import CardFrameBank
import locale
import emoji
import home_db_query
import home_db_fun
import random
from frame_bank.card_frame_bank import CardFrameBank
from source_ui.categories import Category, Payments_Type, Texts_Erros
from PySide2.QtCore import *
from PySide2 import QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
from asyncio.windows_events import NULL
from time import sleep
from random import randint
from login_pyside24 import Ui_MainWindow
from PySide2.QtCharts import QtCharts
import sys 
import pandas as pd



class Planilhas(Ui_MainWindow):
    
    
    
    
    
    def Open_Xlsx(self):
        self.table_view = self.tableWidget_2
        # apaga a tabela
        self.table_view.setRowCount(0)
        
        print('cartao para importar: ', self.id_card_xlsx_cliked.text())
        try:
            file = QFileDialog.getOpenFileName(
                self, 'Open file', 'c:\\', "Pdf files (*.xlsx)")
            file_name = file[0]
            self.label_51.setText(str(file_name))
            # Ler arquivo Excel usando pandas
            df = pd.read_excel(file_name,sheet_name=0, usecols=[
                        "categoria", "transacao", "data", "operacao", "parcela","valor"])

            # Converter a coluna de data em um objeto datetime e formatá-la como dd/mm/yyyy
            df['data'] = df['data'].apply(lambda x: x.strftime('%d/%m/%Y'))

            #Seta os dados no TableWidget
            #insere os dados
            for row_number, row_data in df.iterrows():
                self.table_view.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.table_view.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                    # alinha
                    self.table_view.item(row_number, column_number).setTextAlignment(Qt.AlignCenter)
            
            return True
        except Exception as e:
            print('erro ao abrir arquivo: ')
            return e



