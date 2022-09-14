
import sqlite3
import pyautogui
import os.path
import effects
import os 
import re
import threading
import card_db_test
import card_db_fun
import calendar
import locale
import emoji
import home_db_query
import random
from PySide2.QtCore import *
from PySide2 import QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from datetime import datetime
from dateutil.relativedelta import relativedelta
from datetime import date
from asyncio.windows_events import NULL
from time import sleep
from random import randint
from login_pyside24 import Ui_MainWindow
from PySide2.QtCharts import QtCharts



class mainpage(Ui_MainWindow):





    #NOVO LANCAMENTO
    def _new_lancamento(self):
        #OBRIGATORIOS

        # TABLE new_lancamento
        id_lancamento = randint(0,99999999)
        id_bank = self.comboBox_11.currentText() # ID DA CONTA BANCO PARA DEBITO
        tipo = self.comboBox_25.currentText() #Entrada ou Saida
        
        data_lancamento = self.lancamento_programado_2.text()
        format_data_lancamento = datetime.strptime(data_lancamento, '%d/%m/%Y').strftime('%Y-%m-%d')
        data_lancamento = format_data_lancamento
        
        
        categoria = self.comboBox_21.currentText()
        pagamento = self.comboBox_27.currentText()
        valor = self.lineEdit_13.text()
        descricao = self.lineEdit_11.text()
        dados = [id_bank, data_lancamento, categoria, pagamento, valor,tipo, descricao]
        
        #EXECUTE QUERY
        home_db_query.Add_values._add_new_lancamento(id_lancamento,dados)
        # TABLE config_lancamento
        id_lancamento_config_lancamento =id_lancamento
        id_bank = self.comboBox_11.currentText() # ID DA CONTA BANCO PARA DEBITO
        if self.comboBox_23.currentText() == 'Sim':
            recorrente= self.comboBox_23.currentText()
            recorrente_m_d_s_y = self.comboBox_26.currentText()
            recorrente_dia = self.lineEdit_14.text()
        else:
            recorrente= self.comboBox_23.currentText()
            recorrente_m_d_s_y = 'False'
            recorrente_dia = 'False'
            
        
        anexos = 'test.pdf'
        dados_lan =[id_bank, recorrente, recorrente_m_d_s_y, recorrente_dia, anexos]
        #EXECUTE QUERY
        home_db_query.Add_values._config_lancamento(id_lancamento_config_lancamento,dados_lan)
        
        
        #TABLE STATUS_LANCAMENTO:
        id_lancamento_status =id_lancamento
        id_bank = self.comboBox_11.currentText() # ID DA CONTA BANCO PARA DEBITO
        vencimento = ''
        if self.comboBox_22.currentText() == 'Sim':
            vencimento = self.lancamento_programado_2.text() # NAO PROGRAMADO JA FOI RECEBIDO
            status_pago = 'pago'
        else:
            vencimento = self.lancamento_programado.text() # PROGRAMADO NAO FOI RECEBIDO
            status_pago = 'pendente'
        dados_status = [id_bank, vencimento,status_pago]
        #EXECUTE QUERY
        home_db_query.Add_values._status_lancamento(id_lancamento_status,dados_status)
        
        
        
        #TABLE_PRIORIDADE VALOR:
        id_lancamentoprioridade = id_lancamento
        id_bank = self.comboBox_11.currentText() # ID DA CONTA BANCO PARA DEBITO
        prioridade = ''
        if int(valor) >1000:
            prioridade = 'alto'
        elif int(valor) >500:
            prioridade = 'medio'
        else:
            prioridade = 'baixo'
        
        dados_prioridade = [id_bank, prioridade]
        #EXECUTE QUERY
        home_db_query.Add_values._prioridade_value(id_lancamentoprioridade, dados_prioridade)

        #ADD TO TABLE LANCAMENTO
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)

        #LEGENDA:
        # 0 = CHECKBOX
        # 1 = ID_LANCAMENTO
        # 2 = ID_CONTA / ID_CARTAO / ID BANK
        # 3 = TIPO: ENTRADA / SAIDA
        # 4 = DATA DO LANÇAMENTO
        # 5 = PRIORIDADE 
        # 6 = CATEGORIA
        # 7 = METODO DE PAGAMENTO
        # 8 = VALOR
        # 9 = STATUS
        # 10 = SALDO

        i = rowPosition
            
        # 0 = CHECKBOX:
        
        self.widget_item = QWidget()
        self.layout = QHBoxLayout()
        self.chebox = QCheckBox()
        self.chebox.setObjectName(u"chebox")
        self.chebox.setText(u"")
        self.chebox.setGeometry(QRect(0, 0, 40, 40))
        self.chebox.setChecked(False)
        self.chebox.setStyleSheet(u"background-color: rgba(255, 255, 255,0); margin-left:10px; \n")
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.chebox)
        self.widget_item.setLayout(self.layout)
        self.table.setCellWidget(i, 0, self.chebox)

        
        # 1 = ID_LANCAMENTO

        self.table.setItem(i, 1, QTableWidgetItem(str(id_lancamento)))
        
        # 2 = ID_CONTA / ID_CARTAO / ID BANK
        

        self.table.setItem(i, 2, QTableWidgetItem(str(id_bank)))
        
        # 3 = TIPO: ENTRADA / SAIDA

        self.table.setItem(i, 3, QTableWidgetItem(str(tipo)))
        
        
        
        # 4 = DATA DO LANÇAMENTO 
        self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
        self.dateedit.setDateTime(QtCore.QDateTime.currentDateTime()) # MUDAR DPOIS
        self.dateedit.calendarWidget().setGridVisible(True)
        self.dateedit.calendarWidget().setFirstDayOfWeek(Qt.Monday)
        self.dateedit.calendarWidget().setStyleSheet("QCalendarWidget QToolButton { color: white; font-size: 12px; icon-size: 20px, 20px; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QMenu { left: 20px; color: white; font-size: 14px; background-color: rgb(100, 100, 100); } QCalendarWidget QSpinBox { font-size: 14px; color: white; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); selection-background-color: rgb(136, 136, 136); selection-color: rgb(255, 255, 255); } QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:65px; } QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;} QCalendarWidget QSpinBox::up-arrow { width:56px;  height:56px; } QCalendarWidget QSpinBox::down-arrow { width:56px;  height:56px; } /* header row */ QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); } /* normal days */ QCalendarWidget QAbstractItemView:enabled { font-size: 14px; color: rgb(180, 180, 180); background-color: black; selection-background-color: rgb(64, 64, 64); selection-color: rgb(0, 255, 0); } /* days in other months */ /* navigation bar */ QCalendarWidget QWidget#qt_calendar_navigationbar { background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QAbstractItemView:disabled { color: rgb(64, 64, 64);}")

        self.table.setCellWidget(i, 4, self.dateedit)
        
        # 5 = PRIORIDDE 


        self.table.setItem(i, 5, QTableWidgetItem(str(prioridade)))
        backgroud = '#00ff00'
        if prioridade == 'baixo':
            backgroud = '#ff0000'
        elif prioridade == 'medio':
            backgroud = '#ffa500'
        elif prioridade == 'alto':
            backgroud = '#00ff00'
        
        self.table.setItem(i, 5, QTableWidgetItem(str(prioridade)))
        self.table.item(i,5).setTextAlignment(Qt.AlignCenter)

        
        self.frame = QFrame()
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(7, 16777215))
        self.frame.setStyleSheet(u"background-color:"+backgroud+"; border-radius:3px; margin:7px;")
        self.table.setCellWidget(i, 5, self.frame)
        
        
        # 6 = CATEGORIA

        
        list_icon = ["delivery","appstrans","comida","mercado","lazer","icons8-casa-96","inuteis","servicos","streaming","urgencia","gatos","dogs","medico","viagem","eletronico","domesticos"]
        icone = QFrame()
        icone.setMaximumSize(QSize(35, 35))
        icone.setStyleSheet(u"background-color:rgba(255,255,255,0);border-image: url(:/icons-cards/src-page-cartoes/"+list_icon[randint(0,10)]+".png);\n"
            "\n"
            "\n"
            "background-position: center;\n"
            "\n"
            "background-repeat:no-repeat;")
        self.table.setItem(i, 6, QTableWidgetItem(str(categoria)))
        self.table.item(i,6).setTextAlignment(Qt.AlignCenter)
        self.table.setCellWidget(i, 6, icone)
        
   

        # 7 = METODO DE PAGAMENTO

        #todo mudar aqui dps

        if tipo == 'Entrada':
            color_label = '#00ff00'
        else:
            color_label = '#ff000'

            
        self.label = QLabel()
        self.label.setStyleSheet(u"background-color:rgb(101, 53, 145);border-radius:3px; margin:7px;")
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Bahnschrift Light Condensed")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\";color:"+color_label+";\">"+pagamento+"</span></p></body></html>", None))
        self.table.setCellWidget(i, 7, self.label)
        
        
        #/PAGAM




        # 8 = VALOR

        
        self.table.setItem(i, 8, QTableWidgetItem(str("R$%s"%valor)))
        self.table.item(i,8).setTextAlignment(Qt.AlignCenter)
        
        
        
        
        # 9 = STATUS

        
        self.pushButton_pago = QPushButton()
        self.pushButton_pago.setObjectName(u"pagobuto")
        self.pushButton_pago.setGeometry(QRect(140, 180, 61, 31))
           

        if status_pago == 'pago':
            
            self.pushButton_pago.setStyleSheet("QPushButton{margin:10px;border-radius:3px;background-color: rgb(86, 202, 164);border: 1px solid  rgb(55, 55, 55);}QPushButton:hover{background-color: rgb(65, 160, 88);border: 2px solid  rgb(255, 255, 255);}QPushButton:pressed{background-color: rgb(65, 160, 88);border: 2px solid  rgb(55, 55, 55);}")
            self.pushButton_pago.setText("Pago")
        else:
            self.pushButton_pago.setStyleSheet("QPushButton{margin:10px;border-radius:3px;background-color: rgb(214, 154, 90);border: 1px solid  rgb(55, 55, 55);}QPushButton:hover{background-color: rgb(163, 117, 68);border: 2px solid  rgb(255, 255, 255);}QPushButton:pressed{background-color: rgb(163, 117, 68) ;border: 2px solid  rgb(55, 55, 55);}")
            self.pushButton_pago.setText("Pendene")

            
        self.pushButton_pago.setFont(self.font)
        self.table.setCellWidget(i, 9, self.pushButton_pago)

        # 10 = SALDO
        return_saldo = home_db_query.Return_values.return_saldo()
        self.table.setItem(i, 10, QTableWidgetItem(str("R$%s"%return_saldo)))
        self.table.item(i,10).setTextAlignment(Qt.AlignCenter)
        


    #EVENTS FOR BUTTONS
    def _event_change_stakecard(self):
        if self.comboBox_24.currentText() == "Sim":
            return self.stackedWidgetadc_2.setCurrentWidget(self.page_10)
        else:
         self.stackedWidgetadc_2.setCurrentWidget(self.stackedWidgetadc_2Page1)
        
    # ADD VALORES AO BANCO DE DADOS BANK
    def _add_bank(self):
        # CONTA BANCARIA
        nome_bank = self.select_conta_bancaria.currentText()
        titular = self.adctitular_conta.text()
        agencia = self.adcagencia_conta.text()
        conta = self.adc_conta_conta.text()
        saldo_inicial = self.adc_saldo_conta.text()
        if_credit_card = self.comboBox_24.currentText()
        
        
        #CARTAO DE CREDITO
        cartao_nome = self.select_conta_bancaria.currentText()
        limite = self.adclimite_2.text()
        titular_card = self.adctitular_2.text()
        final_card = self.adcfinal_2.text()
        vencimento = self.adcvencimento_2.text()
        fechamento = self.adcfechamento_2.text()
        
        rand_id = randint(0, 999999) # ID

        # CONEXAO COM O BANCO DE DADOS
        data = []
        
        default_bank= self.combo_bank_padrao.currentText()
        if default_bank == 'Sim':
            
            home_db_query.Add_values._default_bank(rand_id)
        elif default_bank == '':
            pass
        else:
            pass
        
        if if_credit_card == "Sim":
            
            # colunas_contas = ['saldo_inicial','nome_banco','agencia','num_conta','titular','cartao_credito_id']
            # colunas_cartao = ['nome_cartao','titular','limite','final','vencimento','fechamento']
            data.append(([saldo_inicial, nome_bank, agencia, conta, titular, if_credit_card], [cartao_nome, titular_card, limite, final_card, vencimento, fechamento]))
            credit_card = True
            home_db_query.Add_values._add_new_bank(data[0], credit_card, rand_id)
            return card_db_fun.funcoes_cartao.inicia_cartoes_oculto_se_nao_existir(self)
            
            
        elif if_credit_card == '':
            print("Não tem cartão de crédito selecionar algo no campo")
        else:
            data.append((nome_bank, titular, agencia, conta, saldo_inicial, if_credit_card))
            credit_card = False
            return home_db_query.Add_values._add_new_bank(data, credit_card, rand_id)

        
    def _categorias_entra_said(self):
        saidas = ['Energia','Gás','Água','Luz','Telefone','Internet','Boletos','Servicos','Aluguel','Impostos','Veiculos','IPVA','IPTU','Outros']
        entradas =['Salario','Rendimentos','Beneficios','Criptomoedas','Investimentos','Cheques','Transferencia','Depositos','Pagamentos','Outros']
        
        metodos_pagamento_entrada = ['Credito em Conta','Dinheiro','Transferência','Cheque','Outros','Rendimentos','Criptomoedas','Pix']
        
        metodos_pagamento_saida = ['Debito em Conta','Dinheiro','Transferência','Cheque','Outros','Pix']
        
        if self.comboBox_25.currentText() == "Entrada":
            self.comboBox_21.clear()
            self.comboBox_27.clear()
            self.comboBox_27.addItems(metodos_pagamento_entrada)
            self.comboBox_21.addItems(entradas)
            
            
        elif self.comboBox_25.currentText() == "":
            self.comboBox_21.clear()
            self.comboBox_27.clear()
            return QMessageBox.warning(self, "Atenção", "Selecione uma categoria")
        else:
            self.comboBox_21.clear()
            self.comboBox_27.clear()
            self.comboBox_21.addItems(saidas)
            self.comboBox_27.addItems(metodos_pagamento_saida)

    def open_pdf(self):
        
        return self.frame_options_pdf.show()
        
    def change_color(self):
        rand_color = randint(0,255), randint(0,255), randint(0,255)
        # self.s.setStyleSheet("background-color: rgb(0, 0, 0)")
    def filtro_table_header(self, logicalIndex):
        icon4 = QIcon()
        
        if logicalIndex >1:
        
            if self.table.horizontalHeaderItem(logicalIndex).data(256) == "DOW":
                item = self.table.horizontalHeaderItem(logicalIndex)
                icon4.addFile(u":/main_menutable/main_page_tables/decrecente.png", QSize(), QIcon.Normal, QIcon.Off)
                self.table.horizontalHeaderItem(logicalIndex).setData(256, "UP")
                item.setIcon(icon4)

            else:
                item = self.table.horizontalHeaderItem(logicalIndex)
                icon4.addFile(u":/main_menutable/main_page_tables/ascendente.png", QSize(), QIcon.Normal, QIcon.Off)
                self.table.horizontalHeaderItem(logicalIndex).setData(256, "DOW")
                item.setIcon(icon4)
        else:
            
            if self.table.cellWidget(0, 0).isChecked() ==False:
                row_count = self.table.rowCount()
                item = self.table.horizontalHeaderItem(logicalIndex)
                icon4.addFile(u":/main_menutable/main_page_tables/checked.png", QSize(), QIcon.Normal, QIcon.Off)
                item.setIcon(icon4)
                for i in range(row_count):
                    self.table.cellWidget(i, 0).setChecked(True)
            else:
                row_count = self.table.rowCount()
                item = self.table.horizontalHeaderItem(logicalIndex)
                icon4.addFile(u":/main_menutable/main_page_tables/unchecked.png", QSize(), QIcon.Normal, QIcon.Off)
                item.setIcon(icon4)
                for i in range(row_count):
                    self.table.cellWidget(i, 0).setChecked(False)

            
        return True


    def load_extrato_filter(self):
        self.table = self.tableWidget
        cont = self.table.rowCount()
        if cont > 0:
            for i in range (cont): 
                if self.table.rowCount() >= 0:
                    self.table.removeRow(self.table.rowCount()-1)
        
        #LEGENDA:
        # 0 = CHECKBOX
        # 1 = ID_LANCAMENTO
        # 2 = ID_CONTA / ID_CARTAO / ID BANK
        # 3 = TIPO: ENTRADA / SAIDA
        # 4 = DATA DO LANÇAMENTO
        # 5 = PRIORIDADE 
        # 6 = CATEGORIA
        # 7 = METODO DE PAGAMENTO
        # 8 = VALOR
        # 9 = STATUS
        # 10 = SALDO
        ids = card_db_test.Main_page_values._cards_ids_all()
        print("COUNT IDSSS-----------",len(ids))

        # TODO LANCAMENTO DE FATURAS CARTOES
        if not ids:
            pass
        else:
            for i in range(len(ids)):
                row_count = self.table.rowCount()
                add_row = self.table.insertRow(row_count)


                # 0 = CHECKBOX:

                self.widget_item = QWidget()
                self.layout = QHBoxLayout()
                self.chebox = QCheckBox()
                self.chebox.setObjectName(u"chebox")
                self.chebox.setText(u"")
                self.chebox.setGeometry(QRect(0, 0, 40, 40))
                self.chebox.setChecked(False)
                self.chebox.setStyleSheet(u"background-color: rgba(255, 255, 255,0); margin-left:10px; \n")
                self.layout.setAlignment(Qt.AlignCenter)
                self.layout.addWidget(self.chebox)
                self.widget_item.setLayout(self.layout)
                self.table.setCellWidget(i, 0, self.chebox)


                # 1 = ID_LANCAMENTO
                id_lancamento = ids[i][0]
                self.table.setItem(row_count, 1, QTableWidgetItem(str(id_lancamento)))
                print("ID_LANCAMENTO",id_lancamento)
                # 2 = ID_CONTA / ID_CARTAO / ID BANK

                id_conta = ids[i][0]
                self.table.setItem(row_count, 2, QTableWidgetItem(str(id_conta)))
                print("ID_CONTA",id_conta)
                # 3 = TIPO: ENTRADA / SAIDA
                entra_saida = 'SAIDA'
                self.table.setItem(row_count, 3, QTableWidgetItem(str(entra_saida)))
                print("ENTRA_SAIDA",entra_saida)


                # 4 = DATA DO LANÇAMENTO 
                # VENCIMENTO DA FATURA
                
                date_ven = card_db_test.Ui_db._vencimento(ids[i][0])
                mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                #TODO LOGICA %S CONSULTA DB DIA VENCIMENTO , MES E ANO ATUAL
                #M D Y
                vencimento = "%s-%s-%s"%(date_ven,mes,Dates_end_times.current_date_extrato(self)[0])
                print("VENCIMENTO",vencimento)
                self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
                self.dateedit.setDate(QtCore.QDate.fromString(vencimento, "dd-MM-yyyy")) #NAO SEI SE TA CERTO
                self.dateedit.calendarWidget().setGridVisible(True)
                self.dateedit.calendarWidget().setFirstDayOfWeek(Qt.Monday)
                self.dateedit.calendarWidget().setStyleSheet("QCalendarWidget QToolButton { color: white; font-size: 12px; icon-size: 20px, 20px; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QMenu { left: 20px; color: white; font-size: 14px; background-color: rgb(100, 100, 100); } QCalendarWidget QSpinBox { font-size: 14px; color: white; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); selection-background-color: rgb(136, 136, 136); selection-color: rgb(255, 255, 255); } QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:65px; } QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;} QCalendarWidget QSpinBox::up-arrow { width:56px;  height:56px; } QCalendarWidget QSpinBox::down-arrow { width:56px;  height:56px; } /* header row */ QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); } /* normal days */ QCalendarWidget QAbstractItemView:enabled { font-size: 14px; color: rgb(180, 180, 180); background-color: black; selection-background-color: rgb(64, 64, 64); selection-color: rgb(0, 255, 0); } /* days in other months */ /* navigation bar */ QCalendarWidget QWidget#qt_calendar_navigationbar { background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QAbstractItemView:disabled { color: rgb(64, 64, 64); }")

                self.table.setCellWidget(row_count, 4, self.dateedit)

                # 5 = PRIORIDADE 

                mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                ano = self.label_72.text()
                format = "%s-%s"%(ano,mes)

                priori = card_db_test.Return_Values_Calcs._fatural_atual(ids[i][0],format)
                print("ANO_MES_VALOR",format)
                print("PRIORIDADE",priori)


                backgroud = '#00ff00'
                print(priori,"ERROR 'PRIORIDADE'")
                format_value = priori.replace('.', '')
                if int(format_value) >= 0 and int(format_value) < 200:
                    text_priori = 'Baixo'
                    backgroud = '#ff0000'
                elif int(format_value) > 200 and int(format_value) < 400:
                    text_priori = 'Medio'
                    backgroud = '#ffa500'
                else:
                    text_priori = 'Alto'
                    backgroud = '#00ff00' 

                self.table.setItem(row_count, 5, QTableWidgetItem(str(text_priori)))
                self.table.item(row_count,5).setTextAlignment(Qt.AlignCenter)


                self.frame = QFrame()
                self.frame.setObjectName(u"frame")
                self.frame.setMaximumSize(QSize(7, 16777215))
                self.frame.setStyleSheet(u"background-color:"+backgroud+"; border-radius:3px; margin:7px;")
                self.table.setCellWidget(row_count, 5, self.frame)


                # 6 = CATEGORIA
                cate = 'Fatura'

                list_icon = ["delivery","appstrans","comida","mercado","lazer","icons8-casa-96","inuteis","servicos","streaming","urgencia","gatos","dogs","medico","viagem","eletronico","domesticos"]
                icone = QFrame()
                icone.setMaximumSize(QSize(35, 35))
                icone.setStyleSheet(u"background-color:rgba(255,255,255,0);border-image: url(:/icons-cards/src-page-cartoes/"+list_icon[randint(0,10)]+".png);\n"
                    "\n"
                    "\n"
                    "background-position: center;\n"
                    "\n"
                    "background-repeat:no-repeat;")
                self.table.setItem(row_count, 6, QTableWidgetItem(str(cate)))
                self.table.item(row_count,6).setTextAlignment(Qt.AlignCenter)
                self.table.setCellWidget(row_count, 6, icone)



                # 7 = METODO DE PAGAMENTO
                metodo = 'Fatura'
                #todo mudar aqui dps
                print(metodo,"error")
                if entra_saida == 'Entrada':
                    color_label = '#00ff00'
                else:
                    color_label = '#ff0000'


                self.label = QLabel()
                self.label.setStyleSheet(u"background-color:rgb(101, 53, 145);border-radius:3px; margin:7px;")
                self.label.setObjectName(u"label")
                font = QFont()
                font.setFamily(u"Bahnschrift Light Condensed")
                font.setPointSize(14)
                self.label.setFont(font)
                self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\";color:"+color_label+";\">"+metodo+"</span></p></body></html>", None))
                self.table.setCellWidget(row_count, 7, self.label)


                #/PAGAMENTO




                # 8 = VALOR
                valor = card_db_test.Return_Values_Calcs._fatural_atual(ids[i][0],format)
                print(valor,"VALOR'")
                self.table.setItem(row_count, 8, QTableWidgetItem(str("R$%s"%valor)))
                self.table.item(row_count,8).setTextAlignment(Qt.AlignCenter)



                # 9 = STATUS
                
                mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                ano = self.label_72.text()
                
                status = card_db_test.Return_Values_Calcs._status_fatura(ids[i][0],mes,ano)
                print(status,"STATUS")
                self.pushButton_pago = QPushButton()
                self.pushButton_pago.setObjectName(u"pagobuto")
                self.pushButton_pago.setGeometry(QRect(140, 180, 61, 31))


                if status == 'pago':

                    self.pushButton_pago.setStyleSheet("QPushButton{margin:10px;border-radius:3px;background-color: rgb(86, 202, 164);border: 1px solid  rgb(55, 55, 55);}QPushButton:hover{background-color: rgb(65, 160, 88);border: 2px solid  rgb(255, 255, 255);}QPushButton:pressed{background-color: rgb(65, 160, 88);border: 2px solid  rgb(55, 55, 55);}")
                    self.pushButton_pago.setText("Pago")
                    
                else:
                    self.pushButton_pago.setStyleSheet("QPushButton{margin:10px;border-radius:3px;background-color: rgb(214, 154, 90);border: 1px solid  rgb(55, 55, 55);}QPushButton:hover{background-color: rgb(163, 117, 68);border: 2px solid  rgb(255, 255, 255);}QPushButton:pressed{background-color: rgb(163, 117, 68) ;border: 2px solid  rgb(55, 55, 55);}")
                    self.pushButton_pago.setText("Pendente")


                self.pushButton_pago.setFont(self.font)
                self.table.setCellWidget(row_count, 9, self.pushButton_pago)

                # 10 = SALDO
                return_saldo = home_db_query.Return_values.return_saldo()
                self.table.setItem(row_count, 10, QTableWidgetItem(str("R$%s"%return_saldo)))
                self.table.item(row_count,10).setTextAlignment(Qt.AlignCenter)

        mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
        ano = self.label_72.text()

        
        dados = home_db_query.Return_Values_Conditions.return_lancamentos_month(ano,mes) #LINHAS DA TABELA

        if not dados:
            pass
        else:
            for i in range(len(dados)):
                row_count = self.table.rowCount()
                add_row = self.table.insertRow(row_count)


                # 0 = CHECKBOX:

                self.widget_item = QWidget()
                self.layout = QHBoxLayout()
                self.chebox = QCheckBox()
                self.chebox.setObjectName(u"chebox")
                self.chebox.setText(u"")
                self.chebox.setGeometry(QRect(0, 0, 40, 40))
                self.chebox.setChecked(False)
                self.chebox.setStyleSheet(u"background-color: rgba(255, 255, 255,0); margin-left:10px; \n")
                self.layout.setAlignment(Qt.AlignCenter)
                self.layout.addWidget(self.chebox)
                self.widget_item.setLayout(self.layout)
                self.table.setCellWidget(row_count, 0, self.chebox)


                # 1 = ID_LANCAMENTO
                id_lancamento = dados[i][0]
                self.table.setItem(row_count, 1, QTableWidgetItem(str(id_lancamento)))

                # 2 = ID_CONTA / ID_CARTAO / ID BANK

                id_conta = dados[i][1]
                self.table.setItem(row_count, 2, QTableWidgetItem(str(id_conta)))

                # 3 = TIPO: ENTRADA / SAIDA
                entra_saida = dados[i][2]
                self.table.setItem(row_count, 3, QTableWidgetItem(str(entra_saida)))



                # 4 = DATA DO LANÇAMENTO 
                self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
                self.dateedit.setDateTime(QtCore.QDateTime.currentDateTime()) # MUDAR DPOIS
                self.dateedit.calendarWidget().setGridVisible(True)
                self.dateedit.calendarWidget().setFirstDayOfWeek(Qt.Monday)
                self.dateedit.calendarWidget().setStyleSheet("QCalendarWidget QToolButton { color: white; font-size: 12px; icon-size: 20px, 20px; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QMenu { left: 20px; color: white; font-size: 14px; background-color: rgb(100, 100, 100); } QCalendarWidget QSpinBox { font-size: 14px; color: white; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); selection-background-color: rgb(136, 136, 136); selection-color: rgb(255, 255, 255); } QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:65px; } QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;} QCalendarWidget QSpinBox::up-arrow { width:56px;  height:56px; } QCalendarWidget QSpinBox::down-arrow { width:56px;  height:56px; } /* header row */ QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); } /* normal days */ QCalendarWidget QAbstractItemView:enabled { font-size: 14px; color: rgb(180, 180, 180); background-color: black; selection-background-color: rgb(64, 64, 64); selection-color: rgb(0, 255, 0); } /* days in other months */ /* navigation bar */ QCalendarWidget QWidget#qt_calendar_navigationbar { background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QAbstractItemView:disabled { color: rgb(64, 64, 64); }")

                self.table.setCellWidget(row_count, 4, self.dateedit)

                # 5 = PRIORIDADE 

                priori = dados[i][4]
                self.table.setItem(row_count, 5, QTableWidgetItem(str(priori)))
                backgroud = '#00ff00'
                if priori == 'baixo':
                    backgroud = '#ff0000'
                elif priori == 'medio':
                    backgroud = '#ffa500'
                elif priori == 'alto':
                    backgroud = '#00ff00'

                self.table.setItem(row_count, 5, QTableWidgetItem(str(priori)))
                self.table.item(row_count,5).setTextAlignment(Qt.AlignCenter)


                self.frame = QFrame()
                self.frame.setObjectName(u"frame")
                self.frame.setMaximumSize(QSize(7, 16777215))
                self.frame.setStyleSheet(u"background-color:"+backgroud+"; border-radius:3px; margin:7px;")
                self.table.setCellWidget(row_count, 5, self.frame)


                # 6 = CATEGORIA
                cate = dados[i][5]

                list_icon = ["delivery","appstrans","comida","mercado","lazer","icons8-casa-96","inuteis","servicos","streaming","urgencia","gatos","dogs","medico","viagem","eletronico","domesticos"]
                icone = QFrame()
                icone.setMaximumSize(QSize(35, 35))
                icone.setStyleSheet(u"background-color:rgba(255,255,255,0);border-image: url(:/icons-cards/src-page-cartoes/"+list_icon[randint(0,10)]+".png);\n"
                    "\n"
                    "\n"
                    "background-position: center;\n"
                    "\n"
                    "background-repeat:no-repeat;")
                self.table.setItem(row_count, 6, QTableWidgetItem(str(cate)))
                self.table.item(row_count,6).setTextAlignment(Qt.AlignCenter)
                self.table.setCellWidget(row_count, 6, icone)



                # 7 = METODO DE PAGAMENTO
                metodo = dados[i][6]
                #todo mudar aqui dps
                print(metodo,"error")
                if entra_saida == 'Entrada':
                    color_label = '#00ff00'
                else:
                    color_label = '#ff0000'


                self.label = QLabel()
                self.label.setStyleSheet(u"background-color:rgb(101, 53, 145);border-radius:3px; margin:7px;")
                self.label.setObjectName(u"label")
                font = QFont()
                font.setFamily(u"Bahnschrift Light Condensed")
                font.setPointSize(14)
                self.label.setFont(font)
                self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\";color:"+color_label+";\">"+metodo+"</span></p></body></html>", None))
                self.table.setCellWidget(row_count, 7, self.label)


                #/PAGAMENTO




                # 8 = VALOR
                valor = dados[i][7]

                self.table.setItem(row_count, 8, QTableWidgetItem(str("R$%s"%valor)))
                self.table.item(row_count,8).setTextAlignment(Qt.AlignCenter)




                # 9 = STATUS
                status = dados[i][8]

                self.pushButton_pago = QPushButton()
                self.pushButton_pago.setObjectName(u"pagobuto")
                self.pushButton_pago.setGeometry(QRect(140, 180, 61, 31))


                if status == 'pago':
    
                    self.pushButton_pago.setStyleSheet("QPushButton{margin:10px;border-radius:3px;background-color: rgb(86, 202, 164);border: 1px solid  rgb(55, 55, 55);}QPushButton:hover{background-color: rgb(65, 160, 88);border: 2px solid  rgb(255, 255, 255);}QPushButton:pressed{background-color: rgb(65, 160, 88);border: 2px solid  rgb(55, 55, 55);}")
                    self.pushButton_pago.setText("Pago")
                else:
                    self.pushButton_pago.setStyleSheet("QPushButton{margin:10px;border-radius:3px;background-color: rgb(214, 154, 90);border: 1px solid  rgb(55, 55, 55);}QPushButton:hover{background-color: rgb(163, 117, 68);border: 2px solid  rgb(255, 255, 255);}QPushButton:pressed{background-color: rgb(163, 117, 68) ;border: 2px solid  rgb(55, 55, 55);}")
                    self.pushButton_pago.setText("Pendente")


                self.pushButton_pago.setFont(self.font)
                self.table.setCellWidget(row_count, 9, self.pushButton_pago)

                # 10 = SALDO
                return_saldo = home_db_query.Return_values.return_saldo()
                self.table.setItem(row_count, 10, QTableWidgetItem(str("R$%s"%return_saldo)))
                self.table.item(row_count,10).setTextAlignment(Qt.AlignCenter)
            

        

        

