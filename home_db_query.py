from random import randint
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
import card_db_test



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
            credit_card = False
            a = (os.path.dirname(os.path.realpath(__file__)))
            banco = sqlite3.connect(''+a+'/bando_de_valores.db')
            cursor = banco.cursor()
            
            #CREATE INDEX
            cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_bank_active ON contas_bancarias(id)")
            #INSERT ID
            cursor.execute("INSERT INTO  contas_bancarias (id) VALUES ('"+str(id)+"')")

            #ARGUMENTS:
            tabelas_db = ['contas_bancarias']
            colunas_contas = ['nome_banco','titular','agencia','num_conta','saldo_inicial','cartao_credito_id']
            coluns = [colunas_contas]
            #QUERY EXAMPLE (['C6', '1580', 'Jhonatan titualr card', '1010 final', 'venci 10', 'fefhca 10'], ['C6', 'Jhonatan', 'ag0111', 'cont 1010', 'r$1,580,00', 'Sim'])
            # data[0] TEM EM LISTA : [0] = ARGUMENTOS CONTA
            for i in range(len(data[0])):
                # print(data[0][i])
                cursor.execute("UPDATE "+tabelas_db[0]+" SET "+colunas_contas[i]+" = '"+str(data[0][i])+"' WHERE id = '"+str(id)+"'")
                banco.commit()
            
            banco.close()
            return True
            
    def _default_bank(rand_id):
        default = rand_id
        
            
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()

        # VERIFY IF DEFAULT BANK IS ALREADY SET
        cursor.execute("SELECT * FROM config_contas")
        data = cursor.fetchall()
        if len(data) == 0:
            cursor.execute("INSERT INTO  config_contas (conta_padrao_bank) VALUES ('"+str(default)+"')")
            banco.commit()
        else:
            cursor.execute("UPDATE config_contas SET conta_padrao_bank = '"+str(default)+"'")
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

    def _add_new_lancamento_recorrente(id_lancamento,id_bank,mes,ano):
            
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #TABLE status_lancamento
        #id_lancamento
        #id_bank
        #vencimento
        #status_pago
        
        #VERIFI_DATA_RECORRENCIA
        dia_reco = Return_Values_Conditions._retur_data_recorrente_mes(id_lancamento)
        fomrt_date = str(ano)+'-'+str(mes)+'-'+str(dia_reco)
        cursor.execute("INSERT INTO status_lancamento (id_lancamento,id_bank,vencimento,status_pago) VALUES ('"+str(id_lancamento)+"','"+str(id_bank)+"','"+str(fomrt_date)+"','pago')")
        banco.commit()
        banco.close()
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
                     SELECT DISTINCT new_lancamento.id_lancamento, \
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

    def return_saldo_banks(id_bank):
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("SELECT saldo_inicial FROM contas_bancarias WHERE id = '"+str(id_bank)+"'")
        result = cursor.fetchall()
        banco.close()
        print("???",result)
        if not result:
            print("retornou none")
            return None
  
        else:
            print("retornou valor")
            return result[0][0]

    def _return_default_bank():
        #id_lancamento
        #data_lancamento
        #recorrente_m_d_s_y
        #recorrente_dia
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("SELECT config_contas.conta_padrao_bank FROM config_contas")
        dados = cursor.fetchall()
        
        if dados:
            return dados[0][0]
        else:
            return None
    
    
