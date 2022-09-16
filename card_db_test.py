from ctypes import util
from operator import index
from re import S
import sqlite3
from PySide2.QtCore import *
import os.path
from datetime import datetime
from re import S
from cairo import Extend
from dateutil.relativedelta import relativedelta
from datetime import datetime
from datetime import date 
import calendar



class Ui_db: # valores fixos
    
    def _titular(id):
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #QUERY
        cursor.execute("SELECT titular FROM card_active WHERE id = "+str(id)+" ")
        result = cursor.fetchall()
        
        #RETURN:
        return result[0][0]

    def _final_cartao(id):
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #QUERY
        cursor.execute("SELECT final FROM card_active WHERE id = "+str(id)+" ")
        result = cursor.fetchall()
        
        #RETURN:
        return result[0][0]

    def _limite(id):
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #QUERY
        cursor.execute("SELECT limite FROM card_active WHERE id = "+str(id)+" ")
        result = cursor.fetchall()
        
        #FORMAT:
        format = result[0][0]
        format=("{:.2f}".format(format))
        
        #RETURN:
        return str(format)
      
    def _vencimento(id):
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #QUERY
        cursor.execute("SELECT vencimento FROM card_active WHERE id = "+str(id)+" ")
        result = cursor.fetchall()
        
        #RETURN:
        return result[0][0]
    def _fechamento(id):
            
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #QUERY
        cursor.execute("SELECT fechamento FROM card_active WHERE id = "+str(id)+" ")
        result = cursor.fetchall()
        print(result,"db_test valu fechamento")
        #RETURN:
        return result[0][0]
     
    def _cartao(id):
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #QUERY
        cursor.execute("SELECT nome_cartao FROM card_active WHERE id = "+str(id)+" ")
        result = cursor.fetchall()
        
        #RETURN:
        return result[0][0]

    def _extrato(id,mes): #EXTRATO MENSAL 
        
        #CONNECT DB:
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        card = 'extrato_cartao_%s'%(id)
        
        #QUERY:
        cursor.execute("SELECT * FROM "+str(card)+"  where strftime('%m%Y', data_filter) = '"+mes+"' ORDER BY data_filter DESC")
        result = cursor.fetchall()
        
        #QT INDEX LINES:
        lines = len(result)
        
        #RETURN:
        return [int(lines),result]



