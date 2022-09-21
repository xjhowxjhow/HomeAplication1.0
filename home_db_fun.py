
import sqlite3
from turtle import color
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

class Group:
    def execs(self):
        Dates_end_times.set_text_extrato_startup(self)
        Set_values_startup._set_Saldo(self)
        Set_values_startup.set_values_table_bank(self)
        Set_values_startup.set_banks_combobox_new_lan(self)
        mainpage.load_extrato_filter(self)
        Combobox_startup.default_combox_hidem(self)
        

class mainpage(Ui_MainWindow):





    #NOVO LANCAMENTO
    def _new_lancamento(self):
        #OBRIGATORIOS

        # TABLE new_lancamento
        id_lancamento = randint(0,99999999)
        id_bank = self.comboBox_11.currentText() # ID DA CONTA BANCO PARA DEBITO
        tipo = self.comboBox_25.currentText() #Entrada ou Saida
        
        
        if self.comboBox_22.currentText() == 'Sim':
            data_lancamento = self.lancamento_programado_2.text() # NAO PROGRAMADO JA FOI RECEBIDO
            status_pago = 'pago'
        else:
            data_lancamento = self.lancamento_programado.text() # PROGRAMADO NAO FOI RECEBIDO
        

        format_data_lancamento = datetime.strptime(data_lancamento, '%d/%m/%Y').strftime('%Y-%m-%d')
        data_lancamento = format_data_lancamento
        
        categoria = self.comboBox_21.currentText()
        pagamento = self.comboBox_27.currentText()
        valor = self.lineEdit_13.text()
        brl_usd = Convert_Moedas._brl_to_usd(self,valor)
        descricao = self.lineEdit_11.text()
        
        dados = [id_bank, data_lancamento, categoria, pagamento, brl_usd,tipo, descricao]
        
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
            
        format_data_lancamento = datetime.strptime(vencimento, '%d/%m/%Y').strftime('%Y-%m-%d')
        print("format_data_lancamento: AND STATUS ",format_data_lancamento,status_pago)
            
        dados_status = [id_bank,format_data_lancamento,status_pago]
        #EXECUTE QUERY
     
            
        home_db_query.Add_values._status_lancamento(id_lancamento_status,dados_status)
            
            #TODO

        
        
        #TABLE_PRIORIDADE VALOR:
        id_lancamentoprioridade = id_lancamento
        id_bank = self.comboBox_11.currentText() # ID DA CONTA BANCO PARA DEBITO
        prioridade = ''
        brl_usd = Convert_Moedas._brl_to_usd(self,valor)
        
        if float(brl_usd) >1000.00:
            prioridade = 'alto'
        elif float(brl_usd) >500.00:
            prioridade = 'medio'
        else:
            prioridade = 'baixo'
        
        dados_prioridade = [id_bank, prioridade]
        #EXECUTE QUERY
        home_db_query.Add_values._prioridade_value(id_lancamentoprioridade, dados_prioridade)


        #UPDATE SALDO SE FOR JA PAGO/RECEBIDO
        if status_pago == 'pago':
            format_date = datetime.strptime(data_lancamento, '%Y-%m-%d').strftime('%d/%m/%Y')
            get_ano = datetime.strptime(format_date, '%d/%m/%Y').strftime('%Y')
            get_mes = datetime.strptime(format_date, '%d/%m/%Y').strftime('%m')
            if tipo == 'Entrada':
                home_db_query.Saldos._pagar_lancamento(id_lancamento,id_bank,'Entrada',get_ano,get_mes)
                print("tipoooo",tipo)
            else:
                home_db_query.Saldos._pagar_lancamento(id_lancamento,id_bank,'Saida',get_ano,get_mes)
                print("tipoooo",tipo)
                
        mainpage.load_extrato_filter(self)
        self.chart_gastos_all_2.setCurrentWidget(self.page_Tabe_main1)
        Set_values_startup._set_Saldo(self)


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
        # 3 = ICON_BANK
        # 4 = TIPO: ENTRADA / SAIDA
        # 5 = DATA DO LANÇAMENTO
        # 6 = PRIORIDADE 
        # 7 = CATEGORIA
        # 8 = METODO DE PAGAMENTO
        # 9 = VALOR
        # 10 = STATUS
        # 11 = SALDO
        ids = card_db_test.Main_page_values._cards_ids_all()
        print("COUNT IDSSS-----------",len(ids))
        
        mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
        ano = self.label_72.text()
        fomrmat = f"{ano}-{mes}"
        
        # LANCAMENTO DE FATURAS CARTOES:
        if not ids:
            pass
        else:
            for i in range(len(ids)):
                validador = home_db_query.Return_values_configs._return_default_h_s_z()
                if validador == 'True':
                    pass
                else:
                    print("VALIDADOR",validador)
            # for i in range(len(ids)):
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
                    self.table.setItem(row_count, 4, QTableWidgetItem(str(entra_saida)))
                    print("ENTRA_SAIDA",entra_saida)

                    #icone BANK
                    icon = QIcon()
                    name_bank = card_db_test.Ui_db._cartao(str(id_conta))
                    style_icon_URL = effects.Effetc_slides._icon_main_pacth(self,name_bank)


                    icon.addFile(style_icon_URL, QSize(), QIcon.Normal, QIcon.Off)
                    self.table.setItem(row_count, 3, QTableWidgetItem(icon, ""))

                    # 4 = DATA DO LANÇAMENTO 
                    # VENCIMENTO DA FATURA

                    date_ven = card_db_test.Ui_db._vencimento(ids[i][0])
                    mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                    ano = self.label_72.text()
                    print("anoooo",ano)
                    #TODO LOGICA %S CONSULTA DB DIA VENCIMENTO , MES E ANO ATUAL
                    #M D Y
                    vencimento = "%s-%s-%s"%(date_ven,mes,ano)
                    print("VENCIMENTO",vencimento)
                    self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
                    self.dateedit.setDate(QtCore.QDate.fromString(vencimento, "dd-MM-yyyy")) #NAO SEI SE TA CERTO
                    self.dateedit.calendarWidget().setGridVisible(True)
                    self.dateedit.calendarWidget().setFirstDayOfWeek(Qt.Monday)
                    self.dateedit.calendarWidget().setStyleSheet("QCalendarWidget QToolButton { color: white; font-size: 12px; icon-size: 20px, 20px; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QMenu { left: 20px; color: white; font-size: 14px; background-color: rgb(100, 100, 100); } QCalendarWidget QSpinBox { font-size: 14px; color: white; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); selection-background-color: rgb(136, 136, 136); selection-color: rgb(255, 255, 255); } QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:65px; } QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;} QCalendarWidget QSpinBox::up-arrow { width:56px;  height:56px; } QCalendarWidget QSpinBox::down-arrow { width:56px;  height:56px; } /* header row */ QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); } /* normal days */ QCalendarWidget QAbstractItemView:enabled { font-size: 14px; color: rgb(180, 180, 180); background-color: black; selection-background-color: rgb(64, 64, 64); selection-color: rgb(0, 255, 0); } /* days in other months */ /* navigation bar */ QCalendarWidget QWidget#qt_calendar_navigationbar { background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QAbstractItemView:disabled { color: rgb(64, 64, 64); }")

                    self.table.setCellWidget(row_count, 5, self.dateedit)

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

                    self.table.setItem(row_count, 6, QTableWidgetItem(str(text_priori)))
                    self.table.item(row_count,6).setTextAlignment(Qt.AlignCenter)


                    self.frame = QFrame()
                    self.frame.setObjectName(u"frame")
                    self.frame.setMaximumSize(QSize(7, 16777215))
                    self.frame.setStyleSheet(u"background-color:"+backgroud+"; border-radius:3px; margin:7px;")
                    self.table.setCellWidget(row_count, 6, self.frame)


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
                    self.table.setItem(row_count, 7, QTableWidgetItem(str(cate)))
                    self.table.item(row_count,7).setTextAlignment(Qt.AlignCenter)
                    self.table.setCellWidget(row_count, 7, icone)



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
                    self.table.setCellWidget(row_count, 8, self.label)


                    #/PAGAMENTO


                    mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                    ano = self.label_72.text()
                    valor = card_db_test.Return_Values_Calcs._valor_fatura(ids[i][0],mes,ano)
                    print("VALOR CARDAO DE TCRI",valor)
                    usd_to_brl = Convert_Moedas._usd_to_brl(self,valor)
                    valor = usd_to_brl
                    # 8 = VALOR
                    if entra_saida == 'Entrada':
                        format_valor = "+ %s"%(valor)
                        color_label = '#00ff00'
                    else:  
                        format_valor = "- %s"%(valor)
                        color_label = '#ff0000'
                    
                    print(valor,"VALOR'")
                    self.table.setItem(row_count, 9, QTableWidgetItem(str(format_valor)))
                    self.table.item(row_count,9).setTextAlignment(Qt.AlignCenter)
                    self.table.item(row_count,9).setTextColor(QColor(color_label))



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
                    self.table.setCellWidget(row_count, 10, self.pushButton_pago)

                    # 10 = SALDO
                    
                    return_saldo = home_db_query.Return_values.return_saldo()
                    self.table.setItem(row_count, 11, QTableWidgetItem(str("R$%s"%return_saldo)))
                    self.table.item(row_count,11).setTextAlignment(Qt.AlignCenter)

        # LACAMENTO RECORRENTES:

        mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
        ano = self.label_72.text()
        dados = home_db_query.Return_Values_Conditions.return_lancamentos_recorretes() #LINHAS DA TABELA
        #nao retonra data de lancamento vai ser o do mes atual

        current_mes = Dates_end_times.convert_string_date(self,self.label_67.text())
        current_mes_local = datetime.now().month
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
                self.table.setItem(row_count, 4, QTableWidgetItem(str(entra_saida)))

                #4 ICONE
                icon = QIcon()
                name_bank = home_db_query.Return_Values_Conditions._return_name_bank(str(id_conta))
                style_icon_URL = effects.Effetc_slides._icon_main_pacth(self,name_bank)


                icon.addFile(style_icon_URL, QSize(), QIcon.Normal, QIcon.Off)
                self.table.setItem(row_count, 3, QTableWidgetItem(icon, ""))
                
                
                
                # 4 = DATA DO LANÇAMENTO 
                date_ven = home_db_query.Return_Values_Conditions._retur_data_recorrente_mes(str(dados[i][0]))
                print(date_ven,"DATA VENCIMENTO RECORRENTE")
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

                self.table.setCellWidget(row_count, 5, self.dateedit)

                # 5 = PRIORIDADE 

                priori = dados[i][3]
                self.table.setItem(row_count, 6, QTableWidgetItem(str(priori)))
                backgroud = '#00ff00'
                if priori == 'baixo':
                    backgroud = '#ff0000'
                elif priori == 'medio':
                    backgroud = '#ffa500'
                elif priori == 'alto':
                    backgroud = '#00ff00'

                self.table.setItem(row_count, 6, QTableWidgetItem(str(priori)))
                self.table.item(row_count,6).setTextAlignment(Qt.AlignCenter)


                self.frame = QFrame()
                self.frame.setObjectName(u"frame")
                self.frame.setMaximumSize(QSize(7, 16777215))
                self.frame.setStyleSheet(u"background-color:"+backgroud+"; border-radius:3px; margin:7px;")
                self.table.setCellWidget(row_count, 6, self.frame)


                # 6 = CATEGORIA
                cate = dados[i][4]

                list_icon = ["delivery","appstrans","comida","mercado","lazer","icons8-casa-96","inuteis","servicos","streaming","urgencia","gatos","dogs","medico","viagem","eletronico","domesticos"]
                icone = QFrame()
                icone.setMaximumSize(QSize(35, 35))
                icone.setStyleSheet(u"background-color:rgba(255,255,255,0);border-image: url(:/icons-cards/src-page-cartoes/"+list_icon[randint(0,10)]+".png);\n"
                    "\n"
                    "\n"
                    "background-position: center;\n"
                    "\n"
                    "background-repeat:no-repeat;")
                self.table.setItem(row_count, 7, QTableWidgetItem(str(cate)))
                self.table.item(row_count,7).setTextAlignment(Qt.AlignCenter)
                self.table.setCellWidget(row_count, 7, icone)



                # 7 = METODO DE PAGAMENTO
                metodo = dados[i][5]
                #todo mudar aqui dps
                print(metodo,"error")
                if entra_saida == 'Entrada':
                    color_label = '#00ff00'
                else:
                    color_label = '#ff0000'


                self.label = QLabel()
                self.label.setStyleSheet(u"background-color:rgba(101, 53, 145);border-radius:3px; margin:7px;")
                self.label.setObjectName(u"label")
                font = QFont()
                font.setFamily(u"Bahnschrift Light Condensed")
                font.setPointSize(14)
                self.label.setFont(font)
                self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\";color:"+color_label+";\">"+metodo+"</span></p></body></html>", None))
                self.table.setCellWidget(row_count, 8, self.label)


                #/PAGAMENTO




                # 8 = VALOR
                valor = dados[i][6]
                usd_to_brl = Convert_Moedas._usd_to_brl(self,valor)
                valor = usd_to_brl
                if entra_saida == 'Entrada':
                    format_valor = "+ %s"%(valor)
                    color_label = '#00ff00'
                else:  
                    format_valor = "- %s"%(valor)
                    color_label = '#ff0000'

                self.table.setItem(row_count, 9, QTableWidgetItem(str(format_valor)))
                self.table.item(row_count,9).setTextAlignment(Qt.AlignCenter)
                self.table.item(row_count,9).setTextColor(QColor(color_label))




                # 9 = STATUS
                
                mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                ano = self.label_72.text()
                vali_status = home_db_query.Return_Values_Conditions._verifi_pago_recorrente(str(dados[i][0]),mes,ano)
                
                if vali_status == True:
                    status = 'pago'
                else:
                    status = 'pendente'
                print("LODAINDG",status,id_lancamento)

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
                self.table.setCellWidget(row_count, 10, self.pushButton_pago)

                # 10 = SALDO
                return_saldo = home_db_query.Return_values.return_saldo()
                saldo_brl = Convert_Moedas._usd_to_brl(self,return_saldo)
                self.table.setItem(row_count, 11, QTableWidgetItem(str("%s"%saldo_brl)))
                self.table.item(row_count,11).setTextAlignment(Qt.AlignCenter)

        # LANÇAMENTOS DE CONTAS :
        
        # "FILTRO:>"
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
                self.table.setItem(row_count, 4, QTableWidgetItem(str(entra_saida)))

                # 4 = ICONE

                icon = QIcon()
                name_bank = home_db_query.Return_Values_Conditions._return_name_bank(str(id_conta))
                style_icon_URL = effects.Effetc_slides._icon_main_pacth(self,name_bank)


                icon.addFile(style_icon_URL, QSize(), QIcon.Normal, QIcon.Off)
                self.table.setItem(row_count, 3, QTableWidgetItem(icon, ""))
                # 4 = DATA DO LANÇAMENTO 
                data_lancamento = dados[i][3]
                convert_d_m_y  = '%s-%s-%s'%(data_lancamento[8:10],data_lancamento[5:7],data_lancamento[0:4])
                self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
                self.dateedit.setDate(QtCore.QDate.fromString(convert_d_m_y, "dd-MM-yyyy"))
                self.dateedit.calendarWidget().setGridVisible(True)
                self.dateedit.calendarWidget().setFirstDayOfWeek(Qt.Monday)
                self.dateedit.calendarWidget().setStyleSheet("QCalendarWidget QToolButton { color: white; font-size: 12px; icon-size: 20px, 20px; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QMenu { left: 20px; color: white; font-size: 14px; background-color: rgb(100, 100, 100); } QCalendarWidget QSpinBox { font-size: 14px; color: white; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); selection-background-color: rgb(136, 136, 136); selection-color: rgb(255, 255, 255); } QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:65px; } QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;} QCalendarWidget QSpinBox::up-arrow { width:56px;  height:56px; } QCalendarWidget QSpinBox::down-arrow { width:56px;  height:56px; } /* header row */ QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); } /* normal days */ QCalendarWidget QAbstractItemView:enabled { font-size: 14px; color: rgb(180, 180, 180); background-color: black; selection-background-color: rgb(64, 64, 64); selection-color: rgb(0, 255, 0); } /* days in other months */ /* navigation bar */ QCalendarWidget QWidget#qt_calendar_navigationbar { background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); } QCalendarWidget QAbstractItemView:disabled { color: rgb(64, 64, 64); }")

                self.table.setCellWidget(row_count, 5, self.dateedit)

                # 5 = PRIORIDADE 

                priori = dados[i][4]
                self.table.setItem(row_count, 6, QTableWidgetItem(str(priori)))
                backgroud = '#00ff00'
                if priori == 'baixo':
                    backgroud = '#ff0000'
                elif priori == 'medio':
                    backgroud = '#ffa500'
                elif priori == 'alto':
                    backgroud = '#00ff00'

                self.table.setItem(row_count, 6, QTableWidgetItem(str(priori)))
                self.table.item(row_count,6).setTextAlignment(Qt.AlignCenter)


                self.frame = QFrame()
                self.frame.setObjectName(u"frame")
                self.frame.setMaximumSize(QSize(7, 16777215))
                self.frame.setStyleSheet(u"background-color:"+backgroud+"; border-radius:3px; margin:7px;")
                self.table.setCellWidget(row_count, 6, self.frame)


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
                self.table.setItem(row_count, 7, QTableWidgetItem(str(cate)))
                self.table.item(row_count,7).setTextAlignment(Qt.AlignCenter)
                self.table.setCellWidget(row_count, 7, icone)



                # 7 = METODO DE PAGAMENTO
                metodo = dados[i][6]
                #todo mudar aqui dps
                print(metodo,"error")
                if entra_saida == 'Entrada':
                    color_label = '#00ff00'
                else:
                    color_label = '#ffffff'


                self.label = QLabel()
                self.label.setStyleSheet(u"background-color:rgb(75, 79, 167);border-radius:3px; margin:7px;")
                self.label.setObjectName(u"label")
                font = QFont()
                font.setFamily(u"Bahnschrift Light Condensed")
                font.setPointSize(14)
                self.label.setFont(font)
                self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\";color:"+color_label+";\">"+metodo+"</span></p></body></html>", None))
                self.table.setCellWidget(row_count, 8, self.label)


                #/PAGAMENTO




                # 8 = VALOR
                valor = dados[i][7]
                usd_to_brl = Convert_Moedas._usd_to_brl(self,valor)
                if entra_saida == 'Entrada':
                    format_valor = "+ R$ %s"%(valor)
                    color_label = '#00ff00'
                else:  
                    format_valor = "- R$ %s"%(valor)
                    color_label = '#ff0000'

                self.table.setItem(row_count, 9, QTableWidgetItem(str(format_valor)))
                self.table.item(row_count,9).setTextAlignment(Qt.AlignCenter)
                self.table.item(row_count,9).setTextColor(QColor(color_label))




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
                self.table.setCellWidget(row_count, 10, self.pushButton_pago)

                # 10 = SALDO
                return_saldo = home_db_query.Return_values.return_saldo()
                usd_to_brl = Convert_Moedas._usd_to_brl(self,return_saldo)
                self.table.setItem(row_count, 11, QTableWidgetItem(str("%s"%usd_to_brl)))
                self.table.item(row_count,11).setTextAlignment(Qt.AlignCenter)
            

        



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
        combo = self.comboBox_11
        if combo.count() > 0:
            pass
        else:
            for i in range(len(dados)):
                print("COMBOBOX",dados[i][0])
                # formats = "ID - %s Bank - %s"%(dados[i][0],dados[i][1])
                formats = "%s"%str(dados[i][0])
                print("COMBOBOX",formats)
                self.comboBox_11.addItem(formats)
            
    def load_table_fluxo_caixa(self): 
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
        mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
        ano = self.label_72.text()
        fomrmat = f"{ano}-{mes}"
        
        # LANCAMENTO DE FATURAS CARTOES:
        if not ids:
            pass
        else:
            for i in range(len(ids)):
                validadors = card_db_test.Return_Values_Calcs._fatural_atual(ids[i],fomrmat)
                print("VALIDADOR2",validadors,ids[i])
                if validadors == '0.00' or validadors == 0.00 or validadors == 0 or validadors == '0' or validadors == None:
                    pass
                else:
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
                    print("VENCIMENTO CARTAO DE CREDITO",vencimento)
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
                data = dados[i][3]
                covert_d_m_a = '%s-%s-%s'%(data[8:10],data[5:7],data[0:4])
                self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
                self.dateedit.setDate(QtCore.QDate.fromString(covert_d_m_a, "dd-MM-yyyy")) # MUDAR DPOIS
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
                if entra_saida == 'Entrada':
                    valor = "+ R$ "+str(valor)
                    color_label = '#00ff00'
                else:
                    valor = "- R$ "+str(valor)
                    color_label = '#ff0000'
                self.table.setItem(row_count, 8, QTableWidgetItem(str(valor)))
                self.table.item(row_count,8).setTextAlignment(Qt.AlignCenter)
                self.table.item(row_count,8).setTextColor(QColor(color_label))





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
        
    def _set_Saldo(self):
        valor = home_db_query.Saldos.Set_saldo_inicial()
        usd_to_brl = Convert_Moedas._usd_to_brl(self,valor)
        valor = usd_to_brl
        self.label_70.setText("%s"%valor)
        self.label_70.setWordWrap(True)
        self.label_70.setTextInteractionFlags(Qt.NoTextInteraction)

