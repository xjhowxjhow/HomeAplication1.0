import sqlite3
from PySide2.QtCore import *
import pyautogui
import os.path




class salva_dados:    
    #TODO# CRIA BANCO DE DADOS
    def testedb(self):
        while True:
            a = (os.path.dirname(os.path.realpath(__file__)))
            if(os.path.exists(''+a+'/bando_de_valores.db')):
                pyautogui.alert('Banco de Dados já criado na pasta raiz, portanto nao será possivel criar um novo Arquivo\ Por favor acesse as configurações do programa para apagar o DB já existente.')
                break
            else:
                pyautogui.alert('Banco de dados nao encontrado Criando no diretorio raiz favor aguarde')
                banco=sqlite3.connect(''+a+'/bando_de_valores.db')
                cursor=banco.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS card_active (id INTEGER,nome_cartao text,titular text,limite REAL,final INTEGER,vencimento text,fechamento text)")
                
                #TABLE CONTAS BANCARIAS
                cursor.execute("CREATE TABLE IF NOT EXISTS contas_bancarias(id int,saldo_inicial text,nome_banco text,agencia int,num_conta int,titular text, cartao_credito_id text)")
                #TABLE PAGAMENTOS SALDO
                cursor.execute("CREATE TABLE IF NOT EXISTS pagamentos_saldo(id_lancamento int,id_bank int,tipo_e_s text,valor ,ref_vencimento text,data_pagamento text,saldo_atual text,id_discount int)")
                
                #CONFIGURACOES DE CONTAS
                cursor.execute("CREATE TABLE IF NOT EXISTS config_contas(conta_padrao_bank int)")
                
                
                #NOVO LANÇAMENTO
                cursor.execute("CREATE TABLE IF NOT EXISTS new_lancamento (id_lancamento int,id_bank int,data_lancamento text,categoria text,pagamento text,valor int,tipo text,descricao text)")
                #LANCAMENTO VENCIMENTO
                cursor.execute("CREATE TABLE IF NOT EXISTS status_lancamento  (id_lancamento int,id_bank int,vencimento text,status_pago text)")
                #LANÇAMENTO RECORRENTE
                cursor.execute("CREATE TABLE IF NOT EXISTS config_lancamento(id_lancamento int,id_bank int,recorrente text,recorrente_m_d_s_y text,recorrente_dia text,anexo text)")
                #SETS PRIORIDADE
                cursor.execute("CREATE TABLE IF NOT EXISTS prioridade_value(id_lancamento int,id_bank int,prioridade text)")
                # PDF PATCHS 
                cursor.execute("CREATE TABLE IF NOT EXISTS pdf_patchs(id_lancamento int,id_bank int,patch text, date_insert text, date_update text, ref_mes text)")
                
                #CONFIGURAÇÕES DA APLICAÇÃO:
                cursor.execute("CREATE TABLE IF NOT EXISTS config_aplicacao (id int,tema text,hide_show_zeros_faturas text)")
                banco.close()
                pyautogui.alert('Banco de dados Criado no diretorio raiz')

                
                break 