class Return_Values_Conditions:
    
    
    def return_talbe_banks(id_bank,id_card):#RETONA DADOS DO BANCO E DO CARTAO DE CREDITO PARA TABLE
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        if id_card != "Não":
            cursor.execute("SELECT contas_bancarias.nome_banco,\
	                               contas_bancarias.agencia,\
	                               contas_bancarias.num_conta,\
	                               contas_bancarias.saldo_inicial,\
	                               card_active.limite,\
	                               card_active.final,\
	                               card_active.titular,\
	                               card_active.vencimento,\
	                               card_active.fechamento\
                            FROM contas_bancarias\
                            INNER JOIN card_active\
                            ON contas_bancarias.id = card_active.id\
                            WHERE contas_bancarias.id ='"+str(id_bank)+"'")
            dados = cursor.fetchall()
            banco.close()
            print("dados",dados)
            return dados[0]
            
        else:
            cursor.execute("SELECT contas_bancarias.nome_banco,\
                                   contas_bancarias.agencia,\
                                   contas_bancarias.num_conta,\
                                   contas_bancarias.saldo_inicial\
                            FROM contas_bancarias\
                            WHERE contas_bancarias.id ='"+str(id_bank)+"'")
            dados = cursor.fetchall()
            banco.close()
            return dados[0]
    
        
    
    def get_valor_transacao(id_lancamento,id_bank,tipo,ano,mes):
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("SELECT valor FROM new_lancamento WHERE id_lancamento = '"+str(id_lancamento)+"' AND id_bank = '"+str(id_bank)+"' AND tipo = '"+str(tipo)+"' AND strftime('%Y',data_lancamento) = '"+str(ano)+"' AND strftime('%m',data_lancamento) = '"+str(mes)+"'")
        dados = cursor.fetchall()
        return dados[0][0]
    
    
    def _update_default_bank(id_bank):
        #id_lancamento
        #data_lancamento
        #recorrente_m_d_s_y
        #recorrente_dia
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        #VERIFICA SE JA TEM UM PADRAO
        cursor.execute("SELECT config_contas.conta_padrao_bank FROM config_contas")
        dados = cursor.fetchall()
        if dados:
            cursor.execute("UPDATE config_contas SET conta_padrao_bank = '"+str(id_bank)+"'")
            banco.commit()
            banco.close()
            return True
        else:
            cursor.execute("INSERT INTO config_contas(conta_padrao_bank) VALUES('"+str(id_bank)+"')")
            banco.commit()
            banco.close()
            return True

        
        
    def _return_ag_b_t_c(id):
        #TITULAR
        #AGENCIA
        #CONTA
        #SALDO
        #BANCO

        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()

        cursor.execute("SELECT titular,agencia,num_conta,saldo_inicial,nome_banco FROM contas_bancarias WHERE id = '"+str(id)+"'")
        dados = cursor.fetchall()
        banco.close()
        if dados:
            return dados[0]
        else:
            return None
    
    def return_lancamentos_month(ano,mes): # TODO RETONA COMPRAS NAO RECORRENTES
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
                                status_lancamento.status_pago,\
                                config_lancamento.recorrente\
                        FROM new_lancamento\
                        INNER JOIN prioridade_value\
                        ON new_lancamento.id_lancamento = prioridade_value.id_lancamento\
                        INNER JOIN status_lancamento\
                        ON new_lancamento.id_lancamento = status_lancamento.id_lancamento\
                        INNER JOIN config_lancamento\
                        ON new_lancamento.id_lancamento = config_lancamento.id_lancamento\
                        WHERE strftime('%Y-%m', new_lancamento.data_lancamento) = '"+str(ano)+"-"+str(mes)+"' AND config_lancamento.recorrente = 'Não'\
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
        
        # cursor.execute("\
        #             SELECT DISTINCT new_lancamento.id_lancamento,\
        #                     new_lancamento.id_bank,\
        #                     new_lancamento.tipo,\
        #                     prioridade_value.prioridade,\
        #                     new_lancamento.categoria,\
        #                     new_lancamento.pagamento,\
        #                     new_lancamento.valor,\
        #                     status_lancamento.status_pago,\
        #             		config_lancamento.recorrente_m_d_s_y,\
        #             		config_lancamento.recorrente_dia\
        #             FROM new_lancamento\
        #             INNER JOIN prioridade_value\
        #             ON new_lancamento.id_lancamento = prioridade_value.id_lancamento\
        #             INNER JOIN status_lancamento\
        #             ON new_lancamento.id_lancamento = status_lancamento.id_lancamento\
        #             INNER JOIN config_lancamento\
        #             ON new_lancamento.id_lancamento = config_lancamento.id_lancamento\
        #             WHERE config_lancamento.recorrente_m_d_s_y = 'Mes'\
        #             ORDER BY status_lancamento.status_pago DESC")
        cursor.execute("\
                        SELECT DISTINCT new_lancamento.id_lancamento,\
                                new_lancamento.id_bank,\
                                new_lancamento.tipo,\
                                prioridade_value.prioridade,\
                                new_lancamento.categoria,\
                                new_lancamento.pagamento,\
                                new_lancamento.valor,\
                        		config_lancamento.recorrente_m_d_s_y,\
                        		config_lancamento.recorrente_dia\
                        FROM new_lancamento\
                        INNER JOIN prioridade_value\
                        ON new_lancamento.id_lancamento = prioridade_value.id_lancamento\
                        INNER JOIN config_lancamento\
                        ON new_lancamento.id_lancamento = config_lancamento.id_lancamento\
                        WHERE config_lancamento.recorrente_m_d_s_y = 'Mes'")
        
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

    def _return_if_recorrente(id):
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("\
                        SELECT  config_lancamento.recorrente\
                        FROM config_lancamento\
                        WHERE config_lancamento.id_lancamento = '"+id+"'")
        dados = cursor.fetchall()
        print("recos?",dados)
        if dados[0][0] == 'Não':
            return False
        else:   
            return True


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

    def _return_saldo(id):
        #id_bank
        #saldo
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("SELECT contas_bancarias.saldo_inicial FROM contas_bancarias WHERE id= '"+id+"'")
        dados = cursor.fetchall()
        return dados[0][0]

    def _verifi_pago_recorrente(id,mes,ano):
        #id_lancamento
        #data_lancamento
        #recorrente_m_d_s_y
        #recorrente_dia
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("\
            SELECT status_lancamento.status_pago\
            FROM status_lancamento\
            WHERE status_lancamento.id_lancamento = '"+id+"' AND strftime('%Y-%m', status_lancamento.vencimento) = '"+str(ano)+"-"+str(mes)+"'")
        dados = cursor.fetchall()
        print(dados)
        if not dados:
            return False
        elif dados[0][0] == 'pendente':
            return False
        else:
            return True


    def _return_descricao(id):
        #id_lancamento
        #data_lancamento
        #recorrente_m_d_s_y
        #recorrente_dia
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("SELECT new_lancamento.descricao FROM new_lancamento WHERE id_lancamento = '"+id+"'")
        dados = cursor.fetchall()
        return dados[0][0]
    
    def _verify_id_is_credit_card(id):
        #id_lancamento
        #data_lancamento
        #recorrente_m_d_s_y
        #recorrente_dia
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("SELECT card_active.id FROM card_active WHERE id = '"+id+"'")
        dados = cursor.fetchall()
        if not dados:
            return False
        else:
            return True

    
    def _return_name_bank(id):
 
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("SELECT contas_bancarias.nome_banco FROM contas_bancarias  WHERE id = '"+id+"'")
        dados = cursor.fetchall()
        return dados[0][0]
    
    def _return_bank_id(id):

        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("SELECT * FROM contas_bancarias  WHERE id = '"+id+"'")
        dados = cursor.fetchall()
        return dados

    def _detalhes_lancamento(id,bank,mes,ano,tipo):


        print("id",id,"bank",bank,"mes",mes,"ano",ano,"tipo",tipo)
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        like = 'fatu%'
        if tipo == 'fatura':
            cursor.execute("\
                SELECT pagamentos_saldo.id_bank,\
                       pagamentos_saldo.id_discount,\
                       pagamentos_saldo.ref_vencimento,\
                       pagamentos_saldo.data_pagamento\
                FROM pagamentos_saldo\
                WHERE pagamentos_saldo.id_bank = '"+bank+"' AND strftime('%Y-%m', pagamentos_saldo.ref_vencimento) = '"+str(ano)+"-"+str(mes)+"'\
                AND pagamentos_saldo.tipo_e_s LIKE '"+like+"'\
                ORDER BY pagamentos_saldo.data_pagamento DESC")
            dados = cursor.fetchall()
            print(dados)
        else:
            cursor.execute("\
                SELECT pagamentos_saldo.id_bank,\
                       pagamentos_saldo.ref_vencimento,\
                       pagamentos_saldo.data_pagamento\
                FROM pagamentos_saldo\
                WHERE pagamentos_saldo.id_lancamento = '"+id+"' AND strftime('%Y-%m', pagamentos_saldo.ref_vencimento) = '"+str(ano)+"-"+str(mes)+"' and pagamentos_saldo.id_bank = '"+bank+"'")
            dados = cursor.fetchall()
            print(dados)
            
        banco.close()

        if dados:
            
            return dados
        else:
            return False
        

    
