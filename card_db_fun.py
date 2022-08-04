
import sqlite3
import pyautogui
import os.path
import effects
import os 
import re
import threading
import card_db_test
import calendar
import locale
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



GLOBAL_SELECT_CARD_ADD = 0; 
NUMERO_DE_CARTOES = NULL;
CARD_SELECTED = 0; 
EXTRATO_ATUAL = 0; 



class funcoes_cartao(Ui_MainWindow):    


    def _start_values(self): 
        def thead():

            
            indexdb= 0
            list = []
            self.frames = self.verticalLayout_3
            for i in range(self.frames.count()):
                a = self.frames.itemAt(i).widget().objectName()
                index = re.sub('[^0-9]', '', a)
                list.append(index)
                indexdb = indexdb +1
                


            
            # MES PARA FILTRO FATURA ATUAL:
            mes = funcoes_cartao._mes(self)
            
            
            for i in range(indexdb): 

                #CAPTURA VALOR DAS COMPRAS TOTAL   
                listdb= list[i]


                #LIMITE UTILIZADO :
                limite_utilizado = card_db_test.Return_Values_Calcs._limite_utilizado(listdb)
                self.labelTitle_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#5c9bcf;\">Limite Utilizado:</span></p><p><span style=\" font-size:11pt; font-weight:600; color:#5c9bcf;\">R$"+str(limite_utilizado)+"</span></p></body></html>", None))


                #LIMITE DISPONIVEL 

                limite_disponivel= card_db_test.Return_Values_Calcs._limite_disponivel(listdb)
                self.labelTitle_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#00aa00;\">Limite Disponivel</span></p><p><span style=\" font-size:11pt; font-weight:600; color:#00aa00;\">R$"+str(limite_disponivel)+"</span></p></body></html>", None))
                
                
                for val in range (2):
                    
                    #SETA FATURA CARTAO E LIMITE DISPONIVEL
                    card_info = ['valor_faturaatual_cartao_','valor_limitedisponivel_cartao_']
                    fatura_atual = card_db_test.Return_Values_Calcs._fatural_atual(listdb,mes)
                    limite_disponivel= card_db_test.Return_Values_Calcs._limite_disponivel(listdb)

                    text = [(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff\">R$"+str(fatura_atual)+"</span></p></body></html>", None)),
                            (QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-weight:600; color:#ffffff;\">R$"+str(limite_disponivel)+"</span></p></body></html>", None))]
                    self.botoes = self.findChildren(QLabel , str(card_info[val]+list[i]))
                    

                    self.botoes[0].setText(text[val])
                    
                try:
                    
                    #SETA FINAL DO CARTAO
                    
                    final_cartao = card_db_test.Ui_db._final_cartao(listdb)
                    card_info = 'txt_final_cartao_'
                    text_fimal = (QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">XXXX-XXXX-XXXX-"+str(final_cartao)+"</span></p></body></html>", None))                
                    self.botoes = self.findChildren(QLabel , str(card_info+list[i]))
                    self.botoes[0].setText(text_fimal)
                
                except:
                    pass

                try:
                    
                    #SETA TITULAR DO CARTAO
        
                    titular_cartao = card_db_test.Ui_db._titular(listdb)
                    card_info = 'txt_titular_cartao_'
                    text_fimal = (QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">"+str(titular_cartao)+"</span></p></body></html>", None))
                    self.botoes = self.findChildren(QLabel , str(card_info+list[i]))
                    self.botoes[0].setText(text_fimal)

                except:
                    pass
                
                
                
                
        thread = threading.Thread(target=thead)
        thread.start()


    def _addRow(self): #TODO ADICIONA NOVA LINHA NO EXTRATO CARTAO #NTS
        def thead(self):
            label_0 = self.lineEdit.text() # nome str
            label_2 = self.lineEdit_2.text() # data str
            label_3_ui = self.lineEdit_3.text() #valor int


            #VALIDADOR DE CARACTERES
            
            if (label_0== '') and (label_2== '')  and (label_3_ui== '') :
                pyautogui.confirm(text='Não foi preenchido os campos: \nNome, Valor e Data de transação ', title='Lançamento incorreto!', buttons=['OK', 'Cancel'])
           
            elif (label_0== '') or (label_2== '')  or (label_3_ui== '') :
                pyautogui.confirm(text='Esta faltando campos: \nNome, Valor ou Data esta em branco! ', title='Lançamento incorreto!', buttons=['OK', 'Cancel'])
                
            elif bool(re.search(r'\d', str(label_3_ui))) == False:
                pyautogui.confirm(text='Valor invalido', title='Invalido!', buttons=['OK', 'Cancel'])
            
            else:
                
                PARCELADO = False
                
                parcelas = str(self.comboBox_3.currentText())
                label_3 = funcoes_cartao._brl_to_usd(label_3_ui)
                #PARCELADO:
                
                if parcelas == "Avista":
                    PARCELADO = False
                    parcelas = 1
                else:
                    valor_transacao = float(label_3)/float(parcelas)
                    resultado_float=("{:.2f}".format(float(valor_transacao)))
                    PARCELADO = True
                    
                #DATA:
                

                data_transacao = self.lineEdit_2.text() # para soma e filtro
                data_transacao_original = self.lineEdit_2.text() # para ui
                bug_fix = 0
                index_parcelas = 0
                
                
                data_transacao_original = funcoes_cartao._data_br_to_eng(self,data_transacao_original)
                data_transacao = funcoes_cartao._data_br_to_eng(self,data_transacao)
                
                
                
                
                rand_id = randint(0, 999999) # ID DA COMPRA
                
                
                for i in range(int(parcelas)):
                    
                    soma_data = data_transacao

                    

                    data_e_hora_em_texto = soma_data
                    format_date = datetime.strptime(data_e_hora_em_texto, '%Y-%m-%d')
                    date = format_date.date()
                    soma_mes = relativedelta(months=+1)
                    ab= date + soma_mes
                    data_transacao = str(ab)
                    soma_data =str(ab)

                        
                    rowPosition = self.extrato_cartao_0.rowCount()
                    self.extrato_cartao_0.insertRow(rowPosition)
                    
                    #TODO CAPTURA NOVO LANÇAMENTO E SETA NOVA LINHA
                    categoria_transacao = str(self.comboBox_2.currentText())
                    nome_transacao = self.lineEdit.text()
                    operacao = str(self.comboBox_4.currentText())
                    parcelas = str(self.comboBox_3.currentText())
                    stats_payment = 'pendente'
                    
                    if PARCELADO == False:
                        
                        valor = label_3
                        qt_parcel = 'Avista'
                    else:
                        
                        valor =resultado_float
                        index_parcelas = index_parcelas +1 
                        qt_parcel = str("%s/%s"%(index_parcelas,parcelas))
                         
        
                    self.extrato_cartao_0.setItem(rowPosition , 1, QtWidgets.QTableWidgetItem(categoria_transacao))
                    self.extrato_cartao_0.setItem(rowPosition , 2, QtWidgets.QTableWidgetItem(nome_transacao))
                    self.extrato_cartao_0.setItem(rowPosition , 3, QtWidgets.QTableWidgetItem(data_transacao_original)) # data original para ui
                    self.extrato_cartao_0.setItem(rowPosition , 4, QtWidgets.QTableWidgetItem(operacao))
                    self.extrato_cartao_0.setItem(rowPosition , 5, QtWidgets.QTableWidgetItem(str(qt_parcel)))
                    self.extrato_cartao_0.setItem(rowPosition , 6, QtWidgets.QTableWidgetItem(str(valor)))
                    self.extrato_cartao_0.setItem(rowPosition , 7, QtWidgets.QTableWidgetItem(str(rand_id)))
                    self.extrato_cartao_0.setItem(rowPosition , 8, QtWidgets.QTableWidgetItem(soma_data)) # data somada para filtros
                    self.extrato_cartao_0.setItem(rowPosition , 9, QtWidgets.QTableWidgetItem(stats_payment))
                    
                    
                    

                    # TODO COPIA DE FUNÇÃO SALVA EXTRATO
                    global EXTRATO_ATUAL
                    card = EXTRATO_ATUAL
                    
                    iddb = 'extrato_cartao_%s (id)'%(card)
                    db = 'extrato_cartao_%s'%(card)
                    idexdb = 'ids_transation_%s'%(card)
                    
                    a = (os.path.dirname(os.path.realpath(__file__)))
                    banco = sqlite3.connect(''+a+'/bando_de_valores.db')
                    cursor = banco.cursor()
                    #finaliza busca
                    rowPosition = self.extrato_cartao_0.rowCount()
                    
                    
                    
                    
                    # cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS "+idexdb+" ON "+iddb+"")
                    
                    
                    rowPosition2 = self.extrato_cartao_0.rowCount()
                    rowPosition2 = rowPosition2-1
                    list= []
                    # colunasdb =['categoria_transacao','nome_transacao','data_transacao','operacao','parcelas','valor_transacao']
                    for col in range(9):
                        fix = col+1
                        captura_valroes_linha = self.extrato_cartao_0.item(rowPosition2,fix).text()
                        list.append(captura_valroes_linha)
                        # cursor.execute("UPDATE "+db+" SET '"+str(colunasdb[col])+"' =  '"+str(captura_valroes_linha)+"'  WHERE id = '"+str(sla)+"'")
                    
                    cursor.execute("INSERT INTO  "+db+" (categoria_transacao, nome_transacao, data_transacao, operacao, parcelas, valor_transacao, id, data_filter,status_payment) VALUES ('"+str(list[0])+"','"+str(list[1])+"','"+str(list[2])+"','"+str(list[3])+"','"+str(list[4])+"','"+str(list[5])+"','"+str(list[6])+"','"+str(list[7])+"','"+str(list[8])+"')")
                    banco.commit()


                self.stacked_configcartao0.setCurrentWidget(self.page_extrato)
                today = datetime.today().strftime('%m%Y')
                
                funcoes_cartao.carrega_extrato_mes(self,str(today))
                funcoes_cartao._Values_Individual(self)
                funcoes_cartao.icontable_extrato(self)

                try:
                    self.grafico_categoria.setParent(None)
                except:
                    pass
            

        thread = threading.Thread(target=thead(self))
        thread.start()


    def icontable_extrato(self): # TODO MUDA ICONES QTABLEWIDGET
        def theard():
                try:                
                    rowPosition = self.extrato_cartao_0.rowCount()
                    #TODO 16 CATEGORIAS
                    list = ["delivery","appstrans","comida","mercado","lazer","icons8-casa-96","inuteis","servicos","streaming","urgencia","gatos","dogs","medico","viagem","eletronico","domesticos"]
                    icones=["Delivery",
                            "Apps Transporte",
                            "Comida",
                            "Mercado",
                            "Lazer",
                            "Casa",
                            "Coisas Inuteis",
                            "Serviços",
                            "Streaming",
                            "Urgencia",
                            "Gatos",
                            "Dogs",
                            "Medico",
                            "Viagem",
                            "Eletronicos",
                            "Domesticos"]
                    for row in range (rowPosition):
                        for seticon in range (16):
                            if self.extrato_cartao_0.item(row,1).text()  == icones[seticon]:
                                icone = QIcon()
                                icone.addFile(u":/icons-cards/src-page-cartoes/"+list[seticon]+".png", QSize(), QIcon.Normal, QIcon.Off)
                                __qtablewidgetitem7900 = QtWidgets.QTableWidgetItem()
                                __qtablewidgetitem7900.setIcon(icone)
                                self.extrato_cartao_0.setItem(row, 0, QtWidgets.QTableWidgetItem(__qtablewidgetitem7900))
                except:
                    pass
                    

        thread = threading.Thread(target=theard)
        thread.start()


    def hide_show_container(self):
        def thead(self):
            list = []


            self.frames = self.verticalLayout_3

            for i in range(self.frames.count()):
                a = self.frames.itemAt(i).widget().objectName()
                list.append(a)
            count = len(list)
            if count ==0:
                self.CONTAINER_geral.hide()
            else:
                self.CONTAINER_geral.show()
            
        thread = threading.Thread(target=thead(self))
        thread.start()


    def hide_show_logoff(self): #T
        def thead(self):
            list = []


            self.frames = self.verticalLayout_3

            for i in range(self.frames.count()):
                a = self.frames.itemAt(i).widget().objectName()
                list.append(a)
            count = len(list)
            if count ==0:
                funcoes_cartao.inicia_cartoes_oculto_se_nao_existir(self)
            else:
                pass
        thread = threading.Thread(target=thead(self))
        thread.start()
    
    
    def inicia_cartoes_oculto_se_nao_existir(self): #T
        def thead(self):
                
            #todo Ao iniciar pegar o id do db 



            a = (os.path.dirname(os.path.realpath(__file__)))
            banco = sqlite3.connect(''+a+'/bando_de_valores.db')




            #TODO PEGA NOME
            cursor = banco.cursor()
            cursor.execute("SELECT nome_cartao FROM  card_active")
            dadoslidos = cursor.fetchall()

            lista = []
            id_list = []

            index: int = 0


            for i in dadoslidos:
                lista.append(dadoslidos[index][0])

                index = index +1


            index3: int = 0
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM card_active")
            dadoslidos3 = cursor.fetchall()

            funcoes_cartao.hide_show_container(self)

            for i in  dadoslidos:
                id_list.append(dadoslidos3[index3])
                index3 = index3 +1


            cartoes = lista

            index2: int = NULL

            for card in cartoes:

                if card in lista:
                    global GLOBAL_SELECT_CARD_ADD

                    GLOBAL_SELECT_CARD_ADD = card
                    funcoes_cartao.creat_new_widget(self,id_list[index2][0])



                else:
                    pass
                index2 = index2 +1

            funcoes_cartao.hide_show_container(self)
            #TODO SUBFUNÇÃO CARREGA DADOS PARA PAGINA 2
            try:

                

                a = (os.path.dirname(os.path.realpath(__file__)))            
                banco = sqlite3.connect(''+a+'/bando_de_valores.db')


                cursor = banco.cursor()
                cursor.execute("SELECT id FROM card_active") 
                dadoslidos = cursor.fetchall()


                nome_col = ["nome_cartao","titular","limite","final","vencimento"]


                index: int = 0
                for linha in dadoslidos:


                    rowPosition = self.table_active_cards.rowCount()
                    self.table_active_cards.insertRow(rowPosition)
                    

                    lista = []
                    for col in range(0,5):
                        cursor = banco.cursor()
                        cursor.execute("SELECT "+str(nome_col[col])+" FROM card_active")
                        dadoslidos2 = cursor.fetchall()
                        lista.append(dadoslidos2[index][0])
                        self.table_active_cards.setItem(index, col, QtWidgets.QTableWidgetItem(str(dadoslidos2[index][0]))) 

                    index = index+1
            except:
                pass
        thread = threading.Thread(target=thead(self))
        thread.start()


    def destroy_frame_card(self): #NA PAG2 de config, ao remover um card, REMOVE DO DB, E REMOVE FRAME PAG 1 #T
        def thead(self):
            linha_selecionada = self.table_active_cards.currentRow() 
            if linha_selecionada >=0:
                alert = pyautogui.confirm(text='Tem certeza que deseja remover este cartão?\nAo remover, todos os dados serão perdidos\nDeseja prossegur?', title='Importante!', buttons=['OK', 'Cancel'])
                #try

                if alert == "OK":

                    self.table_active_cards.removeRow(linha_selecionada)

                    lista_ids_active = []

                    a = (os.path.dirname(os.path.realpath(__file__)))
                    banco = sqlite3.connect(''+a+'/bando_de_valores.db')
                    cursor = banco.cursor()

                    cursor.execute("SELECT * FROM card_active")
                    dadoslidos = cursor.fetchall()
                    inde = 0
                    for i in  dadoslidos:
                        lista_ids_active.append(dadoslidos[inde])
                        inde = inde +1
                    rowcount = self.table_active_cards.rowCount()

                    a = (os.path.dirname(os.path.realpath(__file__)))
                    banco = sqlite3.connect(''+a+'/bando_de_valores.db')
                    cursor = banco.cursor()
                    cursor.execute("DELETE FROM card_active   WHERE id = "+str(lista_ids_active[linha_selecionada][0])+"")

                    card_delet = lista_ids_active[linha_selecionada][0]

                    #PEGAR O ID DA LINHA SELECIONADA AQUI NOVA FUNÇAO

                    iddb = 'extrato_cartao_%s'%(card_delet)
                    idexdb = 'ids_transation_%s'%(card_delet)
                    idex2 = 'index_cartao_%s'%(card_delet)

                    #TODO 18/06/2022 GERE
                    cursor.execute("DROP TABLE IF EXISTS "+str(iddb)+"")
                    cursor.execute("DROP INDEX IF EXISTS "+str(idexdb)+"")
                    cursor.execute("DROP INDEX IF EXISTS "+str(idex2)+"")

                    #apaga extrato e tudo do db



                    #apagar widget

                    list = []

                    self.frames = self.verticalLayout_3

                    for i in range(self.frames.count()):
                        a = self.frames.itemAt(i).widget().objectName()
                        list.append(a)


                    self.frame_remove = self.findChildren(QStackedWidget , str(list[linha_selecionada]))
                    self.frame_remove[0].deleteLater()
                    list.pop(linha_selecionada)




                    banco.commit()
                    banco.close()
                    global NUMERO_DE_CARTOES
                    NUMERO_DE_CARTOES = NUMERO_DE_CARTOES -1

                else:
                    pass
            else:
                pyautogui.confirm(text='Nenhum cartão localizado ou Selecionado', title='Alerta', buttons=['OK'])
                pass
        thread = threading.Thread(target=thead(self))
        thread.start()


    def mudaicondespesa(self): #NT
        list = ["nulsmal","delivery","appstrans","comida","mercado","lazer","icons8-casa-96","inuteis","servicos","streaming","urgencia","gatos","dogs","medico","viagem","eletronico","domesticos"]
        contents = self.comboBox_2.currentIndex()
        self.frame_68.setStyleSheet(u"border-image: url(:/icons-cards/src-page-cartoes/"+list[contents]+".png);\n"
        "\n"
        "\n"
        "background-position: center;\n"
        "\n"
        "background-repeat:no-repeat;")


    def adicionar_cartao(self): #T
        def thead(self):
            #TODO INICIO 0.4
            #todo vai chamar a funcao cartao ativos agopra 15/06
            label_0 = self.lineEdit.text() # nome str
            label_2 = self.lineEdit_2.text() # data str
            label_3_ui = self.lineEdit_3.text() #valor int


            #VALIDADOR DE CARACTERES
            titular = self.adctitular.text()
            limite = self.adclimite.text()
            final = self.adcfinal.text()
            vencimento = self.adcvencimento.text()
            
            if (titular== '') and (limite== '')  and (final== '') and (vencimento== ''):
                pyautogui.confirm(text='Não foi preenchido os campos: Titular, Limite, Final do cartao e Vencimento ', title='Lançamento incorreto!', buttons=['OK', 'Cancel'])
           
            elif (titular== '') or (limite== '')  or (final== '') or (vencimento== '') :
                pyautogui.confirm(text='Esta faltando campos: \nTitular, Limite, Final do cartao ou Vencimento esta em branco! ', title='Lançamento incorreto!', buttons=['OK', 'Cancel'])
                
            elif bool(re.search(r'\d', str(limite))) == False:
                pyautogui.confirm(text='Valor de limite invalido', title='Invalido!', buttons=['OK', 'Cancel'])

            elif bool(re.search(r'\d', str(final))) == False:
                pyautogui.confirm(text='Final de cartao invalido', title='Invalido!', buttons=['OK', 'Cancel'])
                
            elif bool(re.search(r'\d', str(vencimento))) == False:
                pyautogui.confirm(text='Vencimento de cartao invalido', title='Invalido!', buttons=['OK', 'Cancel'])
                
            elif int(vencimento) > 31 :
                pyautogui.confirm(text='Vencimento de cartao invalido data acima de 31', title='Invalido!', buttons=['OK', 'Cancel'])
    
            elif int(vencimento) < 0 :
                pyautogui.confirm(text='Vencimento de cartao invalido data invalida', title='Invalido!', buttons=['OK', 'Cancel'])
            
            else:
            
                rowPosition = self.table_active_cards.rowCount()
                self.table_active_cards.insertRow(rowPosition)
                colunas = self.table_active_cards.columnCount()
                cartao_selected = self.select_card.currentText()

                for i in range(colunas):

                    labels = [self.select_card.currentText(),self.adctitular.text(),self.adclimite.text(),self.adcfinal.text(),self.adcvencimento.text()]

                    self.table_active_cards.setItem(rowPosition , i, QtWidgets.QTableWidgetItem(labels[i]))

                    #TODO AGORA VAI SALVAR NO DB
                # try:



                a = (os.path.dirname(os.path.realpath(__file__)))
                banco = sqlite3.connect(''+a+'/bando_de_valores.db')
                cursor = banco.cursor()

                #finaliza busca
                rowPosition = self.table_active_cards.rowCount()-1


                cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_card_active ON card_active(id)")
                #AQUI CRIA O ID DE ACORDO COM A QUANTIDADE DE CARTOES


                rand_id = randint(0, 999999) 



                #TODO aqui agr vai criar um id aletaorio de 4 digitos
                cursor.execute("INSERT INTO  card_active (id) VALUES ('"+str(rand_id)+"')")


                #todo parei aqui 15/06
                colunas = self.table_active_cards.columnCount()
                for i in range(colunas):
                    nome_col = [ "nome_cartao", "titular", "limite","final","vencimento"]

                    cardsrow= self.table_active_cards.item(rowPosition,i).text()
                    # cursor.execute("UPDATE card_active SET nome_cartao = '"+str()+"' WHERE id = '"+str(sla)+"'")
                    cursor.execute("UPDATE card_active SET "+str(nome_col[i])+" = '"+str(cardsrow)+"' WHERE id = '"+str(rand_id)+"'")
                    banco.commit()
                #TODO INICIO 0.3
                rowPosition = self.table_active_cards.rowCount()
                try:
                    a = (os.path.dirname(os.path.realpath(__file__)))            
                    banco = sqlite3.connect(''+a+'/bando_de_valores.db')
                    cursor = banco.cursor()
                    cursor.execute("CREATE TABLE IF NOT EXISTS extrato_cartao_"+str(rand_id)+" (nome_cartao text, categoria_transacao text, nome_transacao text, data_transacao date, operacao text, parcelas text, valor_transacao text, id text,data_filter text,status_payment)")
                except:
                    pass

                variaveasdsa = 0
                id = rand_id


                global GLOBAL_SELECT_CARD_ADD
                GLOBAL_SELECT_CARD_ADD = cartao_selected

                global NUMERO_DE_CARTOES
                NUMERO_DE_CARTOES = NUMERO_DE_CARTOES +1





                #TODO NOVAS ADICOES DE LOOP 21/06
                funcoes_cartao.creat_new_widget(self,id)
                funcoes_cartao.hide_show_container(self)

                try:



                    cursor.execute("SELECT final FROM card_active WHERE id = "+str(rand_id)+"") 
                    final_card = cursor.fetchall()
                    card_info = 'txt_final_cartao_'
                    text_fimal = (QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">XXXX-XXXX-XXXX-"+str(final_card[0][0])+"</span></p></body></html>", None))                
                    self.botoes = self.findChildren(QLabel , str(card_info+str(rand_id)))

                    self.botoes[0].setText(text_fimal)
                except:
                    pass


                try:

                    #SETA TITULAR DO CARTAO

                    cursor.execute("SELECT titular FROM card_active WHERE id = "+str(rand_id)+"")
                    final_card = cursor.fetchall()
                    card_info = 'txt_titular_cartao_'
                    text_fimal = (QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">"+str(final_card[0][0])+"</span></p></body></html>", None))
                    self.botoes = self.findChildren(QLabel , str(card_info+str(rand_id)))
                    self.botoes[0].setText(text_fimal)
                except:
                    pass
        thread = threading.Thread(target=thead(self))
        thread.start()


    def _Values_Individual(self): # valor do grafico do extrato esse #TODO ESSE PODE SER INDIVIDUAL #NTS
        def thead(): 
            a = (os.path.dirname(os.path.realpath(__file__)))
            banco = sqlite3.connect(''+a+'/bando_de_valores.db')
            cursor = banco.cursor()
            global EXTRATO_ATUAL 
            id =EXTRATO_ATUAL
            mes = funcoes_cartao._mes(self)
            
            
            #TODO CAPTURA FATURA MES:
            
            fatura_atual = card_db_test.Return_Values_Calcs._fatural_atual(id,mes)
            

            #TODO PEGAR TOTAL UTILIZADO:
            
            limite_utilizado = card_db_test.Return_Values_Calcs._limite_utilizado(id)
            
            #TODO CAPTURA LIMITE DISPONIVEL:
            
            limite_disponivel = card_db_test.Return_Values_Calcs._limite_disponivel(id)
            
            
            #TODO CAPTURA PORCETAGEM UTILIZADA:
            
            porcentagem_utilizada = card_db_test.Return_Values_Calcs._porcentagem_utilizada(id)
            
            # SETA PORCENTAGEM:
            
            self.labelPercentage_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt;\">"+porcentagem_utilizada+"</span><span style=\" font-size:20pt; vertical-align:super;\">%</span></p></body></html>", None))
            
            #MUDA PROGRESS BAR :
            bar = ("{:.0f}".format(float(porcentagem_utilizada))) #TODO Pega o porcetual sem ponto 
            fix= int(bar) #todo FIX para caso nao seja dezena o valor e bugar a barra 
            if fix >= 100:
                bar = "99"
            if fix <= 9:
                bar = ("0{:.0f}".format(float(porcentagem_utilizada)))
            self.circularProgress_2.setStyleSheet(u"QFrame{\n"
            "	border-radius: 85px;\n"
            "	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0."+bar+"1 rgba(255, 0, 127, 0), stop:0."+bar+"0 rgba(85, 170, 255, 255));\n"
            "}")
            
            #muda limite barra
            try:
                setbarra = int(bar) 
                usado=setbarra/100*750
                #todo muda tamnho da barra limite usado
                self.usado.setMaximumSize(QSize(usado, 16777215))
                if fix > 80:
                    pass

                    
            except:
                pass
            
            try:
                

                #TODO LIMITE TOTAL

                #todo VALORE RESTANTE


                for val in range (2):
                    card_info = ['valor_faturaatual_cartao_','valor_limitedisponivel_cartao_']
                    text = [(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff\">R$"+str(fatura_atual)+"</span></p></body></html>", None)),
                            (QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-weight:600; color:#ffffff;\">R$"+str(limite_disponivel)+"</span></p></body></html>", None))]
                    self.botoes = self.findChildren(QLabel , str(card_info[val]+id))
                    self.botoes[0].setText(text[val])

            except:
                pass

            id =int(EXTRATO_ATUAL)
            funcoes_cartao._limite_disponive_usado(self,id)


        thread = threading.Thread(target=thead)
        thread.start()


    def remove_compra(self): #NAO TINHA THEAD 
        def thead():

            global EXTRATO_ATUAL
            id_fatura =EXTRATO_ATUAL


            extrato_card_selected ='extrato_cartao_'+EXTRATO_ATUAL



                #CAPTURA VALOR DAS COMPRAS TOTAL   
            listdb= extrato_card_selected


            linha_selecionada = self.extrato_cartao_0.currentRow()
            


            id_remove = self.extrato_cartao_0.item(int(linha_selecionada),7).text()

            self.extrato_cartao_0.removeRow(linha_selecionada)


            a = (os.path.dirname(os.path.realpath(__file__)))
            banco = sqlite3.connect(''+a+'/bando_de_valores.db')
            cursor = banco.cursor()

            lista_ids_active = []
            
            cursor.execute("SELECT * FROM '"+str(listdb)+"'") 

            dadoslidos = cursor.fetchall()

            inde = 0
            for i in  dadoslidos:
                lista_ids_active.append(dadoslidos[inde])
                inde = inde +1




            #pega o id 
            cursor.execute("DELETE FROM '"+str(listdb)+"' WHERE id = "+str(id_remove)+"")
            banco.commit()
            banco.close()
            
            funcoes_cartao._Values_Individual(self)
            

            try:
                self.grafico_categoria.setParent(None)
            except:
                pass
        thread = threading.Thread(target=thead)
        thread.start()


    def retorna_style_card(): #NT
        global GLOBAL_SELECT_CARD_ADD
        return GLOBAL_SELECT_CARD_ADD


    def creat_new_widget(self,id): #T
        def thead(self):
            NUMERO_DE_CARTOES = id


            styler = effects.efeitos_geral.style_sheet_card_(self)

            #TODO CACARTERIZAÇÃO DO WIDGET:


            self.stackedWidget_cartao_0 = QStackedWidget(self.scrollAreaWidgetContents_3)
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

            self.ver_compras_cartao_0 = QPushButton(self.frame_cartao_0, clicked = lambda:funcoes_cartao.exec_function(self))
            self.ver_compras_cartao_0.setObjectName(u"ver_compras_cartao_"+str(NUMERO_DE_CARTOES))
            self.ver_compras_cartao_0.setGeometry(QRect(280, 150, 110, 30))
            self.ver_compras_cartao_0.setMinimumSize(QSize(110, 30))
            self.ver_compras_cartao_0.setMaximumSize(QSize(110, 25))
            self.ver_compras_cartao_0.setFont(font3)
            self.ver_compras_cartao_0.setStyleSheet(u"\n"
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

            #TODO NOME DO TITULAR:
            self.txt_titular_cartao_0 = QLabel(self.frame_cartao_0)
            self.txt_titular_cartao_0.setObjectName(u"txt_titular_cartao_"+str(NUMERO_DE_CARTOES))
            self.txt_titular_cartao_0.setGeometry(QRect(200, 10, 151, 36))
            self.txt_titular_cartao_0.setStyleSheet(u"border: 0px;")
            self.txt_titular_cartao_0.setTextFormat(Qt.AutoText)
            self.txt_titular_cartao_0.setScaledContents(False)
            self.txt_titular_cartao_0.setAlignment(Qt.AlignCenter)
            self.txt_titular_cartao_0.setWordWrap(False)

            #TODO BOTAO 3 PONTINHOS DE CONFIG PARA IR PARA PAG 2:

            self.config_cartao_0 = QPushButton(self.frame_cartao_0)

            self.config_cartao_0.setObjectName(u"config_cartao_"+str(NUMERO_DE_CARTOES))
            self.config_cartao_0.setGeometry(QRect(370, 10, 25, 19))
            self.config_cartao_0.setStyleSheet(u"")

            #TODO TEXTO FINAL DO TITULAR:

            self.txt_final_cartao_0 = QLabel(self.frame_cartao_0)
            self.txt_final_cartao_0.setObjectName(u"txt_final_cartao_"+str(NUMERO_DE_CARTOES))
            self.txt_final_cartao_0.setGeometry(QRect(10, 170, 201, 31))
            self.txt_final_cartao_0.setStyleSheet(u"border: 0px")
            self.txt_final_cartao_0.setTextFormat(Qt.AutoText)
            self.txt_final_cartao_0.setScaledContents(False)
            self.txt_final_cartao_0.setAlignment(Qt.AlignCenter)
            self.txt_final_cartao_0.setWordWrap(False)

            #TODO VALOR LIMITE DISPOINIVEL "R$0":

            self.valor_limitedisponivel_cartao_0 = QLabel(self.frame_cartao_0)
            self.valor_limitedisponivel_cartao_0.setObjectName(u"valor_limitedisponivel_cartao_"+str(NUMERO_DE_CARTOES))
            self.valor_limitedisponivel_cartao_0.setGeometry(QRect(150, 130, 121, 36))
            self.valor_limitedisponivel_cartao_0.setStyleSheet(u"border: 0px;")
            self.valor_limitedisponivel_cartao_0.setTextFormat(Qt.AutoText)
            self.valor_limitedisponivel_cartao_0.setScaledContents(False)
            self.valor_limitedisponivel_cartao_0.setAlignment(Qt.AlignCenter)
            self.valor_limitedisponivel_cartao_0.setWordWrap(False)

            #TODO TEXTO DO LIMITE DISPONIVEL"LIMITE DISPONIVEL"
            self.txt_limite_disponivel_cartao_0 = QLabel(self.frame_cartao_0)
            self.txt_limite_disponivel_cartao_0.setObjectName(u"txt_limite_disponivel_cartao_"+str(NUMERO_DE_CARTOES))
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
            self.valor_faturaatual_cartao_0.setObjectName(u"valor_faturaatual_cartao_"+str(NUMERO_DE_CARTOES))
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
            self.salva_configcartao_0 = QPushButton(self.frame_config_cartao_0,clicked = lambda:funcoes_cartao.exec_function(self))
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

            self.verticalLayout_3.addWidget(self.stackedWidget_cartao_0)







            #TODO AQUI VAI SETAR OS TEXTOS POR PADRAO

            self.valor_faturaatual_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:20pt; font-weight:600; color:#ffffff\">R$ 0</span></p></body></html>", None))
            self.txt_limite_disponivel_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Limite disponivel:</span></p></body></html>", None))
            self.ver_compras_cartao_0.setText(QCoreApplication.translate("MainWindow", u"VER COMPRAS", None))
            self.txt_fatura_atual_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Fatura atual</span></p></body></html>", None))
            self.valor_limitedisponivel_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-weight:600; color:#ffffff;\">R$ 0,00</span></p></body></html>", None))
            self.config_cartao_0.setText(QCoreApplication.translate("MainWindow", u"...", None))
            self.txt_titular_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Madalena Souza</span></p></body></html>", None))
            self.txt_final_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">XXXX-XXXX-XXXX-0474</span></p></body></html>", None))
            self.limite_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Limite Total do Cartao</span></p></body></html>", None))
            self.salva_configcartao_0.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
            self.setlimitcartao_0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$", None))
            self.titular_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Titular</span></p></body></html>", None))
            self.final_cartao_0.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Final do Cart\u00e3o</span></p></body></html>", None))
            self.setfinalcartao_0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXX", None))
        thread = threading.Thread(target=thead(self))
        thread.start()


    def object_name(self): #NT
        
        #_____________________________________________________
        # Pega nome do botao que foi clicado na hora:
        name_obj = self.focusWidget().objectName()
        #PARA ACESSAR OS BOTOES TERIAMOS QUE UTILIZAR UM INDEX DA LISTA DE BOTOES.
        self.botoes = self.findChildren(QPushButton , str(name_obj))
        #e vai fazer a validação e direcionar para a função certa no return 
        return [name_obj,self.botoes]


    def exec_function(self): #QPushButton # NAO PODE TER THEAD 
            
        execut = None

        self.functio = funcoes_cartao.object_name(self)

        #3 FUNÇÕES, 0 VER_COMRAS, 1 CONFIG_CARTAO, 2 SALVA_CONFIG

        # 1 PEGAR O INDEX DO STACKEWIDGET
        #remove letras do nome do obj ´pra pegar o index
        index = self.functio[0]
        index = re.sub('[^0-9]', '', self.functio[0])
        stacked = "stackedWidget_cartao_"+str(index)
        self.find_stacked = self.findChildren(QStackedWidget, str(stacked))



        if "ver_compras_cartao_" in self.functio[0]:
            a = (os.path.dirname(os.path.realpath(__file__)))
            if (os.path.exists(''+a+'/bando_de_valores.db')):
                global EXTRATO_ATUAL
                EXTRATO_ATUAL = index
                execut = lambda:effects.efeitos_geral.expandecomprascartao(self)
                effects.efeitos_geral.expandecomprascartao(self)
                mes = datetime.today().strftime('%m%Y')
                funcoes_cartao._return_mes_string(self)
                funcoes_cartao.carrega_extrato_mes(self,mes)
                funcoes_cartao._Values_Individual(self)
                effects.efeitos_geral.txt_progess_circular(self)
                funcoes_cartao.clean_option_extrato(self)
                funcoes_cartao._circular_progress_name(self,index)
                funcoes_cartao._faturas(self)
                funcoes_cartao._current_date(self,'none')
                try:
                    Chart_one.clear(self)
                except:
                    pass
                try:
                    self.stacked_configcartao0.setCurrentIndex(0)
                    for tres in range(3):
                        self.creat_eraser = [self.grafico_categoria,self.grafico_data,self.grafico_evolucao]
                        self.creat_eraser[tres].setParent(None)
                except:
                    pass
            else:
                pass



        if "config_cartao_" in self.functio[0]:
            global CARD_SELECTED
            CARD_SELECTED = index
            execut = self.find_stacked[0].setCurrentIndex(1)

        if "salva_configcartao_" in self.functio[0]:
            a = (os.path.dirname(os.path.realpath(__file__)))
            if (os.path.exists(''+a+'/bando_de_valores.db')):
                pass
            else:
                pass
        return execut,index


    def raname_value(self): #NT
        label_3 = self.lineEdit_3.text() 

    def raname_date(self): #NT
        list = []
        label_2 = self.lineEdit_2.text()  # data str  
        count = (len(label_2))
        
        for label_2 in label_2:
            list.append(label_2)
            
        if count <=1:
            pass
        
        elif count == 2:
            form =('%s%s/' %(list[0],list[1]))
            self.lineEdit_2.setText(form)
        elif count == 5:
            form =('%s%s/%s%s/' %(list[0],list[1],list[3],list[4]))
            self.lineEdit_2.setText(form)

        elif count == 10:
            form =('%s%s/%s%s/%s%s%s%s' %(list[0],list[1],list[3],list[4],list[6],list[7],list[8],list[9]))
            self.lineEdit_2.setText(form)

        elif count > 10:
            form =('%s%s/%s%s/%s%s%s%s' %(list[0],list[1],list[3],list[4],list[6],list[7],list[8],list[9]))
            self.lineEdit_2.setText(form)



    def _today(self): #NT
        today = datetime.today().strftime('%m%Y')
        return today


        
    def clean_option_extrato(self): #NT
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')

        
    def style_config_card(self):

        selected = self.select_card.currentText()
        style = effects.efeitos_geral.style_sheet_config(self,selected)
        
        self.frameadc.setStyleSheet(u"QFrame{background-color: "+style[0]+";\n"
                                     "border-radius: 10px;\n"
                                     "border: 3px solid  rgb(0, 0, 0);\n"
                                     "border:0px;\n"
                                     "}\n"
                                     "\n"
                                     "QFrame:hover{\n"
                                     "border: 3px solid  "+style[1]+";\n"
                                     "\n"
                                     "}")
        self.logoadc.setStyleSheet(u"border: 0px;\n"
                                    "background-image: "+style[2]+";\n"
                                    "")


    def carrega_extrato_mes(self, mes): #NTS
        def thead():
            cont = self.extrato_cartao_0.rowCount()
            if cont > 0:
                for i in range (cont): #TODO TERMINAR AQUI AMANHA 24/05
                    if self.extrato_cartao_0.rowCount() >= 0:
                        self.extrato_cartao_0.removeRow(self.extrato_cartao_0.rowCount()-1)
            #VALIDADOR ONMDE VAI EXCOLHER QUAL EXTRATO FOI CHAMADO DE QUAL CARTAO

            
            global EXTRATO_ATUAL
            id = EXTRATO_ATUAL

            extrato = card_db_test.Ui_db._extrato(id,mes)
            dados = extrato[1]


            for i in range(extrato[0]):
                rowPosition = self.extrato_cartao_0.rowCount()
                self.extrato_cartao_0.insertRow(rowPosition)    
                
            if not extrato[0]:
                pass
                
                
                self.stack_extrato_pages.setCurrentWidget(self.page_emdia)
            else:
                self.stack_extrato_pages.setCurrentWidget(self.extrato_cards_dbs)

                
                index = 0


                for linhas in dados: 
                    col = dados[index] 
                    colunasc = 0
                    for colunas in col:
                        if colunasc == 3:
                            eng_tobr= funcoes_cartao._data_eng_to_br(self,colunas)
                            colunas = eng_tobr
                        if colunasc == 6:
                            usd_to_brl = funcoes_cartao._usd_to_brl(self,float(colunas))
                            colunas=str(usd_to_brl)
                        else:
                            pass
                        self.extrato_cartao_0.setItem(index , colunasc, QtWidgets.QTableWidgetItem(colunas))
                        colunasc = colunasc+1
                    index = index +1

                funcoes_cartao.icontable_extrato(self)
        thread = threading.Thread(target=thead)
        thread.start()


    def convert_date(self,y,m,d):
        a = "%s-%s-%s"% (d,m,y)
        return a
        

    def _current_date(self,event):
        mes = self.label_3.text()
        ano = self.label_2.text()
        stacked = self.extrat_meses
        
        valores = {'Janeiro':1,'Fevereiro':2,'Marco':3,'Abril':4,'Maio':5,'Junho':6,'Julho':7,'Agosto':8,'Setembro':9,'Outubro':10,'Novembro':11,'Dezembro':12}
        
        captura_int_mes = valores[mes]
        
        format_date = datetime.strptime(str(captura_int_mes)+ano, '%m%Y')
        date = format_date.date()
        
        #adiciona mes
        if event == "Next":
            soma_mes = relativedelta(months=+1)
        elif event == "none":
            pass
        else:
            soma_mes = relativedelta(months=-1)
        
        if event == "Next":
            ab= date + soma_mes
            ab = str(ab)
        elif event == "none":
            ab= date
            ab = str(ab)
        else:
            ab= date + soma_mes
            ab = str(ab)
        
        
        #ALTERA TEXTO UI
        

        mes_string = ab
        set_mes = mes_string[5:7]


        #inverte a lista pra pegar no final a palavra do mes
        invert = {'01':'Janeiro','02':'Fevereiro','03':'Marco','04':'Abril','05':'Maio','06':'Junho','07':'Julho','08':'Agosto','09':'Setembro','10':'Outubro','11':'Novembro','12':'Dezembro'}

        captura_str_mes = invert[set_mes]
        self.label_3.setText(captura_str_mes)
        set_ano = mes_string[0:4]
        self.label_2.setText(set_ano) 
        
        id = EXTRATO_ATUAL
        
        db = set_mes+set_ano
        status = card_db_test.Return_Values_Calcs._status_fatura(id,set_mes,set_ano)
        
        if status == 'pago':
            self.extrat_meses.setStyleSheet("border-radius:7px; background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.00398406 rgba(117, 160, 153, 255), stop:0.33833 rgba(34, 121, 37, 159), stop:0.66167 rgba(80, 58, 161, 27), stop:1 rgba(106, 151, 135, 255));")
        
        elif status == 'proximas':
            self.extrat_meses.setStyleSheet("border-radius:7px; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.135747 rgba(242, 170, 116, 252), stop:0.30922 rgba(255, 154, 80, 241), stop:0.499246 rgba(217, 131, 68, 255), stop:0.992459 rgba(236, 101, 0, 221));")
        else:
            self.extrat_meses.setStyleSheet("border-radius:7px; background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.00398406 rgba(117, 160, 215, 255), stop:0.250614 rgba(0, 109, 187, 242), stop:0.641278 rgba(34, 121, 152, 159), stop:0.644963 rgba(34, 121, 152, 159), stop:1 rgba(106, 151, 221, 255));")
        
        return funcoes_cartao.carrega_extrato_mes(self,db)
        
        
    def _search_compras(self):

        def thead():
            
            # REMOVE LINHAS AUTAIS DO QTALBE
            cont = self.extrato_cartao_0.rowCount()
            if cont > 0:
                for i in range (cont): #TODO TERMINAR AQUI AMANHA 24/05
                    if self.extrato_cartao_0.rowCount() >= 0:
                        self.extrato_cartao_0.removeRow(self.extrato_cartao_0.rowCount()-1)
            #VALIDADOR ONMDE VAI EXCOLHER QUAL EXTRATO FOI CHAMADO DE QUAL CARTAO

            #filtro:
            global EXTRATO_ATUAL
            id = EXTRATO_ATUAL
            ano = self.line_y.text()
            mes = self.line_m.text()
            dia = self.line_d.text()
            

            dados = card_db_test.Return_Values_Calcs._filtra_compra(id,ano,mes,dia)

            
            
            if not dados:
                self.stack_extrato_pages.setCurrentWidget(self.page_not_found)
                
            else:
                self.stack_extrato_pages.setCurrentWidget(self.extrato_cards_dbs)
                
                
                for i in dados:
                    rowPosition = self.extrato_cartao_0.rowCount()
                    self.extrato_cartao_0.insertRow(rowPosition)    

                index = 0

                for linhas in dados: #14 linhas
                    col = dados[index] # pega a 1 linha
                    colunasc = 0
                    for colunas in col: # pega dados coluna 1 linha
                        self.extrato_cartao_0.setItem(index , colunasc, QtWidgets.QTableWidgetItem(colunas))
                        colunasc = colunasc+1
                    index = index +1
                    
                funcoes_cartao.icontable_extrato(self)
            
        thread = threading.Thread(target=thead)
        thread.start()
        
        
    def _return_mes_string(self):
        mes_string = funcoes_cartao._mes2(self)
        invert = {'01':'Janeiro','02':'Fevereiro','03':'Marco','04':'Abril','05':'Maio','06':'Junho','07':'Julho','08':'Agosto','09':'Setembro','10':'Outubro','11':'Novembro','12':'Dezembro'}
        set_mes = mes_string[0:2]
        captura_str_mes = invert[set_mes]
        set_ano = mes_string[2:6]
        self.label_2.setText(set_ano) 
        funcoes_cartao.carrega_extrato_mes(self,mes_string)
        return self.label_3.setText(captura_str_mes)
        
        
    def _limite_disponive_usado(self,id): #TODO PAGINA DE EXTRASTO, MOSTRA DETALHES DO CARD
        
        #LIMITE CARTAO:
        limite = card_db_test.Ui_db._limite(id)
        self.label_28.setText('R$'+limite)
        #VENCIMENTO:
        vencimento = card_db_test.Ui_db._vencimento(id)
        self.label_32.setText('Todo dia '+str(vencimento))
        self.label_34.setText('Todo dia '+str(vencimento))
        #LIMITE UTILIZADO :
        limite_utilizado = card_db_test.Return_Values_Calcs._limite_utilizado(id)
        self.labelTitle_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#5c9bcf;\">Limite Utilizado:</span></p><p><span style=\" font-size:11pt; font-weight:600; color:#5c9bcf;\">R$"+str(limite_utilizado)+"</span></p></body></html>", None))
        #LIMITE DISPONIVEL
        limite_disponivel= card_db_test.Return_Values_Calcs._limite_disponivel(id)
        self.labelTitle_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#00aa00;\">Limite Disponivel</span></p><p><span style=\" font-size:11pt; font-weight:600; color:#00aa00;\">R$"+str(limite_disponivel)+"</span></p></body></html>", None))
        self.label_30.setText('R$'+limite_disponivel)
        #NOME DO CARTAO:
        nome = card_db_test.Ui_db._cartao(id)
        self.name_bank_2.setText(nome)
        logo = nome
        #LOGO DO CARTAO:
        icon = effects.efeitos_geral.style_sheet_card_icon(self,logo)
        self.icon_2.setStyleSheet(u"border-bottom: 0px;border-radius: 5px;border-image: "+icon+";")
        

    def _mes(self):
        today = date.today()
        soma_mes = relativedelta(months=+1)
        mes= today + soma_mes
        mes = str(mes)
        ano = mes[0:4]
        mesf = mes[5:7]
        mes = '%s-%s'%(ano,mesf)
        return mes
    
    
    def _mes2(self): #sempre retora proximo mes e ano atual 082022
        today = date.today()
        soma_mes = relativedelta(months=+1)
        mes= today + soma_mes
        mes = str(mes)
        ano = mes[0:4]
        mesf = mes[5:7]
        mes = '%s%s'%(mesf,ano)
        return mes


    def _mes_load_extrato(self):
        today = date.today()
        soma_mes = relativedelta(months=+1)
        mes= today + soma_mes
        mes = str(mes)
        ano = mes[0:4]
        mesf = mes[5:7]
        mes = '%s%s'%(mesf,ano)
        return mes
    
    
    def _circular_progress_name(self,id):
        #GET NAME:
        name = card_db_test.Ui_db._cartao(id)
        #SET TEXT:
        self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:13pt; font-weight:600; color:#9b9bff;\">"+name+"</span></p></body></html>", None))

    def _faturas(self):
        def thead(self):
            id = EXTRATO_ATUAL
            
            ano_txt =self.label_10.text()
            
            dados = card_db_test.Return_Values_Calcs._todas_faturas(id,ano_txt)

    
            cont = self.table_faturas_ind.rowCount()
            if cont > 0:
                for i in range (cont): #TODO TERMINAR AQUI AMANHA 24/05
                    if self.table_faturas_ind.rowCount() >= 0:
                        self.table_faturas_ind.removeRow(self.table_faturas_ind.rowCount()-1)
                
            index = 0
            index_name_mes = 1
            line = 0
            for linhas in dados: #12 0-11 linhas
                if str(linhas) == 'None':
                    d = '0'
                else:
                    d = dados[index]
                rowPosition = self.table_faturas_ind.rowCount()
                self.table_faturas_ind.insertRow(rowPosition)
                
                diconario = {'1':'Janeiro','2':'Fevereiro','3':'Marco','4':'Abril','5':'Maio','6':'Junho','7':'Julho','8':'Agosto','9':'Setembro','10':'Outubro','11':'Novembro','12':'Dezembro'}
                diconario_mes_int_str = {'1':'01','2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08','9':'09','10':'10','11':'11','12':'12'}
                todays_date = date.today()


                valor = ("{:.2f}".format(float(d))) # pega a 1 linha
                valor_pago = ("{:.2f}".format(float(d))) # pega a 3 linha
                ano = "%s de %s"%(diconario[str(index_name_mes)],ano_txt)# pega a 4 linha
                
                self.pushButton_pago = QPushButton(self.table_faturas_ind, clicked = lambda:funcoes_cartao.btn_qtable_pagar_fatura(self))
                self.pushButton_pago.setObjectName(u"pagobuto")
                self.pushButton_pago.setGeometry(QRect(140, 180, 61, 31))
                
                status_int = diconario_mes_int_str[str(index_name_mes)]
                if card_db_test.Return_Values_Calcs._status_fatura(id,status_int,ano_txt) == 'pago':
                    
                    self.pushButton_pago.setStyleSheet("QPushButton{font: 13pt;border-radius:3px;background-color: rgb(50, 122, 67);border: 1px solid  rgb(55, 55, 55);}QPushButton:hover{background-color: rgb(65, 160, 88);border: 2px solid  rgb(255, 255, 255);}QPushButton:pressed{background-color: rgb(65, 160, 88);border: 2px solid  rgb(55, 55, 55);}")
                    self.pushButton_pago.setText("Pago")
                elif card_db_test.Return_Values_Calcs._status_fatura(id,status_int,ano_txt) == 'proximas':
                    self.pushButton_pago.setStyleSheet("QPushButton{font: 13pt;border-radius:3px;background-color: rgb(214, 154, 90);border: 1px solid  rgb(55, 55, 55);}QPushButton:hover{background-color: rgb(163, 117, 68);border: 2px solid  rgb(255, 255, 255);}QPushButton:pressed{background-color: rgb(163, 117, 68) ;border: 2px solid  rgb(55, 55, 55);}")
                    self.pushButton_pago.setText("Futuras")
                else:
                    self.pushButton_pago.setStyleSheet("QPushButton{font: 13pt;border-radius:3px;background-color: rgb(8, 110, 179);border: 1px solid  rgb(55, 55, 55);}QPushButton:hover{background-color: rgb(9, 133, 217);border: 2px solid  rgb(255, 255, 255);}QPushButton:pressed{background-color: rgb(9, 133, 217);border: 2px solid  rgb(55, 55, 55);}")
                    self.pushButton_pago.setText("Pendente")


                self.table_faturas_ind.setItem(line , 0, QtWidgets.QTableWidgetItem(str(ano)))
                # self.table_faturas_ind.setItem(index , 1, QtWidgets.QTableWidgetItem(str(valor)))
                self.table_faturas_ind.setItem(line , 2, QtWidgets.QTableWidgetItem(str(valor)))
                self.table_faturas_ind.setItem(line , 3, QtWidgets.QTableWidgetItem(str(valor_pago)))
                self.table_faturas_ind.setCellWidget(line, 4, self.pushButton_pago)
                for colunas in range(3):
                    if colunas == 1:
                        colunas = 2
                    item = self.table_faturas_ind.item(line, colunas)
                    item.setTextAlignment(Qt.AlignCenter)

                index = index +1
                index_name_mes = index_name_mes+1
                line= line+1
        thread = threading.Thread(target=thead(self))
        thread.start()        

    def _pagar_fatura(self):
        
        id = EXTRATO_ATUAL
        mes = self.label_3.text()
        ano = self.label_2.text()
        valores = {'Janeiro':'01','Fevereiro':'02','Marco':'03','Abril':'04','Maio':'05','Junho':'06','Julho':'07','Agosto':'08','Setembro':'09','Outubro':'10','Novembro':'11','Dezembro':'12'}
        captura_int_mes = valores[mes]
        card_db_test.Return_Values_Calcs._pagar_fatura(id,captura_int_mes,ano)
        extrato = captura_int_mes+ano
        funcoes_cartao.carrega_extrato_mes(self,extrato)

    
    def _return_mes_ano(self,mes,ano):
        mes = '01' #self txt 
        ano ='2022' #self text

        format_date = datetime.strptime(mes+ano, '%m%Y')
        date = format_date.date()
        soma_mes = relativedelta(months=+1)
        result= date + soma_mes
        ab = str(result)
        return ab 

    def btn_qtable_pagar_fatura(self):
        # botao self.pushButton_pago
        id = EXTRATO_ATUAL
        mes = self.label_3.text()
        ano = self.label_2.text()
        valores = {'Janeiro':'01','Fevereiro':'02','Marco':'03','Abril':'04','Maio':'05','Junho':'06','Julho':'07','Agosto':'08','Setembro':'09','Outubro':'10','Novembro':'11','Dezembro':'12'}
        captura_int_mes = valores[mes]
        extrato = captura_int_mes+ano


    def _filter_year_faturas(self,event):
        ano = self.label_10.text()
        if event == ('Next'):
            soma = int(ano) +1
            self.label_10.setText(str(soma))
        else:
            menos = int(ano)-1
            self.label_10.setText(str(menos))

    def _data_eng_to_br(self,data_eng):
        ano = data_eng[0:4]
        mes = data_eng [5:7]
        dia =  data_eng [8:10]
        return "%s/%s/%s"%(dia,mes,ano)

    def _data_br_to_eng(self,data_br):
        dia= data_br[0:2]
        mes=data_br[3:5]
        ano=data_br[6:10]
        return  "%s-%s-%s"%(ano,mes,dia)

    def _usd_to_brl(self,valor):
        valor = valor 
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        valor = locale.currency(valor, grouping=True, symbol=True)
        return ('%s' % valor)

    def today(self): #NT
        today = datetime.today().strftime('%d/%m/%Y')
        self.lineEdit_2.setText(today)
    
    def _brl_to_usd(valor):
        new_string = valor
        to_remove = "."
        for x in to_remove:
            new_string = new_string.replace(x, '')
            new_string = new_string.replace(',','.')
        return new_string