class Combobox_startup(Ui_MainWindow):

    def default_combox_hidem(self):
        self.frame_programar_data.hide()
        self.frame_recorrente_config.hide()
        self.frame_recorrente_config_date.hide()
        #DATEEDITS
        self.lancamento_programado_2.setDate(QDate.currentDate())
        self.lancamento_programado.setDate(QDate.currentDate())

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
            
            
            


class Descricao_lancamento(Ui_MainWindow):
    def set_descricao_lancamento(self,id):
        
        if home_db_query.Return_Values_Conditions._verify_id_is_credit_card(id) == True:
            self.textEdit.setText("Fatura")
            
            return "fatura"
        elif home_db_query.Return_Values_Conditions._verify_id_is_credit_card(id) == False:
            descricao = home_db_query.Return_Values_Conditions._return_descricao(id)
            if not descricao:
                self.textEdit.setText("Sem descriçao")
                return 'n/d'
            self.textEdit.setText(descricao)
        else:
            self.textEdit.setText("Sem descriçao")
            return "n/d"
        
    def set_icon_desc(self,id):
        card =  card_db_test.Ui_db._cartao(id)
        return_icon = effects.efeitos_geral.style_sheet_card_icon(self,card)
        
        self.frame_if_card_main.show()
        self.label_if_card.show()
        return self.icon_if_card.setStyleSheet(u"background-image:"+return_icon+";background-position: center;background-repeat:no-repeat;")

    def Change_text_btn_pagar_receber(self,id):
        val = home_db_query.Verify_status_payment.verify_type_lanca(id) 
        if val == True:
            self.paga_fatura_3.setText("Receber")
            
        elif val == False:
            self.paga_fatura_3.setText("Pagar")
        else:
            self.paga_fatura_3.setText("Pagar Fatura")
            
        print(val)


