
import sqlite3
import pyautogui
import os.path
import effects
import os 
import re
import threading
import card_db_test
import home_db_fun
import card_db_fun
import home_db_query
import calendar
import locale
import emoji
from PySide2.QtCore import *
from PySide2 import QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
from asyncio.windows_events import NULL
from time import sleep
from random import randint
from login_pyside24 import Ui_MainWindow
from PySide2.QtCharts import QtCharts    


class CardFrameBank(Ui_MainWindow):
    
    def creat_new_widget(self,dados): #T
        def thead(self):
            NUMERO_DE_CARTOES = dados[0]
            id = '224993'
            #DADOS[0] = ID BANK
            #DADOS[1] = SALDO
            #DADOS[2] = NOME DO BANCO
            #DADOS[3] = AGENCIA
            #DADOS[4] = CONTA
            #DADOS[5] = TITULAR
            
            styler = CardFrameBank.style_sheet_card_(self,dados[2])

            #TODO CACARTERIZAÇÃO DO WIDGET:
 


            self.stackedWidget_cartao_0 = QStackedWidget()
            self.stackedWidget_cartao_0.setObjectName(u"stackedWidget_cartao_"+str(NUMERO_DE_CARTOES))
            sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
            sizePolicy1.setHorizontalStretch(65)
            sizePolicy1.setVerticalStretch(0)
            sizePolicy1.setHeightForWidth(self.stackedWidget_cartao_0.sizePolicy().hasHeightForWidth())

            #FONTE DO WIDGET
            font3 = QFont()
            font3.setFamily(u"Microsoft YaHei Light")
            font3.setPointSize(10)
            font3.setBold(False)
            font3.setItalic(False)
            font3.setWeight(3)

            #TODO O STACKETD_WIDGET PRINCIPAL:

            self.stackedWidget_cartao_0.setMinimumSize(QSize(400, 200))
            self.stackedWidget_cartao_0.setMaximumSize(QSize(400, 200))
            #TODO STYLE SHET FRENTE
            self.stackedWidget_cartao_0.setStyleSheet("QStackedWidget:hover{border-radius: 10px; border: 3px solid  "+styler[0]+"} QStackedWidget{ background-color: "+styler[1]+"; border-radius: 10px; border: 3px solid rgb(0, 0, 0);border:0px;}")
            self.stackedWidget_cartao_0.setFrameShape(QFrame.StyledPanel)
            self.stackedWidget_cartao_0.setFrameShadow(QFrame.Raised)

            # TODO PAGE 1 DO STACKED E SEUS TRIBUTOS:

            self.frame_cartao_0 = QWidget()
            self.frame_cartao_0.setObjectName(u"frame_cartao_"+str(NUMERO_DE_CARTOES))

            #TODO LOGO DO CARTAO DE ACORDO COM O CARTAO SELECIONADO:

            self.logo_cartao_0 = QFrame(self.frame_cartao_0)
            self.logo_cartao_0.setObjectName(u"logo_cartao_"+str(NUMERO_DE_CARTOES))
            self.logo_cartao_0.setGeometry(QRect(10, 10, 40, 40))
            self.logo_cartao_0.setMaximumSize(QSize(40, 40))
            self.logo_cartao_0.setStyleSheet(u"border: 0px; background-image: "+styler[2]+"")
            self.logo_cartao_0.setFrameShape(QFrame.StyledPanel)
            self.logo_cartao_0.setFrameShadow(QFrame.Raised)

            #TODO BOTAO DE VER COMRPAS DO CARD:

            self.ver_compras_cartao_0 = QPushButton(self.frame_cartao_0, clicked = lambda:CardFrameBank.set_default_bank(self))
            self.ver_compras_cartao_0.setObjectName(u"ver_compras_cartao_"+str(NUMERO_DE_CARTOES))
            self.ver_compras_cartao_0.setGeometry(QRect(280, 150, 110, 30))
            self.ver_compras_cartao_0.setMinimumSize(QSize(110, 30))
            self.ver_compras_cartao_0.setMaximumSize(QSize(110, 25))
            self.ver_compras_cartao_0.setFont(font3)
            self.ver_compras_cartao_0.setStyleSheet(u"\n"
            "\n"
            "QPushButton{\n"
            "	\n"
            "	border-radius: 10px;color:rgb(0,0,0);\n"
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

            #TODO NOME DO TITULAR:
            self.txt_titular_cartao_0 = QLabel(self.frame_cartao_0)
            self.txt_titular_cartao_0.setObjectName(u"txttitular_cartao_"+str(NUMERO_DE_CARTOES))
            self.txt_titular_cartao_0.setGeometry(QRect(200, 10, 151, 36))
            self.txt_titular_cartao_0.setStyleSheet(u"border: 0px;")
            self.txt_titular_cartao_0.setTextFormat(Qt.AutoText)
            self.txt_titular_cartao_0.setScaledContents(False)
            self.txt_titular_cartao_0.setAlignment(Qt.AlignCenter)
            self.txt_titular_cartao_0.setWordWrap(False)

            #TODO BOTAO 3 PONTINHOS DE CONFIG PARA IR PARA PAG 2 OBS: NAO USADO MAIS:

            self.config_cartao_0 = QPushButton(self.frame_cartao_0)

            self.config_cartao_0.setObjectName(u"config_cartao_"+str(NUMERO_DE_CARTOES))
            self.config_cartao_0.setGeometry(QRect(370, 10, 25, 19))
            self.config_cartao_0.setStyleSheet(u"")

            #TODO TEXTO FINAL DO TITULAR:

            self.txt_final_cartao_0 = QLabel(self.frame_cartao_0)
            self.txt_final_cartao_0.setObjectName(u"txtfinal_cartao_"+str(NUMERO_DE_CARTOES))
            self.txt_final_cartao_0.setGeometry(QRect(10, 170, 201, 31))
            self.txt_final_cartao_0.setStyleSheet(u"border: 0px")
            self.txt_final_cartao_0.setTextFormat(Qt.AutoText)
            self.txt_final_cartao_0.setScaledContents(False)
            self.txt_final_cartao_0.setAlignment(Qt.AlignCenter)
            self.txt_final_cartao_0.setWordWrap(False)

            #TODO VALOR LIMITE DISPOINIVEL "R$0":

            self.valor_limitedisponivel_cartao_0 = QLabel(self.frame_cartao_0)
            self.valor_limitedisponivel_cartao_0.setObjectName(u"limitedisponivel_cartao_"+str(NUMERO_DE_CARTOES))
            self.valor_limitedisponivel_cartao_0.setGeometry(QRect(150, 130, 121, 36))
            self.valor_limitedisponivel_cartao_0.setStyleSheet(u"border: 0px;")
            self.valor_limitedisponivel_cartao_0.setTextFormat(Qt.AutoText)
            self.valor_limitedisponivel_cartao_0.setScaledContents(False)
            self.valor_limitedisponivel_cartao_0.setAlignment(Qt.AlignCenter)
            self.valor_limitedisponivel_cartao_0.setWordWrap(False)

            #TODO TEXTO DO LIMITE DISPONIVEL"LIMITE DISPONIVEL"
            self.txt_limite_disponivel_cartao_0 = QLabel(self.frame_cartao_0)
            self.txt_limite_disponivel_cartao_0.setObjectName(u"limite_disponivel_cartao_"+str(NUMERO_DE_CARTOES))
            self.txt_limite_disponivel_cartao_0.setGeometry(QRect(10, 130, 141, 36))
            self.txt_limite_disponivel_cartao_0.setStyleSheet(u"border: 0px;")
            self.txt_limite_disponivel_cartao_0.setTextFormat(Qt.AutoText)
            self.txt_limite_disponivel_cartao_0.setScaledContents(False)
            self.txt_limite_disponivel_cartao_0.setAlignment(Qt.AlignCenter)
            self.txt_limite_disponivel_cartao_0.setWordWrap(False)

            #TODO LABEL TEXTO DO FATURA ATUAL:

            self.txt_fatura_atual_cartao_0 = QLabel(self.frame_cartao_0)
            self.txt_fatura_atual_cartao_0.setObjectName(u"txt_fatura_atual_cartao_"+str(NUMERO_DE_CARTOES))
            self.txt_fatura_atual_cartao_0.setGeometry(QRect(10, 70, 111, 36))
            self.txt_fatura_atual_cartao_0.setStyleSheet(u"border: 0px;")
            self.txt_fatura_atual_cartao_0.setTextFormat(Qt.AutoText)
            self.txt_fatura_atual_cartao_0.setScaledContents(False)
            self.txt_fatura_atual_cartao_0.setAlignment(Qt.AlignCenter)
            self.txt_fatura_atual_cartao_0.setWordWrap(False)

            #TODO LABEL VALOR DE FATURA ATUAL: 
            self.valor_faturaatual_cartao_0 = QLabel(self.frame_cartao_0)
            self.valor_faturaatual_cartao_0.setObjectName(u"saldo_bancario_"+str(NUMERO_DE_CARTOES))
            self.valor_faturaatual_cartao_0.setGeometry(QRect(10, 100, 178, 36))
            self.valor_faturaatual_cartao_0.setStyleSheet(u"border: 0px;")
            self.valor_faturaatual_cartao_0.setTextFormat(Qt.AutoText)
            self.valor_faturaatual_cartao_0.setScaledContents(False)
            self.valor_faturaatual_cartao_0.setAlignment(Qt.AlignCenter)
            self.valor_faturaatual_cartao_0.setWordWrap(False)
            self.stackedWidget_cartao_0.addWidget(self.frame_cartao_0)

            #TODO PAGE 2 DO CARTAO FRAME CONFIG :


            self.frame_verso_0 = QWidget()
            self.frame_verso_0.setObjectName(u"frame_verso_"+str(NUMERO_DE_CARTOES))

            # TODO FRAME DO WIDGET TOTAL PAG 2 (QUE CONTEM OS INTENS):

            #CONFIG DA PAGE
            self.frame_config_cartao_0 = QFrame(self.frame_verso_0)
            self.frame_config_cartao_0.setObjectName(u"frame_config_cartao_"+str(NUMERO_DE_CARTOES))
            self.frame_config_cartao_0.setGeometry(QRect(0, 0, 400, 200))
            sizePolicy1.setHeightForWidth(self.frame_config_cartao_0.sizePolicy().hasHeightForWidth())
            self.frame_config_cartao_0.setSizePolicy(sizePolicy1)
            self.frame_config_cartao_0.setMinimumSize(QSize(0, 0))
            self.frame_config_cartao_0.setMaximumSize(QSize(400, 200))
            self.frame_config_cartao_0.setStyleSheet(u"background-color: "+styler[1]+";\n"
            "border-radius: 10px;\n"
            "border: 3px solid  rgb(0, 0, 0);\n"
            "border:0px;")
            self.frame_config_cartao_0.setFrameShape(QFrame.StyledPanel)
            self.frame_config_cartao_0.setFrameShadow(QFrame.Raised)


            # TODO VERSO LOGO 2
            self.logo_config_cartao_0 = QFrame(self.frame_config_cartao_0)
            self.logo_config_cartao_0.setObjectName(u"logo_config_cartao_"+str(NUMERO_DE_CARTOES))
            self.logo_config_cartao_0.setGeometry(QRect(10, 10, 40, 40))
            self.logo_config_cartao_0.setMaximumSize(QSize(40, 40))
            self.logo_config_cartao_0.setStyleSheet(u"border: 0px;\n"
            "background-image: "+styler[2]+";\n"
            "")
            self.logo_config_cartao_0.setFrameShape(QFrame.StyledPanel)
            self.logo_config_cartao_0.setFrameShadow(QFrame.Raised)

            #TODO LABEL LIMITE CARTAO:

            self.limite_cartao_0 = QLabel(self.frame_config_cartao_0)
            self.limite_cartao_0.setObjectName(u"limite_cartao_"+str(NUMERO_DE_CARTOES))
            self.limite_cartao_0.setGeometry(QRect(10, 50, 181, 36))
            self.limite_cartao_0.setStyleSheet(u"border: 0px;background-color: rgba(255, 255, 255, 0);")
            self.limite_cartao_0.setTextFormat(Qt.AutoText)
            self.limite_cartao_0.setScaledContents(False)
            self.limite_cartao_0.setAlignment(Qt.AlignCenter)
            self.limite_cartao_0.setWordWrap(False)

            #TODO BOTAO SALVA CONFIG CARTAO VERSO LIMITE E ETC:
            self.salva_configcartao_0 = QPushButton(self.frame_config_cartao_0,clicked = lambda:CardFrameBank.object_name(self))
            self.salva_configcartao_0.setObjectName(u"salva_configcartao_"+str(NUMERO_DE_CARTOES))
            self.salva_configcartao_0.setGeometry(QRect(280, 150, 110, 30))
            self.salva_configcartao_0.setMinimumSize(QSize(110, 30))
            self.salva_configcartao_0.setMaximumSize(QSize(110, 25))
            self.salva_configcartao_0.setFont(font3)
            self.salva_configcartao_0.setStyleSheet(u"\n"
            "\n"
            "QPushButton{\n"
            "	\n"
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

            # TODO LABEL DE COLOCAR LIMITE DO CARTAO:
            self.setlimitcartao_0 = QLineEdit(self.frame_config_cartao_0)
            self.setlimitcartao_0.setObjectName(u"setlimitcartao_"+str(NUMERO_DE_CARTOES))
            self.setlimitcartao_0.setGeometry(QRect(10, 80, 171, 31))
            self.setlimitcartao_0.setStyleSheet(u"background-color: rgba(255, 255, 255, 0); \n"
            "\n"
            "	border-radius: 10px;\n"
            "\n"
            "	\n"
            "	background-color: rgb(238, 238, 238);\n"
            "\n"
            "	border: 1px solid  rgb(55, 55, 55);")
            self.setlimitcartao_0.setAlignment(Qt.AlignCenter)

            # TODO LABEL SETA NOME DO TITULAR:

            self.titular_cartao_0 = QLabel(self.frame_config_cartao_0)
            self.titular_cartao_0.setObjectName(u"titular_cartao_"+str(NUMERO_DE_CARTOES))
            self.titular_cartao_0.setGeometry(QRect(200, 50, 181, 36))
            self.titular_cartao_0.setStyleSheet(u"border: 0px; background-color: rgba(255, 255, 255, 0); ")
            self.titular_cartao_0.setTextFormat(Qt.AutoText)
            self.titular_cartao_0.setScaledContents(False)
            self.titular_cartao_0.setAlignment(Qt.AlignCenter)
            self.titular_cartao_0.setWordWrap(False)
            self.settitularcartao_0 = QLineEdit(self.frame_config_cartao_0)
            self.settitularcartao_0.setObjectName(u"settitularcartao_"+str(NUMERO_DE_CARTOES))
            self.settitularcartao_0.setGeometry(QRect(200, 80, 171, 31))
            self.settitularcartao_0.setStyleSheet(u"	font: 25 10pt \"Microsoft YaHei Light\";\n"
            "\n"
            "	border-radius: 10px;\n"
            "\n"
            "	\n"
            "	background-color: rgb(238, 238, 238);\n"
            "\n"
            "	border: 1px solid  rgb(55, 55, 55);")
            self.settitularcartao_0.setAlignment(Qt.AlignCenter)

            #TODO LABEL SET FINAL DO CARTAO:

            self.final_cartao_0 = QLabel(self.frame_config_cartao_0)
            self.final_cartao_0.setObjectName(u"final_cartao_"+str(NUMERO_DE_CARTOES))
            self.final_cartao_0.setGeometry(QRect(10, 120, 181, 36))
            self.final_cartao_0.setStyleSheet(u"border: 0px;background-color: rgba(255, 255, 255, 0); \n"
            "font: 25 12pt \"Microsoft YaHei Light\";")
            self.final_cartao_0.setTextFormat(Qt.AutoText)
            self.final_cartao_0.setScaledContents(False)
            self.final_cartao_0.setAlignment(Qt.AlignCenter)
            self.final_cartao_0.setWordWrap(False)

            # TODO SET LABEL FINAL DO CARTAO OS NUMEROS:

            self.setfinalcartao_0 = QLineEdit(self.frame_config_cartao_0)
            self.setfinalcartao_0.setObjectName(u"setfinalcartao_"+str(NUMERO_DE_CARTOES))
            self.setfinalcartao_0.setGeometry(QRect(10, 150, 171, 31))
            self.setfinalcartao_0.setStyleSheet(u"border-radius: 10px;\n"
            "\n"
            "	\n"
            "	background-color: rgb(238, 238, 238);\n"
            "\n"
            "	border: 1px solid  rgb(55, 55, 55);")
            self.setfinalcartao_0.setAlignment(Qt.AlignCenter)
            self.stackedWidget_cartao_0.addWidget(self.frame_verso_0)

            self.layout_add_frame_bank.addWidget(self.stackedWidget_cartao_0)
            


            #DADOS[0] = ID BANK
            #DADOS[1] = SALDO
            #DADOS[2] = NOME DO BANCO
            #DADOS[3] = AGENCIA
            #DADOS[4] = CONTA
            #DADOS[5] = TITULAR


            format_val = "{:.2f}".format(float(dados[1]))


            #TODO AQUI VAI SETAR OS TEXTOS POR PADRAO

            self.valor_faturaatual_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff\">R$"+str(format_val)+"</span></p></body></html>", None))
            self.txt_limite_disponivel_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\"></span></p></body></html>", None))
            self.ver_compras_cartao_0.setText(QCoreApplication.translate("MainWindow", u"Trocar Principal", None))
            self.txt_fatura_atual_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Saldo Disponivel</span></p></body></html>", None))
            self.valor_limitedisponivel_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-weight:600; color:#ffffff;\"></span></p></body></html>", None))
            self.config_cartao_0.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.txt_titular_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">"+str(dados[5])+"</span></p></body></html>", None))
            self.txt_final_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Agencia: "+str(dados[3])+" Conta: "+str(dados[4])+"</span></p></body></html>", None))
            self.limite_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Limite Total do Cartao</span></p></body></html>", None))
            self.salva_configcartao_0.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
            self.setlimitcartao_0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$", None))
            self.titular_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Titular</span></p></body></html>", None))
            self.final_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Final do Cart\u00e3o</span></p></body></html>", None))
            self.setfinalcartao_0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXX", None))
        thread = threading.Thread(target=thead(self))
        thread.start()
        
        
    def style_sheet_card_(self,nome_bank):

        
        card_select = nome_bank
        
        
        if card_select == 'C6':
            style_hover ="rgb(255, 255, 255)"
            style2_main ="qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(16, 16, 16, 255), stop:0.482307 rgba(50, 50, 50, 255), stop:0.996068 rgba(16, 16, 16, 255), stop:1 rgba(0, 0, 0, 255))"
            icon = "url(:/menu/c6.jpg)"

            return [style_hover,style2_main,icon]

        if card_select == 'NUBANK':   
            style_hover ="rgb(93, 7, 150)"
            style2_main ="rgb(130, 10, 209)"
            icon = "url(:/menu/nu-icon.png)"

            return [style_hover,style2_main,icon]

        
        if card_select == 'BTG':
            style_hover ="rgb(93, 7, 150)"
            style2_main ="qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0052356 rgba(8, 28, 43, 255), stop:0.434555 rgba(19, 51, 71, 255), stop:0.825916 rgba(29, 72, 98, 255));"
            icon = "url(:/menu/btg-icon.png)"

            return [style_hover,style2_main,icon]

        
        if card_select == 'SANTANDER':
            style_hover ="rgb(55, 55, 55)"
            style2_main ="qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0052356 rgba(242, 0, 0, 255), stop:0.434555 rgba(217, 43, 0, 255), stop:0.825916 rgba(152, 50, 0, 255))"
            icon = "url(:/menu/santander-icon.png)"

            return [style_hover,style2_main,icon]

        
        if card_select == 'ITAU':
            style_hover ="rgb(0, 48, 145)"
            style2_main ="qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0052356 rgba(242, 104, 1, 255), stop:0.434555 rgba(255, 126, 1, 255), stop:0.825916 rgba(255, 159, 0, 255));"
            icon = "url(:/menu/itau-icon.png)"

            return [style_hover,style2_main,icon]

        
        if card_select == 'BRADESCO':
            style_hover ="rgb(242, 0, 0)"
            style2_main ="qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0052356 rgba(170, 29, 113, 255), stop:0.434555 rgba(204, 16, 91, 255), stop:0.825916 rgba(235, 5, 65, 255))"
            icon = "url(:/menu/bradesco-icon.png)"

            return [style_hover,style2_main,icon]


        if card_select == 'CAIXA ECONOMICA':
            style_hover ="rgb(248, 162, 61)"
            style2_main ="rgb(0, 106, 166)"
            icon = "url(:/menu/caixa-icon.png)"

            return [style_hover,style2_main,icon]
        
        

    def set_default_bank(self): #NT
        
        #_____________________________________________________
        # Pega nome do botao que foi clicado na hora:
        name_obj = self.focusWidget().objectName()

        #PARA ACESSAR OS BOTOES TERIAMOS QUE UTILIZAR UM INDEX DA LISTA DE BOTOES.
        self.botoes = self.findChildren(QPushButton , str(name_obj))
        #PEGA O ID PELO NO DO BT
        ids = re.sub('[^0-9]', '', name_obj)
        home_db_query.Return_Values_Conditions._update_default_bank(ids)
        
        #UPDATE_UI
        home_db_fun.Set_values_startup._set_start_ag_b_t(self)
        home_db_fun.Set_values_startup._set_Saldo(self)
        return True
    
    
    
    def _update_frame_cards_saldo(self,id):
        saldo = home_db_query.Return_Values_Conditions._return_saldo(id)
        convert = home_db_fun.Convert_Moedas._usd_to_brl(self,saldo)
        print('id chil saldo',convert)

        card_info = 'saldo_bancario_'
        text = (QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff\">"+str(convert)+"</span></p></body></html>", None))
        self.qlabel = self.findChildren(QLabel , str(card_info+str(id)))
        self.qlabel[0].setText(text)

    
    
    def count_cards_startup(self):
        #GET IDS BANKS
        ids_banks = home_db_query.Return_values.return_banks_active()
        
        #LAYOUT self.layout_add_frame_bank
    

        list = []
        self.frames2 = self.layout_add_frame_bank
        print('self.frames',self.frames2.count())
        for i in range (self.frames2.count()):
            a = self.frames2.itemAt(i).widget().objectName()
            list.append(a)
        print(list)
        
        if len(list) < len(ids_banks):
            return True
        else:
            return False