class Return_Values_Calcs:
    
    def _fatural_atual(id,mes): # TODO Calculo Coluna Paga/Pendente
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        card = 'extrato_cartao_%s'%(id)
        print("card escolhido",card)
        
        #QUERY
        cursor.execute("SELECT SUM (valor_transacao) FROM "+str(card)+" where strftime('%Y-%m', data_filter) = '"+mes+"' GROUP BY status_payment  HAVING status_payment = 'pendente' ")
        result=cursor.fetchall()
        
        #NONE:

        if not result:
            format = '0.00'
            
        else:
            
        #FORMAT TO FLOAT-STRING:
            format = result[0][0]
            format=("{:.2f}".format(format))
        
        #RETURN:
        return str(format)

    def _limite_utilizado(id): # TODO Calculo Funcao - limite ui
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        card = 'extrato_cartao_%s'%(id)

        
        
        #QUERY:
        cursor.execute("SELECT SUM (valor_transacao) FROM "+str(card)+" GROUP BY status_payment  HAVING status_payment = 'pendente'  ")
        result = cursor.fetchall()
        
        #NONE:

        if not result:
            format = '0'
            
        else:
            
        #FORMAT TO FLOAT-STRING:
            format = result[0][0]
            format=("{:.2f}".format(format))
        
        #RETURN:

        return str(format)
    
    def _limite_disponivel(id): # TODO Calculo
        
        #CONNECT DB
        limite = Ui_db._limite(id)
        utilizado = Return_Values_Calcs._limite_utilizado(id)
        
        #OPERATION:
        
        result = float(limite) - float(utilizado)
        
        #FORMAT:
        format = result
        format=("{:.2f}".format(format))
        
        #RETURN:
        return str(format)
    
    def _porcentagem_utilizada(id): # TODO Calculo
        
        #CONNECT DB
        limite = Ui_db._limite(id)
        utilizado = Return_Values_Calcs._limite_utilizado(id)

        #OPERATION:
        result = float(utilizado)*100/float(limite)
        
        #FORMAT TO FLOAT-STRING:
        result=("{:.2f}".format(result))
        
        #RETURN:
        return str(result)

    def _fatura_paga(id,mes): # TODO Consulta
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #QUERY
        cursor.execute("SELECT nome_cartao FROM card_active WHERE id = "+str(id)+" ")
        result = cursor.fetchall()
        
        #RETURN:
        return result[0][0]

    def _filtra_compra(id,ano,mes,dia): # TODO filtra compra por DD/MM/AAAA
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        card = 'extrato_cartao_%s'%(id)
        data_select = "%s%s%s"%(ano,mes,dia)
        
        #QUERY
        cursor.execute("SELECT * FROM "+str(card)+"  where strftime('%Y%m%d', data_transacao) = '"+data_select+"' ") #TODO Carrega FINAL_CARTAO DB e seta
        result = cursor.fetchall()
        
        
        #QT INDEX LINES:
        lines = len(result)
        
        #RETURN:
        return result
        
    def _todas_faturas(id,ano):
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        card = 'extrato_cartao_%s'%(id)
        
        
        lista_meses= []

        mes = '01'
        ano = ano
        janeiro = 0

        

      
        
        for i in range(12):
            nome_mes = i+1
            if  janeiro > 0:
                add = 1
            else:
                add = 0
                
            format_date = datetime.strptime(mes+ano, '%m%Y')
            date = format_date.date()
            soma_mes = relativedelta(months=+add)
            result= date + soma_mes
            ab = str(result)
            ano = ab[0:4]
            mes =  ab[5:7]
            filter = "%s-%s"%(ano,mes)
            janeiro = janeiro +1
            
        #QUERY
            #apenas pendente             cursor.execute("SELECT SUM (valor_transacao) FROM "+str(card)+"  where strftime('%Y-%m', data_filter) = '"+filter+"' GROUP BY status_payment  HAVING status_payment = 'pendente' ") #TODO Carrega FINAL_CARTAO DB e seta

            cursor.execute("SELECT SUM (valor_transacao) FROM "+str(card)+"  where strftime('%Y-%m', data_filter) = '"+filter+"'") #TODO Carrega FINAL_CARTAO DB e seta
            result = cursor.fetchall()
            lista_meses.append(result[0][0])
            invert = {'01':'Janeiro','02':'Fevereiro','03':'Marco','04':'Abril','05':'Maio','06':'Junho','07':'Julho','08':'Agosto','09':'Setembro','10':'Outubro','11':'Novembro','12':'Dezembro'}


        #QT INDEX LINES:
        lines = len(result)
        
        #RETURN:
        return lista_meses

    def _pagar_fatura(id,mes,ano):
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        card = 'extrato_cartao_%s'%(id)
        data_select = "%s%s"%(ano,mes)

        #QUERY
            #TODO 1 POR LINHA


        cursor.execute("UPDATE "+card+" SET status_payment =  'pago'  where strftime('%Y%m', data_filter) = '"+data_select+"'")
        banco.commit()
        
        
        #QT INDEX LINES:

        
        #RETURN:
        return 0

    def _status_fatura(id,mes,ano):
                
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        card = 'extrato_cartao_%s'%(id)
        data_select = "%s%s"%(ano,mes)

        
        today = datetime.today()
        soma_mes = relativedelta(months=+1)
        actual= today + soma_mes
        actual = str(actual)

        data_sell = datetime.strptime(data_select, '%Y%m')


        if data_sell < today:
            anterior = True
        else:
            anterior = False

        #QUERY
        cursor.execute("SELECT (status_payment) FROM "+str(card)+"  where strftime('%Y%m', data_filter) = '"+data_select+"' GROUP BY status_payment  HAVING status_payment = 'pendente'") #TODO Carrega FINAL_CARTAO DB e seta
        result = cursor.fetchall()

        try:
            if result[0][0] == 'pendente':
                return 'pendente'
        except:
            pass
        
        cursor.execute("SELECT (status_payment) FROM "+str(card)+"  where strftime('%Y%m', data_filter) = '"+data_select+"' GROUP BY status_payment  HAVING status_payment = 'pago'") #TODO Carrega FINAL_CARTAO DB e seta
        result = cursor.fetchall()

        try:
            if result[0][0] == 'pago':
                return 'pago'
            
        except:
            if anterior == True:
                return 'pago'
            else:
                return "proximas"
            


