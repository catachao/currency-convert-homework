# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Currency_Convert2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 248)
        MainWindow.setAccessibleName("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblConvertir = QtWidgets.QLabel(self.centralwidget)
        self.lblConvertir.setGeometry(QtCore.QRect(50, 40, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        self.lblConvertir.setFont(font)
        self.lblConvertir.setObjectName("lblConvertir")
        self.lblResultado = QtWidgets.QLabel(self.centralwidget)
        self.lblResultado.setGeometry(QtCore.QRect(290, 100, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.lblResultado.setFont(font)
        self.lblResultado.setObjectName("lblResultado")
        self.lblCambio = QtWidgets.QLabel(self.centralwidget)
        self.lblCambio.setGeometry(QtCore.QRect(290, 120, 47, 13))
        self.lblCambio.setObjectName("lblCambio")
        self.leImporte = QtWidgets.QLineEdit(self.centralwidget)
        self.leImporte.setGeometry(QtCore.QRect(110, 40, 113, 20))
        self.leImporte.setObjectName("leImporte")
        self.gbDe = QtWidgets.QGroupBox(self.centralwidget)
        self.gbDe.setGeometry(QtCore.QRect(40, 80, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        self.gbDe.setFont(font)
        self.gbDe.setObjectName("gbDe")
        self.rbDeUSD = QtWidgets.QRadioButton(self.gbDe)
        self.rbDeUSD.setGeometry(QtCore.QRect(20, 20, 51, 17))
        self.rbDeUSD.setObjectName("rbDeUSD")
        self.rbDeEUR = QtWidgets.QRadioButton(self.gbDe)
        self.rbDeEUR.setGeometry(QtCore.QRect(20, 40, 51, 17))
        self.rbDeEUR.setObjectName("rbDeEUR")
        self.rbDePEN = QtWidgets.QRadioButton(self.gbDe)
        self.rbDePEN.setGeometry(QtCore.QRect(20, 60, 51, 17))
        self.rbDePEN.setObjectName("rbDePEN")
        self.gbA = QtWidgets.QGroupBox(self.centralwidget)
        self.gbA.setGeometry(QtCore.QRect(160, 80, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        self.gbA.setFont(font)
        self.gbA.setObjectName("gbA")
        self.rbAUSD = QtWidgets.QRadioButton(self.gbA)
        self.rbAUSD.setGeometry(QtCore.QRect(20, 20, 61, 17))
        self.rbAUSD.setObjectName("rbAUSD")
        self.rbAEUR = QtWidgets.QRadioButton(self.gbA)
        self.rbAEUR.setGeometry(QtCore.QRect(20, 40, 51, 17))
        self.rbAEUR.setObjectName("rbAEUR")
        self.rbAPEN = QtWidgets.QRadioButton(self.gbA)
        self.rbAPEN.setGeometry(QtCore.QRect(20, 60, 51, 17))
        self.rbAPEN.setObjectName("rbAPEN")
        self.pbTipoCambio = QtWidgets.QPushButton(self.centralwidget)
        self.pbTipoCambio.setGeometry(QtCore.QRect(320, 180, 75, 23))
        self.pbTipoCambio.setObjectName("pbTipoCambio")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tipo de Cambio"))
        self.lblConvertir.setText(_translate("MainWindow", "Convertir"))
        self.lblResultado.setText(_translate("MainWindow", "Resultado"))
        self.lblCambio.setText(_translate("MainWindow", "0"))
        self.gbDe.setTitle(_translate("MainWindow", "De:"))
        self.rbDeUSD.setText(_translate("MainWindow", "USD"))
        self.rbDeEUR.setText(_translate("MainWindow", "EUR"))
        self.rbDePEN.setText(_translate("MainWindow", "PEN"))
        self.gbA.setTitle(_translate("MainWindow", "A:"))
        self.rbAUSD.setText(_translate("MainWindow", "USD"))
        self.rbAEUR.setText(_translate("MainWindow", "EUR"))
        self.rbAPEN.setText(_translate("MainWindow", "PEN"))
        self.pbTipoCambio.setText(_translate("MainWindow", "Covertir"))
