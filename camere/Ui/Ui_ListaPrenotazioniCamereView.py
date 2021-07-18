# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lista_prenotazioni_camere.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ListaPrenotazioniCamere(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1644, 699)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\resources/logo/logo_small_icon_only_inverted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tW_lista_prenotazioni_camere = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tW_lista_prenotazioni_camere.setFont(font)
        self.tW_lista_prenotazioni_camere.setStyleSheet("background-image: url(:/ombrelloni/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 225), stop:1 rgba(255, 255, 255, 227));")
        self.tW_lista_prenotazioni_camere.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tW_lista_prenotazioni_camere.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tW_lista_prenotazioni_camere.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tW_lista_prenotazioni_camere.setObjectName("tW_lista_prenotazioni_camere")
        self.tW_lista_prenotazioni_camere.setColumnCount(9)
        self.tW_lista_prenotazioni_camere.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_prenotazioni_camere.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_prenotazioni_camere.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_prenotazioni_camere.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_prenotazioni_camere.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_prenotazioni_camere.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_prenotazioni_camere.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_prenotazioni_camere.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_prenotazioni_camere.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_prenotazioni_camere.setHorizontalHeaderItem(8, item)
        self.tW_lista_prenotazioni_camere.horizontalHeader().setDefaultSectionSize(210)
        self.tW_lista_prenotazioni_camere.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tW_lista_prenotazioni_camere)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pB_checkout = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pB_checkout.setFont(font)
        self.pB_checkout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_checkout.setStyleSheet("background-image: url(:/ombrelloni/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.pB_checkout.setObjectName("pB_checkout")
        self.horizontalLayout.addWidget(self.pB_checkout)
        self.pB_elimina = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pB_elimina.setFont(font)
        self.pB_elimina.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_elimina.setStyleSheet("background-image: url(:/ombrelloni/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.pB_elimina.setObjectName("pB_elimina")
        self.horizontalLayout.addWidget(self.pB_elimina)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lista prenotazioni camere"))
        item = self.tW_lista_prenotazioni_camere.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tW_lista_prenotazioni_camere.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMINATIVO"))
        item = self.tW_lista_prenotazioni_camere.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "CAMERA"))
        item = self.tW_lista_prenotazioni_camere.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CHECK-IN"))
        item = self.tW_lista_prenotazioni_camere.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CHECK-OUT"))
        item = self.tW_lista_prenotazioni_camere.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "DATA PRENOTAZIONE"))
        item = self.tW_lista_prenotazioni_camere.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "TIPO PAGAMENTO"))
        item = self.tW_lista_prenotazioni_camere.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "COSTO TOT."))
        item = self.tW_lista_prenotazioni_camere.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "DIPENDENTE"))
        self.pB_checkout.setText(_translate("MainWindow", "Checkout"))
        self.pB_elimina.setText(_translate("MainWindow", "Elimina"))

