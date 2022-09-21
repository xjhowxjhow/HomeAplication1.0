from PySide2.QtCore import *
from PySide2 import QtWidgets
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from random import randrange
from threading import Timer
import threading
from login_pyside24 import Ui_MainWindow
from login_pyside24 import *


EXPAND_CARD = 80;
EXPAND_CARD2 = 80;
HIDE_CARDS = 0;


class efeitos_geral(Ui_MainWindow):

    
    def mudacorframes(self):
        a =randrange(255)
        b = randrange(255)
        c = randrange(255)
        d= (a,b,c)
        try:    #todo cor boa :rgb(38, 150, 147)
                #rgb(147, 178, 143)rgb(147, 178, 143)rgb(147, 178, 143) 
                # gradiente u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba"+str(d)+", stop:1 rgba(255, 255, 255, 255));\n"
                self.frame.setStyleSheet(u"background-color:rgb"+str(d)+";\n"
                "	border-radius: 10px;\n"
                "border: 3px solid  rgb(0, 0, 0);")
        #         self.frame_5.setStyleSheet(u"background-color:rgb"+str(d)+";\n"
        
        # "border: 3px solid  rgb(0, 0, 0);")
                self.error.setStyleSheet(u"background-color:rgb"+str(d)+";\n"
                "border-radius: 10px;\n"
        
        "border: 3px solid  rgb(0, 0, 0);")
                self.frame_3.setStyleSheet(u"background-color:rgb"+str(d)+";\n"
        "border-radius: 10px;\n"
        
        "border: 3px solid  rgb(0, 0, 0);")
                self.frame_4.setStyleSheet(u"background-color:rgb"+str(d)+";\n"
        "border-radius: 10px;\n"
        "border: 3px solid  rgb(0, 0, 0);")
        #         self.frame_13.setStyleSheet(u"background-color:rgb"+str(d)+";\n"
        
        # "border: 3px solid  rgb"+str(d)+";")
        #         self.frame_22.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba"+str(d)+", stop:1 rgba(255, 255, 255, 255));\n"
        
        # "border: 3px solid  rgb"+str(d)+";")
        except ValueError:
                pass
    