class Saldos:

    def Set_saldo_inicial():

        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        #SELECT DEFAULT BANK
        cursor.execute("SELECT config_contas.conta_padrao_bank FROM config_contas")
        conta_padrao = cursor.fetchall()
        print("conta padrao:",conta_padrao)
        if conta_padrao:
            #SELECT SALDO INICIAL
            cursor.execute("SELECT contas_bancarias.saldo_inicial FROM contas_bancarias WHERE id = '"+str(conta_padrao[0][0])+"'")
            saldo_inicial = cursor.fetchall()

            if saldo_inicial:
                saldo_inicial = saldo_inicial[0][0]

            else:
                saldo_inicial = str(0)
        else:
            saldo_inicial = str(0)
       
        return saldo_inicial
    

    def _pagar_lancamento(id,id_bank,tipo,ano,mes):
        #id_lancamento
        #ID_BANK
        #TIPO_E_S
        #VALOR
        #DATA DE PAGAMENTO
        #SALDO_ATUAL
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()

        print("-------------------------")
 
        #GET SALDO ATUAL
        cursor.execute("SELECT contas_bancarias.saldo_inicial FROM contas_bancarias WHERE id = '"+str(id_bank)+"'")
        saldo_inicial = cursor.fetchall()
        saldo_inicial = saldo_inicial[0][0]
        print(saldo_inicial)
        #GET VALOR DO LANÇAMENTO
        cursor.execute("SELECT new_lancamento.valor FROM new_lancamento WHERE id_lancamento = '"+str(id)+"'")
        
        valor_lancamento = cursor.fetchall()
        valor_lancamento = valor_lancamento[0][0]

        #OPERACAO PARA SALDO ATUAL
        if tipo == "Entrada":
            saldo_atual = float(saldo_inicial) + (valor_lancamento)
        else:
            saldo_atual = float(saldo_inicial) - float(valor_lancamento)
        print(tipo,"-",valor_lancamento,"=",saldo_atual)
        print(saldo_atual,"SALTDO TIOI")
        # SELECT DADOS DO LANÇAMENTO E INSERT IN NEW_LANCAMENTO
        cursor.execute("INSERT INTO pagamentos_saldo (id_lancamento,id_bank,tipo_e_s,valor,ref_vencimento,data_pagamento,saldo_atual)\
                        SELECT new_lancamento.id_lancamento,\
                               new_lancamento.id_bank,\
                               new_lancamento.tipo,\
                               new_lancamento.valor,\
                               status_lancamento.vencimento,\
                               DateTime('now','localtime'),\
                               "+str(saldo_atual)+"\
                        FROM new_lancamento \
                        INNER JOIN status_lancamento\
                        ON new_lancamento.id_lancamento = status_lancamento.id_lancamento\
                        WHERE new_lancamento.id_lancamento = '"+str(id)+"' AND new_lancamento.id_bank = '"+str(id_bank)+"'\
                        AND strftime('%Y-%m', status_lancamento.vencimento) = '"+str(ano)+"-"+str(mes)+"'")
        banco.commit()

        # UPDATE SALDO ATUAL
        cursor.execute("UPDATE contas_bancarias SET saldo_inicial = '"+str(saldo_atual)+"' WHERE id = '"+str(id_bank)+"'")
        banco.commit()
        
        #UPDATE STATUS DO LANÇAMENTO
        cursor.execute("UPDATE status_lancamento SET status_pago = 'pago' WHERE id_lancamento = '"+str(id)+"' AND status_lancamento.id_bank = '"+str(id_bank)+"'AND strftime('%Y-%m',status_lancamento.vencimento) = '"+str(ano)+"-"+str(mes)+"'")

        print("-------------------------")
        banco.commit()
        banco.close()
        return True
    
    
    def _pagar_fatura(id_bank,id_no_bank,mes,ano):


        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()

        if  id_no_bank == 0:
            id_bank_s_n = id_bank
            id_discount = id_bank
        else:
            id_bank_s_n = id_no_bank #SE NAO TEM CONTA VINCULADO AO CARTAO DE CREDITO
            id_discount = id_bank #id da conta que vai receber o desconto


        print("-------------------------")

        #GET SALDO ATUAL
        cursor.execute("SELECT contas_bancarias.saldo_inicial FROM contas_bancarias WHERE id = '"+str(id_discount)+"'")
        saldo_inicial = cursor.fetchall()
        saldo_inicial = saldo_inicial[0][0]
        print(saldo_inicial)
        #GET VALOR DA FATURA
        format_anomes = str(ano)+"-"+str(mes)
        valor_fatu = card_db_test.Return_Values_Calcs._valor_fatura(id_bank_s_n,mes,ano) #
        print("VALOR DA FATURA",valor_fatu)
        print("VALOR DA FATURA",valor_fatu,id_bank_s_n,mes,ano)
        #EWRRO AQ COLOCA INPUTM, NAO TA POAGANDO A FAT
        #OPERACAO PARA SALDO ATUAL

        saldo_atual = float(saldo_inicial) - float(valor_fatu)
        print(ano,mes)
        ref = "fatura-ref "+str(mes)+"/"+str(ano)
        id_fatura = randint(100000,999999)
        return_vencimento = card_db_test.Ui_db._vencimento(id_bank_s_n)
        ref_mes = str(ano)+"-"+str(mes)+"-"+str(return_vencimento)
        # SELECT DADOS DO LANÇAMENTO E INSERT IN NEW_LANCAMENTO
        cursor.execute("INSERT INTO pagamentos_saldo (id_lancamento,id_bank,tipo_e_s,valor,ref_vencimento,data_pagamento,saldo_atual,id_discount)\
                        VALUES ('"+str(id_fatura)+"','"+str(id_bank_s_n)+"','"+str(ref)+"','"+str(valor_fatu)+"','"+str(ref_mes)+"',DateTime('now','localtime'),'"+str(saldo_atual)+"' ,'"+str(id_discount)+"')")
        banco.commit()

        # UPDATE SALDO ATUAL
        cursor.execute("UPDATE contas_bancarias SET saldo_inicial = '"+str(saldo_atual)+"' WHERE id = '"+str(id_discount)+"'")
        banco.commit()
        
        #UPDATE STATUS DO LANÇAMENTO
        cursor.execute("UPDATE status_lancamento SET status_pago = 'pago' WHERE id_lancamento = '"+str(id_discount)+"' AND status_lancamento.id_bank = '"+str(id_discount)+"'AND strftime('%Y-%m',status_lancamento.vencimento) = '"+str(ano)+"-"+str(mes)+"'")

        print("-------------------------")
        banco.commit()
        banco.close()
        return True



