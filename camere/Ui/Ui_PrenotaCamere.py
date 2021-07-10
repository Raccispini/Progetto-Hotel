# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prenota_camere.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PrenotaCamere(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(966, 694)
        MainWindow.setStyleSheet("font: 10pt \"Arial\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.timeEdit_orario_arrivo = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit_orario_arrivo.setObjectName("timeEdit_orario_arrivo")
        self.horizontalLayout.addWidget(self.timeEdit_orario_arrivo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.pb_aggiungi_cliente = QtWidgets.QPushButton(self.centralwidget)
        self.pb_aggiungi_cliente.setMinimumSize(QtCore.QSize(20, 0))
        self.pb_aggiungi_cliente.setObjectName("pb_aggiungi_cliente")
        self.horizontalLayout_6.addWidget(self.pb_aggiungi_cliente)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label_note = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_note.setFont(font)
        self.label_note.setObjectName("label_note")
        self.verticalLayout.addWidget(self.label_note)
        self.textBrowser_info_chec_in = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_info_chec_in.setObjectName("textBrowser_info_chec_in")
        self.verticalLayout.addWidget(self.textBrowser_info_chec_in)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pB_annulla = QtWidgets.QPushButton(self.centralwidget)
        self.pB_annulla.setObjectName("pB_annulla")
        self.horizontalLayout_2.addWidget(self.pB_annulla)
        self.pB_prenota = QtWidgets.QPushButton(self.centralwidget)
        self.pB_prenota.setObjectName("pB_prenota")
        self.horizontalLayout_2.addWidget(self.pB_prenota)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Clienti:"))
        self.label.setText(_translate("MainWindow", "Orario di arrivo"))
        self.pb_aggiungi_cliente.setText(_translate("MainWindow", "Aggiungi Cliente"))
        self.label_note.setText(_translate("MainWindow", "Note:"))
        self.pB_annulla.setText(_translate("MainWindow", "Prenota"))
        self.pB_prenota.setText(_translate("MainWindow", "Annulla"))
