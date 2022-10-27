
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

from modules.charts_main import Chart
import locale
import emoji
import home_db_query
import random
from frame_bank.card_frame_bank import CardFrameBank
from source_ui.categories import Category,Payments_Type,Texts_Erros
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
import shutil 

#GLOBAL FILE PATCH PDF
file_patch_pdf = ''



class Group:
    def execs(self):
        Dates_end_times.set_text_extrato_startup(self)
        Set_values_startup._set_Saldo(self)
        Set_values_startup._set_start_ag_b_t(self)
        Set_values_startup.set_values_table_bank(self)
        Set_values_startup.set_banks_combobox_new_lan(self)
        mainpage.load_extrato_filter(self)
        Combobox_startup.default_combox_hidem(self)
        


        return True

class mainpage(Ui_MainWindow):

    def _new_lancamento(self):
        #OBRIGATORIOS
        
        validador_empty = Alerts._val_new_lan_pass_or_not(self)
        print(validador_empty,"validador_empty")
        if validador_empty == True:
        
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

            #VERIFY IF PDF EXISTS
            files_inseridos = self.listWidget_3.count()
            if files_inseridos > 0:
                for i in range(files_inseridos):
                    if self.comboBox_23.currentText() == 'Sim':
                        Pdf_funtion.copy_and_move_pdf_to_patch(self,"Recorrente",id_bank,id_lancamento)
                    else:
                        Pdf_funtion.copy_and_move_pdf_to_patch(self,"Unico",id_bank,id_lancamento)
            else:
                pass
        else:
            pass
        
        print("VALIDO?",validador_empty)
        

    #EVENTS FOR BUTTONS
    def _event_change_stakecard(self):
        effects.Effetc_slides._add_banks_credits(self)
        if self.comboBox_24.currentText() == "Sim":
            return self.stackedWidgetadc_2.setCurrentWidget(self.page_config_creduts)
        else:
         return self.stackedWidgetadc_2.setCurrentWidget(self.page_config_counts1)
        
    # ADD VALORES AO BANCO DE DADOS BANK
    def _add_bank(self):
        
        
        validador_empty = Alerts._validador_new_bank(self)
        if validador_empty == True:
            
            
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
            
            #CONVERT VALUES BRL TO USD
            saldo_inicial = Convert_Moedas._brl_to_usd(self,saldo_inicial)
            limite = Convert_Moedas._brl_to_usd(self,limite)

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
                card_db_fun.funcoes_cartao._delete_all_frame_cards(self)
                card_db_fun.funcoes_cartao.hide_show_logoff(self)
                card_db_fun.funcoes_cartao._start_values(self)
                card_db_fun.funcoes_cartao.group_main(self)
                dados = home_db_query.Return_Values_Conditions._return_bank_id(str(rand_id))
                CardFrameBank.creat_new_widget(self,dados[0])
                return Group.execs(self)
            


            elif if_credit_card == '':
                print("Não tem cartão de crédito selecionar algo no campo")
            else:
                data.append(([nome_bank, titular, agencia, conta, saldo_inicial, if_credit_card],[]))
                credit_card = False
                print("data",data)
                home_db_query.Add_values._add_new_bank(data[0], credit_card, rand_id)
                dados = home_db_query.Return_Values_Conditions._return_bank_id(str(rand_id))
                CardFrameBank.creat_new_widget(self,dados[0])
                return Group.execs(self)
        else:
            return Loading_screen_gif.error_gif(self)


    def _categorias_entra_said(self):
        saidas =  Category._saidas()
        entradas = Category._entradas()
        
        metodos_pagamento_entrada = Payments_Type._entradas()
        
        metodos_pagamento_saida = Payments_Type._saidas()
        
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
        def thead(self):
            Loading_screen_gif.show_loading_screen(self)
            #LOADING GIF ANIMATION THREAD
            # START WORKER
        
            
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
            #SETTINGS CREDIT CARD ZEROS HIDDEN
            validador = home_db_query.Return_values_configs._return_default_h_s_z()
            # LANCAMENTO DE FATURAS CARTOES:
            if not ids:
                pass
            else:
                for i in range(len(ids)):
                    
                    #verifica se saldo é zero
                    fatura_zero = card_db_test.Return_Values_Calcs._valor_fatura(ids[i],mes,ano)
                    if validador == 'True' and fatura_zero == '0':
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
                        # mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                        # ano = self.label_72.text()
                        print("anoooo",ano)
                        #TODO LOGICA %S CONSULTA DB DIA VENCIMENTO , MES E ANO ATUAL
                        #M D Y
                        vencimento = "%s-%s-%s"%(date_ven,mes,ano)
                        print("VENCIMENTO",vencimento)
                        self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
                        self.dateedit.setDate(QtCore.QDate.fromString(vencimento, "dd-MM-yyyy")) #NAO SEI SE TA CERTO
                        self.dateedit.calendarWidget().setGridVisible(True)
                        self.dateedit.calendarWidget().setFirstDayOfWeek(Qt.Monday)
                        self.dateedit.calendarWidget().setStyleSheet("QDateEdit{ border:none; border-radius:0px;} QCalendarWidget QToolButton { height: 20px; width: 80px; border:none; border-radius:0px; color: white; font-size: 18px; icon-size: 20px, 20px; background-color:rgb(0,0,0); } QCalendarWidget QMenu { width: 100px; left: 20px; color: white; font-size: 18px; background-color:rgb(0,0,0); } QCalendarWidget QSpinBox { width: 100px; font-size: 18px;; color: white; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); selection-background-color: rgb(136, 136, 136); selection-color: rgb(255, 255, 255); } QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:20px; } QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:20px;} QCalendarWidget QSpinBox::up-arrow { width:20px;  height:20px; } QCalendarWidget QSpinBox::down-arrow { width:20px;  height:20px; } QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); } QCalendarWidget QAbstractItemView:enabled { font-size: 18px; background-color:rgb(0,0,0); background-color: black; selection-background-color: rgb(0, 0, 0); selection-color: rgb(0, 255, 0); } QCalendarWidget QWidget#qt_calendar_navigationbar { background-color:rgb(0,0,0);} QCalendarWidget QAbstractItemView:disabled { color: rgb(64, 64, 64); }")

                        self.table.setCellWidget(row_count, 5, self.dateedit)

                        # 5 = PRIORIDADE 

                        # mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                        # ano = self.label_72.text()
                        format = "%s-%s"%(ano,mes)

                        priori = card_db_test.Return_Values_Calcs._fatural_atual(ids[i][0],format)
                        print("ANO_MES_VALOR",format)
                        print("PRIORIDADE",priori)


                        backgroud = '#00ff00'
                        print(priori,"ERROR 'PRIORIDADE'")
                        format_value = priori.replace('.', '')
                        if int(format_value) >= 0 and int(format_value) < 200:
                            text_priori = 'Baixo'
                            backgroud = '#6aa84f'
                        elif int(format_value) > 200 and int(format_value) < 400:
                            text_priori = 'Medio'
                            backgroud = '#ffd966'
                        else:
                            text_priori = 'Alto'
                            backgroud = '#cc0000' 
                            

                        self.table.setItem(row_count, 6, QTableWidgetItem(str(text_priori)))
                        self.table.item(row_count,6).setTextAlignment(Qt.AlignCenter)


                        self.frame = QFrame()
                        self.frame.setObjectName(u"frame")
                        self.frame.setMaximumSize(QSize(7, 16777215))
                        self.frame.setStyleSheet(u"background-color:"+backgroud+"; border-radius:3px; margin:7px;")
                        self.table.setCellWidget(row_count, 6, self.frame)


                        # 6 = CATEGORIA
                        cate = 'Fatura'

                        icone = QFrame()
                        icone.setMaximumSize(QSize(35, 35))
                        icone.setStyleSheet(u"background-color:rgba(255,255,255,0);border-image: url(:/icons-cards/src-page-cartoes/credit-debit.png);\n"
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
                            color_label = '#fffff8'


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


                        # mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                        # ano = self.label_72.text()
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
                            color_label = '#fffff8'

                        print(valor,"VALOR'")
                        self.table.setItem(row_count, 9, QTableWidgetItem(str(format_valor)))
                        self.table.item(row_count,9).setTextAlignment(Qt.AlignCenter)
                        self.table.item(row_count,9).setTextColor(QColor(color_label))



                        # 9 = STATUS

                        # mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                        # ano = self.label_72.text()

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

            # mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
            # ano = self.label_72.text()
            dados = home_db_query.Return_Values_Conditions.return_lancamentos_recorretes() #LINHAS DA TABELA
            #nao retonra data de lancamento vai ser o do mes atual

            # current_mes = Dates_end_times.convert_string_date(self,self.label_67.text())
            # current_mes_local = datetime.now().month
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
                    # mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                    #TODO LOGICA %S CONSULTA DB DIA VENCIMENTO , MES E ANO ATUAL
                    #M D Y
                    vencimento = "%s-%s-%s"%(date_ven,mes,Dates_end_times.current_date_extrato(self)[0])
                    print("VENCIMENTO",vencimento)
                    self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
                    self.dateedit.setDate(QtCore.QDate.fromString(vencimento, "dd-MM-yyyy")) #NAO SEI SE TA CERTO
                    self.dateedit.calendarWidget().setGridVisible(True)
                    self.dateedit.calendarWidget().setFirstDayOfWeek(Qt.Monday)
                    self.dateedit.calendarWidget().setStyleSheet("QDateEdit{ border:none; border-radius:0px;} QCalendarWidget QToolButton { height: 20px; width: 80px; border:none; border-radius:0px; color: white; font-size: 18px; icon-size: 20px, 20px; background-color:rgb(0,0,0); } QCalendarWidget QMenu { width: 100px; left: 20px; color: white; font-size: 18px; background-color:rgb(0,0,0); } QCalendarWidget QSpinBox { width: 100px; font-size: 18px;; color: white; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); selection-background-color: rgb(136, 136, 136); selection-color: rgb(255, 255, 255); } QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:20px; } QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:20px;} QCalendarWidget QSpinBox::up-arrow { width:20px;  height:20px; } QCalendarWidget QSpinBox::down-arrow { width:20px;  height:20px; } QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); } QCalendarWidget QAbstractItemView:enabled { font-size: 18px; background-color:rgb(0,0,0); background-color: black; selection-background-color: rgb(0, 0, 0); selection-color: rgb(0, 255, 0); } QCalendarWidget QWidget#qt_calendar_navigationbar { background-color:rgb(0,0,0);} QCalendarWidget QAbstractItemView:disabled { color: rgb(64, 64, 64); }")

                    self.table.setCellWidget(row_count, 5, self.dateedit)

                    # 5 = PRIORIDADE 

                    priori = dados[i][3]
                    self.table.setItem(row_count, 6, QTableWidgetItem(str(priori)))
                    backgroud = '#00ff00'
                    if priori == 'baixo':
                        backgroud = '#6aa84f'
                    elif priori == 'medio':
                        backgroud = '#ffd966'
                    elif priori == 'alto':
                        backgroud = '#cc0000'

                    self.table.setItem(row_count, 6, QTableWidgetItem(str(priori)))
                    self.table.item(row_count,6).setTextAlignment(Qt.AlignCenter)


                    self.frame = QFrame()
                    self.frame.setObjectName(u"frame")
                    self.frame.setMaximumSize(QSize(7, 16777215))
                    self.frame.setStyleSheet(u"background-color:"+backgroud+"; border-radius:3px; margin:7px;")
                    self.table.setCellWidget(row_count, 6, self.frame)


                    # 6 = CATEGORIA
                    cate = dados[i][4]

                    url_icon = Category.patch_icons(str(cate))
                    icone = QFrame()
                    icone.setMaximumSize(QSize(35, 35))
                    icone.setStyleSheet(u"background-color:rgba(255,255,255,0);border-image: url("+url_icon+");\n"
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
                        color_label = '#fffff8'


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




                    # 8 = VALOR
                    valor = dados[i][6]
                    usd_to_brl = Convert_Moedas._usd_to_brl(self,valor)
                    valor = usd_to_brl
                    if entra_saida == 'Entrada':
                        format_valor = "+ %s"%(valor)
                        color_label = '#00ff00'
                    else:  
                        format_valor = "- %s"%(valor)
                        color_label = '#fffff8'

                    self.table.setItem(row_count, 9, QTableWidgetItem(str(format_valor)))
                    self.table.item(row_count,9).setTextAlignment(Qt.AlignCenter)
                    self.table.item(row_count,9).setTextColor(QColor(color_label))




                    # 9 = STATUS

                    # mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                    # ano = self.label_72.text()
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
            # mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
            # ano = self.label_72.text()
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
                    self.dateedit.calendarWidget().setStyleSheet("QDateEdit{ border:none; border-radius:0px;} QCalendarWidget QToolButton { height: 20px; width: 80px; border:none; border-radius:0px; color: white; font-size: 18px; icon-size: 20px, 20px; background-color:rgb(0,0,0); } QCalendarWidget QMenu { width: 100px; left: 20px; color: white; font-size: 18px; background-color:rgb(0,0,0); } QCalendarWidget QSpinBox { width: 100px; font-size: 18px;; color: white; background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); selection-background-color: rgb(136, 136, 136); selection-color: rgb(255, 255, 255); } QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:20px; } QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:20px;} QCalendarWidget QSpinBox::up-arrow { width:20px;  height:20px; } QCalendarWidget QSpinBox::down-arrow { width:20px;  height:20px; } QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); } QCalendarWidget QAbstractItemView:enabled { font-size: 18px; background-color:rgb(0,0,0); background-color: black; selection-background-color: rgb(0, 0, 0); selection-color: rgb(0, 255, 0); } QCalendarWidget QWidget#qt_calendar_navigationbar { background-color:rgb(0,0,0);} QCalendarWidget QAbstractItemView:disabled { color: rgb(64, 64, 64); }")

                    self.table.setCellWidget(row_count, 5, self.dateedit)

                    # 5 = PRIORIDADE 

                    priori = dados[i][4]
                    self.table.setItem(row_count, 6, QTableWidgetItem(str(priori)))
                    backgroud = '#00ff00'
                    if priori == 'baixo':
                        backgroud = '#6aa84f'
                    elif priori == 'medio':
                        backgroud = '#ffd966'
                    elif priori == 'alto':
                        backgroud = '#cc0000'

                    self.table.setItem(row_count, 6, QTableWidgetItem(str(priori)))
                    self.table.item(row_count,6).setTextAlignment(Qt.AlignCenter)


                    self.frame = QFrame()
                    self.frame.setObjectName(u"frame")
                    self.frame.setMaximumSize(QSize(7, 16777215))
                    self.frame.setStyleSheet(u"background-color:"+backgroud+"; border-radius:3px; margin:7px;")
                    self.table.setCellWidget(row_count, 6, self.frame)


                    # 6 = CATEGORIA
                    cate = dados[i][5]
                    url_icon = Category.patch_icons(str(cate))
                    icone = QFrame()
                    icone.setMaximumSize(QSize(35, 35))
                    icone.setStyleSheet(u"background-color:rgba(255,255,255,0);border-image: url("+url_icon+");\n"
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
                        color_label = '#fffff8'


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
                        format_valor = "+ %s"%(usd_to_brl)
                        color_label = '#00ff00'
                    else:  
                        format_valor = "- %s"%(usd_to_brl)
                        color_label = '#fffff8'

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
            


        thread = ThreadWithReturnValue(target=thead(self))
        thread.start()








class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                        **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return

    def get_return(self):
        return self._return
    


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
        print(dados)
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
        for i in range (len(dados)):
            #NOME BANCO, ID BANCO
            if CardFrameBank.count_cards_startup(self) == True:
                CardFrameBank.creat_new_widget(self,dados[i])
                print('Criado',dados[i])
            else:
                #JA TEM FRAME EXISTENTE
                pass
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
        
        
        return 0
    




    def _set_Saldo(self):
        
        
        
        
        valor = home_db_query.Saldos.Set_saldo_inicial()
        usd_to_brl = Convert_Moedas._usd_to_brl(self,valor)
        valor = usd_to_brl
        self.label_70.setText("%s"%valor)
        self.label_70.setWordWrap(True)
        self.label_70.setTextInteractionFlags(Qt.NoTextInteraction)
        
    def _set_start_ag_b_t(self):
        # titular,agencia,num_conta,saldo_inicial,nome_banco
        dados = home_db_query.Return_values._return_default_bank()
        if dados:
            print("DADOS",dados)
            dados_l = home_db_query.Return_Values_Conditions._return_ag_b_t_c(str(dados))
            print("DADOS",dados_l)
            titular = self.label_68.setText(dados_l[0])
            agencia = self.label_77.setText("Agencia: "+str(dados_l[1]))
            num_conta = self.label_78.setText("Conta: "+str(dados_l[2]))
            icon_nam_style = effects.efeitos_geral.style_sheet_card_icon(self,str(dados_l[4]))
            self.frame_97.setStyleSheet("background-image: "+icon_nam_style+"; background-repeat:no-repeat; background-position:center;")
        else:
            pass
        return True

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
        

    def set_detalhes_lancamneto_menu(self,id,id_bank,tipo):
        
        lancamento = id
        banco = id_bank
        mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
        ano = self.label_72.text()
        if tipo == "fatura":
            query = home_db_query.Return_Values_Conditions._detalhes_lancamento(lancamento,banco,mes,ano,"fatura")
            print("QUWETYY",query)
            try:
                card =  card_db_test.Ui_db._cartao(query[0][1])

                if not card:
                    card = home_db_query.Return_Values_Conditions._return_name_bank(str(query[0][1]))

                style_icon = effects.efeitos_geral.style_sheet_card_icon(self,str(card))

                icon_ui = self.icon_payout_com.setStyleSheet("background-image: "+style_icon+"; background-repeat:no-repeat; background-position:center;")
                #data pagamento
                #DATAS 2022-09-26 03:03:58 QUERTY [0][2]
                data_pagamento = query[0][3]
                data_vencimento = query[0][2]
                self.set_payment_date.setDateTime(QDateTime.fromString(data_pagamento, "yyyy-MM-dd hh:mm:ss"))
                #data programada
                self.set_vencimento_lan.setDate(QDate.fromString(data_vencimento, "yyyy-MM-dd"))
            except:
                    #NAO ESTA PAGO
                    print("NAO ESTA PAGO")
                    self.set_payment_date.setDateTime(QDateTime.currentDateTime())
                    self.set_vencimento_lan.setDate(QDate.currentDate())
                    
                                 
        else:
            qyert_name_bank = home_db_query.Return_Values_Conditions._return_name_bank(banco)
            query = home_db_query.Return_Values_Conditions._detalhes_lancamento(lancamento,banco,mes,ano,"lancamento")
            style_icon = effects.efeitos_geral.style_sheet_card_icon(self,str(qyert_name_bank))
            
            icon_ui = self.icon_payout_com.setStyleSheet("background-image: "+style_icon+"; background-repeat:no-repeat; background-position:center;")
            #data pagamento
            #DATAS 2022-09-26 03:03:58 QUERTY [0][2]
            data_pagamento = query[0][2]
            data_vencimento = query[0][1]
            self.set_payment_date.setDateTime(QDateTime.fromString(data_pagamento, "yyyy-MM-dd hh:mm:ss"))
            #data programada
            self.set_vencimento_lan.setDate(QDate.fromString(data_vencimento, "yyyy-MM-dd"))

        print("QUREY",query)
        #ex [(974257, '2022-08-10', '2022-09-26 03:03:58')]
        #icon
        

        
    def _verifi_is_credit_card(self,id):
        if home_db_query.Return_Values_Conditions._verify_id_is_credit_card(id) == True:
            print("cartao")
            
            return True
        else:
            print("nao cartao")
            return False
class Pagamento(Ui_MainWindow):

    def _pagar_lancamento(self):
        Loading_screen_gif()
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
                ui_val =self.table.item(current_row,9).text()
                format_split = ui_val.split(" ")
                
                valor =  Convert_Moedas._brl_to_usd(self,format_split[2])
                saldo_atual = home_db_query.Return_values.return_saldo_banks(id_bank)
                operacao = float(saldo_atual) - float(valor)
                valor_to_blr = Convert_Moedas._usd_to_brl(self,valor)
                operacao_to_blr = Convert_Moedas._usd_to_brl(self,operacao)
                
                alert_confirm = Confirn_Frame._show(self, str(valor_to_blr), str(operacao_to_blr))

                if alert_confirm == True:
                    print("Lancamento recorrente")
                    home_db_query.Add_values._add_new_lancamento_recorrente(id_lancamento,id_bank,mes,ano)
                    #ANIMANCAO
                    home_db_query.Saldos._pagar_lancamento(id_lancamento,id_bank,'Saida',ano,mes)


                    #TODO TESTE ANIMCAÇAO dps

                    Set_values_startup._set_Saldo(self)
                    mainpage.load_extrato_filter(self)
                    CardFrameBank._update_frame_cards_saldo(self,id_bank)
                    Loading_screen_gif._payout_receiver_sucess(self)
                else:
                    pass
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText("Lançamento já pago")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                Loading_screen_gif.error_gif(self)
        else:
            if pago == False:
                ui_val =self.table.item(current_row,9).text()
                format_split = ui_val.split(" ")
                
                valor =  Convert_Moedas._brl_to_usd(self,format_split[2])
                saldo_atual = home_db_query.Return_values.return_saldo_banks(id_bank)
                operacao = float(saldo_atual) - float(valor)
                valor_to_blr = Convert_Moedas._usd_to_brl(self,valor)
                operacao_to_blr = Convert_Moedas._usd_to_brl(self,operacao)
                
                alert_confirm = Confirn_Frame._show(self, str(valor_to_blr), str(operacao_to_blr))
                if alert_confirm == True:
                    id_lancamento = self.table.item(current_row,1).text()
                    id_bank = self.table.item(current_row,2).text()
                    home_db_query.Saldos._pagar_lancamento(id_lancamento,id_bank,'Saida',ano,mes)
                    Set_values_startup._set_Saldo(self)
                    mainpage.load_extrato_filter(self)
                    CardFrameBank._update_frame_cards_saldo(self,id_bank)
                    #MENSAGEM BOX
                    # msg = QMessageBox()
                    # msg.setWindowTitle("Sucesso")
                    # msg.setText("Lançamento pago com sucesso")
                    # msg.setIcon(QMessageBox.Information)
                    # msg.exec_()
                    Loading_screen_gif._payout_receiver_sucess(self)
                else:
                    pass
                
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText("Lançamento já pago")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                Loading_screen_gif.error_gif(self)

            
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
                ui_val =self.table.item(current_row,9).text()
                format_split = ui_val.split(" ")
                
                valor =  Convert_Moedas._brl_to_usd(self,format_split[2])
                saldo_atual = home_db_query.Return_values.return_saldo_banks(id_bank)
                operacao = float(saldo_atual) + float(valor)
                valor_to_blr = Convert_Moedas._usd_to_brl(self,valor)
                operacao_to_blr = Convert_Moedas._usd_to_brl(self,operacao)
                
                alert_confirm = Confirn_Frame._show(self, str(valor_to_blr), str(operacao_to_blr))
                if alert_confirm == True:
                    print("Lancamento recorrente, deseja receber todos os lançamentos?")
                    home_db_query.Add_values._add_new_lancamento_recorrente(id_lancamento,id_bank,mes,ano)
                    home_db_query.Saldos._pagar_lancamento(id_lancamento,id_bank,'Entrada',ano,mes)
                    Set_values_startup._set_Saldo(self)

                    mainpage.load_extrato_filter(self)
                    CardFrameBank._update_frame_cards_saldo(self,id_bank)
                    #TEMQ FAZER A VALIDADAO POR DATA DO LKANCAMENTO
                    Loading_screen_gif._payout_receiver_sucess(self)
                else:
                    pass
                
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText("Lançamento já Recebido")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                Loading_screen_gif.error_gif(self)
        else:
            if pago == False:
                ui_val =self.table.item(current_row,9).text()
                format_split = ui_val.split(" ")
                
                valor =  Convert_Moedas._brl_to_usd(self,format_split[2])
                saldo_atual = home_db_query.Return_values.return_saldo_banks(id_bank)
                operacao = float(saldo_atual) + float(valor)
                valor_to_blr = Convert_Moedas._usd_to_brl(self,valor)
                operacao_to_blr = Convert_Moedas._usd_to_brl(self,operacao)
                
                alert_confirm = Confirn_Frame._show(self, str(valor_to_blr), str(operacao_to_blr))
                if alert_confirm == True:
                    id_lancamento = self.table.item(current_row,1).text()
                    id_bank = self.table.item(current_row,2).text()
                    home_db_query.Saldos._pagar_lancamento(id_lancamento,id_bank,'Entrada',ano,mes)
                    Set_values_startup._set_Saldo(self)
                    mainpage.load_extrato_filter(self)
                    CardFrameBank._update_frame_cards_saldo(self,id_bank)
                    #MENSAGEM BOX
                    # msg = QMessageBox()
                    # msg.setWindowTitle("Sucesso")
                    # msg.setText("Lançamento Recebido com sucesso")
                    # msg.setIcon(QMessageBox.Information)
                    # msg.exec_()
                    Loading_screen_gif._payout_receiver_sucess(self)
                else:
                    pass
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Erro")
                msg.setText("Lançamento já recebido")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
                Loading_screen_gif.error_gif(self)

            
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
                ui_val =self.table.item(current_row,9).text()
                format_split = ui_val.split(" ")
                
                valor =  Convert_Moedas._brl_to_usd(self,format_split[2])
                saldo_atual = home_db_query.Return_values.return_saldo_banks(id_bank)
                operacao = float(saldo_atual) - float(valor)
                valor_to_blr = Convert_Moedas._usd_to_brl(self,valor)
                operacao_to_blr = Convert_Moedas._usd_to_brl(self,operacao)
                
                alert_confirm = Confirn_Frame._show(self, str(valor_to_blr), str(operacao_to_blr))
                if alert_confirm == True:
                    print("SALDO",home_db_query.Return_values.return_saldo_banks(id_bank))
                    home_db_query.Saldos._pagar_fatura(id_bank,0,mes,ano)
                    card_db_test.Return_Values_Calcs._pagar_fatura(id_bank,mes,ano)
                    Set_values_startup._set_Saldo(self)
                    CardFrameBank._update_frame_cards_saldo(self,id_bank)
                    mainpage.load_extrato_filter(self)
                    msg = QMessageBox()
                    msg.setWindowTitle("Sucesso")
                    msg.setText("Fatura paga com sucesso")
                    msg.setIcon(QMessageBox.Information)
                    msg.exec_()
                    Loading_screen_gif._payout_receiver_sucess(self)
                else:
                    pass
                
            else:
                validate = Alerts._alerta_fatura_banco_indiferente(self)
                if validate == True:
                    default_bank = home_db_query.Return_values._return_default_bank()
                    ui_val =self.table.item(current_row,9).text()
                    format_split = ui_val.split(" ")

                    valor =  Convert_Moedas._brl_to_usd(self,format_split[2])
                    saldo_atual = home_db_query.Return_values.return_saldo_banks(default_bank)
                    operacao = float(saldo_atual) - float(valor)
                    valor_to_blr = Convert_Moedas._usd_to_brl(self,valor)
                    operacao_to_blr = Convert_Moedas._usd_to_brl(self,operacao)

                    alert_confirm = Confirn_Frame._show(self, str(valor_to_blr), str(operacao_to_blr))
                    
                    if alert_confirm == True:
                        

                        home_db_query.Saldos._pagar_fatura(str(default_bank),id_bank,mes,ano)
                        card_db_test.Return_Values_Calcs._pagar_fatura(id_bank,mes,ano)
                        # TODO ERRO AQ
                        Set_values_startup._set_Saldo(self)
                        mainpage.load_extrato_filter(self)
                        CardFrameBank._update_frame_cards_saldo(self,id_bank)
                        msg = QMessageBox()
                        msg.setWindowTitle("Sucesso")
                        msg.setText("Fatura paga com sucesso debitado da conta principal!")
                        msg.setIcon(QMessageBox.Information)
                        msg.exec_()
                        Loading_screen_gif._payout_receiver_sucess(self)
                    else:
                        pass
                else:
                    pass
                    return False
                    print("NÃO PAGAR FATURA")
        elif verifi_if_pago == 'pago':
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText("Fatura já paga")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            Loading_screen_gif.error_gif(self)
        elif verifi_if_pago == 'proximas':
            msg = QMessageBox()
            msg.setWindowTitle("Erro")
            msg.setText("Fatura ainda não venceu Ou nao existe Valor")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
            Loading_screen_gif.error_gif(self)
     

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
        qdialog.setWindowFlags(Qt.FramelessWindowHint)
        qdialog.setFixedSize(400, 200)
        qdialog.setStyleSheet("background-color:rgb(40, 42, 54); border: 1px solid rgba(255,255,255,30);")

        qdialog.setWindowModality(Qt.ApplicationModal)

        #FONTE
        #fonte
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light SemiCondensed")
        font3.setPointSize(10)

        true_or_false = 0
        #OK BUTTON CANC BUTTON
        ok_button = QPushButton("Sim",qdialog)
        ok_button.setGeometry(300,150,80,30)
        ok_button.setStyleSheet("QPushButton{ border-radius:10px; color: rgb(255, 255, 255); background-color:rgba(255,255,255,10); border: 1px solid rgba(255,255,255,20); border-radius:7px; } QPushButton:hover{ background-color:rgba(31, 168, 49,70);} QPushButton:pressed{ background-color:rgba(31, 168, 49,170); }")
        ok_button.clicked.connect(qdialog.accept)
        ok_button.setFont(font3)
        
        #CANCEL BUTTON
        cancel_button = QPushButton("Não",qdialog)
        cancel_button.setGeometry(200,150,80,30)
        cancel_button.clicked.connect(qdialog.reject) 
        cancel_button.setStyleSheet("QPushButton{ border-radius:10px; color: rgb(255, 255, 255); background-color:rgba(255,255,255,10); border: 1px solid rgba(255,255,255,20); border-radius:7px; } QPushButton:hover{ background-color:rgba(225, 60, 47,70); } QPushButton:pressed{ background-color:rgba(225, 60, 47,170); }")
        cancel_button.setFont(font3)

    

        #LABEL
        label = QLabel(qdialog)
        label.setGeometry(10,10,380,130)
        label.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(255,255,255,0); border:none;")
        label.setText("Está fatura é de um banco diferente do principal!\nNao existe conta bancaria vinculado a este Cartao de Credito \npara descontar o valor\ndeseja descontar no debito do banco Principal?")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(font3)
        qdialog.exec_()
        return qdialog.result()


    def _combobox_empty(self,recorrente,pago):
        #CONTA comboBox_11
        #OPERAÇÃO comboBox_25
        #PAGAMENTO comboBox_27
        #CATEGORIA comboBox_21
        #DESCRIÇÃO lineEdit_11
        #DATA DA TRANSAÇÃO NAO RECORRENTE lancamento_programado_2
        # VALOR   lineEdit_13
        #PAGO/RECEBIDO comboBox_22
        #RECORRENTE?  comboBox_23
        #recorrente programar data lancamento_programado
        #CONFIGURAR RECORRENCIA comboBox_26
        #.TODOS DIA? lineEdit_14

        #VALIDADOR SE RECORRENTE:
        if recorrente == True:
            #VALIDADOR SE paPAGO:
            if pago == True:
                if self.comboBox_11.currentText() == "" or self.comboBox_25.currentText() == "" or self.comboBox_27.currentText() == "" or self.comboBox_21.currentText() == "" or self.lineEdit_11.text() == "" or self.lineEdit_13.text() == "" or self.comboBox_22.currentText() == "" or self.comboBox_23.currentText() == "" or self.comboBox_26.currentText() == "" or self.lineEdit_14.text() == "":
                    return False
                else:
                    #VERIFICA SE DATA TODO DIA RECORRENTE É VALIDO
                    if self.lineEdit_14.text() == "0" or self.lineEdit_14.text() == "00" or len(self.lineEdit_14.text()) > 2 or len(self.lineEdit_14.text()) < 2 or int(self.lineEdit_14.text()) > 31 or int(self.lineEdit_14.text()) < 1:
                        return False
                    else:
                        val = self.lineEdit_13.text()
                        if Alerts._validador_int(val) == False:
                            print ("error?????????????????????",Alerts._validador_int(val))
                            return False
                        else:
                            if len(self.lineEdit_14.text()) == 2:
                                return True

            if pago == False:
                if self.comboBox_11.currentText() == "" or self.comboBox_25.currentText() == "" or self.comboBox_27.currentText() == "" or self.comboBox_21.currentText() == "" or self.lineEdit_11.text() == "" or self.lineEdit_13.text() == "" or self.comboBox_22.currentText() == "" or self.comboBox_23.currentText() == "" or self.comboBox_26.currentText() == "" or self.lineEdit_14.text() == "":
                    return False
                else:
                    val = self.lineEdit_13.text()
                    if Alerts._validador_int(val) == False:
                        print ("error?????????????????????",Alerts._validador_int(val))
                        return False
                    else:
                        if len(self.lineEdit_14.text()) == 2:
                            return True
        if recorrente == False:
            if pago == True:
                if self.comboBox_11.currentText() == "" or self.comboBox_25.currentText() == "" or self.comboBox_27.currentText() == "" or self.comboBox_21.currentText() == "" or self.lineEdit_11.text() == "" or self.lineEdit_13.text() == "" or self.comboBox_22.currentText() == "" or self.comboBox_23.currentText() == "":
                    return False
                else:
                    #VERIFICA VALOR SE CONTEM STRING
                    val = self.lineEdit_13.text()
                    if Alerts._validador_int(val) == False:
                        return False
                    else:
                        return True
            if pago == False:
                
                if self.comboBox_11.currentText() == "" or self.comboBox_25.currentText() == "" or self.comboBox_27.currentText() == "" or self.comboBox_21.currentText() == "" or self.lineEdit_11.text() == "" or self.lineEdit_13.text() == "" or self.comboBox_22.currentText() == "" or self.comboBox_23.currentText() == "":
                    
                    return False
                else:
                    
                    val = self.lineEdit_13.text()
                    print("valor dando errado", val)
                    if Alerts._validador_int(val) == False:
                        
                        return False
                    else:
                        return True
        
    def _val_new_lan_pass_or_not(self):
        recorrente = self.comboBox_23.currentText()
        pago_text = self.comboBox_22.currentText()
        reco_ = True
        pago_ = True
        print(recorrente,pago_text,"texto")
        if recorrente == "Sim" and pago_text == "Sim":
            reco_ = True
            pago_ = True
            print("pago", pago_)
            
            if Alerts._combobox_empty(self,reco_,pago_) == True:
                print("passou",)
                return True
            else:
                Qms = QMessageBox()
                Qms.setText("Preencha todos os campos corretamente!")
                Qms.setIcon(QMessageBox.Warning)
                Qms.exec_()
                return False
            
        elif recorrente == "Sim" and pago_text == "Não":
            reco_ = True
            pago_ = False
            print("pago", pago_)
            if Alerts._combobox_empty(self,reco_,pago_) == True:
                return True
            else:
                Qms = QMessageBox()
                Qms.setText("Preencha todos os campos corretamente!")
                Qms.setIcon(QMessageBox.Warning)
                Qms.exec_()
                return False
            
        elif recorrente == "Não" and pago_text == "Sim":
            reco_ = False

            pago_ = True
            if Alerts._combobox_empty(self,reco_,pago_) == True:
                return True
            else:
                Qms = QMessageBox()
                Qms.setText("Preencha todos os campos corretamente!")
                Qms.setIcon(QMessageBox.Warning)
                Qms.exec_()
                return False
            
        elif recorrente == "Não" and pago_text == "Não":
            reco_ = False
            pago_ = False
            if Alerts._combobox_empty(self,reco_,pago_) == True:
                return True
            else:
                Qms = QMessageBox()
                Qms.setText("Preencha todos os campos corretamente!")
                Qms.setIcon(QMessageBox.Warning)
                Qms.exec_()
                return False
            
    def _validador_int(value):
        
        value = re.sub('[.,]', '', value)
        if value.isdigit():
            print("passou")
            return True
        else:
            print("nao passou")
            return False
        
    def _validador_new_bank(self):
        #config banco
        #BANCO = self.select_conta_bancaria.currentText()
        #PADRAO = self.combo_bank_padrao.currentText()
        #TITULAR  = self.adctitular_conta.text()
        #AGENCIA = self.adcagencia_conta.text()
        #CONTA = self.adc_conta_conta.text()
        #SALDO INICIAL = self.adc_saldo_conta.text()
        
        # IF CREDIT CARD
        
        #credito s/n  =  self.comboBox_24.currentText()
        
        #CONFIG CARD
        
        # LIMITE TOTAL DO CARTAO  = self.adclimite_2.text()
        #titular do cartao = self.adctitular_2.text()
        #final do cartao = self.adcfinal_2.text()
        #vebcuneto do cartao = self.adcvencimento_2.text()
        #fechamneto do cartao = self.adcfechamento_2.text()
        
        #   VERIFICA SE VAI TER CARTAO DE CREDITO :
        if self.comboBox_24.currentText() == "Sim": #COM CARTAO DE CREDITO
            if self.select_conta_bancaria.currentText() == "" or self.combo_bank_padrao.currentText() == ""\
                or self.adctitular_conta.text() == "" or self.adcagencia_conta.text() == "" or self.adc_conta_conta.text() == "" \
                    or self.adc_saldo_conta.text() == "" or self.adclimite_2.text() == "" or self.adctitular_2.text() == "" or \
                        self.adcfinal_2.text() == "" or self.adcvencimento_2.text() == "" or self.adcfechamento_2.text() == "":
                return False
            else :
                #VERIFICA SALDO INICIAL E LIMITE SE CONTEM STRING
                val = self.adc_saldo_conta.text()
                val2 = self.adclimite_2.text()
                if Alerts._validador_int(val) == False or Alerts._validador_int(val2) == False:
                    return False
                #VERIFCA DATA DE FECHAMENTO E VENCIMENTO:
                elif len(self.adcvencimento_2.text()) != 2 or len(self.adcfechamento_2.text()) != 2 or self.adcvencimento_2.text().isdigit() == False or self.adcfechamento_2.text().isdigit() == False or int(self.adcvencimento_2.text()) > 31 or int(self.adcfechamento_2.text()) > 31 or int(self.adcvencimento_2.text()) < 1 or int(self.adcfechamento_2.text()) < 1: 
                    return False
                
                #VERIFICA FINAL DO CARTAO:
                elif  self.adcfinal_2.text().isdigit() == False:
                    return False
                
                #VERIFICA SE AGENCIA E CONTA SAO NUMEROS:
                elif self.adcagencia_conta.text().isdigit() == False or self.adc_conta_conta.text().isdigit() == False:
                    return False
                else:
                    return True
                
        else: #SEM CARTAO DE CREDITO
            if self.select_conta_bancaria.currentText() == "" or self.combo_bank_padrao.currentText() == ""\
                or self.adctitular_conta.text() == "" or self.adcagencia_conta.text() == "" or self.adc_conta_conta.text() == "" \
                    or self.adc_saldo_conta.text() == "":
                return False
            else :
                #VERIFICA SALDO INICIAL SE CONTEM STRING
                val = self.adc_saldo_conta.text()
                if Alerts._validador_int(val) == False:
                    return False
                #VERIFICA SE AGENCIA E CONTA SAO NUMEROS:
                elif self.adcagencia_conta.text().isdigit() == False or self.adc_conta_conta.text().isdigit() == False:
                    return False
                else:
                    return True
        
    def Alert_Remove_Bank(self):
        qdialog = QDialog()
        qdialog.setWindowTitle("Alerta")
        qdialog.setWindowIcon(QIcon(':/icons/icons/Alerta.png'))
        qdialog.setWindowFlags(Qt.FramelessWindowHint)
        qdialog.setFixedSize(450, 200)
        qdialog.setStyleSheet("background-color:rgb(40, 42, 54); border: 1px solid rgba(255,255,255,30);")

        qdialog.setWindowModality(Qt.ApplicationModal)

        #FONTE
        #fonte
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light SemiCondensed")
        font3.setPointSize(10)

        true_or_false = 0
        #OK BUTTON CANC BUTTON
        ok_button = QPushButton("Sim",qdialog)
        ok_button.setGeometry(300,150,80,30)
        ok_button.setStyleSheet("QPushButton{ border-radius:10px; color: rgb(255, 255, 255); background-color:rgba(255,255,255,10); border: 1px solid rgba(255,255,255,20); border-radius:7px; } QPushButton:hover{ background-color:rgba(31, 168, 49,70);} QPushButton:pressed{ background-color:rgba(31, 168, 49,170); }")
        ok_button.clicked.connect(qdialog.accept)
        ok_button.setFont(font3)
        
        #CANCEL BUTTON
        cancel_button = QPushButton("Não",qdialog)
        cancel_button.setGeometry(200,150,80,30)
        cancel_button.clicked.connect(qdialog.reject) 
        cancel_button.setStyleSheet("QPushButton{ border-radius:10px; color: rgb(255, 255, 255); background-color:rgba(255,255,255,10); border: 1px solid rgba(255,255,255,20); border-radius:7px; } QPushButton:hover{ background-color:rgba(225, 60, 47,70); } QPushButton:pressed{ background-color:rgba(225, 60, 47,170); }")
        cancel_button.setFont(font3)

    

        #LABEL
        label = QLabel(qdialog)
        label.setGeometry(10,10,440,130)
        label.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(255,255,255,0); border:none;")
        label.setText("Deseja realmente remover esta conta bancária ?\n\nATENÇÃO: Esta ação não poderá ser desfeita.\n Todos os lançamentos desta conta serão removidos, e não poderão ser recuperados\n\n Juntamente com os cartões de crédito vinculados a esta conta se houver.")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(font3)
        qdialog.exec_()
        return qdialog.result()
        
    def Alert_Remove_Lancamento(self):
        qdialog = QDialog()
        qdialog.setWindowTitle("Alerta")
        qdialog.setWindowIcon(QIcon(':/icons/icons/Alerta.png'))
        qdialog.setWindowFlags(Qt.FramelessWindowHint)
        qdialog.setFixedSize(400, 200)
        qdialog.setStyleSheet("background-color:rgb(40, 42, 54); border: 1px solid rgba(255,255,255,30);")

        qdialog.setWindowModality(Qt.ApplicationModal)

        #FONTE
        #fonte
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light SemiCondensed")
        font3.setPointSize(10)

        true_or_false = 0
        #OK BUTTON CANC BUTTON
        ok_button = QPushButton("Sim",qdialog)
        ok_button.setGeometry(300,150,80,30)
        ok_button.setStyleSheet("QPushButton{ border-radius:10px; color: rgb(255, 255, 255); background-color:rgba(255,255,255,10); border: 1px solid rgba(255,255,255,20); border-radius:7px; } QPushButton:hover{ background-color:rgba(31, 168, 49,70);} QPushButton:pressed{ background-color:rgba(31, 168, 49,170); }")
        ok_button.clicked.connect(qdialog.accept)
        ok_button.setFont(font3)
        
        #CANCEL BUTTON
        cancel_button = QPushButton("Não",qdialog)
        cancel_button.setGeometry(200,150,80,30)
        cancel_button.clicked.connect(qdialog.reject) 
        cancel_button.setStyleSheet("QPushButton{ border-radius:10px; color: rgb(255, 255, 255); background-color:rgba(255,255,255,10); border: 1px solid rgba(255,255,255,20); border-radius:7px; } QPushButton:hover{ background-color:rgba(225, 60, 47,70); } QPushButton:pressed{ background-color:rgba(225, 60, 47,170); }")
        cancel_button.setFont(font3)

    

        #LABEL
        label = QLabel(qdialog)
        label.setGeometry(10,10,380,130)
        label.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(255,255,255,0); border:none;")
        label.setText("Deseja realmente remover este lançamento ?\n\nATENÇÃO: Esta ação não poderá ser desfeita.\n")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(font3)
        qdialog.exec_()
        return qdialog.result()
        
    def Alert_all_error(self,text):
        qdialog = QDialog()
        qdialog.setWindowTitle("Alerta")
        qdialog.setWindowIcon(QIcon(':/icons/icons/Alerta.png'))
        qdialog.setWindowFlags(Qt.FramelessWindowHint)
        qdialog.setFixedSize(400, 200)
        qdialog.setStyleSheet("background-color:rgb(40, 42, 54); border: 1px solid rgba(255,255,255,30);")

        qdialog.setWindowModality(Qt.ApplicationModal)

        #FONTE
        #fonte
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light SemiCondensed")
        font3.setPointSize(10)

        true_or_false = 0
        #OK BUTTON CANC BUTTON
        ok_button = QPushButton("Compreendi",qdialog)
        ok_button.setGeometry(300,150,80,30)
        ok_button.setStyleSheet("QPushButton{ border-radius:10px; color: rgb(255, 255, 255); background-color:rgba(255,255,255,10); border: 1px solid rgba(255,255,255,20); border-radius:7px; } QPushButton:hover{ background-color:rgba(31, 168, 49,70);} QPushButton:pressed{ background-color:rgba(31, 168, 49,170); }")
        ok_button.clicked.connect(qdialog.accept)
        ok_button.setFont(font3)
        
        #LABEL
        label = QLabel(qdialog)
        label.setGeometry(10,10,380,130)
        label.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(255,255,255,0); border:none;")
        label.setText(text)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(font3)
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
        
    def show_hide_shadow(self,condicao):
        if condicao == True:
            home_db_query.Return_values_configs.shadow_ui(True)
            #REINICIA A APLICAÇÃO
            Qms = QMessageBox()
            Qms.setWindowTitle("Sucesso")
            Qms.setText("Sombra habilitadas com sucesso")
            Qms.setIcon(QMessageBox.Information)
            Qms.exec_()
            return os.execl(sys.executable, sys.executable, *sys.argv)

        elif condicao == False:
            home_db_query.Return_values_configs.shadow_ui(False)
            #REINICIA A APLICAÇÃO
            Qms = QMessageBox()
            Qms.setWindowTitle("Sucesso")
            Qms.setText("Sombra ocultada com sucesso")
            Qms.setIcon(QMessageBox.Information)
            Qms.exec_()
            return os.execl(sys.executable, sys.executable, *sys.argv)

            
class Pdf_funtion(Ui_MainWindow):
    
    #PFD FOLDER PATCH /pdf
    
    def create_folder_pdf(self):
        a = (os.path.dirname(os.path.realpath(__file__)))
        print(a)
        if not os.path.exists(a+"/pdf"):
            os.mkdir(a+"/pdf")
            if not os.path.exists(a+"/pdf/anexos"):
                os.mkdir(a+"/pdf/anexos")
            return True
        else:
            return True
    
    
    def open_pdf(self): # BUSCA PDF PARA SALVAR AO LANCAR NOVO LANÇAMENTO
        file = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Pdf files (*.pdf)")
        if file[0]:
            print(file[0])
            #SET GLOBAL VAR
            global file_patch_pdf
            pdf_file = file_patch_pdf
            
            # VERIFICA SE JA TEM UM PDF ANEXADO NO GLOBAL VAR
            if pdf_file == "" or pdf_file == None:
                pdf_file = file[0]
            else:
                pdf_file = pdf_file + "," + file[0]
            #SET GLOBAL VAR
            file_patch_pdf = pdf_file
            print("ARV FILE GLOBAL ADDED",pdf_file)
            
            
            #INSERT IN LISTWIDGET
            icon = QIcon()
            item = QListWidgetItem()
            item.setText(file[0])
            icon.addFile(u":/category_main/category_main/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
            item.setIcon(icon)
            self.listWidget_3.addItem(item)

            
            return True
        else:
            return None
    
    def copy_and_move_pdf_to_patch(self,tipo,id_bank,id_lancamento): # INSERE NO DB E MOVE O PDF PARA A PASTA PDF
        #get global var
        global file_patch_pdf
        file = file_patch_pdf
        print(file,"file")
        for i in file.split(","):
        
            if tipo == "Recorrente":
                new_name = "recorrente_"+str(id_bank)+"_"+str(id_lancamento)+".pdf"
                verifi_if_file_exists = os.path.isfile(os.path.dirname(os.path.realpath(__file__))+"/pdf/anexos/"+new_name)
                if verifi_if_file_exists == True:
                    randint = random.randint(1,10000)
                    new_name = "recorrente_"+str(id_bank)+"_"+str(id_lancamento)+"_"+str(randint)+"_part.pdf"
            else:
                new_name = "lancamento_"+str(id_bank)+"_"+str(id_lancamento)+".pdf"
                verifi_if_file_exists = os.path.isfile(os.path.dirname(os.path.realpath(__file__))+"/pdf/anexos/"+new_name)
                if verifi_if_file_exists == True:
                    randint = random.randint(1,10000)
                    new_name = "lancamento_"+str(id_bank)+"_"+str(id_lancamento)+"_"+str(randint)+"_part.pdf"


                #RENAME
            if file != None:
                a = (os.path.dirname(os.path.realpath(__file__)))
                print(a)
                #VERIFY IF FOLDER PDF EXISTS
                if Pdf_funtion.create_folder_pdf(self) == True:
                    #MOVE FILE TO PDF FOLDER
                    shutil.copy(i, a+"/pdf/anexos")
                    #RENAME FILE PDF
                    file_name = i.split("/")[-1]
                    print(file_name)
                    os.rename(a+"/pdf/anexos/"+file_name, a+"/pdf/anexos/"+new_name)
                    #INSERT IN DB
                    get_file = a+"/pdf/anexos/"+new_name
                    mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                    ano = self.label_72.text()
                    home_db_query.Pdf.insert_pdf(id_lancamento,id_bank,get_file,ano,mes)
                    return True
            else:
                return False
            
    def search_pdf(self,id_lancamento,id_bank): #BUSCA PDF APENAS PELO ID AO CLICAR NA TABELA
        mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
        ano = self.label_72.text()
        
        data_patch = home_db_query.Pdf.search_pdf(id_lancamento,id_bank,ano,mes)
        
        self.listWidget_2.clear()
        if data_patch:
            self.listWidget_2.clear()
            if len(data_patch) > 3:
                #AUMENTA FRAME
                self.listWidget_2.setMinimumHeight(220)
            elif len(data_patch) < 3:
                #DIMINUI FRAME
                self.listWidget_2.setMinimumHeight(120)
            else:
                #DIMINUI FRAME
                self.listWidget_2.setMinimumHeight(70)
            for i in range(len(data_patch)):
                icon = QIcon()
                icon.addFile(u":/category_main/category_main/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
                item = QListWidgetItem()
                item.setText(data_patch[i][0])
                item.setIcon(icon)
                self.listWidget_2.addItem(item)
        else:
            self.listWidget_2.clear()
            self.listWidget_2.setMinimumHeight(70)
            return False

    def save_pdf(self): # BAIXAR O PDF OU DOWNLOAD OU SALVAR EM OUTRO LOCAL
        file = self.listWidget_2.currentItem().text()
        print(file)
        if file:
            save_file = QFileDialog.getSaveFileName(self, 'Save file', 'c:\\',"Pdf files (*.pdf)")
            print(save_file)
            if save_file[0]:
                shutil.copy(file, save_file[0])
                #OPEN EXPLORER
                os.startfile(os.path.dirname(save_file[0]))
                return True
            else:
                return False
            
    
    def options_tool_btn_file(self): # ACOES DO MENU TOOL
        tool_btn = self.toolButton_pdf_opt
        menu = QMenu()
        
        #ACTIONS:
        action1 = QAction('Inserir Anexo')
        action2 = QAction('Abrir PDF (sem salvar)')
        action1.triggered.connect(lambda:Pdf_funtion.open_pdf_menu(self))
        action2.triggered.connect(lambda:Pdf_funtion.open_pdf_browser(self))
        menu = QMenu()
        menu.addAction(action1)
        menu.addAction(action2)
        menu.setStyleSheet("QMenu {background-color: #2d2d2d;color: #fff; font-size: 12px; font-family: 'Segoe UI';} QMenu::item:selected {background-color: #3d3d3d;}")
        menu.style().unpolish(menu)
        tool_btn.setMenu(menu)
        tool_btn.setPopupMode(QToolButton.DelayedPopup)
        #SHOW
        menu.exec_(QCursor.pos())
        

    def open_pdf_menu(self): #BUSCA E ABRE O PDF PELO MENU TOOL BUTTON QUANDO QUISER ADICIONAR MAIS ALGUINS PDFS
        file = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Pdf files (*.pdf)")
        current_row = self.tableWidget.currentRow()
        id_lancamento = self.tableWidget.item(current_row, 1).text()
        id_bank = self.table.item(current_row, 2).text()
        if self.tableWidget.item(current_row,7).text() == "Fatura":
            tipo = "Recorrente"
        else:
            tipo = home_db_query.Return_Values_Conditions._return_if_recorrente(id_lancamento)
            
            if tipo == True:
                tipo = "Recorrente"
            else:
                tipo = "Lançamento"

            
        if file[0]:
            print(file[0])
            #SET GLOBAL VAR
            global file_patch_pdf
            pdf_file = file_patch_pdf
            
            # VERIFICA SE JA TEM UM PDF ANEXADO NO GLOBAL VAR
            if pdf_file == "" or pdf_file == None:
                pdf_file = file[0]
            else:
                #CLEAR GLOABAL
                pdf_file = ""
                pdf_file = file[0]
            #SET GLOBAL VAR
            file_patch_pdf = pdf_file
            print("ARV FILE GLOBAL ADDED",pdf_file)
            
            
            #INSERT IN LISTWIDGET
            icon = QIcon()
            item = QListWidgetItem()
            item.setText(file[0])
            icon.addFile(u":/category_main/category_main/pdf.png", QSize(), QIcon.Normal, QIcon.Off)
            item.setIcon(icon)
            self.listWidget_2.addItem(item)
            #INSERT IN DB

            Pdf_funtion.copy_and_move_pdf_to_patch(self,tipo,id_bank,id_lancamento)

            
            
    def open_pdf_browser(self): # APENAS ABRE O PDF NO NAVEGADOR
        #GET CURRENT ROW LISTWIDGET TEXT
        patch = self.listWidget_2.currentItem().text()
        
        #OPEN IN BROWSER
        format_patch = patch.replace("\\","/")
        if patch:
            os.startfile(format_patch)
            return True
        else:
            return False
        
        





class Loading_screen_gif(Ui_MainWindow):

    def show_loading_screen(self):
        label_gif = QLabel(self)
        #GET REAL TIME CENTER
        label_gif.setGeometry(795,500, 100, 100)
        #transparente
        label_gif.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        label_gif.setWindowFlags(Qt.FramelessWindowHint)
        #center
        #PATCH GIF SRC/LOADING.GIF
        movie = QMovie("src/loading_1.gif")
        label_gif.setMovie(movie)
        movie.start()
        
        print("GIF LOADING")
        def close_loading():
            
            label_gif.show()
            sleep(1)
            label_gif.close()
            label_gif.deleteLater()
            print("GIF CLOSED")
            #FISH THREAD
            return True


        thread = threading.Thread(target=close_loading)
        thread.start()
    
    def close_loading_screen(self):
        
        label_gif = QLabel(self)
        label_gif.close()
        return True

    def loadingico_salvabt(self):
        print("LOADING ICO")
        
    def test_anin(self):
        label_gif2 = QLabel(self)
        #GET REAL TIME CENTER
        label_gif2.setGeometry(795,500, 500, 500)
        #transparente
        label_gif2.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        label_gif2.setWindowFlags(Qt.FramelessWindowHint)
        #center
        #PATCH GIF SRC/LOADING.GIF
        movie2 = QMovie("src/anin/gatin.gif")
        label_gif2.setMovie(movie2)
        movie2.start()
        
        print("GIF LOADING")
        def close_loading2():
            
            label_gif2.show()
            sleep(5)
            label_gif2.close()
            label_gif2.deleteLater()
            print("GIF CLOSED")
            #FISH THREAD
            return True
        thread = threading.Thread(target=close_loading2)
        thread.start()
        
    def _payout_receiver_sucess(self):
        self.label_gif3 = QLabel(self)
        #GET REAL TIME CENTER
        self.label_gif3.setGeometry(740,390, 150, 150)
        #transparente
        self.label_gif3.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_gif3.setWindowFlags(Qt.FramelessWindowHint)
        #center
        #PATCH GIF SRC/LOADING.GIF
        self.movie3 = QMovie("src/payouts/chk.gif")
        self.label_gif3.setMovie(self.movie3)
        self.movie3.start()
        
        
        print("GIF LOADING")
        def close_loading3():

            self.label_gif3.show()
            sleep(3)
            self.label_gif3.close()
            
            #DELETE LABEL
            self.label_gif3.deleteLater()


            print("GIF CLOSED")
            #FISH THREAD
            return True
        thread = threading.Thread(target=close_loading3)
        thread.start()


    def error_gif(self):
        self.label_gif4 = QLabel(self)
        #GET REAL TIME CENTER
        self.label_gif4.setGeometry(740,390, 150, 150)
        #transparente
        self.label_gif4.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.label_gif4.setWindowFlags(Qt.FramelessWindowHint)
        #center
        #PATCH GIF SRC/LOADING.GIF
        self.movie4 = QMovie("src/error/error.gif")
        self.label_gif4.setMovie(self.movie4)
        self.movie4.start()
        
        
        print("GIF LOADING")
        def close_loading4():

            self.label_gif4.show()
            sleep(3)
            self.label_gif4.close()
            
            #DELETE LABEL
            self.label_gif4.deleteLater()


            print("GIF CLOSED")
            #FISH THREAD
            return True
        thread = threading.Thread(target=close_loading4)
        thread.start()





class Confirn_Frame(Ui_MainWindow):
    def _show(self, valor,saldo_apos):

        
        qdialog = QDialog()
        qdialog.setWindowFlags(Qt.FramelessWindowHint)
        qdialog.setStyleSheet("background-color:rgb(40, 42, 54); border: 1px solid rgba(255,255,255,30);")
        #get position Ui_MainWindow
        x = self.frameGeometry().x()
        y = self.frameGeometry().y()
        #set position

        
        qdialog.setGeometry(QRect(x+650,y+400, 331, 251))
        
        qdialog.setModal(True)
        
        label_confirm = QLabel(qdialog)
        label_confirm.setObjectName(u"label_confirm")
        label_confirm.setGeometry(QRect(60, 20, 201, 41))
        font = QFont()
        font.setFamily(u"Bahnschrift Light Condensed")
        font.setPointSize(15)
    
        label_confirm.setFont(font)
        label_confirm.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(255,255,255,0); border:none;")
        label_confirm.setAlignment(Qt.AlignCenter)
        sald_confirm = QLabel(qdialog)
        sald_confirm.setObjectName(u"sald_confirm")
        sald_confirm.setGeometry(QRect(20, 143, 301, 31))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Light SemiCondensed")
        font1.setPointSize(11)
        
        
        sald_confirm.setFont(font1)
        sald_confirm.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(255,255,255,0); border:none;")
        line_confirm = QFrame(qdialog)
        line_confirm.setObjectName(u"line_confirm")
        line_confirm.setGeometry(QRect(20, 136, 291, 1))
        line_confirm.setMaximumSize(QSize(16777215, 1))
        line_confirm.setFrameShape(QFrame.HLine)
        line_confirm.setFrameShadow(QFrame.Sunken)
        val_confirm = QLabel(qdialog)
        val_confirm.setObjectName(u"val_confirm")
        val_confirm.setGeometry(QRect(20, 107, 291, 31))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light SemiCondensed")
        font2.setPointSize(13)
        
        val_confirm.setFont(font2)
        val_confirm.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(255,255,255,0); border:none;")
        pushOK = QPushButton(qdialog)
        pushOK.setObjectName(u"pushOK")
        pushOK.setGeometry(QRect(40, 202, 75, 31))
        
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light SemiCondensed")
        font3.setPointSize(10)
        
        
        pushOK.setFont(font3)
        pushOK.setStyleSheet("QPushButton{ border-radius:10px; color: rgb(255, 255, 255); background-color:rgba(255,255,255,10); border: 1px solid rgba(255,255,255,20); border-radius:7px; } QPushButton:hover{ background-color:rgba(31, 168, 49,70);} QPushButton:pressed{ background-color:rgba(31, 168, 49,170); }")
        pushOK.clicked.connect(qdialog.accept)
        
        pushCAN = QPushButton(qdialog)
        pushCAN.setObjectName(u"pushCAN")
        pushCAN.setGeometry(QRect(210, 202, 75, 31))
        pushCAN.setFont(font3)
        pushCAN.setStyleSheet("QPushButton{ border-radius:10px; color: rgb(255, 255, 255); background-color:rgba(255,255,255,10); border: 1px solid rgba(255,255,255,20); border-radius:7px; } QPushButton:hover{ background-color:rgba(225, 60, 47,70); } QPushButton:pressed{ background-color:rgba(225, 60, 47,170); }")
        pushCAN.clicked.connect(qdialog.reject) 
        
        valor = str(valor)
        saldo_apos = str(saldo_apos)
        
        
        # #set text
        label_confirm.setText("Confirmar o Pagamento")
        val_confirm.setText("Valor: "+valor)
        sald_confirm.setText("Saldo após a Transação: "+saldo_apos)
        pushOK.setText("Continuar")
        pushCAN.setText("Cancelar")

        #show
        qdialog.exec_()
        
        return qdialog.result()
        

    def _devoler_pagamento_remove(self, valor,saldo_apos):
    
        
        qdialog = QDialog()
        qdialog.setWindowFlags(Qt.FramelessWindowHint)
        qdialog.setStyleSheet("background-color:rgb(40, 42, 54); border: 1px solid rgba(255,255,255,30);")
        #get position Ui_MainWindow
        x = self.frameGeometry().x()
        y = self.frameGeometry().y()
        #set position

        
        qdialog.setGeometry(QRect(x+650,y+400, 331, 251))
        
        qdialog.setModal(True)
        
        label_confirm = QLabel(qdialog)
        label_confirm.setObjectName(u"label_confirm")
        label_confirm.setGeometry(QRect(60, 20, 201, 41))
        font = QFont()
        font.setFamily(u"Bahnschrift Light Condensed")
        font.setPointSize(15)
    
        label_confirm.setFont(font)
        label_confirm.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(255,255,255,0); border:none;")
        label_confirm.setAlignment(Qt.AlignCenter)
        sald_confirm = QLabel(qdialog)
        sald_confirm.setObjectName(u"sald_confirm")
        sald_confirm.setGeometry(QRect(20, 143, 301, 31))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Light SemiCondensed")
        font1.setPointSize(11)
        
        
        sald_confirm.setFont(font1)
        sald_confirm.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(255,255,255,0); border:none;")
        line_confirm = QFrame(qdialog)
        line_confirm.setObjectName(u"line_confirm")
        line_confirm.setGeometry(QRect(20, 136, 291, 1))
        line_confirm.setMaximumSize(QSize(16777215, 1))
        line_confirm.setFrameShape(QFrame.HLine)
        line_confirm.setFrameShadow(QFrame.Sunken)
        val_confirm = QLabel(qdialog)
        val_confirm.setObjectName(u"val_confirm")
        val_confirm.setGeometry(QRect(20, 107, 291, 31))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light SemiCondensed")
        font2.setPointSize(13)
        
        val_confirm.setFont(font2)
        val_confirm.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(255,255,255,0); border:none;")
        pushOK = QPushButton(qdialog)
        pushOK.setObjectName(u"pushOK")
        pushOK.setGeometry(QRect(40, 202, 75, 31))
        
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light SemiCondensed")
        font3.setPointSize(10)
        
        
        pushOK.setFont(font3)
        pushOK.setStyleSheet("QPushButton{ border-radius:10px; color: rgb(255, 255, 255); background-color:rgba(255,255,255,10); border: 1px solid rgba(255,255,255,20); border-radius:7px; } QPushButton:hover{ background-color:rgba(31, 168, 49,70);} QPushButton:pressed{ background-color:rgba(31, 168, 49,170); }")
        pushOK.clicked.connect(qdialog.accept)
        
        pushCAN = QPushButton(qdialog)
        pushCAN.setObjectName(u"pushCAN")
        pushCAN.setGeometry(QRect(210, 202, 75, 31))
        pushCAN.setFont(font3)
        pushCAN.setStyleSheet("QPushButton{ border-radius:10px; color: rgb(255, 255, 255); background-color:rgba(255,255,255,10); border: 1px solid rgba(255,255,255,20); border-radius:7px; } QPushButton:hover{ background-color:rgba(225, 60, 47,70); } QPushButton:pressed{ background-color:rgba(225, 60, 47,170); }")
        pushCAN.clicked.connect(qdialog.reject) 
        
        valor = str(valor)
        saldo_apos = str(saldo_apos)
        
        
        # #set text
        label_confirm.setText("Devolver o Pagamento?")
        val_confirm.setText("Valor: "+valor)
        sald_confirm.setText("Saldo após a Devolução: "+saldo_apos)
        pushOK.setText("Sim")
        pushCAN.setText("Nao")

        #show
        qdialog.exec_()
        
        return qdialog.result()
    




class Table_Banks_Remove_Update(Ui_MainWindow):
    
    def set_values_frame(self,id_bank,id_card): #SETA OS VALORES NO FRAME DE "ALTERAR DADOS"
        #lineedits para setText
        
        #CONTA:
        # self.plainTextEdit.se
        #BANCO = self.plainTextEdit
        #agencia self.plainTextEdit_2
        #conta self.plainTextEdit_3
        #saldo self.plainTextEdit_4
        
        #CARTAO:
        
        #LIMITE self.plainTextEdit_5
        #FINAL DO CARTAO self.plainTextEdit_9
        #TITULAR self.plainTextEdit_6
        #VENCIMENTO self.plainTextEdit_8
        #FECHAMENTO self.plainTextEdit_7
        
        dados = home_db_query.Return_Values_Conditions.return_talbe_banks(id_bank,id_card)
        
        if id_card != "Não":
            self.plainTextEdit.setPlainText(str(dados[0]))
            self.plainTextEdit_2.setPlainText(str(dados[1]))
            self.plainTextEdit_3.setPlainText(str(dados[2]))
            self.plainTextEdit_4.setPlainText(str(dados[3]))
            self.plainTextEdit_5.setPlainText(str(dados[4]))
            self.plainTextEdit_9.setPlainText(str(dados[5]))
            self.plainTextEdit_6.setPlainText(str(dados[6]))
            self.plainTextEdit_8.setPlainText(str(dados[7]))
            self.plainTextEdit_7.setPlainText(str(dados[8]))
        else:
            self.plainTextEdit.setPlainText(str(dados[0]))
            self.plainTextEdit_2.setPlainText(str(dados[1]))
            self.plainTextEdit_3.setPlainText(str(dados[2]))
            self.plainTextEdit_4.setPlainText(str(dados[3]))
            self.plainTextEdit_5.setPlainText(str("Não Possui"))
            self.plainTextEdit_9.setPlainText(str("Não Possui"))
            self.plainTextEdit_6.setPlainText(str("Não Possui"))
            self.plainTextEdit_8.setPlainText(str("Não Possui"))
            self.plainTextEdit_7.setPlainText(str("Não Possui"))
        
        return True
        
        
    
    def _update_table_banks(self,id_bank,id_card):
        #CONTA:
        # self.plainTextEdit.se
        #BANCO = self.plainTextEdit
        #agencia self.plainTextEdit_2
        #conta self.plainTextEdit_3
        #saldo self.plainTextEdit_4
        
        #CARTAO:
        
        #LIMITE self.plainTextEdit_5
        #FINAL DO CARTAO self.plainTextEdit_9
        #TITULAR self.plainTextEdit_6
        #VENCIMENTO self.plainTextEdit_8
        #FECHAMENTO self.plainTextEdit_7
        
        if id_card != "Não":
            #VALIDA OS DADOS SE TIVER VAZIO DPS
            banco = self.plainTextEdit.toPlainText()
            agencia = self.plainTextEdit_2.toPlainText()
            conta = self.plainTextEdit_3.toPlainText()
            saldo = self.plainTextEdit_4.toPlainText()
            limite = self.plainTextEdit_5.toPlainText()
            final_cartao = self.plainTextEdit_9.toPlainText()
            titular = self.plainTextEdit_6.toPlainText()
            vencimento = self.plainTextEdit_8.toPlainText()
            fechamento = self.plainTextEdit_7.toPlainText()
            
            dados = [banco,agencia,conta,saldo,limite,final_cartao,titular,vencimento,fechamento]

            #update
            home_db_query.Update_Remove._update_table_banks_cards(id_bank,id_card,dados)
        
        else:
            #VALIDA OS DADOS SE TIVER VAZIO DPS
            banco = self.plainTextEdit.toPlainText()
            agencia = self.plainTextEdit_2.toPlainText()
            conta = self.plainTextEdit_3.toPlainText()
            saldo = self.plainTextEdit_4.toPlainText()
            
            dados = [banco,agencia,conta,saldo]

            #update
            home_db_query.Update_Remove._update_table_banks_cards(id_bank,id_card,dados)
        
        
        #ATT DADOS UI
        Group.execs(self)
        
        
        
        
    def _remove_table_banks(self,id_bank,id_card):
        
        #confirmação de remoção
        validacao = Alerts.Alert_Remove_Bank(self)
        if id_card != "Não":
            if validacao == True:
                home_db_query.Update_Remove._remove_table_banks_cards(id_bank,id_card)
                self.comboBox_11.clear()

                Group.execs(self)

                
                #DELET WIDGET FRAME BANK #LAYOUT self.layout_add_frame_bank
                name_staked = "stackedWidget_cartao_"+str(id_bank)
                self.frame_remove = self.findChildren(QStackedWidget, str(name_staked))
                self.frame_remove[0].deleteLater()
                self.frame_remove[1].deleteLater()


            else:
                print("Cancelado")
                pass
        else:
            if validacao == True:
                home_db_query.Update_Remove._remove_table_banks_cards(id_bank,id_card)

                self.comboBox_11.clear()
                
                Group.execs(self)
            
                #DELET WIDGET FRAME BANK #LAYOUT self.layout_add_frame_bank
                name_staked = "stackedWidget_cartao_"+str(id_bank)
                self.frame_remove = self.findChildren(QStackedWidget, str(name_staked))
                self.frame_remove[0].deleteLater()
    

            else:
                print("Cancelado")
                pass
            



class Remove_lancamentos(Ui_MainWindow):
    
    def _Delet_lancamento(self,id_lancamento):
        current_row = self.table.currentRow()
        id = self.table.item(current_row, 1).text()
        id_bank = self.table.item(current_row, 2).text()
        tipo = home_db_query.Verify_status_payment.verify_type_lanca(id_lancamento)
        if tipo =="fatura":
            text = Texts_Erros.deletar_fatura_no_menu()
            Alerts.Alert_all_error(self,text)
        else:
            Alert = Alerts.Alert_Remove_Lancamento(self)
            if Alert == True:
                #verifica se ja foi pago/recebido
                if home_db_query.Verify_status_payment.return_status_p_pago(id_lancamento,id_bank) == True:


                    mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
                    ano = self.label_72.text()


                    if tipo == True:
                        tipo = "Entrada"
                    elif tipo == False:
                        tipo = "Saida"
                    else: tipo ="Fatura"

                    print(id_lancamento,id_bank,tipo,mes,ano)
                    value_lancamento = home_db_query.Return_Values_Conditions.get_valor_transacao(id_lancamento,id_bank,tipo,ano,mes)

                    saldo_atual = home_db_query.Return_Values_Conditions._return_saldo(id_bank)

                    if tipo == "Entrada":
                        saldo_atual = float(saldo_atual) - float(value_lancamento)
                    else:
                        saldo_atual = float(saldo_atual) + float(value_lancamento)


                    #Devolução do saldo
                    #formts
                    vl = Convert_Moedas._usd_to_brl(self,str(value_lancamento))
                    sa = Convert_Moedas._usd_to_brl(self,str(saldo_atual))

                    Devoler_dinheiro = Confirn_Frame._devoler_pagamento_remove(self,vl,sa)
                    if Devoler_dinheiro == True:
                        print("Devolução de dinheiro")
                        saldo = float(saldo_atual)

                        home_db_query.Saldos.Update_Saldo(id_bank,saldo)
                        home_db_query.Update_Remove._Delete_lancamento(id_lancamento)
                        Group.execs(self)
                    else:
                        print("nao devolvido de dinheiro")
                        home_db_query.Update_Remove._Delete_lancamento(id_lancamento)
                        Group.execs(self)
                else:
                        print("nao pago/recebido portanto nao devolvio")
                        home_db_query.Update_Remove._Delete_lancamento(id_lancamento)
                        Group.execs(self)

            else:
                pass
            
        return True
    
    


class Charts_Main(Ui_MainWindow):

    def Show_Chart(self):
        self.chart = Chart(self)
        
        mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
        ano = self.label_72.text()
        value = home_db_query.Query_Charts._Saidas_Entradas(ano,mes)
        
        #printa item do value
        for i in range(len(value)):
            print(value[i])
        
        layout = self.chart_main_e_s
        #envia dados para o chart
        self.chart.create_chart('Entradas e Saidas',value)
        #adiciona no layout
        layout.addWidget(self.chart)
        #mostra
        self.chart.show()
        return True
    
    def Update_Chart_E_S(self):
        mes = Dates_end_times.convert_string_date_query(self,self.label_67.text())
        ano = self.label_72.text()
        value = home_db_query.Query_Charts._Saidas_Entradas(ano,mes)
        self.chart.Update_Chart(value)
        return True