#TODO EFFECTS PAGINA CARTOES

    def expandecomprascartao(self):

        duration = 1150
        global EXPAND_CARD
        
        if EXPAND_CARD == 80:
                # self.frame_31.show()

                
                self.expandemenucartaocompras0 = QPropertyAnimation(self.CONTAINER_geral, b"minimumHeight")
                self.expandemenucartaocompras0.setDuration(duration)
                self.expandemenucartaocompras0.setStartValue(200)
                # selexpandemenucartaocompras0_cartao1_config.show()
                self.expandemenucartaocompras0.setEndValue(800)
                self.expandemenucartaocompras0.setEasingCurve(QEasingCurve.OutExpo)
                self.expandemenucartaocompras0.start()
                
                self.frame_31.show()
                self.submenuanim = QPropertyAnimation(self.frame_31, b"maximumHeight")
                self.submenuanim.setDuration(duration)
                self.submenuanim.setStartValue(0)
                self.submenuanim.setEndValue(800)
                self.submenuanim.setEasingCurve(QEasingCurve.OutExpo)
                self.submenuanim.start()

    def style_sheet_card_(self):
        import card_db_fun
        from login_pyside24 import Ui_MainWindow
        
        
        card_select = card_db_fun.funcoes_cartao.retorna_style_card()
        
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

    def txt_progess_circular(self):
        def thead(self):
            import card_db_fun
            card_select = card_db_fun.funcoes_cartao.retorna_style_card()

            if card_select == 'C6':
                cirlular_progess =self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#9b9bff;\">C6</span></p></body></html>", None))
                return cirlular_progess
            if card_select == 'NUBANK':                                     
                cirlular_progess =self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#9b9bff;\">Nubank</span></p></body></html>", None))
                return cirlular_progess
            if card_select == 'BTG':
                cirlular_progess =self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#9b9bff;\">BTG</span></p></body></html>", None))
                return cirlular_progess
            if card_select == 'SANTANDER':
                cirlular_progess =self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#9b9bff;\">Santander</span></p></body></html>", None))
                return cirlular_progess
            if card_select == 'ITAU':
                cirlular_progess =self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#9b9bff;\">Itau</span></p></body></html>", None))
                return cirlular_progess
            if card_select == 'BRADESCO':
                cirlular_progess =self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#9b9bff;\">Bradesco</span></p></body></html>", None))
                return cirlular_progess
            if card_select == 'CAIXA ECONOMICA':
                cirlular_progess =self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#9b9bff;\">Caixa</span></p></body></html>", None))
                return cirlular_progess
        thread = threading.Thread(target=thead(self))
        thread.start()
        
    def style_sheet_config(self,id):
        
        import card_db_fun

        if id == 'C6':
            hover ="rgb(255, 255, 255)"
            main ="qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(16, 16, 16, 255), stop:0.482307 rgba(50, 50, 50, 255), stop:0.996068 rgba(16, 16, 16, 255), stop:1 rgba(0, 0, 0, 255))"
            icon = "url(:/menu/c6.jpg)"
            return [main,hover,icon]
        if id == 'NUBANK':   
            hover ="rgb(93, 7, 150)"
            main ="rgb(130, 10, 209)"
            icon = "url(:/menu/nu-icon.png)"
            return [main,hover,icon]
        if id == 'BTG':
            hover ="rgb(93, 7, 150)"
            main ="qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0052356 rgba(8, 28, 43, 255), stop:0.434555 rgba(19, 51, 71, 255), stop:0.825916 rgba(29, 72, 98, 255));"
            icon = "url(:/menu/btg-icon.png)"
            return [main,hover,icon]
        if id == 'SANTANDER':
            hover ="rgb(55, 55, 55)"
            main ="qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0052356 rgba(242, 0, 0, 255), stop:0.434555 rgba(217, 43, 0, 255), stop:0.825916 rgba(152, 50, 0, 255))"
            icon = "url(:/menu/santander-icon.png)"
            return [main,hover,icon]
        if id == 'ITAU':
            hover ="rgb(0, 48, 145)"
            main ="qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0052356 rgba(242, 104, 1, 255), stop:0.434555 rgba(255, 126, 1, 255), stop:0.825916 rgba(255, 159, 0, 255));"
            icon = "url(:/menu/itau-icon.png)"
            return [main,hover,icon]
        if id == 'BRADESCO':
            hover ="rgb(242, 0, 0)"
            main ="qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0052356 rgba(170, 29, 113, 255), stop:0.434555 rgba(204, 16, 91, 255), stop:0.825916 rgba(235, 5, 65, 255))"
            icon = "url(:/menu/bradesco-icon.png)"
            return [main,hover,icon]
        if id == 'CAIXA ECONOMICA':
            hover ="rgb(248, 162, 61)"
            main ="rgb(0, 106, 166)"
            icon = "url(:/menu/caixa-icon.png)"
            return [main,hover,icon]
        
    def style_sheet_main_cards(self):
        
        list =[]
        list2=[]

        a =randrange(255)
        b = randrange(255)
        c = randrange(255)
        list.append(str('(%s,%s,%s)'%(a,b,c)))

        a =randrange(255)
        b = randrange(255)
        c = randrange(255)


        list2.append(str('(%s,%s,%s)'%(a,b,c)))
        #TODO TOP ESSE THEMA:
        # Insira o rgb para o menu ateral:rgb(40, 48, 70)
        # Insira o rgb para o fundo:rgb(22, 29, 49)
        # Insira o rgb para os detahes:rgb(39, 51, 87)
        
        #TODO AZUL CLARO:
        # Insira o rgb para o menu ateral:rgb(82, 151, 236)
        # Insira o rgb para o fundo:rgb(64, 118, 185)
        # Insira o rgb para os detahes:rgb(46, 85, 133)
        self.stackedWidget_2.setStyleSheet(u"background-color:rgb"+str(list[0])+";\n"
        "border-radius: 10px;")
        
        self.CONTAINER_geral.setStyleSheet(u"QFrame{\n"
        "background-color:rgb"+str(list2[0])+";\n"
        "	border-radius: 10px;\n"
        "	border-bottom: 0px solid rgb(45, 45, 68);\n"
        "	border-right: 0px solid rgb(45, 45, 68);\n"
        "\n"
        "}")


        self.menu.setStyleSheet(u"background-color:rgb"+str(list2[0])+";\n"
        "border-top-right-radius:0px;\n"
        "border-bottom-right-radius:0px;\n"
        "\n"
        "")
    def style_sheet_card_icon(self,nome_cartao):

        card_select = nome_cartao
        
        if card_select == 'C6':
            icon = "url(:/menu/c6.jpg)"
            return icon

        if card_select == 'NUBANK':   
            icon = "url(:/menu/nu-icon.png)"
            return icon

        
        if card_select == 'BTG':
            icon = "url(:/menu/btg-icon.png)"
            return icon

        
        if card_select == 'SANTANDER':
            icon = "url(:/menu/santander-icon.png)"
            return icon

        
        if card_select == 'ITAU':
            icon = "url(:/menu/itau-icon.png)"
            return icon

        
        if card_select == 'BRADESCO':
            icon = "url(:/menu/bradesco-icon.png)"
            return icon


        if card_select == 'CAIXA ECONOMICA':
            icon = "url(:/menu/caixa-icon.png)"

            return icon

