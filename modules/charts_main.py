
import sqlite3
import os.path
from turtle import color
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
import locale
import emoji
import home_db_query
import home_db_fun 
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


#cria classe do grafico para setar no frame

class Chart(QtCharts.QChartView):#GRAFICO BAR GASTOS MENSAL EXTRATO MAIN
    def __init__(self, parent=None):
        super(Chart, self).__init__(parent)
        self.chart = QtCharts.QChart()
        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        self.chart.legend().setVisible(False)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)
        self.chart.setBackgroundRoundness(7)
        self.chart.setBackgroundBrush(QBrush(QColor(255, 255, 255,0)))
        # self.chart.setTheme(QtCharts.QChart.ChartThemeBlueCerulean)
        #font
        font = QFont('Bahnschrift Light Condensed', 14)
        #color
        color = QColor(255, 255, 255, 255)
        #seta fonte e cor
        self.chart.setTitleFont(font)
        self.chart.setTitleBrush(color)
        #margin
                #adjust layout
        self.chart.layout().setContentsMargins(10, 10, 10, 10)
        
        #max height
        


    
#cria classe do grafico horizontal de barras para setar no frame
    def create_chart(self, title, data): #GRAFICO BAR GASTOS MENSAL EXTRATO MAIN
        self.chart.setTitle(title)
        self.set0 = QtCharts.QBarSet('Entradas')
        self.set1 = QtCharts.QBarSet('Saídas')
        self.set0.append([data[0],0])
        self.set1.append([0,data[1]])
        #border color
        

        self.series = QtCharts.QHorizontalStackedBarSeries()
        #font
        
        self.series.append(self.set0)
        self.series.append(self.set1)


        self.set0.setColor(QColor(86, 202, 164,255))
        self.set1.setColor(QColor(254, 130, 139,255))
        self.set0.setLabelFont(QFont('Bahnschrift Light Condensed', 13))
        self.set1.setLabelFont(QFont('Bahnschrift Light Condensed', 13))
        self.set0.setBorderColor(QColor(86, 202, 164,255))
        self.set1.setBorderColor(QColor(254, 130, 139,255))
        self.set0.setLabelColor(QColor(255, 255, 255,255))
        self.set1.setLabelColor(QColor(255, 255, 255,255))
        
        #height bar
        self.series.setBarWidth(0.3)
        self.series.setLabelsVisible(True)
        self.series.setLabelsFormat("R$"+"@value")
        
        #label out of bar
        self.series.setLabelsPosition(QtCharts.QAbstractBarSeries.LabelsOutsideEnd)
        

        self.chart.addSeries(self.series)

        self.chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)  
        months = ('Entrada', 'Saida')  
        self.axisY = QtCharts.QBarCategoryAxis()
        self.axisY.append(months)
        #color label
        self.axisY.setLabelsColor(QColor(255, 255, 255, 255))
        #font label
        self.axisY.setLabelsFont(QFont('Bahnschrift Light Condensed', 12))
        #grid line
        self.axisY.setGridLineVisible(False)
        self.axisY.setLineVisible(False)
        

        #border color
        self.axisY.setShadesColor(QColor(58, 62, 130, 255))



        
        
        self.chart.addAxis(self.axisY, Qt.AlignLeft)
        self.series.attachAxis(self.axisY)

        return True
    
    def Update_Chart(self, data):
        
        self.set0.replace(0,data[0])
        self.set1.replace(1,data[1])
        self.chart.update()
        
        
        
        return True
    



class Chart_1_Dashboard_Main(QtCharts.QChartView): #GRAFICO BAR GASTOS ANUAIS PAGE DASHBOARD MAIN
    def __init__(self, parent=None):
        super(Chart_1_Dashboard_Main, self).__init__(parent)
        self.chart1 = QtCharts.QChart()
        self.chart1.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        self.setRenderHint(QPainter.Antialiasing)
        self.chart1.setBackgroundRoundness(7)
        self.chart1.setBackgroundBrush(QBrush(QColor(255, 255, 255,0)))
        #font
        font = QFont('Bahnschrift Light Condensed', 14)
        #color
        color = QColor(255, 255, 255, 255)
        #seta fonte e cor
        self.chart1.setTitleFont(font)
        self.chart1.setTitleBrush(color)
        self.chart1.setFont(QFont('Bahnschrift Light Condensed', 12))
        self.chart1.setTitleFont(QFont('Bahnschrift Light Condensed', 12))

        #adjust legend

        self.chart1.legend().setVisible(True)
        self.chart1.legend().setAlignment(Qt.AlignBottom)
        self.chart1.legend().setBackgroundVisible(False)
        self.chart1.legend().setFont(QFont('Bahnschrift Light Condensed', 12))
        self.chart1.legend().setColor(QColor(255, 255, 255, 255))
        self.setChart(self.chart1)
    
    def create_chart(self, title, data):
        self.chart1.setTitle(title)
        self.set_0 = QtCharts.QBarSet('entrada')
        self.set_1 = QtCharts.QBarSet('saida')
        
        for i in range(0,12):
            #[[0.0, 800.18], [0.0, 994.92], 
            self.set_0.append(data[i][0])
            self.set_1.append(data[i][1])
        #border color
        self.set_0.setColor(QColor(86, 202, 164,255))
        self.set_1.setColor(QColor(254, 130, 139,255))
        
        self.set_0.setLabelFont(QFont('Bahnschrift Light Condensed', 13))
        self.set_1.setLabelFont(QFont('Bahnschrift Light Condensed', 13))
        self.set_0.setBorderColor(QColor(86, 202, 164,255))
        self.set_1.setBorderColor(QColor(254, 130, 139,255))
        
        self.set_0.setLabelColor(QColor(255, 255, 255,255))
        self.set_1.setLabelColor(QColor(255, 255, 255,255))

        self.series1 = QtCharts.QStackedBarSeries()
        self.series1.append(self.set_0)
        self.series1.append(self.set_1)
        self.series1.setLabelsVisible(True)
        self.series1.setLabelsFormat("R$"+"@value")
        
        #label out of bar
        self.series1.setLabelsPosition(QtCharts.QAbstractBarSeries.LabelsOutsideEnd)
        
        
        mes = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
        axis = QtCharts.QBarCategoryAxis()
        axis.append(mes)
        axis.setGridLineVisible(False)
        axis.setLineVisible(False)
        axis.setLabelsFont(QFont('Bahnschrift Light Condensed', 12))
        axis.setLabelsColor(QColor(255, 255, 255, 255))
        self.chart1.createDefaultAxes()
        self.chart1.setAxisX(axis, self.series1)
        
        self.chart1.addSeries(self.series1)




    def Update_Chart_2(self, data):
        print(data)
        # meses

        for index in range(12):
            self.set_0.replace(index,data[index][0])
            self.set_1.replace(index,data[index][1])
        self.chart1.update()
        
        #change thema
        return True