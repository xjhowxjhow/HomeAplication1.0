
from PySide2.QtCore import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from login_pyside24 import Ui_MainWindow
from time import sleep
from threading import Timer
from card_db_fun import Chart_one
from datetime import datetime
from frame_bank.card_frame_bank import CardFrameBank
from source_ui.shadow import InitShadow ,set_shadow
import card_db_fun
import home_db_fun
import  home_db_query
import pyautogui
import database
import webbrowser
import sys
import os
import database
import effects
import sys
import funcoes
import atexit
import requests

from home_db_fun import Loading_screen_gif
WINDOW_SIZE = 0
TOGLE_STATUS = 80
CARD_SELECTED = 0
GLOBAL_VERSION = '1.14'


class MainWindow(Ui_MainWindow,QtWidgets.QMainWindow):
    stackSignal = Signal() 
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        self.show()
        self.center()
        self.ui = Ui_MainWindow()
        global window_obj
        window_obj = self.ui
        
        

        # SOMBRAS PARA FRAMES
        set_shadow.sets(self)
 

        
        #NOTIFICAÇÃO SE CLICADA ACTION
        tray.messageClicked.connect(lambda: messageClicked(self))
        action_hide.triggered.connect(lambda: self.hide())
        action_show.triggered.connect(lambda: self.showNormal())
        
        #FONTE DA TABELA MENU
        self.font = QFont()
        self.font.setFamily(u"Bahnschrift Light Condensed")
        self.font.setPointSize(14)
        
        #CONFIGURANDO A TABELA
        self.table = self.tableWidget
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table.verticalHeader().setDefaultSectionSize(50)
        self.table.setFont(self.font)
        self.table.horizontalHeaderItem(0).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.horizontalHeaderItem(2).setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)
        self.table.setStyleSheet("QWidget { color: #fffff8; border-radius:0px; } QHeaderView::section { background-color: rgb(53, 53, 53); border:none; width:45px; height: 50px; border-radius:0px; } QTableWidget { gridline-color: #fffff8; border-radius:0px; border-radius:0px; } QTableWidget QTableCornerButton::section { background-color: #646464; border-radius:0px; } QTableView:item { border-bottom: 0.5px solid qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:0.45677 rgba(0, 0, 0, 0), stop:0.479846 rgba(255, 255, 255, 255), stop:0.50571 rgba(239, 236, 55, 0), stop:1 rgba(239, 236, 55, 0)); border-radius:0px; } QTableView::item:selected{ background-color:rgba(255, 255, 255,30); color: rgb(255, 255, 255); }")
        self.table.horizontalHeader().sectionClicked.connect(self.filtro_table_header)
        #StlypeSheet veritcal ScrollBar
     
        #HIDDEN TABELA
        self.table.setColumnHidden(1, True)
        self.table.setColumnHidden(2, True)
        self.table.setColumnHidden(11, True)
        
        self.table.setColumnHidden(4, True)
        #TAMANHO DAS COLUNAS
        #CHECK
        self.table.setColumnWidth(0, 25)
        #COLUNA ICONE
        self.table.setColumnWidth(3, 60)
        #COLUNA DATA
        self.table.setColumnWidth(5, 100)
        #COLUNA PRIORIDADE
        self.table.setColumnWidth(6, 150)
        #COLUNA CATEGORIA
        self.table.setColumnWidth(7, 170)
        #COLUNA PAGAMENTO:
        self.table.setColumnWidth(8, 150)
        #COLUNA VALOR
        self.table.setColumnWidth(9, 300)
        #COLUNA SATUS
        self.table.setColumnWidth(10, 80)
        

        #CONFIGURANDO CONTA SE TIVER CARDAO DE CREDITO
        self.comboBox_24.currentIndexChanged.connect(lambda:home_db_fun.mainpage._event_change_stakecard(self))
        self.comboBox_25.currentIndexChanged.connect(lambda:home_db_fun.mainpage._categorias_entra_said(self))
        self.comboBox_22.currentIndexChanged.connect(lambda:home_db_fun.Combobox_startup.show_programar_date(self))
        self.comboBox_23.currentIndexChanged.connect(lambda:home_db_fun.Combobox_startup.show_recorrencia_options(self))
        self.comboBox_23.currentIndexChanged.connect(lambda:home_db_fun.Combobox_startup.show_recorrencia_options(self))
        self.comboBox_26.currentIndexChanged.connect(lambda:home_db_fun.Combobox_startup.show_set_dia_recorrencia(self))
        
        #PDF VIWER:
        self.listWidget_2.itemDoubleClicked.connect(lambda:home_db_fun.mainpage.open_pdf(self))
        #OCULTOS AS COLUNAS E BOTOES TABELA MENU
        
        
        self.frame_if_card_main.hide()
        self.label_if_card.hide()
        self.frame_options_pdf.hide()

        
        
        self.salvar_4.clicked.connect(lambda:self.close())
        self.exit.clicked.connect(lambda: self.close())
        self.minimize.clicked.connect(lambda: self.showMinimized())
        self.maxmize.clicked.connect(lambda: self.restore_or_maximize_window())
        self.pushButton_7.clicked.connect(lambda:self.pop_error.hide())
        self.pop_error.hide()
        self.pop_error_cartao.hide()
        
        self.buton_login.clicked.connect(self.campo_de_verificacao)
        self.pushButton.clicked.connect(self.toggleMenu)
        self.salvar_6.clicked.connect(lambda:database.salva_dados.testedb(self))
        self.salvar_5.clicked.connect(self.desloga)

        # print(self.comboBox_2.count()-1)
        # print(self.comboBox_2.itemText(1))
        

        self.nova_despesa.clicked.connect(lambda:self.stacked_configcartao0.setCurrentWidget(self.page_new_lancamento))
        effects.Effetc_slides.menu_card(self)
        
        #OCULTA COLUNA ID DE EXTRATO CARTAO
        self.extrato_cartao_0.setColumnHidden(7, True) # COLUNA ID OCULTADA
        self.extrato_cartao_0.setColumnHidden(8, True) # SOMA DATA PARA FILTRO OCULTADA
        self.extrato_cartao_0.setColumnHidden(9, True) # STATUS DO PAGAMENTO PARA FILTRO OCULTADA
        self.table_faturas_ind_3.setColumnHidden(3, True) # COLUNA ID OCULTADA
        self.table_active_cards.setColumnHidden(6, True) # COLUNA ID OCULTADA
        
        
        #TABLE DE BANCOS ATIVOS OCULTA
        
        self.table_active_banks.setColumnHidden(0, True) # COLUNA ID OCULTADA
        self.table_active_banks.setColumnHidden(1, True) # COLUNA SALDO INICIAL
        self.table_active_banks.setColumnHidden(6, True) # COLUNA  ID CREDIT CARD
        
        #selecação do linha interia
        self.table_active_banks.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.table_faturas_ind_3.horizontalHeader().setVisible(True)
        self.table_faturas_ind.horizontalHeader().setVisible(True)
        self.table_active_cards.horizontalHeader().setVisible(True)
        self.table_active_banks.horizontalHeader().setVisible(True)
        self.table_faturas_ind_3.horizontalHeader().setDefaultSectionSize(310)
        self.table_active_cards.horizontalHeader().setDefaultSectionSize(145)
        self.table.horizontalHeader().setVisible(True)
        
        
        
        
        self.extrat_meses.setTransitionDirection(QtCore.Qt.Horizontal)
        self.extrat_meses.setTransitionSpeed(500)
        self.extrat_meses.setTransitionEasingCurve(QtCore.QEasingCurve.InOutExpo)
        self.extrat_meses.setSlideTransition(True)
        
        self.grid.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page))
        self.grid_2.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page2))
        effects.Effetc_slides.grid_cards(self)
        effects.Effetc_slides._conent_geral_cards(self)
        
        self.add_card_3.clicked.connect(lambda:card_db_fun.funcoes_cartao.adicionar_cartao(self))
        self.remover_card_3.clicked.connect(lambda:card_db_fun.funcoes_cartao.destroy_frame_card(self))
        self.apaga_compra.clicked.connect(lambda:card_db_fun.funcoes_cartao.remove_compra(self))
        self.pushButton_6.clicked.connect(self.open_webbrowser)
        self.pushButton_17.clicked.connect(lambda:card_db_fun.funcoes_cartao.today(self))
       
        # TIMERS
        
        # self.timer.timeout.connect(card_db_fun.funcoes_cartao._clock_page_cards(self))
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda:card_db_fun.funcoes_cartao._clock_page_cards(self))
        self.timer.start(1000)

        #RADIO CONFIG:
        self.hidden_saldo_fat0_true.clicked.connect(lambda:home_db_fun.Configs.hide_show_saldos_zeros(self,True))
        self.hidden_saldo_fat0_false.clicked.connect(lambda:home_db_fun.Configs.hide_show_saldos_zeros(self,False))
        
        #SHADOW ENABLE OR DISABLE
        self.shadow_true.clicked.connect(lambda:home_db_fun.Configs.show_hide_shadow(self,True))
        self.shadow_false.clicked.connect(lambda:home_db_fun.Configs.show_hide_shadow(self,False))
        
        
        self.hide_cards_main_2.clicked.connect(lambda:home_db_fun.Confirn_Frame._show(self))
        
        
        # self.show_cards_main_2.clicked.connect(lambda:home_db_fun.Loading_screen_gif.close_loading(self))
        
        
        card_db_fun.Main_page_Cards._itemlist_metas(self)
        #FILTRO DE EVENTOS#
        
        self.pushButton_8.installEventFilter(self)
        self.pushButton_9.installEventFilter(self)
        self.pushButton_10.installEventFilter(self)
        self.pushButton_11.installEventFilter(self)
        self.pushButton_12.installEventFilter(self)
        self.pushButton_14.installEventFilter(self)
        self.pushButton_15.installEventFilter(self)
        self.pushButton_16.installEventFilter(self)
        self.pushButton_18.installEventFilter(self)
        self.previus_month.installEventFilter(self)
        self.next_month.installEventFilter(self)
        self.filter_dates_btn.installEventFilter(self) 
        self.pushButton_3.installEventFilter(self)
        self.pushButton_2.installEventFilter(self)
        self.compras.installEventFilter(self)
        self.faturas.installEventFilter(self)
        self.paga_fatura.installEventFilter(self)
        self.lanca.installEventFilter(self)
        self.next_month_3.installEventFilter(self)
        self.previus_month_3.installEventFilter(self)
        self.pushButton_14.installEventFilter(self)
        self.back_main_dash.installEventFilter(self)
        self.pushButton_20.installEventFilter(self)
        self.hide_cards_main.installEventFilter(self)
        self.show_cards_main.installEventFilter(self)
        self.hide_cards_det.installEventFilter(self)
        self.show_cards_det.installEventFilter(self)
        self.table_faturas_ind_3.installEventFilter(self)
        self.listWidget.installEventFilter(self)
        self.table_active_cards.installEventFilter(self)
        self.pushButton_23.installEventFilter(self)
        self.table.installEventFilter(self)
        self.add_bank.installEventFilter(self)
        self.add_lancamento_btn.installEventFilter(self)
        self.previus_month_2.installEventFilter(self)
        self.next_month_2.installEventFilter(self)
        self.paga_fatura_3.installEventFilter(self)
        self.download_pdf_2.installEventFilter(self)
        self.download_pdf.installEventFilter(self)
        self.toolButton_pdf_opt.installEventFilter(self)
        self.config_ccoun.installEventFilter(self)
        self.config_crdit_c.installEventFilter(self)
        self.parcela_fatura_3.installEventFilter(self)
        self.paga_fatura_4.installEventFilter(self)
        self.listWidget_3.installEventFilter(self)
        self.table_active_banks.installEventFilter(self)
        self.update_bank.installEventFilter(self)
        self.remover_bank.installEventFilter(self)


        
    
    def eventFilter(self, obj, event):

            if obj == self.pushButton_8 and event.type() == QtCore.QEvent.MouseButtonPress:
                btn = "conta"
                return effects.Effetc_slides.grid_lateral_menu(self,btn)
            if obj == self.pushButton_9 and event.type() == QtCore.QEvent.MouseButtonPress:
                btn = "investimento"
                return effects.Effetc_slides.grid_lateral_menu(self,btn)
            if obj == self.pushButton_10 and event.type() == QtCore.QEvent.MouseButtonPress:
                btn = "cartao"
                return effects.Effetc_slides.grid_lateral_menu(self,btn)
            if obj == self.pushButton_11 and event.type() == QtCore.QEvent.MouseButtonPress:
                btn = "transferencia"
                return effects.Effetc_slides.grid_lateral_menu(self,btn)
            if obj == self.pushButton_15 and event.type() == QtCore.QEvent.MouseButtonPress:
                btn = "estoque"
                return effects.Effetc_slides.grid_lateral_menu(self,btn)
            
            if obj == self.pushButton_16 and event.type() == QtCore.QEvent.MouseButtonPress:
                btn = "config"
                return effects.Effetc_slides.grid_lateral_menu(self,btn)

            if obj == self.previus_month and event.type() == QtCore.QEvent.MouseButtonPress:
                acao = "Previus"
                objects = self.page_2
                effects.Effetc_slides.grid_filter(self,acao,objects)
                card_db_fun.funcoes_cartao._current_date(self,acao)
                return card_db_fun.Chart_one.clear(self)

            
            if obj == self.next_month and event.type() == QtCore.QEvent.MouseButtonPress:
                acao = "Next"
                objects = self.page_2
                effects.Effetc_slides.grid_filter(self,acao,objects)
                card_db_fun.funcoes_cartao._current_date(self,acao)
                return card_db_fun.Chart_one.clear(self)
            
            if obj == self.pushButton_3 and event.type() == QtCore.QEvent.MouseButtonPress:
                
                #TODO VOLTA  FILTRO NEXT E PREV MESES
                self.extrat_meses.setCurrentWidget(self.page_2)
                self.stack_extrato_pages.setCurrentWidget(self.extrato_cards_dbs)
                mes = card_db_fun.funcoes_cartao._mes2(self)
                card_db_fun.funcoes_cartao._return_mes_string(self)
                card_db_fun.funcoes_cartao._current_date(self,'none')
                return card_db_fun.funcoes_cartao.carrega_extrato_mes(self,mes)

            if obj == self.pushButton_2 and event.type() == QtCore.QEvent.MouseButtonPress:
                #TODO FILTRA COMPRA
                return card_db_fun.funcoes_cartao._search_compras(self)

            if obj == self.compras and event.type() == QtCore.QEvent.MouseButtonPress:
                #TODO  COMPRAS MENU DIREITO
                card_db_fun.funcoes_cartao._return_mes_string(self)
                card_db_fun.funcoes_cartao._current_date(self,"none")
                self.extrat_meses.setCurrentWidget(self.page_2)
                return self.stacked_configcartao0.setCurrentWidget(self.page_extrato)



            if obj == self.faturas and event.type() == QtCore.QEvent.MouseButtonPress:
                #TODO  COMPRAS MENU DIREITO
                self.extrat_meses.setCurrentWidget(self.page_8)
                return self.stacked_configcartao0.setCurrentWidget(self.page_Faturas)
            

            if obj == self.next_month_3 and event.type() == QtCore.QEvent.MouseButtonPress:
                #TODO  COMPRAS MENU DIREITO
                objects = self.page_8

                acao = "Next"
                effects.Effetc_slides.grid_filter(self,acao,objects)
                card_db_fun.funcoes_cartao._filter_year_faturas(self,"Next")
                return card_db_fun.funcoes_cartao._faturas(self)
            


            if obj == self.previus_month_3 and event.type() == QtCore.QEvent.MouseButtonPress:
                #TODO  COMPRAS MENU DIREITO
                objects = self.page_8
                acao = "Previus"
                effects.Effetc_slides.grid_filter(self,acao,objects)
                card_db_fun.funcoes_cartao._filter_year_faturas(self,"Previus")
                return card_db_fun.funcoes_cartao._faturas(self)
            
            
            if obj == self.paga_fatura and event.type() == QtCore.QEvent.MouseButtonPress:
                #TODO  COMPRAS MENU DIREITO
                card_db_fun.funcoes_cartao._pagar_fatura(self)
                card_db_fun.funcoes_cartao._faturas(self)
                card_db_fun.funcoes_cartao._current_date(self,"none")
                card_db_fun.Main_page_Cards._top_main_values_update(self)
                card_db_fun.Main_page_Cards._middle_main_values_update(self)
                return card_db_fun.funcoes_cartao._Values_Individual(self)
            
            if obj == self.filter_dates_btn and event.type() == QtCore.QEvent.MouseButtonPress:
                #TODO  COMPRAS MENU DIREITO
                self.extrat_meses.setCurrentWidget(self.extrat_mesesPage1)
                self.extrat_meses.setStyleSheet("border-radius:7px; background-color: rgba(0, 0, 0,0); ")
                return 0

            if obj == self.pushButton_12 and event.type() == QtCore.QEvent.MouseButtonPress:
                return effects.efeitos_geral.style_sheet_main_cards(self)
            
            
            if obj == self.lanca and event.type() == QtCore.QEvent.MouseButtonPress:
                card_db_fun.funcoes_cartao._addRow(self)
                card_db_fun.funcoes_cartao._faturas(self) 
                return card_db_fun.funcoes_cartao._current_date(self,"none")
            
            if obj == self.pushButton_14 and event.type() == QtCore.QEvent.MouseButtonPress:
                self.stacked_configcartao0.setCurrentWidget(self.charts_indvidual)
                self.extrat_meses.setCurrentWidget(self.page_2)
                return Chart_one._creat_charts(self)
            
            if obj == self.pushButton_18 and event.type() == QtCore.QEvent.MouseButtonPress:
                btn = "dev"
                return effects.Effetc_slides.grid_lateral_menu(self,btn)
            
            if obj == self.back_main_dash and event.type() == QtCore.QEvent.MouseButtonPress:
                
                return self.detalhes_cartao.setCurrentWidget(self.dashboard_cards)
                
            
            if obj == self.pushButton_20 and event.type() == QtCore.QEvent.MouseButtonPress:
                
                return self.detalhes_cartao.setCurrentWidget(self.detalhes_cartaoPage1)
            
            
            #todo Animation cards grid
            if obj == self.hide_cards_main and event.type() == QtCore.QEvent.MouseButtonPress:
                return effects.Effetc_slides._hide_group_cards(self)
            if obj == self.hide_cards_det and event.type() == QtCore.QEvent.MouseButtonPress:
                return effects.Effetc_slides._hide_group_cards(self)

            if obj == self.table_faturas_ind_3 and event.type() == QtCore.Qt.LeftButton or event.type() == QtCore.Qt.RightButton: 
                try:
                    self.table_faturas_ind_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
                    linha = self.table_faturas_ind_3.currentRow()
                    id = self.table_faturas_ind_3.item(linha,3).text()
                    card_db_fun.Main_page_Cards._table_main_values_update(self,id)
                except:

                        pass
            if obj == self.listWidget and event.type() == QtCore.Qt.LeftButton or event.type() == QtCore.Qt.RightButton: 
                try:
                    currentcate = self.listWidget.currentItem().text()
                    card_db_fun.Main_page_Cards._categoria_metas(self,currentcate)
                except:
                    pass

            if obj == self.table_active_cards and event.type() == QtWidgets.QAbstractItemView.SelectRows:
                try:
                    self.table_active_cards.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
                    linha = self.table_active_cards.currentRow()
                    id = self.table_active_cards.item(linha,6).text()
                    card_db_fun.funcoes_cartao.style_config_card_talbe_slected(self,id)
                    
                except:
                    pass
                
            if obj == self.pushButton_23 and event.type() == QtCore.QEvent.MouseButtonPress:
                try:
                    card_db_fun.funcoes_cartao._update_cards_config(self)
                    card_db_fun.funcoes_cartao._update_table_config(self)
                except:
                    pass

            if obj == self.table and event.type() == QtWidgets.QAbstractItemView.SelectRows:
                current_row = self.table.currentRow()
                current_column = self.table.currentColumn()
                id = self.table.item(current_row, 1).text()
                tipo = home_db_fun.Descricao_lancamento._verifi_is_credit_card(self,id) 

                #PRINT CELL WIDGET TEXT
                

                id = self.table.item(current_row, 1).text()
                id_bank = self.table.item(current_row, 2).text()
                #SE FOR ENTRADA MUDA TEXTO BOTAO PAGAMENTO
                home_db_fun.Descricao_lancamento.Change_text_btn_pagar_receber(self,id)
                #CHAMA QUERY PARA PEGAR A DESCRCAO DO LANÇAMENTO
                validador = home_db_fun.Descricao_lancamento.set_descricao_lancamento(self,id)
                #SET TEXT DETALHES DO LANÇAMENTO:
                
                
                self.frame_options_pdf.hide()
                if validador== "fatura":
                    home_db_fun.Descricao_lancamento.set_icon_desc(self,id)
                else:
                    self.frame_if_card_main.hide()
                    self.label_if_card.hide()
                
                home_db_fun.Pdf_funtion.search_pdf(self,id,id_bank)
                
                if tipo == True:
                    home_db_fun.Descricao_lancamento.set_detalhes_lancamneto_menu(self,id,id_bank,"fatura")
                else:
                    home_db_fun.Descricao_lancamento.set_detalhes_lancamneto_menu(self,id,id_bank,"lancamento")



            if obj == self.add_bank and event.type() == QtCore.QEvent.MouseButtonPress:
                
                return home_db_fun.mainpage._add_bank(self)

            if obj ==self.add_lancamento_btn and event.type() == QtCore.QEvent.MouseButtonPress:
                
                return home_db_fun.mainpage._new_lancamento(self)
            
            # TODO EXTRATO MENU PRINCIPAL
            
            
            if obj == self.previus_month_2 and event.type() == QtCore.QEvent.MouseButtonPress:
                action = "Previus"
                home_db_fun.Dates_end_times.methodo_date_extrato(self,action)
                return home_db_fun.mainpage.load_extrato_filter(self)
                
            if obj == self.next_month_2 and event.type() == QtCore.QEvent.MouseButtonPress:
                action = "Next"
                home_db_fun.Dates_end_times.methodo_date_extrato(self,action)
                return home_db_fun.mainpage.load_extrato_filter(self)

            if obj == self.paga_fatura_3 and event.type() == QtCore.QEvent.MouseButtonPress:
                current_row = self.table.currentRow()

                if self.paga_fatura_3.text() == "Pagar":
                    
                    return home_db_fun.Pagamento._pagar_lancamento(self)
                elif self.paga_fatura_3.text() == "Pagar Fatura":
                    return home_db_fun.Pagamento._pagar_fatura(self)
                else:
                    return home_db_fun.Pagamento._receber_lancamento(self)
                 
            if obj == self.download_pdf_2 and event.type() == QtCore.QEvent.MouseButtonPress:                
                    #SELECIONAR PDF PAR ASALVAR NO LANCAMENTO
                return home_db_fun.Pdf_funtion.open_pdf(self)
            
            
            if obj == self.download_pdf and event.type() == QtCore.QEvent.MouseButtonPress:
                return home_db_fun.Pdf_funtion.save_pdf(self)
            
            
            if obj == self.toolButton_pdf_opt and event.type() == QtCore.QEvent.MouseButtonPress:
                return home_db_fun.Pdf_funtion.options_tool_btn_file(self)
            
            if obj == self.config_ccoun and event.type() == QtCore.QEvent.MouseButtonPress:
                effects.Effetc_slides._add_banks_credits(self)
                return self.stackedWidgetadc_2.setCurrentWidget(self.page_config_counts1)
            
            if obj == self.config_crdit_c and event.type() == QtCore.QEvent.MouseButtonPress:
                effects.Effetc_slides._add_banks_credits(self)
                return self.stackedWidgetadc_2.setCurrentWidget(self.page_config_creduts)
            
            #DETALHES LANCAMENTO:
            if obj == self.parcela_fatura_3 and event.type() == QtCore.QEvent.MouseButtonPress:
                effects.Effetc_slides._detalhes_lancamento_slide(self)
                return self.stackedWidget_58.setCurrentWidget(self.stackedWidget_detalhes_lancamento)
            
            #VOLTA MENU DETALHJES LANCAMENTOI:
            if obj == self.paga_fatura_4 and event.type() == QtCore.QEvent.MouseButtonPress:
                effects.Effetc_slides._detalhes_lancamento_slide(self)
                return self.stackedWidget_58.setCurrentWidget(self.stackedWidget_resumo_extrato)
            
            #SE APERTAR DELETE APAGA O O ITEM SELECIONADO DO PDFS PARA LANÇAMENTOS
            if obj == self.listWidget_3 and event.type() == QtCore.QEvent.KeyPress:
                if event.key() == QtCore.Qt.Key_Delete:
                    return self.listWidget_3.takeItem(self.listWidget_3.currentRow()) 

            if obj == self.table_active_banks and event.type() == QtWidgets.QAbstractItemView.SelectRows:
                current_row = self.table_active_banks.currentRow()
                
                id_bank = self.table_active_banks.item(current_row, 0).text()
                id_card = self.table_active_banks.item(current_row, 6).text()
                home_db_fun.Table_Banks_Remove_Update.set_values_frame(self,id_bank,id_card)
                return print(id_bank, id_card)
            if obj == self.update_bank and event.type() == QtCore.QEvent.MouseButtonPress:
                current_row = self.table_active_banks.currentRow()
                id_bank = self.table_active_banks.item(current_row, 0).text()
                id_card = self.table_active_banks.item(current_row, 6).text()
                    
                    
                return home_db_fun.Table_Banks_Remove_Update._update_table_banks(self,id_bank,id_card)
            
            if obj == self.remover_bank and event.type() == QtCore.QEvent.MouseButtonPress:
                current_row = self.table_active_banks.currentRow()
                id_bank = self.table_active_banks.item(current_row, 0).text()
                id_card = self.table_active_banks.item(current_row, 6).text()
                    
                    
                return home_db_fun.Table_Banks_Remove_Update._remove_table_banks(self,id_bank,id_card)
            
            
            return super(MainWindow,self).eventFilter(obj, event)


    def campo_de_verificacao(self):

        usuario = ""
        senha = ""

        def Aparecer_menssagem(mensagem):
            self.pop_error.show()
            self.texto_error.setText(mensagem)

        #TODO CHECA USUARIO AINDA FAZER CONEXAO COM DB
        if not self.enter_user.text():
            usuario = "Usuario nao encontrato"
        else:
            usuario = ""
        #TODO CHECA SENHA 
        if not self.enter_pass.text():
            senha = " Senha nao encontrada"
        else:
            senha = ""
        # checar usuario

        if usuario + senha != '':
            text = usuario + senha
            Aparecer_menssagem(text)

        else:
            
            text = "Bem vindo(a)"
            Aparecer_menssagem(text)

            self.shows()
            a = (os.path.dirname(os.path.realpath(__file__)))
            if (os.path.exists(''+a+'/bando_de_valores.db')):
                card_db_fun.funcoes_cartao.hide_show_logoff(self)
                card_db_fun.funcoes_cartao._start_values(self)
                titulo ='Updates'
                mensagem = 'Procurando Por Atualização'
                try:
                    card_db_fun.funcoes_cartao.group_main(self)
                    
                except:
                    pass
                # home_db_fun.Set_values_startup.set_values_table_bank(self)
                home_db_fun.Group.execs(self)
                self.update()
                show_tray_message(self.ui, tray,titulo,mensagem)
            else:
                self.CONTAINER_geral.hide()
                pyautogui.confirm(text='!!ATENÇÃO!!\nBanco de dados nao foi localizado, Por favor Criar arquivo em MENU>CRIAR BANCO DE DADOS',title='BANCO DE DADOS NAO LOCALIZADO', buttons=['OK', 'Cancel'])
                database.salva_dados.testedb(self)
                
            self.select_card.currentTextChanged.connect(lambda:card_db_fun.funcoes_cartao.style_config_card(self))
            self.comboBox_2.currentTextChanged.connect(lambda:card_db_fun.funcoes_cartao.mudaicondespesa(self))
            self.lineEdit_3.textChanged.connect(lambda:card_db_fun.funcoes_cartao.raname_value(self)) 
            self.lineEdit_2.textChanged.connect(lambda:card_db_fun.funcoes_cartao.raname_date(self)) 
            funcoes.funcoes_geral.data_e_hora(self)
            



        if self.checkBox.isChecked():
            text = text + "  Usuario salvo"
            Aparecer_menssagem(text)

    #TODO APOS CHECK LOGIN, ABRE A MAIN:
    def shows(self):
        self.stackedWidget.setCurrentIndex(1)
        self.stacked_configcartao0.setCurrentIndex(0)
        
    #TODO SE CLICAR EM DESLOGAR
    def desloga(self):
        self.stackedWidget.setCurrentIndex(0)
        self.texto_error.setText("Sistema Deslogado, Até Mais!")



    def filtro_table_header(self, logicalIndex):
        #FUNCAO TEMPORARIO AQUI DPS PARA HOME DB FUN
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


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    #TODO TESTE ANIMCAÇÃO MENU EXPANDIDO
    def toggleMenu(self):
        global TOGLE_STATUS
        STATUS = TOGLE_STATUS
        duration = 500 
        if STATUS == 80:
                
                #TODO ANIMAÇÃO EXPANDINDO
                self.animation = QPropertyAnimation(self.menu, b"minimumWidth")
                self.animation.setDuration(duration)
                self.animation.setStartValue(80)
                self.animation.setEndValue(250)
                self.animation.setEasingCurve(QEasingCurve.OutExpo)
                self.animation.start()
                
                TOGLE_STATUS = 150


        else:  #TODO ANIMAÇÃO RETRAINDO maximumHeight
                self.animation = QPropertyAnimation(self.menu, b"minimumWidth")
                self.animation.setDuration(duration)
                self.animation.setStartValue(250)
                self.animation.setEndValue(80)
                self.animation.setEasingCurve(QEasingCurve.OutExpo)
                self.animation.start()
                TOGLE_STATUS = 80

    def card(self):
        global CARD_SELECTED
        return CARD_SELECTED

    def restore_or_maximize_window(self):
        # variavel global windows tela janela
        global WINDOW_SIZE
        win_status = WINDOW_SIZE
        if win_status == 0:
            WINDOW_SIZE = 1 
            self.showFullScreen() 
            self.extrato_cartao_0.horizontalHeader().setDefaultSectionSize(120)
            self.extrato_cartao_0.verticalHeader().setDefaultSectionSize(40)
            font8 = QFont()
            font8.setFamily(u"Microsoft YaHei")
            font8.setPointSize(12)
            self.extrato_cartao_0.setFont(font8)
            self.extrato_cartao_0.setIconSize(QSize(40, 40))
            self.table_faturas_ind.horizontalHeader().setDefaultSectionSize(255)

        else:
            WINDOW_SIZE = 0
            self.showNormal()
            font8 = QFont()
            font8.setFamily(u"Microsoft YaHei")
            font8.setPointSize(10)
            self.extrato_cartao_0.setFont(font8)
            self.extrato_cartao_0.setIconSize(QSize(35, 35))
            self.extrato_cartao_0.horizontalHeader().setDefaultSectionSize(100)
            self.extrato_cartao_0.verticalHeader().setDefaultSectionSize(40)
            self.table_faturas_ind.horizontalHeader().setDefaultSectionSize(189)

    def mousePressEvent(self, event):
        self.offset = event.pos()

    #MOVE JANELA
    def mouseMoveEvent(self, event):
        try:
            if WINDOW_SIZE == 0:
                x=event.globalX()
                y=event.globalY()
                if self.offset.y() <25:
                    x_w = self.offset.x()
                    y_w = self.offset.y()
                    self.move(x-x_w, y-y_w)
        except:
            pass
    
    def update(self):
        resposta = requests.get('https://raw.githubusercontent.com/xjhowxjhow/HomeAplication1.0/main/version/version.txt')
        with open ('version.txt','wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        

        read = open('version.txt','r')
        acess = read.readlines()
        split = str(acess[0])
        version = split.split()[1]
        # acess[0] = version
        # acess[1 = notes]
        global GLOBAL_VERSION
        act_ver = GLOBAL_VERSION
        if version== act_ver:
            titulo = 'Importante'
            mensagem = 'Nenhuma nova versao encontrada'
            show_tray_message(window_obj, tray,titulo,mensagem)
        else:
            
            titulo = 'Importante'
            mensagem = 'Nova versao encontrada clique para detalhes'
            show_tray_message(window_obj, tray,titulo,mensagem)

    def open_webbrowser(self):
        webbrowser.open('https://github.com/xjhowxjhow')
#######################################################################
def messageClicked(self):
    resposta = requests.get('https://raw.githubusercontent.com/xjhowxjhow/HomeAplication1.0/main/version/version.txt')
    with open ('version.txt','wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)
        
    read = open('version.txt','r')
    acess = read.readlines()
    split = str(acess[0])
    version = split.split()[1]
    global GLOBAL_VERSION
    act_ver = GLOBAL_VERSION
    if version== act_ver:
        pass
    else:
        show_message()

#######################################################################
# SO VAI APARECER SE TIVER ATUALIZAÇÃO
#######################################################################
def show_message():
    resposta = requests.get('https://raw.githubusercontent.com/xjhowxjhow/HomeAplication1.0/main/version/version.txt')
    with open ('version.txt','wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)
        
    read = open('version.txt','r')
    acess = read.readlines()
    split = str(acess[1])
    try:
        resposta = requests.get('https://github.com/xjhowxjhow/HomeAplication1.0/blob/main/version/main.exe?raw=true')
        with open ('HomeAppold.exe','wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
            
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowIcon(QtGui.QIcon(u":/menu/pngwing.com.png)"))
        
            msg.setWindowTitle("Atualização")
            msg.setText("Nova atualização da aplicação foi encontrada, Clique em sair no icone na barra de tarefas para Sair da aplicação E Aplicar nova versao")
            msg.setInformativeText("Clique em hide para saber o que mudou")
            msg.setDetailedText(split)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
            button = msg.clickedButton()
            sb = msg.standardButton(button)
            if sb == QMessageBox.Yes:
                exit()
    except:
        QMessageBox.information(None,
                            "Error",
                            "Falha ao atualizar, por favor, reinicie a aplicação")
    




#######################################################################
# Show tray message when action_tray_message tray action is clicked
#######################################################################
def show_tray_message(self, tray: QSystemTrayIcon,titulo,mensagem):
    notificationTitle = titulo
    notificationMessage =mensagem
    icon = QIcon(u":/icons-cards/src-page-cartoes/urgencia.png")
    duration = 10 * 1000 #3 seconds

    if len(notificationTitle) == 0 or len(notificationMessage) == 0:
        tray.showMessage("Input Something", "Enter your notification tittle and message", icon, duration)
    else:
        tray.showMessage(notificationTitle, notificationMessage, icon, duration)





def exit_handler():
    resposta = requests.get('https://raw.githubusercontent.com/xjhowxjhow/HomeAplication1.0/main/version/version.txt')
    with open ('version.txt','wb') as novo_arquivo:
        novo_arquivo.write(resposta.content)
        
    read = open('version.txt','r')
    acess = read.readlines()
    split = str(acess[0])
    version = split.split()[1]
    global GLOBAL_VERSION
    act_ver = GLOBAL_VERSION
    if version== act_ver:
        pass
    else:
    
        a = (os.path.dirname(os.path.realpath(__file__)))
        if(os.path.exists(''+a+'/update/update.exe')):
            os.startfile(''+a+'/update/update.exe')
            print("sim")
        sys.exit()
    



            
atexit.register(exit_handler)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "System Tray", "System tray was not detected!")
        sys.exit(1)


    app.setQuitOnLastWindowClosed(True)
    tray = QSystemTrayIcon(QIcon(u":/menu/pngwing.com.png"), app)
    menu = QMenu()
    action_hide = QAction("Minimizar Janela")
    menu.addAction(action_hide)

    action_show = QAction("Mostrar Janela")
    menu.addAction(action_show)

    action_exit = QAction("Sair")
    action_exit.triggered.connect(app.exit)
    menu.addAction(action_exit)

    tray.setToolTip("HomeAplication")

    tray.setContextMenu(menu)

    tray.show()
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit()
    