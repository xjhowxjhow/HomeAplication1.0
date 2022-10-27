
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

class Chart(QtCharts.QChartView):
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
    def create_chart(self, title, data):
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
        self.chart.repaint()
        
        
        return True