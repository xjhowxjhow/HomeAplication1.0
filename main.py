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
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import card_db_fun
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

WINDOW_SIZE = 0
TOGLE_STATUS = 80
CARD_SELECTED = 0
GLOBAL_VERSION = '1.0'


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    stackSignal = Signal() 
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setupUi(self)
        self.show()
        self.ui = Ui_MainWindow()
        global window_obj
        window_obj = self.ui
        
        
        #NOTIFICAÇÃO SE CLICADA ACTION
        tray.messageClicked.connect(lambda: messageClicked(self))
        action_hide.triggered.connect(lambda: self.hide())
        action_show.triggered.connect(lambda: self.showNormal())
        
        
        
        self.salvar_4.clicked.connect(lambda:self.close())
        self.exit.clicked.connect(lambda: self.close())
        self.minimize.clicked.connect(lambda: self.showMinimized())
        self.maxmize.clicked.connect(lambda: self.restore_or_maximize_window())
        self.pushButton_7.clicked.connect(lambda:self.pop_error.hide())
        self.pop_error.hide()
        self.pop_error_cartao.hide()
        self.frame_31.hide()
        self.buton_login.clicked.connect(self.campo_de_verificacao)
        self.pushButton.clicked.connect(self.toggleMenu)
        self.salvar_6.clicked.connect(lambda:database.salva_dados.testedb(self))
        self.salvar_5.clicked.connect(self.desloga)



        

        self.nova_despesa.clicked.connect(lambda:self.stacked_configcartao0.setCurrentWidget(self.page_new_lancamento))
        effects.Effetc_slides.menu_card(self)
        
        #OCULTA COLUNA ID DE EXTRATO CARTAO
        self.extrato_cartao_0.setColumnHidden(7, True) # COLUNA ID OCULTADA
        self.extrato_cartao_0.setColumnHidden(8, True) # SOMA DATA PARA FILTRO OCULTADA
        self.extrato_cartao_0.setColumnHidden(9, True) # STATUS DO PAGAMENTO PARA FILTRO OCULTADA
        
        self.extrat_meses.setTransitionDirection(QtCore.Qt.Horizontal)
        self.extrat_meses.setTransitionSpeed(500)
        self.extrat_meses.setTransitionEasingCurve(QtCore.QEasingCurve.InOutExpo)
        self.extrat_meses.setSlideTransition(True)
        
        self.grid.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page))
        self.grid_2.clicked.connect(lambda:self.stackedWidget_3.setCurrentWidget(self.page2))
        effects.Effetc_slides.grid_cards(self)
        
        self.add_card_3.clicked.connect(lambda:card_db_fun.funcoes_cartao.adicionar_cartao(self))
        self.remover_card_3.clicked.connect(lambda:card_db_fun.funcoes_cartao.destroy_frame_card(self))
        self.apaga_compra.clicked.connect(lambda:card_db_fun.funcoes_cartao.remove_compra(self))
        self.pushButton_6.clicked.connect(self.open_webbrowser)
        self.pushButton_17.clicked.connect(lambda:card_db_fun.funcoes_cartao.today(self))
       
        

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
                effects.Effetc_slides.grid_filter(self,acao)
                card_db_fun.funcoes_cartao._current_date(self,acao)
                return card_db_fun.Chart_one.clear(self)

            
            if obj == self.next_month and event.type() == QtCore.QEvent.MouseButtonPress:
                acao = "Next"
                effects.Effetc_slides.grid_filter(self,acao)
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
                card_db_fun.funcoes_cartao._filter_year_faturas(self,"Next")
                return card_db_fun.funcoes_cartao._faturas(self)
            


            if obj == self.previus_month_3 and event.type() == QtCore.QEvent.MouseButtonPress:
                #TODO  COMPRAS MENU DIREITO
                card_db_fun.funcoes_cartao._filter_year_faturas(self,"Previus")
                return card_db_fun.funcoes_cartao._faturas(self)
            
            
            if obj == self.paga_fatura and event.type() == QtCore.QEvent.MouseButtonPress:
                #TODO  COMPRAS MENU DIREITO
                card_db_fun.funcoes_cartao._pagar_fatura(self)
                card_db_fun.funcoes_cartao._faturas(self)
                card_db_fun.funcoes_cartao._current_date(self,"none")
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
                btn = "config"
                return effects.Effetc_slides.grid_lateral_menu(self,btn)
            
            
            
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
                show_tray_message(self.ui, tray,titulo,mensagem)
                self.update()
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
        if WINDOW_SIZE == 0:
            x=event.globalX()
            y=event.globalY()
            if self.offset.y() <25:
                x_w = self.offset.x()
                y_w = self.offset.y()
                self.move(x-x_w, y-y_w)

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
    print("ultima funcao")
    
    a = (os.path.dirname(os.path.realpath(__file__)))
    if(os.path.exists(''+a+'/HomeApp.exe')):
        print(a,"ULTIMA FUN dentro do if")
        os.remove('HomeApp.exe')
        old_name = r"HomeAppold.exe"
        new_name = r"HomeApp.exe"
        os.rename(old_name, new_name)
    



            
atexit.register(exit_handler)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    if not QSystemTrayIcon.isSystemTrayAvailable():
        QMessageBox.critical(None, "System Tray", "System tray was not detected!")
        sys.exit(1)


    app.setQuitOnLastWindowClosed(False)

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
    