class Verify_status_payment:
    
    def return_status_p_pago(id,id_bank):
        #id_lancamento
        #data_lancamento
        #recorrente_m_d_s_y
        #recorrente_dia
        
        #CONNECT DB
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("SELECT status_lancamento.status_pago FROM status_lancamento WHERE status_lancamento.id_lancamento = '"+str(id)+"' AND status_lancamento.id_bank = '"+str(id_bank)+"'")
        dados = cursor.fetchall()
        print("STATUS PAGO",dados)
        if not dados or dados[0][0] == 'pago':
            return True
        else:
            return False
        

    def verify_type_lanca(id):

        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        cursor.execute("SELECT new_lancamento.tipo FROM new_lancamento WHERE new_lancamento.id_lancamento = '"+str(id)+"'")
        dados = cursor.fetchall()
        print("TIPO LANÇAMENTO",dados)
        if not dados:
            return "fatura"
        elif dados[0][0] == "Entrada":
            return True
        elif dados[0][0] == "Saida":
            return False
        else:
            return "fatura"
        # if dados[0][0] == 'Entrada':
        #     return True
        # elif dados[0][0] == 'Saida':
        #     return False
        # elif dados[0][0] == None or dados[0][0] == '' or dados[0][0] == ' ' or dados[0][0] == '[]':
        #     print("ERRO AO VERIFICAR TIPO DE LANÇAMENTO")


        
        