class Chart_one(Ui_MainWindow):

    def _creat_charts(self):
        def thead(self):
            list = []
            self.frames = self.frame_chart_category
            for i in range(self.frames.count()):
                a = self.frames.itemAt(i).widget().objectName()
                list.append(a)
            count = len(list)
            if count ==0:
                Chart_one.grafico_1(self)
                Chart_one.grafico_2(self)
                Chart_one.grafico_3(self)


            elif count > 0:
                Chart_one.grafico_1(self)
                Chart_one.grafico_2(self)
                Chart_one.grafico_3(self)
                pass

        thread = threading.Thread(target=thead(self))
        thread.start()  

        
    def clear(self):
        self.categoria1.clear()
        id = EXTRATO_ATUAL
        mes = self.label_3.text()
        ano = self.label_2.text()
        valores = {'Janeiro':'01','Fevereiro':'02','Marco':'03','Abril':'04','Maio':'05','Junho':'06','Julho':'07','Agosto':'08','Setembro':'09','Outubro':'10','Novembro':'11','Dezembro':'12'}
        captura_int_mes = valores[mes]
        dados = card_db_test.Charts_values._gastos_categoria(id,captura_int_mes,ano)
        #ATT GRAFICO
        index = 0
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light Condensed")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(3)
        
        
        for i in dados[0]:
            self.categoria1.append(dados[0][index],dados[1][index])
            index = index+1

        self.categoria1.setLabelsVisible(True)
        self.categoria1.setLabelsPosition(QtCharts.QPieSlice.LabelOutside)
        
        for slice in self.categoria1.slices():
                slice.setLabel("R${:.2f} {:.2f}%".format(slice.value(),100 * slice.percentage()))
                slice.setLabelFont(font3)
                
        #ATT DESCRIÇÃO

        index_label = 0

        for i in dados[0]:
            self.grafico.legend().markers(self.categoria1)[index_label].setLabel(str(dados[0][index_label]))
            index_label = index_label+1
        
        
    def grafico_1(self):    
        def thead(self):


            id = EXTRATO_ATUAL
            mes = self.label_3.text()
            ano = self.label_2.text()
            valores = {'Janeiro':'01','Fevereiro':'02','Marco':'03','Abril':'04','Maio':'05','Junho':'06','Julho':'07','Agosto':'08','Setembro':'09','Outubro':'10','Novembro':'11','Dezembro':'12'}
            captura_int_mes = valores[mes]

            font3 = QFont()
            font3.setFamily(u"Bahnschrift Light Condensed")
            font3.setPointSize(12)
            font3.setBold(False)
            font3.setItalic(False)
            font3.setWeight(3)
            
            dados = card_db_test.Charts_values._gastos_categoria(id,captura_int_mes,ano)
            index = 0
            self.categoria1 = QtCharts.QPieSeries()

            for i in dados[0]:
                self.categoria1.append(dados[0][index],dados[1][index])
                index = index+1

            self.categoria1.setLabelsVisible(True)
            self.categoria1.setLabelsPosition(QtCharts.QPieSlice.LabelOutside)


            self.grafico = QtCharts.QChart()
            
            self.grafico.addSeries(self.categoria1)
            self.grafico.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
            self.grafico.setTheme(QtCharts.QChart.ChartTheme.ChartThemeBlueCerulean)
            self.grafico.setTitle("Gastos por Categoria")
            self.grafico.legend().setVisible(True)
            self.grafico.legend().setAlignment(Qt.AlignBottom)

            self.grafico.setTitleFont(font3)

            for slice in self.categoria1.slices():
                slice.setLabel("R${:.2f} {:.2f}%".format(slice.value(),100 * slice.percentage()))
                slice.setLabelFont(font3)
            
            index_label = 0
            for i in dados[0]:
                self.grafico.legend().setFont(font3)
                self.grafico.legend().markers(self.categoria1)[index_label].setLabel(str(dados[0][index_label]))
                
                
                index_label = index_label+1

            self.grafico.legend().setBackgroundVisible(True)
            

            self.ver_grafico = QtCharts.QChartView(self.grafico)
            self.ver_grafico.setRenderHint(QPainter.Antialiasing)


            list = []
            self.frames = self.frame_chart_category
            for i in range(self.frames.count()):
                a = self.frames.itemAt(i).widget().objectName()
                list.append(a)
            count = len(list)

            if count ==0:
                self.frame_chart_category.addWidget(self.ver_grafico)



            else:
                while self.frame_chart_category.count():
                    child = self.frame_chart_category.takeAt(0)
                    childWidget = child.widget()
                    if childWidget:
                        childWidget.setParent(None)
                self.frame_chart_category.addWidget(self.ver_grafico)
                pass
        thread = threading.Thread(target=thead(self))
        thread.start()  

    def grafico_2(self):
        def thead(self):   
            id = EXTRATO_ATUAL
            ano = self.label_2.text()
            # self.layout = QVBoxLayout(self)
            self.set0 = QtCharts.QLineSeries()


            filter_list = []
            todas_as_faturas = card_db_test.Return_Values_Calcs._todas_faturas(id,ano)
            index = 0
            for i in todas_as_faturas:
                if not  todas_as_faturas[index]:
                    filter_list.append(0)
                else:
                    filter_list.append(int(todas_as_faturas[index]))
                index = index+1
            index_mes = 0

            for mes in range(12):
                self.set0.append(index_mes,filter_list[index_mes])
                index_mes = index_mes+1



            # for slice in self.categoria1.slices():
            #     slice.setLabel("R${:.2f} {:.2f}%".format(slice.value(),100 * slice.percentage()))

            self.chart = QtCharts.QChart()
            self.chart.addSeries(self.set0)
            self.chart.setTitle("Todas as Faturas")
            self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)


            categories = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun","Jul","Ago","Set","Out","Nov","Dez"]
            axis = QtCharts.QBarCategoryAxis()
            axis.append(categories)
            self.chart.createDefaultAxes()
            self.chart.setAxisX(axis, self.set0)

            self.chart.legend().setVisible(True)
            self.chart.legend().setAlignment(Qt.AlignBottom)



            self.chart_view = QtCharts.QChartView(self.chart)
            self.chart_view.setRenderHint(QPainter.Antialiasing)
            self.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeBlueCerulean)
            
            font3 = QFont()
            font3.setFamily(u"Bahnschrift Light Condensed")
            font3.setPointSize(12)
            font3.setBold(False)
            font3.setItalic(False)
            font3.setWeight(3)

            self.chart.legend().setFont(font3)
            self.chart.setFont(font3)
            self.chart.setTitleFont(font3)
            
            
            

            list = []
            self.frames = self.frame_chart_evolution_fat
            for i in range(self.frames.count()):
                a = self.frames.itemAt(i).widget().objectName()
                list.append(a)
            count = len(list)
            if count ==0:

                self.frame_chart_evolution_fat.addWidget(self.chart_view)



            else:
                while self.frame_chart_evolution_fat.count():
                
                    child = self.frame_chart_evolution_fat.takeAt(0)
                    childWidget = child.widget()
                    if childWidget:
                        childWidget.setParent(None)

                self.frame_chart_evolution_fat.addWidget(self.chart_view)
                pass
        thread = threading.Thread(target=thead(self))
        thread.start()  
        
    def grafico_3(self):    
        def thead(self):
            self.set0 = QtCharts.QBarSet("Delivery")
            self.set1 = QtCharts.QBarSet("Apps Transporte")
            self.set2 = QtCharts.QBarSet("Comida")
            self.set3 = QtCharts.QBarSet("Mercado")
            self.set4 = QtCharts.QBarSet("Lazer")
            self.set5 =  QtCharts.QBarSet("Casa")
            self.set6 =  QtCharts.QBarSet("Coisas Inuteis")
            self.set7 =  QtCharts.QBarSet("Serviços")
            self.set8 =  QtCharts.QBarSet("Streaming")
            self.set9 =  QtCharts.QBarSet("Urgencia")
            self.set10 = QtCharts.QBarSet("Gatos")
            self.set11 = QtCharts.QBarSet("Dogs")
            self.set12 = QtCharts.QBarSet("Medico")
            self.set13 = QtCharts.QBarSet("Viagem")
            self.set14 = QtCharts.QBarSet("Eletronicos")
            self.set15 = QtCharts.QBarSet("Domesticos")
            #VALORES
            ano = self.label_2.text()
            mes = self.label_3.text()
            valores = {'Janeiro':1,'Fevereiro':2,'Marco':3,'Abril':4,'Maio':5,'Junho':6,'Julho':7,'Agosto':8,'Setembro':9,'Outubro':10,'Novembro':11,'Dezembro':12}
            captura_int_mes = valores[mes]
            dias_mes = calendar.monthrange(int(ano),captura_int_mes)
            qt_dias =dias_mes[1]

            count = 0


            for i in range(qt_dias):
                for categoria in range(16):
                    id = EXTRATO_ATUAL
                    mes = self.label_3.text()
                    ano = self.label_2.text()
                    valores = {'Janeiro':'01','Fevereiro':'02','Marco':'03','Abril':'04','Maio':'05','Junho':'06','Julho':'07','Agosto':'08','Setembro':'09','Outubro':'10','Novembro':'11','Dezembro':'12'}
                    captura_int_mes = valores[mes]
                    dia = i+1
                    categ = ["Delivery","Apps Transporte","Comida","Mercado","Lazer","Casa","Coisas Inuteis","Serviços","Streaming","Urgencia","Gatos","Dogs","Medico","Viagem","Eletronicos","Domesticos"]
                    valores = card_db_test.Charts_values._gastos_por_dia(id,dia,captura_int_mes,ano,categ[categoria])
                    list_cet= [self.set0,self.set1,self.set2,self.set3,self.set4,self.set5,self.set6,self.set7,self.set8,self.set9,self.set10,self.set11,self.set12,self.set13,self.set14,self.set15]

                    list_cet[categoria].append(float(valores[0][0]))


    
            self.series = QtCharts.QStackedBarSeries()

            for i in range(16):
                list_cet= [self.set0,self.set1,self.set2,self.set3,self.set4,self.set5,self.set6,self.set7,self.set8,self.set9,self.set10,self.set11,self.set12,self.set13,self.set14,self.set15]
                self.series.append(list_cet[i])

    
            self.chart = QtCharts.QChart()
            self.chart.addSeries(self.series)
            self.chart.setTitle("Gastos por Data")
            self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

            #DATAS
            categories = []
            for i in range(qt_dias):
                categories.append(str(i+1))
                
                
            axis = QtCharts.QBarCategoryAxis()
            axis.append(categories)
            self.chart.createDefaultAxes()
            self.chart.setAxisX(axis, self.series)
            self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
            self.chart.legend().setVisible(True)
            self.chart.legend().setAlignment(Qt.AlignBottom)
            self.chart.setTheme(QtCharts.QChart.ChartTheme.ChartThemeBlueCerulean)
            self.chart.legend().setBackgroundVisible(True)
    
            self.chart_view = QtCharts.QChartView(self.chart)
            self.chart_view.setRenderHint(QPainter.Antialiasing)
            

        



            font3 = QFont()
            font3.setFamily(u"Bahnschrift Light Condensed")
            font3.setPointSize(12)
            font3.setBold(False)
            font3.setItalic(False)
            font3.setWeight(3)

            self.chart.legend().setFont(font3)
            self.chart.setFont(font3)
            self.chart.setTitleFont(font3)
            
            list = []
            self.frames = self.frame_chart_date_day
            for i in range(self.frames.count()):
                a = self.frames.itemAt(i).widget().objectName()
                list.append(a)
            count = len(list)

            if count ==0:

                self.frame_chart_date_day.addWidget(self.chart_view)



            else:
                while self.frame_chart_date_day.count():
                    child = self.frame_chart_date_day.takeAt(0)
                    childWidget = child.widget()
                    if childWidget:
                        childWidget.setParent(None)
                self.frame_chart_date_day.addWidget(self.chart_view)
                pass
        thread = threading.Thread(target=thead(self))
        thread.start()        


        
