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



class Add_values:
    
    def _add_new_bank(data,credit_card,rand_id):
        
        id = rand_id
        data = data
        
        if credit_card == True:
            
            #CONNECT DB
            a = (os.path.dirname(os.path.realpath(__file__)))
            banco = sqlite3.connect(''+a+'/bando_de_valores.db')
            cursor = banco.cursor()


            #CREATE INDEX
            cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_bank_active ON contas_bancarias(id)")
            #INSERT ID
            
            cursor.execute("INSERT INTO  contas_bancarias (id, cartao_credito_id) VALUES ('"+str(id)+"','"+str(id)+"')")
            cursor.execute("INSERT INTO  card_active (id) VALUES ('"+str(id)+"')")
            cursor.execute("CREATE TABLE IF NOT EXISTS extrato_cartao_"+str(id)+" (nome_cartao text, categoria_transacao text, nome_transacao text, data_transacao date, operacao text, parcelas text, valor_transacao text, id text,data_filter text,status_payment)")


            #ARGUMENTS:
            tabelas_db = ['contas_bancarias','card_active']
            colunas_contas = ['saldo_inicial','nome_banco','agencia','num_conta','titular']
            colunas_cartao = ['nome_cartao','titular','limite','final','vencimento','fechamento']
            coluns = [colunas_contas,colunas_cartao]
            #QUERY EXAMPLE (['C6', '1580', 'Jhonatan titualr card', '1010 final', 'venci 10', 'fefhca 10'], ['C6', 'Jhonatan', 'ag0111', 'cont 1010', 'r$1,580,00', 'Sim'])
            
            # data[0] TEM EM LISTA : [0] = ARGUMENTOS CONTA [1] = ARGUMENTOS CARTAO DE CREDITO
            for i in range(len(coluns)):
                for j in range(len(coluns[i])):
                    cursor.execute("UPDATE "+tabelas_db[i]+" SET "+coluns[i][j]+" = '"+str(data[i][j])+"' WHERE id = '"+str(id)+"'")
            banco.commit()
            banco.close()
            #RETURN:
            return True
    
        
        
        else:
            credit_card = 0
            
    def _default_bank(rand_id):
        default = rand_id
        
            
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()

        cursor.execute("INSERT INTO  config_contas (conta_padrao_bank) VALUES ('"+str(default)+"')")
        banco.commit()
        banco.close()
        return True


    def _add_new_lancamento(id_lancamento,dados):
            
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        #CREATE INDEX
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_new_lancamento ON new_lancamento(id_lancamento)")
        
        #INSERT ID
        id = id_lancamento
        cursor.execute("INSERT INTO  new_lancamento (id_lancamento) VALUES ('"+str(id)+"')")
        
        colunas = ['id_bank','data_lancamento','categoria','pagamento','valor','tipo','descricao']
        
        for i in range(len(dados)):
            cursor.execute("UPDATE new_lancamento SET "+colunas[i]+" = '"+str(dados[i])+"' WHERE id_lancamento = '"+str(id)+"'")
        
        banco.commit()
        banco.close()
        return True
    
    
    def _config_lancamento(id_lancamento,dados):
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        #CREATE INDEX
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_config_lancamento ON config_lancamento(id_lancamento)")
        
        #INSERT ID
        id = id_lancamento
        cursor.execute("INSERT INTO  config_lancamento (id_lancamento) VALUES ('"+str(id)+"')")

        colunas = ['id_bank','recorrente','recorrente_m_d_s_y','recorrente_dia','anexo']
        
        for i in range(len(dados)):
            cursor.execute("UPDATE config_lancamento SET "+colunas[i]+" = '"+str(dados[i])+"' WHERE id_lancamento = '"+str(id)+"'")
            
        banco.commit()
        banco.close()
        return True


    def _status_lancamento(id_lancamento,dados):
        


        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #CREATE INDEX
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_status_lancamento ON status_lancamento(id_lancamento)")
        
        #INSERT ID
        id = id_lancamento
        cursor.execute("INSERT INTO  status_lancamento (id_lancamento) VALUES ('"+str(id)+"')")

        colunas = ['id_bank','vencimento','status_pago']

        for i in range(len(dados)):
            cursor.execute("UPDATE status_lancamento SET "+colunas[i]+" = '"+str(dados[i])+"' WHERE id_lancamento = '"+str(id)+"'")

        banco.commit()
        banco.close()
        return True
    
    
    
    def _prioridade_value(id_lancamento,dados):
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        #CREATE INDEX
        cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_prioridade_value ON prioridade_value(id_lancamento)")
        
        #INSERT ID
        id = id_lancamento
        cursor.execute("INSERT INTO  prioridade_value (id_lancamento) VALUES ('"+str(id)+"')")
        
        colunas = ['id_bank','prioridade']
        
        for i in range(len(dados)):
            cursor.execute("UPDATE prioridade_value SET "+colunas[i]+" = '"+str(dados[i])+"' WHERE id_lancamento = '"+str(id)+"'")
        
        banco.commit()
        banco.close()
        return True     

    def _add_recorrent(ano,mes):
        #PRA VIR AQUI TEM QUE TER UM ID LANÇAMENTO E VIR COM O MES E ANO DO FILTRO DA TABELA
        # id_lancamento
        #id_bank
        #data_lancamento
        #categoria
        #pagamento
        #valor
        #tipo
        #descricao
        
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        return_all_recorrentes = Return_Values_Conditions.return_lancamentos_recorretes()


        return True

