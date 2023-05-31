from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(708, 387)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.basvurButton = QtWidgets.QPushButton(self.centralwidget)
        self.basvurButton.setGeometry(QtCore.QRect(210, 250, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.basvurButton.setFont(font)
        self.basvurButton.setObjectName("basvurButton")
        self.iptalButton = QtWidgets.QPushButton(self.centralwidget)
        self.iptalButton.setGeometry(QtCore.QRect(370, 250, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.iptalButton.setFont(font)
        self.iptalButton.setObjectName("iptalButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.isimEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.isimEdit.setGeometry(QtCore.QRect(100, 60, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.isimEdit.setFont(font)
        self.isimEdit.setText("")
        self.isimEdit.setObjectName("isimEdit")
        self.soyisimEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.soyisimEdit.setGeometry(QtCore.QRect(130, 110, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.soyisimEdit.setFont(font)
        self.soyisimEdit.setText("")
        self.soyisimEdit.setObjectName("soyisimEdit")
        self.numaraEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numaraEdit.setGeometry(QtCore.QRect(160, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.numaraEdit.setFont(font)
        self.numaraEdit.setText("")
        self.numaraEdit.setObjectName("numaraEdit")
        self.sehitYakini = QtWidgets.QRadioButton(self.centralwidget)
        self.sehitYakini.setGeometry(QtCore.QRect(360, 40, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sehitYakini.setFont(font)
        self.sehitYakini.setObjectName("sehitYakini")
        self.emekli = QtWidgets.QRadioButton(self.centralwidget)
        self.emekli.setGeometry(QtCore.QRect(360, 80, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.emekli.setFont(font)
        self.emekli.setObjectName("emekli")
        self.engelDurumu = QtWidgets.QRadioButton(self.centralwidget)
        self.engelDurumu.setGeometry(QtCore.QRect(360, 120, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.engelDurumu.setFont(font)
        self.engelDurumu.setObjectName("engelDurumu")
        self.ozeldurumyok = QtWidgets.QRadioButton(self.centralwidget)
        self.ozeldurumyok.setGeometry(QtCore.QRect(360, 160, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ozeldurumyok.setFont(font)
        self.ozeldurumyok.setObjectName("ozeldurumyok")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Başvuru Ekranı"))
        self.basvurButton.setText(_translate("MainWindow", "Başvur"))
        self.iptalButton.setText(_translate("MainWindow", "İptal Et"))
        self.label.setText(_translate("MainWindow", "İsminiz :"))
        self.label_2.setText(_translate("MainWindow", "Soy İsminiz:"))
        self.label_3.setText(_translate("MainWindow", "İrtibat Numarası:"))
        self.sehitYakini.setText(_translate("MainWindow", "Şehit Yakınıyım"))
        self.emekli.setText(_translate("MainWindow", "Emekliyim"))
        self.engelDurumu.setText(_translate("MainWindow", "Engel Durmum Var"))
        self.ozeldurumyok.setText(_translate("MainWindow", "Herhangi Özel Durumum Yok"))

    