class Return_values_configs:
    def _update_default_h_s_z(value):
        
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        verifica_se_existe = cursor.execute("SELECT hide_show_zeros_faturas FROM config_aplicacao")
        verifica_se_existe = cursor.fetchall() 
        print(verifica_se_existe)
        if verifica_se_existe:
            cursor.execute("UPDATE config_aplicacao SET hide_show_zeros_faturas = '"+str(value)+"'")
            banco.commit()
            banco.close()
            return True
        else:
            cursor.execute("INSERT INTO config_aplicacao (hide_show_zeros_faturas) VALUES ('"+str(value)+"')")
            banco.commit()
            banco.close()
            return True


    
    
    def _return_default_h_s_z():
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        cursor.execute("SELECT config_aplicacao.hide_show_zeros_faturas FROM config_aplicacao")
        dados = cursor.fetchall()
        banco.close()
        if not dados:
            return False
        else:
            return dados[0][0]
        
        
        

class Pdf:
    

    def insert_pdf(id_lancamento,id_bank,patch_pdf,ano,mes):
        #INSERT PDF FILE
        ref_mes = str(ano)+"-"+str(mes)+"-"+datetime.now().strftime("%d")
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO pdf_patchs (id_lancamento,id_bank,patch,ref_mes) VALUES ('"+str(id_lancamento)+"','"+str(id_bank)+"','"+str(patch_pdf)+"','"+str(ref_mes)+"')")
        banco.commit()
        banco.close()
    
    def search_pdf(id_lancamento,id_bank,ano,mes):
        #SEARCH PDF FILE
        ref_mes = str(ano)+"-"+str(mes)
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        cursor.execute("SELECT pdf_patchs.patch FROM pdf_patchs WHERE pdf_patchs.id_lancamento = '"+str(id_lancamento)+"' AND pdf_patchs.id_bank = '"+str(id_bank)+"' AND strftime('%Y-%m',pdf_patchs.ref_mes) = '"+str(ref_mes)+"'")
        dados = cursor.fetchall()
        banco.close()
        if not dados:
            return False
        else:
            return dados
        




    