class Return_values:
    
    def return_banks_active():
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        
        cursor.execute("SELECT * FROM contas_bancarias")
        result = cursor.fetchall()
        banco.close()
        return result
    
    def banks_active_id():
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        
        cursor.execute("SELECT id,nome_banco FROM contas_bancarias")
        result = cursor.fetchall()
        banco.close()
        return result
    
    def return_table_lancamento():
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        # 1 = ID_LANCAMENTO = table new_lancamento
        # 2 = ID_CONTA / ID_CARTAO / ID BANK        table new_lancamento
        # 3 = TIPO: ENTRADA / SAIDA                 table new_lancamento
        # 4 = DATA DO LANÇAMENTO                    table new_lancamento
        # 5 = PRIORIDADE                            table prioridade_value
        # 6 = CATEGORIA                             table new_lancamento
        # 7 = METODO DE PAGAMENTO                   table new_lancamento
        # 8 = VALOR                                 table new_lancamento
        # 9 = STATUS                                table status_lancamento
        # 10 = SALDO                                table contas_bancarias ainda nao
        
        # cursor.execute("SELECT new_lancamento.id_lancamento,new_lancamento.id_bank,new_lancamento.tipo,new_lancamento.data_lancamento,prioridade_value.prioridade,new_lancamento.categoria,new_lancamento.pagamento,new_lancamento.valor,status_lancamento.status_pago,contas_bancarias.saldo_inicial FROM new_lancamento INNER JOIN prioridade_value ON new_lancamento.id_lancamento = prioridade_value.id_lancamento INNER JOIN status_lancamento ON new_lancamento.id_lancamento = status_lancamento.id_lancamento INNER JOIN contas_bancarias ON new_lancamento.id_conta = contas_bancarias.id")
        
        cursor.execute("\
                     SELECT new_lancamento.id_lancamento, \
                            new_lancamento.id_bank, \
                            new_lancamento.tipo, \
                            new_lancamento.data_lancamento, \
                            prioridade_value.prioridade, \
                            new_lancamento.categoria, \
                            new_lancamento.pagamento, \
                            new_lancamento.valor, \
                            status_lancamento.status_pago \
                     FROM new_lancamento \
                     INNER JOIN prioridade_value\
                     ON new_lancamento.id_lancamento = prioridade_value.id_lancamento \
                     INNER JOIN status_lancamento\
                     ON new_lancamento.id_lancamento = status_lancamento.id_lancamento")
                    

        result = cursor.fetchall()
        banco.close()
        
        return result
    
    def return_saldo():
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("SELECT saldo_inicial FROM contas_bancarias")
        result = cursor.fetchall()
        banco.close()
        return result[0][0]