class Charts_values:
    
    def _gastos_categoria(id,mes,ano):
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        card = 'extrato_cartao_%s'%(id)
        
        data_select = "%s%s"%(ano,mes)

        
        #QUERY:
        categoria = ['Delivery','Apps Transporte','Comida','Mercado','Lazer','Casa','Coisas Inuteis','Serviços','Streaming','Urgencia','Gatos','Dogs','Medico','Viagem','Eletronicos','Domesticos']
        valores = []
        lista_filtrada =[]

        
        count = 0
        for vezes in categoria: 
            cursor.execute("SELECT SUM (valor_transacao) FROM "+str(card)+" where strftime('%Y%m', data_filter) = '"+data_select+"' GROUP BY categoria_transacao  HAVING categoria_transacao = '"+categoria[count]+"'")
            dadoslidos=cursor.fetchall()
            

            if not dadoslidos:
                count = count+1
                
            else:
                valores.append(dadoslidos[0][0])
                lista_filtrada.append(categoria[count])
                count = count+1


        return lista_filtrada,valores

    def _gastos_por_dia(id,dia,mes,ano,categoria):
                
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        card = 'extrato_cartao_%s'%(id)
        
        lista_filtrada =[]

        dia = int(dia)
        if dia <= 9:
            dia = "0%s"%(dia)

                
        data_select = "%s%s%s"%(ano,mes,dia)
        
            
        cursor.execute("SELECT SUM (valor_transacao) FROM "+str(card)+" where strftime('%Y%m%d', data_filter) = '"+data_select+"' GROUP BY categoria_transacao  HAVING categoria_transacao = '"+categoria+"'")
        dadoslidos=cursor.fetchall()
        if not dadoslidos:
            lista_filtrada.append('0')
        else:
            lista_filtrada.append([dadoslidos[0][0]])

        return lista_filtrada
        
        

    def _cat_ext_gastos_por_dia(id,mes,ano):
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        card = 'extrato_cartao_%s'%(id)
        
        
        lista_filtrada =[]


                
        data_select = "%s%s"%(ano,mes)
        
        cursor.execute("SELECT categoria_transacao FROM "+str(card)+" where strftime('%Y%m', data_filter) = '"+data_select+"' GROUP BY categoria_transacao")
        dadoslidos=cursor.fetchall()
        index = 0
        for i in dadoslidos:
            lista_filtrada.append(dadoslidos[index][0])
            index +=1
        return lista_filtrada
    
    def _count_dias_charts(id,mes,ano):
            #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        card = 'extrato_cartao_%s'%(id)
        
        
        lista_filtrada =[]


                
        data_select = "%s%s"%(ano,mes)
        
        # cursor.execute("SELECT SUM (valor_transacao) FROM "+str(card)+" where strftime('%Y%m%d', data_filter) = '"+data_select+"' GROUP BY categoria_transacao  HAVING categoria_transacao = '"+categoria+"'")
        cursor.execute("SELECT data_filter FROM "+str(card)+" where strftime('%Y%m', data_filter) = '"+data_select+"' GROUP BY data_filter")
        dadoslidos=cursor.fetchall()
        index = 0
        for i in dadoslidos:
            lista_filtrada.append(dadoslidos[index][0][8:10])
            index +=1
        return lista_filtrada