class Pagamento(Ui_MainWindow):

    def _pagar_lancamento(self):
        current_row = self.table.currentRow()
        id_lancamento = self.table.item(current_row,1).text()
        id_bank = self.table.item(current_row,2).text()
        #VERIFICAR SE JA ESTA PAGO
        pago = home_db_query.Verify_status_payment.return_status_p_pago(id_lancamento,id_bank)
        
        # VERIFICA SE LANCAMENTO É RECORRENTE 
        reco = home_db_query.Return_Values_Conditions._return_if_recorrente(id_lancamento)
        #VERIFICA SE LANCAMENTO RECORRENTE DE ACORDO COM O MES DA TABLE JA FOI PAGO
        ano = self.label_72.text()
        mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
        
        pago_recorrente = home_db_query.Return_Values_Conditions._verifi_pago_recorrente(id_lancamento,mes,ano)
        
        if reco == True:
            if pago_recorrente == False:
            #MENSAGEM BOX
                print("Lancamento recorrente")
                home_db_query.Add_values._add_new_lancamento_recorrente(id_lancamento,id_bank,mes,ano)
                home_db_query.Saldos._pagar_lancamento(id_lancamento,id_bank,'Saida',ano,mes)
                Set_values_startup._set_Saldo(self)
                mainpage.load_extrato_filter(self)
                #TEMQ FAZER A VALIDADAO POR DATA DO LKANCAMENTO
                
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText("Lançamento já pago")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        else:
            if pago == False:
                id_lancamento = self.table.item(current_row,1).text()
                id_bank = self.table.item(current_row,2).text()
                home_db_query.Saldos._pagar_lancamento(id_lancamento,id_bank,'Saida',ano,mes)
                Set_values_startup._set_Saldo(self)
                mainpage.load_extrato_filter(self)
                #MENSAGEM BOX
                msg = QMessageBox()
                msg.setWindowTitle("Sucesso")
                msg.setText("Lançamento pago com sucesso")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText("Lançamento já pago")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

            
        return True
    
    def _receber_lancamento(self):
        current_row = self.table.currentRow()
        id_lancamento = self.table.item(current_row,1).text()
        id_bank = self.table.item(current_row,2).text()
        #VERIFICAR SE JA ESTA PAGO
        pago = home_db_query.Verify_status_payment.return_status_p_pago(id_lancamento,id_bank)
        
        # VERIFICA SE LANCAMENTO É RECORRENTE 
        reco = home_db_query.Return_Values_Conditions._return_if_recorrente(id_lancamento)
        #VERIFICA SE LANCAMENTO RECORRENTE DE ACORDO COM O MES DA TABLE JA FOI PAGO
        ano = self.label_72.text()
        mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
        
        pago_recorrente = home_db_query.Return_Values_Conditions._verifi_pago_recorrente(id_lancamento,mes,ano)

        if reco == True:
            if pago_recorrente == False:
            #MENSAGEM BOX
                print("Lancamento recorrente, deseja receber todos os lançamentos?")
                home_db_query.Add_values._add_new_lancamento_recorrente(id_lancamento,id_bank,mes,ano)
                home_db_query.Saldos._pagar_lancamento(id_lancamento,id_bank,'Entrada',ano,mes)
                Set_values_startup._set_Saldo(self)
                mainpage.load_extrato_filter(self)
                #TEMQ FAZER A VALIDADAO POR DATA DO LKANCAMENTO
                
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText("Lançamento já Recebido")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        else:
            if pago == False:
                id_lancamento = self.table.item(current_row,1).text()
                id_bank = self.table.item(current_row,2).text()
                home_db_query.Saldos._pagar_lancamento(id_lancamento,id_bank,'Entrada',ano,mes)
                Set_values_startup._set_Saldo(self)
                mainpage.load_extrato_filter(self)
                #MENSAGEM BOX
                msg = QMessageBox()
                msg.setWindowTitle("Sucesso")
                msg.setText("Lançamento Recebido com sucesso")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
                
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText("Lançamento já recebido")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

            
        return True

    def _pagar_fatura(self):
        current_row = self.table.currentRow()
        id_bank = self.table.item(current_row,2).text()
        mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
        ano = self.label_72.text()
        verifi_if_pago = card_db_test.Return_Values_Calcs._status_fatura(id_bank,mes,ano)
        print("PASDA",verifi_if_pago)
        
        #VERIFICA SE FATURA É DO BANCO PRINCIPAL
        
        
        
        if verifi_if_pago == 'pendente':
            if  home_db_query.Return_values.return_saldo_banks(id_bank) != None:
                print("SALDO",home_db_query.Return_values.return_saldo_banks(id_bank))
                home_db_query.Saldos._pagar_fatura(id_bank,mes,ano)
                card_db_test.Return_Values_Calcs._pagar_fatura(id_bank,mes,ano)
                Set_values_startup._set_Saldo(self)
                mainpage.load_extrato_filter(self)
                msg = QMessageBox()
                msg.setWindowTitle("Sucesso")
                msg.setText("Fatura paga com sucesso")
                msg.setIcon(QMessageBox.Information)
                msg.exec_()
            else:
                validate = Alerts._alerta_fatura_banco_indiferente(self)
                if validate == True:
                    default_bank = home_db_query.Return_values._return_default_bank()
                    home_db_query.Saldos._pagar_fatura(str(default_bank),mes,ano)
                    card_db_test.Return_Values_Calcs._pagar_fatura(id_bank,mes,ano)
                    Set_values_startup._set_Saldo(self)
                    mainpage.load_extrato_filter(self)
                    msg = QMessageBox()
                    msg.setWindowTitle("Sucesso")
                    msg.setText("Fatura paga com sucesso debitado da conta principal!")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                else:
                    print("NÃO PAGAR FATURA")
        elif verifi_if_pago == 'pago':
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText("Fatura já paga")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
        elif verifi_if_pago == 'proximas':
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText("Fatura ainda não venceu Ou nao existe Valor")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
     
            
        #BANCO DIFERENTE N TA DESCONTADO GERANDO ERRO DPS CORRIGIR
        
        