class Effetc_slides(Ui_MainWindow):
    def menu_card(self): #TODO TRANSICAO PRINCIPAL MAIN
        self.stacked_configcartao0.setTransitionDirection(QtCore.Qt.Horizontal)
        self.stacked_configcartao0.setTransitionSpeed(250)
        self.stacked_configcartao0.setTransitionEasingCurve(QtCore.QEasingCurve.OutExpo)
        self.stacked_configcartao0.setSlideTransition(True)
        
    def grid_cards(self):
        self.stackedWidget_3.setTransitionDirection(QtCore.Qt.Horizontal)
        self.stackedWidget_3.setTransitionSpeed(250)
        self.stackedWidget_3.setTransitionEasingCurve(QtCore.QEasingCurve.InExpo)
        self.stackedWidget_3.setSlideTransition(True)
    
    def _conent_geral_cards(self):
        self.detalhes_cartao.setTransitionDirection(QtCore.Qt.Horizontal)
        self.detalhes_cartao.setTransitionSpeed(250)
        self.detalhes_cartao.setTransitionEasingCurve(QtCore.QEasingCurve.InExpo)
        self.detalhes_cartao.setSlideTransition(True)

    def grid_lateral_menu(self,botao):
        
        btn = botao
        duration = 50 #duração animação
        geometry = 0
        if btn == "conta":
            self.stackedWidget_2.setCurrentWidget(self.page_1)       
            geometry = 60
        if btn == "investimento":
            self.stackedWidget_2.setCurrentWidget(self.page_4)
            geometry = 120
        if btn == "cartao":
            self.stackedWidget_2.setCurrentWidget(self.page_3)
            geometry = 180
        if btn == "transferencia":
            self.stackedWidget_2.setCurrentWidget(self.page_5)
            geometry = 240
        if btn == "estoque":
            self.stackedWidget_2.setCurrentWidget(self.page_6)
            geometry = 300
        if btn == "config" :
            self.stackedWidget_2.setCurrentWidget(self.page_6)
            geometry = 360


            
        self.stackedWidget_2.setTransitionDirection(QtCore.Qt.Horizontal)
        self.stackedWidget_2.setTransitionSpeed(350)
        self.stackedWidget_2.setTransitionEasingCurve(QtCore.QEasingCurve.OutExpo)
        self.stackedWidget_2.setSlideTransition(True)
        
        self.animA = QPropertyAnimation(self.animcurretnpage, b"geometry")
        self.animA.setDuration(duration)
        self.animA.setStartValue(QRect(self.animcurretnpage.geometry()))
        self.animA.setEndValue(QRect(0, geometry, 4, 60))
        self.animA.start()
        
    
    
    def grid_filter(self,direction,object):
        btn = direction
        duration = 600 #duração animação
        geometry = 0
        
        withs = self.extrat_meses.frameGeometry().width()
        if btn == "Next":
            self.animation = QPropertyAnimation(object, b"maximumWidth")
            self.animation.setDuration(duration)
            self.animation.setStartValue(0)
            self.animation.setEndValue(withs)
            self.animation.setEasingCurve(QEasingCurve.OutExpo)
            self.animation.start()
            
  
        if btn == "Previus":
            self.animation = QPropertyAnimation(object, b"maximumWidth")
            self.animation.setDuration(duration)
            self.animation.setStartValue(0)
            self.animation.setEndValue(withs)
            self.animation.setEasingCurve(QEasingCurve.OutExpo)
            self.animation.start()
        
        
        
    def grid_not_found(self):
        self.stack_extrato_pages.setTransitionDirection(QtCore.Qt.Vertical)
        self.stack_extrato_pages.setTransitionSpeed(200)
        self.stack_extrato_pages.setTransitionEasingCurve(QtCore.QEasingCurve.OutExpo)
        self.stack_extrato_pages.setSlideTransition(True)
        
        
    
    def _hide_group_cards(self):

        duration = 600 #duração animação
        geometry = 0
        object = self.content_cartao
        global HIDE_CARDS
        
        
        if HIDE_CARDS == 1:
            self.animation = QPropertyAnimation(object, b"maximumWidth")
            self.animation.setDuration(duration)
            self.animation.setStartValue(0)
            self.animation.setEndValue(440)
            self.animation.setEasingCurve(QEasingCurve.OutExpo)
            self.animation.start()
            HIDE_CARDS = 0
            icon = QIcon()
            icon.addFile(u":/backgroud/src-page-cartoes/back.png", QSize(), QIcon.Normal, QIcon.Off)
            self.hide_cards_main.setIcon(icon)
            self.hide_cards_det.setIcon(icon)

            
  
        else:
            self.animation = QPropertyAnimation(object, b"maximumWidth")
            self.animation.setDuration(duration)
            self.animation.setStartValue(440)
            self.animation.setEndValue(0)
            self.animation.setEasingCurve(QEasingCurve.OutExpo)
            self.animation.start()
            HIDE_CARDS = 1
            icon14 = QIcon()
            icon14.addFile(u":/backgroud/src-page-cartoes/next.png", QSize(), QIcon.Normal, QIcon.Off)
            self.hide_cards_main.setIcon(icon14)
            self.hide_cards_det.setIcon(icon14)

    def _icon_main(self,id):
    
        if id == 'C6':
            icon = "url(:/menu/c6.jpg)"
            return icon
        if id == 'NUBANK':   
            icon = "url(:/menu/nu-icon.png)"
            return icon
        if id == 'BTG':
            icon = "url(:/menu/btg-icon.png)"
            return icon
        if id == 'SANTANDER':
            icon = "url(:/menu/santander-icon.png)"
            return icon
        if id == 'ITAU':
            icon = "url(:/menu/itau-icon.png)"
            return icon
        if id == 'BRADESCO':
            icon = "url(:/menu/bradesco-icon.png)"
            return icon
        if id == 'CAIXA ECONOMICA':
            icon = "url(:/menu/caixa-icon.png)"
            return icon

    def _icon_main_pacth(self,id):
    
        if id == 'C6':
            icon = ":/menu/c6.jpg"
            return icon
        if id == 'NUBANK':   
            icon = ":/menu/nu-icon.png"
            return icon
        if id == 'BTG':
            icon = ":/menu/btg-icon.png"
            return icon
        if id == 'SANTANDER':
            icon = ":/menu/santander-icon.png"
            return icon
        if id == 'ITAU':
            icon = ":/menu/itau-icon.png"
            return icon
        if id == 'BRADESCO':
            icon = ":/menu/bradesco-icon.png"
            return icon
        if id == 'CAIXA ECONOMICA':
            icon = ":/menu/caixa-icon.png"
            return icon