class Main_page_values:
    
    def _cards_ids_all():
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        
        
        #QUERY:
        cursor.execute("SELECT id FROM card_active")
        result = cursor.fetchall()
        return result
    
    def _cards_names_all():
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        
        
        #QUERY:
        cursor.execute("SELECT id FROM card_active")
        result = cursor.fetchall()
        return result
    
    def _limite_all():
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        limite = []
        cards_active = Main_page_values._cards_ids_all()
        
        #QUEDY:
        index = 0
        for i in cards_active:
            card = 'extrato_cartao_%s'%(cards_active[index][0])

            cursor.execute("SELECT limite FROM card_active WHERE id = "+str(cards_active[index][0])+" ")
            result = cursor.fetchall()
            print(result)
            #NONE:

            if not result:
                format = '0'

            else:

            #FORMAT TO FLOAT-STRING:
                format = result[0][0]
                format=("{:.2f}".format(format))
            index +=1
            limite.append(float(format))
        
        #RETURN:
        soma = sum(limite)
        return str(soma)
    
    def _limite_utilizado_all():
        
        
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        utilizado = []
        cards_active = Main_page_values._cards_ids_all()
        
        #QUEDY:
        index = 0
        for i in cards_active:
            card = 'extrato_cartao_%s'%(cards_active[index][0])
            #QUERY:
            cursor.execute("SELECT SUM (valor_transacao) FROM "+str(card)+" GROUP BY status_payment  HAVING status_payment = 'pendente'  ")
            result = cursor.fetchall()
            
            #NONE:

            if not result:
                format = '0'

            else:

            #FORMAT TO FLOAT-STRING:
                format = result[0][0]
                format=("{:.2f}".format(format))
            index +=1
            utilizado.append(float(format))

        #RETURN:
        soma = sum(utilizado)
        
        format = soma
        format=("{:.2f}".format(format))
        
        return str(format)
    def _limite_disponivel_all():
        #CONNECT DB
    
        
        
        
        
        utilizado = Main_page_values._limite_utilizado_all()
        limite = Main_page_values._limite_all()
        
        # ARGS:
        
        
        
        #OPERATION:
        
        result = float(limite) - float(utilizado)

        #FORMAT:
        format = result
        format=("{:.2f}".format(format))
            #FORMAT TO FLOAT-STRING:

  
        
        #RETURN:
        return str(format)
    def _porcentagem_utilizada_all(): # TODO Calculo
        
        #CONNECT DB
        limite = Main_page_values._limite_all()
        utilizado = Main_page_values._limite_utilizado_all()

        #OPERATION:
        result = float(utilizado)*100/float(limite)
        
        #FORMAT TO FLOAT-STRING:
        # result=("{:.2f}".format(result))
        
        #RETURN:
        return int(result)
    
    
    def _fatura_atual_all(anomes):
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        lista_de_faturas = []
        cards = Main_page_values._cards_ids_all()
        index = 0
        for i in cards:
            card = 'extrato_cartao_%s'%(cards[index][0])
            print("card escolhido",card)

            #QUERY
            cursor.execute("SELECT SUM (valor_transacao) FROM "+str(card)+" where strftime('%Y-%m', data_filter) = '"+anomes+"' GROUP BY status_payment  HAVING status_payment = 'pendente' ")
            result=cursor.fetchall()
            print("result",result)
            #NONE:

            if not result:
                format = '0.00'
                lista_de_faturas.append(float(format))

            else:

            #FORMAT TO FLOAT-STRING:
                format = result[0][0]
                format=("{:.2f}".format(format))
                lista_de_faturas.append(float(format))
            index +=1
        #RETURN:
        soma = sum(lista_de_faturas)
        format = soma
        format=("{:.2f}".format(format))
        
        return str(format)
        
        
        
        
    def _todas_faturas_all(id,ano):
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        card = 'extrato_cartao_%s'%(id)
        
        
        lista_meses= []

        mes = '01'
        ano = ano
        janeiro = 0

        

      
        
        for i in range(12):
            nome_mes = i+1
            if  janeiro > 0:
                add = 1
            else:
                add = 0
                
            format_date = datetime.strptime(mes+ano, '%m%Y')
            date = format_date.date()
            soma_mes = relativedelta(months=+add)
            result= date + soma_mes
            ab = str(result)
            ano = ab[0:4]
            mes =  ab[5:7]
            filter = "%s-%s"%(ano,mes)
            janeiro = janeiro +1
            
        #QUERY
            #apenas pendente             cursor.execute("SELECT SUM (valor_transacao) FROM "+str(card)+"  where strftime('%Y-%m', data_filter) = '"+filter+"' GROUP BY status_payment  HAVING status_payment = 'pendente' ") #TODO Carrega FINAL_CARTAO DB e seta

            cursor.execute("SELECT SUM (valor_transacao) FROM "+str(card)+"  where strftime('%Y-%m', data_filter) = '"+filter+"'") #TODO Carrega FINAL_CARTAO DB e seta
            result = cursor.fetchall()
            lista_meses.append(result[0][0])
            invert = {'01':'Janeiro','02':'Fevereiro','03':'Marco','04':'Abril','05':'Maio','06':'Junho','07':'Julho','08':'Agosto','09':'Setembro','10':'Outubro','11':'Novembro','12':'Dezembro'}


        #QT INDEX LINES:
        lines = len(result)
        
        #RETURN:
        return lista_meses



class update_values:
    
    def update_cards_config(id,ti,li,fi,ve,fe):
        print("teste",id,ti,li,fi,ve,fe)
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #ARGUMENTS:
        tabela ="card_active"
        colunas = ["titular","limite","final","vencimento","fechamento"]
        valuess = [ti,li,fi,ve,fe]
        for i in range(len(colunas)):
            cursor.execute("UPDATE "+str(tabela)+" SET "+str(colunas[i])+" = '"+str(valuess[i])+"' WHERE id = '"+str(id)+"'")
            banco.commit()
        banco.commit()
        banco.close()
        
        #RETURN:
        return True
        
    
        
# ['01', '04', '05', '06', '08', '11', '12', '13']
# id = '284261'
# mes= '08'
# # dia ='1'
# ano = '2022'
# # a = Return_Values_Calcs._fatural_atual(id,mes)
# # print(a)

# a = Main_page_values._cards_ids_all()
# print(a)


# all_ids = Main_page_values._cards_ids_all() #get all i
# index_ids = 0
# for ids in all_ids:

#     todas_as_faturas = Return_Values_Calcs._todas_faturas(ids[0],ano)

#     print(all_ids[0][0])
# id = '936038'
# mes_y  = '2022-09'
# a = Return_Values_Calcs._fatural_atual(id,mes_y)
