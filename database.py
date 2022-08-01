from re import S
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
                cursor.execute("CREATE TABLE IF NOT EXISTS card_active (id INTEGER,nome_cartao text,titular text,limite REAL,final INTEGER,vencimento text)")
                banco.close()
                pyautogui.alert('Banco de dados Criado no diretorio raiz')
                pyautogui.alert('Agora adicione seus cartoes na No botao acima')
                
                break 