class Dates_end_times(Ui_MainWindow):
    def current_date_extrato(self):
        current_date = date.today()
        y = current_date.year
        m = current_date.month
        d = current_date.day
        return [y,m,d]
        
    def convert_date_string(self,number):
        dict = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
        return dict[number]
    def convert_string_date(self,mes):
        dict = {'Janeiro':1, 'Fevereiro':2, 'Março':3, 'Abril':4, 'Maio':5, 'Junho':6, 'Julho':7, 'Agosto':8, 'Setembro':9, 'Outubro':10, 'Novembro':11, 'Dezembro':12}
        return dict[mes]
    def convert_string_date_query(self,mes):
        dict = {'Janeiro':'01', 'Fevereiro':'02', 'Março':'03', 'Abril':'04', 'Maio':'05', 'Junho':'06', 'Julho':'07', 'Agosto':'08', 'Setembro':'09', 'Outubro':'10', 'Novembro':'11', 'Dezembro':'12'}
        return dict[mes]
    def convert_dezena(self,mes):
        dict = {1:'01', 2:'02', 3:'03', 4:'04', 5:'05', 6:'06', 7:'07', 8:'08', 9:'09', 10:'10', 11:'11', 12:'12'}
        return dict[mes]
    def methodo_date_extrato(self,action):
        label_string_mes = Dates_end_times.convert_string_date(self,self.label_67.text())
        label_string_ano = int(self.label_72.text())
        format_date = datetime.strptime(f'{label_string_ano}-{label_string_mes}-01', '%Y-%m-%d')
        
        if action == 'Next':
            new_date = format_date + relativedelta(months=+1)
            self.label_67.setText(Dates_end_times.convert_date_string(self,new_date.month))
            self.label_72.setText(str(new_date.year))
        elif action == 'Previus':
            new_date = format_date + relativedelta(months=-1)
            self.label_67.setText(Dates_end_times.convert_date_string(self,new_date.month))
            self.label_72.setText(str(new_date.year))
        else:
            return False

    
    def set_text_extrato_startup(self):
        mes = Dates_end_times.current_date_extrato(self)[1]
        ano = Dates_end_times.current_date_extrato(self)[0]
        label_string_mes = self.label_67
        label_string_ano = self.label_72
        
        label_string_mes.setText(Dates_end_times.convert_date_string(self,mes))
        label_string_ano.setText(str(ano))