class Convert_Moedas(Ui_MainWindow):
    def _usd_to_brl(self,valor):
        valor = float(valor) 
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        valor = locale.currency(valor, grouping=True, symbol=True)
        return ('%s' % valor)
    
    def _brl_to_usd(self,valor):
        new_string = valor
        to_remove = "."
        for x in to_remove:
            new_string = new_string.replace(x, '')
            new_string = new_string.replace(',','.')
        return new_string
    
    
    
class Alerts(Ui_MainWindow):

    def _alerta_fatura_banco_indiferente(self):
        qdialog = QDialog()
        qdialog.setWindowTitle("Alerta")
        qdialog.setWindowIcon(QIcon(':/icons/icons/Alerta.png'))
        qdialog.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)
        qdialog.setFixedSize(400, 200)
        qdialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        qdialog.setWindowModality(Qt.ApplicationModal)
        
        true_or_false = 0
        #OK BUTTON CANC BUTTON
        ok_button = QPushButton("Sim",qdialog)
        ok_button.setGeometry(300,150,80,30)
        ok_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        ok_button.clicked.connect(qdialog.accept)
        
        
        #CANCEL BUTTON
        cancel_button = QPushButton("Não",qdialog)
        cancel_button.setGeometry(200,150,80,30)
        cancel_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        cancel_button.clicked.connect(qdialog.reject) 
    

    

        #LABEL
        label = QLabel(qdialog)
        label.setGeometry(10,10,380,130)
        label.setStyleSheet("background-color: rgb(255, 255, 255);")
        label.setText("Está fatura é de um banco diferente do principal!\nNao existe conta bancaria vinculado a este Cartao de Credito \npara descontar o valor\ndeseja descontar no debito do banco Principal?")
        label.setAlignment(Qt.AlignCenter)
        qdialog.exec_()
        return qdialog.result()



        
class Configs(Ui_MainWindow):

    def hide_show_saldos_zeros(self,condicao): #apenas para faturas de cartoes de creditos
        if condicao == True:
            home_db_query.Return_values_configs._update_default_h_s_z(True)
            Qms = QMessageBox()
            Qms.setWindowTitle("Sucesso")
            Qms.setText("Saldos zerados ocultados com sucesso")
            Qms.setIcon(QMessageBox.Information)
            Qms.exec_()
            
            return mainpage.load_extrato_filter(self)
        elif condicao == False:
            home_db_query.Return_values_configs._update_default_h_s_z(False)
            Qms = QMessageBox()
            Qms.setWindowTitle("Sucesso")
            Qms.setText("Saldos zerados mostrados com sucesso")
            Qms.setIcon(QMessageBox.Information)
            Qms.exec_()
            return mainpage.load_extrato_filter(self)