class Return_Values_Conditions:
    
    def return_lancamentos_month(ano,mes):
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
                
        # 1 = ID_LANCAMENTO = table new_lancamento
        # 2 = ID_CONTA / ID_CARTAO / ID BANK        table new_lancamento
        # 3 = TIPO: ENTRADA / SAIDA                 table new_lancamento
        # 4 = DATA DO LANÇAMENTO                    table new_lancamento
        # 5 = PRIORIDADE                            table prioridade_value
        # 6 = CATEGORIA                             table new_lancamento
        # 7 = METODO DE PAGAMENTO                   table new_lancamento
        # 8 = VALOR                                 table new_lancamento
        # 9 = STATUS                                table status_lancamento
        # 10 = SALDO                                table contas_bancarias ainda nao
        
        cursor.execute("\
                        SELECT  new_lancamento.id_lancamento,\
                                new_lancamento.id_bank,\
                                new_lancamento.tipo,\
                                new_lancamento.data_lancamento,\
                                prioridade_value.prioridade,\
                                new_lancamento.categoria,\
                                new_lancamento.pagamento,\
                                new_lancamento.valor,\
                                status_lancamento.status_pago\
                        FROM new_lancamento\
                        INNER JOIN prioridade_value\
                        ON new_lancamento.id_lancamento = prioridade_value.id_lancamento\
                        INNER JOIN status_lancamento\
                        ON new_lancamento.id_lancamento = status_lancamento.id_lancamento\
                        WHERE strftime('%Y-%m', new_lancamento.data_lancamento) = '"+str(ano)+"-"+str(mes)+"'\
                        ORDER BY status_lancamento.status_pago DESC")

        
        result = cursor.fetchall()
        banco.close()
        return result

    

    def return_lancamentos_recorretes():
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
                
        # 1 = ID_LANCAMENTO = table new_lancamento
        # 2 = ID_CONTA / ID_CARTAO / ID BANK        table new_lancamento
        # 3 = TIPO: ENTRADA / SAIDA                 table new_lancamento
        # 4 = DATA DO LANÇAMENTO                    table new_lancamento
        # 5 = PRIORIDADE                            table prioridade_value
        # 6 = CATEGORIA                             table new_lancamento
        # 7 = METODO DE PAGAMENTO                   table new_lancamento
        # 8 = VALOR                                 table new_lancamento
        # 9 = STATUS                                table status_lancamento
        # 10 = SALDO                                table contas_bancarias ainda nao
        
        cursor.execute("\
                    SELECT  new_lancamento.id_lancamento,\
                            new_lancamento.id_bank,\
                            new_lancamento.tipo,\
                            prioridade_value.prioridade,\
                            new_lancamento.categoria,\
                            new_lancamento.pagamento,\
                            new_lancamento.valor,\
                            status_lancamento.status_pago,\
                    		config_lancamento.recorrente_m_d_s_y,\
                    		config_lancamento.recorrente_dia\
                    FROM new_lancamento\
                    INNER JOIN prioridade_value\
                    ON new_lancamento.id_lancamento = prioridade_value.id_lancamento\
                    INNER JOIN status_lancamento\
                    ON new_lancamento.id_lancamento = status_lancamento.id_lancamento\
                    INNER JOIN config_lancamento\
                    ON new_lancamento.id_lancamento = config_lancamento.id_lancamento\
                    WHERE config_lancamento.recorrente_m_d_s_y = 'Mes'\
                    ORDER BY status_lancamento.status_pago DESC")
        
        result = cursor.fetchall()
        banco.close()
        return result
    



        #id_lancamento
        #data_lancamento
        #recorrente_m_d_s_y
        #recorrente_dia
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("\
                        SELECT  new_lancamento.id_lancamento,\
                                new_lancamento.data_lancamento,\
                                config_lancamento.recorrente_m_d_s_y,\
                                config_lancamento.recorrente_dia\
                        FROM new_lancamento\
                        INNER JOIN config_lancamento\
                        ON new_lancamento.id_lancamento = config_lancamento.id_lancamento\
                        WHERE new_lancamento.id_lancamento = '"+id+"' AND strftime('%Y-%m', new_lancamento.data_lancamento) = '"+str(ano)+"-"+str(mes)+"'")
        dados = cursor.fetchall()
        return dados



    def _retur_data_recorrente_mes(id):
        #id_lancamento
        #data_lancamento
        #recorrente_m_d_s_y
        #recorrente_dia
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("SELECT config_lancamento.recorrente_dia FROM config_lancamento WHERE id_lancamento = '"+id+"'")
        dados = cursor.fetchall()
        return dados[0][0]
# ano = '2022'
# mes = '10'