class Group:
    def execs(self):
        Set_values_startup.set_values_table_bank(self)
        Set_values_startup.set_banks_combobox_new_lan(self)
        Set_values_startup.load_table_fluxo_caixa(self)
        Combobox_startup.default_combox_hidem(self)
        Dates_end_times.set_text_extrato_startup(self)
        
        
class Set_values_startup(Ui_MainWindow):

    def set_values_table_bank(self):
        
        dados = home_db_query.Return_values.return_banks_active()
        cont = self.table_active_banks.rowCount()
        if cont > 0:
            for i in range (cont): 
                if self.table_active_banks.rowCount() >= 0:
                    self.table_active_banks.removeRow(self.table.rowCount()-1)
        for i in range(len(dados)):
            rowPosition = self.table_active_banks.rowCount()
            self.table_active_banks.insertRow(rowPosition)  
              
            for j in range(len(dados[i])):
                self.table_active_banks.setItem(i, j, QTableWidgetItem(str(dados[i][j])))
                print(dados[i][j])
        return 0
    
    def set_banks_combobox_new_lan(self):
        
        dados = home_db_query.Return_values.banks_active_id()
        
        
        for i in range(len(dados)):
            print("COMBOBOX",dados[i][0])
            # formats = "ID - %s Bank - %s"%(dados[i][0],dados[i][1])
            formats = "%s"%str(dados[i][0])
            print("COMBOBOX",formats)
            self.comboBox_11.addItem(formats)
            


        
    def load_table_fluxo_caixa(self): #SEMPRE 2º DEPOIS DE load_faturas_table_fluxo CONTAS 
        self.table = self.tableWidget

        cont = self.table.rowCount()
        if cont > 0:
            for i in range (cont): 
                if self.table.rowCount() >= 0:
                    self.table.removeRow(self.table.rowCount()-1)
        
        #LEGENDA:
        # 0 = CHECKBOX
        # 1 = ID_LANCAMENTO
        # 2 = ID_CONTA / ID_CARTAO / ID BANK
        # 3 = TIPO: ENTRADA / SAIDA
        # 4 = DATA DO LANÇAMENTO
        # 5 = PRIORIDADE 
        # 6 = CATEGORIA
        # 7 = METODO DE PAGAMENTO
        # 8 = VALOR
        # 9 = STATUS
        # 10 = SALDO
        
        ids = card_db_test.Main_page_values._cards_ids_all()
        print("COUNT IDSSS-----------",len(ids))

        # TODO LANCAMENTO DE FATURAS CARTOES
        if not ids:
            pass
        else:
            for i in range(len(ids)):
                print("IDSSS-----------",ids[i])
                row_count = self.table.rowCount()
                self.table.insertRow(row_count)
                print("ROW COUNT",row_count)

                # 0 = CHECKBOX:

                self.widget_item = QWidget()
                self.layout = QHBoxLayout()
                self.chebox = QCheckBox()
                self.chebox.setObjectName(u"chebox")
                self.chebox.setText(u"")
                self.chebox.setGeometry(QRect(0, 0, 40, 40))
                self.chebox.setChecked(False)
                self.chebox.setStyleSheet(u"background-color: rgba(255, 255, 255,0); margin-left:10px; \n")
                self.layout.setAlignment(Qt.AlignCenter)
                self.layout.addWidget(self.chebox)
                self.widget_item.setLayout(self.layout)
                self.table.setCellWidget(row_count, 0, self.chebox)


                # 1 = ID_LANCAMENTO
                id_lancamento = ids[i][0]
                self.table.setItem(row_count, 1, QTableWidgetItem(str(id_lancamento)))
                print("ID_LANCAMENTO",id_lancamento)
                # 2 = ID_CONTA / ID_CARTAO / ID BANK

                id_conta = ids[i][0]
                self.table.setItem(row_count, 2, QTableWidgetItem(str(id_conta)))
                print("ID_CONTA",id_conta)
                # 3 = TIPO: ENTRADA / SAIDA
                entra_saida = 'SAIDA'
                self.table.setItem(row_count, 3, QTableWidgetItem(str(entra_saida)))
                print("ENTRA_SAIDA",entra_saida)


                # 4 = DATA DO LANÇAMENTO 
                # VENCIMENTO DA FATURA
                Dates_end_times.current_date_extrato(self)
                date_ven = card_db_test.Ui_db._vencimento(ids[i][0])
                mes = Dates_end_times.convert_dezena(self,Dates_end_times.current_date_extrato(self)[1])
                ano = Dates_end_times.current_date_extrato(self)[0]
                
                #TODO LOGICA %S CONSULTA DB DIA VENCIMENTO , MES E ANO ATUAL
                #M D Y
                vencimento = "%s-%s-%s"%(date_ven,mes,ano)
                print("VENCIMENTO",vencimento)
                self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
                self.dateedit.setDate(QtCore.QDate.fromString(vencimento, "dd-MM-yyyy")) #NAO SEI SE TA CERTO
                self.dateedit.calendarWidget().setGridVisible(True)
                self.dateedit.calendarWidget().setFirstDayOfWeek(Qt.Monday)
                self.dateedit.calendarWidget().setStyleSheet("QCalendarWidget QToolButton { color: white; font-size: 12px; icon-size: 20px, 20px; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QMenu { left: 20px; color: white; font-size: 14px; background-color: rgb(100, 100, 100); } QCalendarWidget QSpinBox { font-size: 14px; color: white; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); selection-background-color: rgb(136, 136, 136); selection-color: rgb(255, 255, 255); } QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:65px; } QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;} QCalendarWidget QSpinBox::up-arrow { width:56px;  height:56px; } QCalendarWidget QSpinBox::down-arrow { width:56px;  height:56px; } /* header row */ QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); } /* normal days */ QCalendarWidget QAbstractItemView:enabled { font-size: 14px; color: rgb(180, 180, 180); background-color: black; selection-background-color: rgb(64, 64, 64); selection-color: rgb(0, 255, 0); } /* days in other months */ /* navigation bar */ QCalendarWidget QWidget#qt_calendar_navigationbar { background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QAbstractItemView:disabled { color: rgb(64, 64, 64); }")

                self.table.setCellWidget(row_count, 4, self.dateedit)

                # 5 = PRIORIDADE 
                mes = Dates_end_times.convert_dezena(self,Dates_end_times.current_date_extrato(self)[1])
                ano_mes = '%s-%s'%(Dates_end_times.current_date_extrato(self)[0],mes)
                priori = card_db_test.Return_Values_Calcs._fatural_atual(ids[i][0],ano_mes)
                print("ANO_MES_VALOR",ano_mes)
                print("PRIORIDADE",priori)


                backgroud = '#00ff00'
                print(priori,"ERROR 'PRIORIDADE'")
                format_value = priori.replace('.', '')
                if int(format_value) >= 0 and int(format_value) < 200:
                    text_priori = 'Baixo'
                    backgroud = '#ff0000'
                elif int(format_value) > 200 and int(format_value) < 400:
                    text_priori = 'Medio'
                    backgroud = '#ffa500'
                else:
                    text_priori = 'Alto'
                    backgroud = '#00ff00' 

                self.table.setItem(row_count, 5, QTableWidgetItem(str(text_priori)))
                self.table.item(row_count,5).setTextAlignment(Qt.AlignCenter)


                self.frame = QFrame()
                self.frame.setObjectName(u"frame")
                self.frame.setMaximumSize(QSize(7, 16777215))
                self.frame.setStyleSheet(u"background-color:"+backgroud+"; border-radius:3px; margin:7px;")
                self.table.setCellWidget(row_count, 5, self.frame)


                # 6 = CATEGORIA
                cate = 'Fatura'

                list_icon = ["delivery","appstrans","comida","mercado","lazer","icons8-casa-96","inuteis","servicos","streaming","urgencia","gatos","dogs","medico","viagem","eletronico","domesticos"]
                icone = QFrame()
                icone.setMaximumSize(QSize(35, 35))
                icone.setStyleSheet(u"background-color:rgba(255,255,255,0);border-image: url(:/icons-cards/src-page-cartoes/"+list_icon[randint(0,10)]+".png);\n"
                    "\n"
                    "\n"
                    "background-position: center;\n"
                    "\n"
                    "background-repeat:no-repeat;")
                self.table.setItem(row_count, 6, QTableWidgetItem(str(cate)))
                self.table.item(row_count,6).setTextAlignment(Qt.AlignCenter)
                self.table.setCellWidget(row_count, 6, icone)



                # 7 = METODO DE PAGAMENTO
                metodo = 'Fatura'
                #todo mudar aqui dps
                print(metodo,"error")
                if entra_saida == 'Entrada':
                    color_label = '#00ff00'
                else:
                    color_label = '#ff0000'


                self.label = QLabel()
                self.label.setStyleSheet(u"background-color:rgb(101, 53, 145);border-radius:3px; margin:7px;")
                self.label.setObjectName(u"label")
                font = QFont()
                font.setFamily(u"Bahnschrift Light Condensed")
                font.setPointSize(14)
                self.label.setFont(font)
                self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\";color:"+color_label+";\">"+metodo+"</span></p></body></html>", None))
                self.table.setCellWidget(row_count, 7, self.label)


                #/PAGAMENTO




                # 8 = VALOR
                valor = card_db_test.Return_Values_Calcs._fatural_atual(ids[i][0],ano_mes)
                print(valor,"VALOR'")
                self.table.setItem(row_count, 8, QTableWidgetItem(str("R$%s"%valor)))
                self.table.item(row_count,8).setTextAlignment(Qt.AlignCenter)


                mes= Dates_end_times.convert_dezena(self,Dates_end_times.current_date_extrato(self)[1])
                ano = Dates_end_times.current_date_extrato(self)[0]
                # 9 = STATUS
                status = card_db_test.Return_Values_Calcs._status_fatura(ids[i][0],mes,ano)
                print(status,"STATUS")
                self.pushButton_pago = QPushButton()
                self.pushButton_pago.setObjectName(u"pagobuto")
                self.pushButton_pago.setGeometry(QRect(140, 180, 61, 31))


                if status == 'pago':

                    self.pushButton_pago.setStyleSheet("QPushButton{margin:10px;border-radius:3px;background-color: rgb(86, 202, 164);border: 1px solid  rgb(55, 55, 55);}QPushButton:hover{background-color: rgb(65, 160, 88);border: 2px solid  rgb(255, 255, 255);}QPushButton:pressed{background-color: rgb(65, 160, 88);border: 2px solid  rgb(55, 55, 55);}")
                    self.pushButton_pago.setText("Pago")
                else:
                    self.pushButton_pago.setStyleSheet("QPushButton{margin:10px;border-radius:3px;background-color: rgb(214, 154, 90);border: 1px solid  rgb(55, 55, 55);}QPushButton:hover{background-color: rgb(163, 117, 68);border: 2px solid  rgb(255, 255, 255);}QPushButton:pressed{background-color: rgb(163, 117, 68) ;border: 2px solid  rgb(55, 55, 55);}")
                    self.pushButton_pago.setText("Pendente")


                self.pushButton_pago.setFont(self.font)
                self.table.setCellWidget(row_count, 9, self.pushButton_pago)

                # 10 = SALDO
                return_saldo = home_db_query.Return_values.return_saldo()
                self.table.setItem(row_count, 10, QTableWidgetItem(str("R$%s"%return_saldo)))
                self.table.item(row_count,10).setTextAlignment(Qt.AlignCenter)

        dados = home_db_query.Return_values.return_table_lancamento() #LINHAS DA TABELA

        # TODO LANÇAMENTOS DE CONTAS
        if not dados:
            return 0
        else:
            for i in range(len(dados)):
                row_count = self.table.rowCount()
                self.table.insertRow(row_count)
                print("ROW LANCAMENTOS",row_count)

                # 0 = CHECKBOX:

                self.widget_item = QWidget()
                self.layout = QHBoxLayout()
                self.chebox = QCheckBox()
                self.chebox.setObjectName(u"chebox")
                self.chebox.setText(u"")
                self.chebox.setGeometry(QRect(0, 0, 40, 40))
                self.chebox.setChecked(False)
                self.chebox.setStyleSheet(u"background-color: rgba(255, 255, 255,0); margin-left:10px; \n")
                self.layout.setAlignment(Qt.AlignCenter)
                self.layout.addWidget(self.chebox)
                self.widget_item.setLayout(self.layout)
                self.table.setCellWidget(row_count, 0, self.chebox)


                # 1 = ID_LANCAMENTO
                id_lancamento = dados[i][0]
                self.table.setItem(row_count, 1, QTableWidgetItem(str(id_lancamento)))

                # 2 = ID_CONTA / ID_CARTAO / ID BANK

                id_conta = dados[i][1]
                self.table.setItem(row_count, 2, QTableWidgetItem(str(id_conta)))

                # 3 = TIPO: ENTRADA / SAIDA
                entra_saida = dados[i][2]
                self.table.setItem(row_count, 3, QTableWidgetItem(str(entra_saida)))



                # 4 = DATA DO LANÇAMENTO 
                self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
                self.dateedit.setDateTime(QtCore.QDateTime.currentDateTime()) # MUDAR DPOIS
                self.dateedit.calendarWidget().setGridVisible(True)
                self.dateedit.calendarWidget().setFirstDayOfWeek(Qt.Monday)
                self.dateedit.calendarWidget().setStyleSheet("QCalendarWidget QToolButton { color: white; font-size: 12px; icon-size: 20px, 20px; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QMenu { left: 20px; color: white; font-size: 14px; background-color: rgb(100, 100, 100); } QCalendarWidget QSpinBox { font-size: 14px; color: white; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); selection-background-color: rgb(136, 136, 136); selection-color: rgb(255, 255, 255); } QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:65px; } QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;} QCalendarWidget QSpinBox::up-arrow { width:56px;  height:56px; } QCalendarWidget QSpinBox::down-arrow { width:56px;  height:56px; } /* header row */ QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); } /* normal days */ QCalendarWidget QAbstractItemView:enabled { font-size: 14px; color: rgb(180, 180, 180); background-color: black; selection-background-color: rgb(64, 64, 64); selection-color: rgb(0, 255, 0); } /* days in other months */ /* navigation bar */ QCalendarWidget QWidget#qt_calendar_navigationbar { background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QAbstractItemView:disabled { color: rgb(64, 64, 64); }")

                self.table.setCellWidget(row_count, 4, self.dateedit)

                # 5 = PRIORIDADE 

                priori = dados[i][4]
                self.table.setItem(row_count, 5, QTableWidgetItem(str(priori)))
                backgroud = '#00ff00'
                if priori == 'baixo':
                    backgroud = '#ff0000'
                elif priori == 'medio':
                    backgroud = '#ffa500'
                elif priori == 'alto':
                    backgroud = '#00ff00'

                self.table.setItem(row_count, 5, QTableWidgetItem(str(priori)))
                self.table.item(row_count,5).setTextAlignment(Qt.AlignCenter)


                self.frame = QFrame()
                self.frame.setObjectName(u"frame")
                self.frame.setMaximumSize(QSize(7, 16777215))
                self.frame.setStyleSheet(u"background-color:"+backgroud+"; border-radius:3px; margin:7px;")
                self.table.setCellWidget(row_count, 5, self.frame)


                # 6 = CATEGORIA
                cate = dados[i][5]

                list_icon = ["delivery","appstrans","comida","mercado","lazer","icons8-casa-96","inuteis","servicos","streaming","urgencia","gatos","dogs","medico","viagem","eletronico","domesticos"]
                icone = QFrame()
                icone.setMaximumSize(QSize(35, 35))
                icone.setStyleSheet(u"background-color:rgba(255,255,255,0);border-image: url(:/icons-cards/src-page-cartoes/"+list_icon[randint(0,10)]+".png);\n"
                    "\n"
                    "\n"
                    "background-position: center;\n"
                    "\n"
                    "background-repeat:no-repeat;")
                self.table.setItem(row_count, 6, QTableWidgetItem(str(cate)))
                self.table.item(row_count,6).setTextAlignment(Qt.AlignCenter)
                self.table.setCellWidget(row_count, 6, icone)



                # 7 = METODO DE PAGAMENTO
                metodo = dados[i][6]
                #todo mudar aqui dps
                print(metodo,"error")
                if entra_saida == 'Entrada':
                    color_label = '#00ff00'
                else:
                    color_label = '#ff0000'


                self.label = QLabel()
                self.label.setStyleSheet(u"background-color:rgb(101, 53, 145);border-radius:3px; margin:7px;")
                self.label.setObjectName(u"label")
                font = QFont()
                font.setFamily(u"Bahnschrift Light Condensed")
                font.setPointSize(14)
                self.label.setFont(font)
                self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\";color:"+color_label+";\">"+metodo+"</span></p></body></html>", None))
                self.table.setCellWidget(row_count, 7, self.label)


                #/PAGAMENTO




                # 8 = VALOR
                valor = dados[i][7]

                self.table.setItem(row_count, 8, QTableWidgetItem(str("R$%s"%valor)))
                self.table.item(row_count,8).setTextAlignment(Qt.AlignCenter)




                # 9 = STATUS
                status = dados[i][8]

                self.pushButton_pago = QPushButton()
                self.pushButton_pago.setObjectName(u"pagobuto")
                self.pushButton_pago.setGeometry(QRect(140, 180, 61, 31))


                if status == 'pago':
    
                    self.pushButton_pago.setStyleSheet("QPushButton{margin:10px;border-radius:3px;background-color: rgb(86, 202, 164);border: 1px solid  rgb(55, 55, 55);}QPushButton:hover{background-color: rgb(65, 160, 88);border: 2px solid  rgb(255, 255, 255);}QPushButton:pressed{background-color: rgb(65, 160, 88);border: 2px solid  rgb(55, 55, 55);}")
                    self.pushButton_pago.setText("Pago")
                else:
                    self.pushButton_pago.setStyleSheet("QPushButton{margin:10px;border-radius:3px;background-color: rgb(214, 154, 90);border: 1px solid  rgb(55, 55, 55);}QPushButton:hover{background-color: rgb(163, 117, 68);border: 2px solid  rgb(255, 255, 255);}QPushButton:pressed{background-color: rgb(163, 117, 68) ;border: 2px solid  rgb(55, 55, 55);}")
                    self.pushButton_pago.setText("Pendente")


                self.pushButton_pago.setFont(self.font)
                self.table.setCellWidget(row_count, 9, self.pushButton_pago)

                # 10 = SALDO
                return_saldo = home_db_query.Return_values.return_saldo()
                self.table.setItem(row_count, 10, QTableWidgetItem(str("R$%s"%return_saldo)))
                self.table.item(row_count,10).setTextAlignment(Qt.AlignCenter)
        
        

        
        
        
        
        
        
        
        
        
        
        
