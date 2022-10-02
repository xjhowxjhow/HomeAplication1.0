    def _show(self, valor,saldo_apos):
        
        self.frame_confirm = QFrame(self)
        self.frame_confirm.setObjectName(u"frame_confirm")
        self.frame_confirm.setGeometry(QRect(650, 400, 331, 251))
        self.frame_confirm.setStyleSheet("background-color:rgb(40, 42, 54); border-radius:10; border: 1px solid rgba(255,255,255,30);")
        self.frame_confirm.setFrameShape(QFrame.StyledPanel)
        self.frame_confirm.setFrameShadow(QFrame.Raised)
        self.label_confirm = QLabel(self.frame_confirm)
        self.label_confirm.setObjectName(u"label_confirm")
        self.label_confirm.setGeometry(QRect(60, 20, 201, 41))
        font = QFont()
        font.setFamily(u"Bahnschrift Light Condensed")
        font.setPointSize(15)
        self.label_confirm.setFont(font)
        self.label_confirm.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(255,255,255,0); border:none;")
        self.label_confirm.setAlignment(Qt.AlignCenter)
        self.sald_confirm = QLabel(self.frame_confirm)
        self.sald_confirm.setObjectName(u"sald_confirm")
        self.sald_confirm.setGeometry(QRect(20, 143, 301, 31))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Light SemiCondensed")
        font1.setPointSize(11)
        self.sald_confirm.setFont(font1)
        self.sald_confirm.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(255,255,255,0); border:none;")
        self.line_confirm = QFrame(self.frame_confirm)
        self.line_confirm.setObjectName(u"line_confirm")
        self.line_confirm.setGeometry(QRect(20, 136, 291, 1))
        self.line_confirm.setMaximumSize(QSize(16777215, 1))
        self.line_confirm.setFrameShape(QFrame.HLine)
        self.line_confirm.setFrameShadow(QFrame.Sunken)
        self.val_confirm = QLabel(self.frame_confirm)
        self.val_confirm.setObjectName(u"val_confirm")
        self.val_confirm.setGeometry(QRect(20, 107, 291, 31))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light SemiCondensed")
        font2.setPointSize(13)
        self.val_confirm.setFont(font2)
        self.val_confirm.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(255,255,255,0); border:none;")
        self.pushOK = QPushButton(self.frame_confirm)
        self.pushOK.setObjectName(u"pushOK")
        self.pushOK.setGeometry(QRect(40, 202, 75, 31))
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light SemiCondensed")
        font3.setPointSize(10)
        self.pushOK.setFont(font3)
        self.pushOK.setStyleSheet("QPushButton{ border-radius:10px; color: rgb(255, 255, 255); background-color:rgba(255,255,255,10); border: 1px solid rgba(255,255,255,20); border-radius:7px; } QPushButton:hover{ background-color:rgba(31, 168, 49,70);} QPushButton:pressed{ background-color:rgba(31, 168, 49,170); }")
        self.pushCAN = QPushButton(self.frame_confirm)
        self.pushCAN.setObjectName(u"pushCAN")
        self.pushCAN.setGeometry(QRect(210, 202, 75, 31))
        self.pushCAN.setFont(font3)
        self.pushCAN.setStyleSheet("QPushButton{ border-radius:10px; color: rgb(255, 255, 255); background-color:rgba(255,255,255,10); border: 1px solid rgba(255,255,255,20); border-radius:7px; } QPushButton:hover{ background-color:rgba(225, 60, 47,70); } QPushButton:pressed{ background-color:rgba(225, 60, 47,170); }")
        
        
        valor = str(valor)
        saldo_apos = str(saldo_apos)
        
        
        #set text
        self.label_confirm.setText("Confirmar o Pagamento")
        self.val_confirm.setText("Valor: "+valor)
        self.sald_confirm.setText("Saldo após a Transação: "+saldo_apos)
        self.pushOK.setText("Pagar")
        self.pushCAN.setText("Cancelar")

        #show
        self.frame_confirm.show()
        #connect
        if self.pushOK.clicked.connect(print("OK")):
            print("OK")
            return True
        if self.pushCAN.clicked.connect(print("CAN")):
            print("CANCEL")
            return False