class Update_Remove:
    
    def _update_table_banks_cards(id_bank,id_card,dados):
        
        #UPDATE TABLE BANKS CARDS
        #id_bank
        #id_card
        # [banco,agencia,conta,saldo,limite,final_cartao,titular,vencimento,fechamento]
        
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()

        if id_card != "Não":
            tabelas = ['card_active','contas_bancarias']
            
            #UPDATE TABLE BANK
            cursor.execute("UPDATE contas_bancarias SET nome_banco = '"+str(dados[0])+"',agencia = '"+str(dados[1])+"',num_conta = '"+str(dados[2])+"',saldo_inicial = '"+str(dados[3])+"' WHERE contas_bancarias.id = '"+str(id_bank)+"'")
            banco.commit()
        
            #UPDATE TABLE CARD
            cursor.execute("UPDATE card_active SET limite = '"+str(dados[4])+"',final = '"+str(dados[5])+"',titular = '"+str(dados[6])+"',vencimento = '"+str(dados[7])+"',fechamento = '"+str(dados[8])+"' WHERE card_active.id = '"+str(id_card)+"'")
            banco.commit()
        
        else:
            tabelas = ['contas_bancarias']
            
            #UPDATE TABLE BANK
            cursor.execute("UPDATE contas_bancarias SET nome_banco = '"+str(dados[0])+"',agencia = '"+str(dados[1])+"',num_conta = '"+str(dados[2])+"',saldo_inicial = '"+str(dados[3])+"' WHERE contas_bancarias.id = '"+str(id_bank)+"'")
            banco.commit()
        return True
    
    
    
    
    def _remove_table_banks_cards(id_bank,id_card):
        
        #REMOVE TABLE BANKS CARDS
        #id_bank
        #id_card
        
        a = (os.path.dirname(os.path.realpath(__file__)))
        banco = sqlite3.connect(''+a+'/bando_de_valores.db')
        cursor = banco.cursor()
        
        if id_card != "Não":
            tabelas = ['card_active','contas_bancarias']
            
            #REMOVE TABLE BANK
            cursor.execute("DELETE FROM contas_bancarias WHERE contas_bancarias.id = '"+str(id_bank)+"'")
            banco.commit()
        
            #REMOVE TABLE CARD
            cursor.execute("DELETE FROM card_active WHERE card_active.id = '"+str(id_card)+"'")
            banco.commit()
            
            #REMOVE TABLE PDF
            cursor.execute("DELETE FROM pdf_patchs WHERE pdf_patchs.id_bank = '"+str(id_bank)+"'")
            banco.commit()
            
            #REMOVE TABLE LANCAMENTOS
            cursor.execute("DELETE FROM new_lancamento WHERE new_lancamento.id_bank = '"+str(id_bank)+"'")
            banco.commit()
            
            #REMOVE PAGAMENTOS_SALDO
            cursor.execute("DELETE FROM pagamentos_saldo WHERE pagamentos_saldo.id_bank = '"+str(id_bank)+"'")
            banco.commit()
            
            #REMOVE STATUS_LANCAMENTO
            cursor.execute("DELETE FROM status_lancamento WHERE status_lancamento.id_bank = '"+str(id_bank)+"'")
            
            #REMOVE prioridade_value
            cursor.execute("DELETE FROM prioridade_value WHERE prioridade_value.id_bank = '"+str(id_bank)+"'")
            
            #REMOVE config_lancamento
            cursor.execute("DELETE FROM config_lancamento WHERE config_lancamento.id_bank = '"+str(id_bank)+"'")
            
            #REMOVE config_contas #CONTA PADRAO
            verify = cursor.execute("SELECT * FROM config_contas WHERE config_contas.conta_padrao_bank = '"+str(id_bank)+"'").fetchall()
            if verify:
                cursor.execute("DELETE FROM config_contas WHERE config_contas.conta_padrao_bank = '"+str(id_bank)+"'")
            banco.commit()

            #DELETE TABLE extrato_cartao_
            cursor.execute("DROP TABLE IF EXISTS extrato_cartao_"+str(id_bank)+"")
            banco.commit()
            

            
        else:

            
            #REMOVE TABLE BANK
            cursor.execute("DELETE FROM contas_bancarias WHERE contas_bancarias.id = '"+str(id_bank)+"'")
            banco.commit()
            
            #REMOVE TABLE PDF
            cursor.execute("DELETE FROM pdf_patchs WHERE pdf_patchs.id_bank = '"+str(id_bank)+"'")
            banco.commit()
            
            #REMOVE TABLE LANCAMENTOS
            cursor.execute("DELETE FROM new_lancamento WHERE new_lancamento.id_bank = '"+str(id_bank)+"'")
            banco.commit()
            
            #REMOVE PAGAMENTOS_SALDO
            cursor.execute("DELETE FROM pagamentos_saldo WHERE pagamentos_saldo.id_bank = '"+str(id_bank)+"'")
            banco.commit()
            
            #REMOVE STATUS_LANCAMENTO
            cursor.execute("DELETE FROM status_lancamento WHERE status_lancamento.id_bank = '"+str(id_bank)+"'")
            
            #REMOVE prioridade_value
            cursor.execute("DELETE FROM prioridade_value WHERE prioridade_value.id_bank = '"+str(id_bank)+"'")
            
            #REMOVE config_lancamento
            cursor.execute("DELETE FROM config_lancamento WHERE config_lancamento.id_bank = '"+str(id_bank)+"'")
            
            #REMOVE config_contas #CONTA PADRAO
            verify = cursor.execute("SELECT * FROM config_contas WHERE config_contas.conta_padrao_bank = '"+str(id_bank)+"'").fetchall()
            if verify:
                cursor.execute("DELETE FROM config_contas WHERE config_contas.conta_padrao_bank = '"+str(id_bank)+"'")
            banco.commit()
            
            
        return True