class Combobox_startup(Ui_MainWindow):

    def default_combox_hidem(self):
        self.frame_programar_data.hide()
        self.frame_recorrente_config.hide()
        self.frame_recorrente_config_date.hide()
    

    def show_programar_date(self):
        #JA PAGO OU RECEBIDO
        if self.comboBox_22.currentText() == 'Não':
            self.frame_programar_data.show()
            self.frame_189.hide()
            
        elif self.comboBox_22.currentText() == '':
            self.frame_programar_data.hide()
            self.frame_189.show()
        else:
            self.frame_programar_data.hide()
            self.frame_189.show()
    
    def show_recorrencia_options(self):
        if self.comboBox_22.currentText() == 'Sim' and self.comboBox_23.currentText() == 'Sim':
            self.frame_programar_data.hide()
            self.frame_recorrente_config.show()
            self.frame_recorrente_config_date.show()
            Combobox_startup.show_set_dia_recorrencia(self)
            
        elif self.comboBox_23.currentText() == 'Sim' and self.comboBox_22.currentText() == 'Não':
            self.frame_programar_data.show()
            self.frame_recorrente_config.show()
            
            
        elif self.comboBox_23.currentText() == '':
            self.frame_recorrente_config.hide()
            self.frame_recorrente_config_date.hide()
        else:
            self.frame_recorrente_config.hide()
            self.frame_recorrente_config_date.hide()
            
    
    def show_set_dia_recorrencia(self):
        if self.comboBox_26.currentText() == 'Mes':
            self.frame_recorrente_config_date.show()
        elif self.comboBox_26.currentText() == '':
            self.frame_recorrente_config_date.hide()
        else:
            self.frame_recorrente_config_date.hide()