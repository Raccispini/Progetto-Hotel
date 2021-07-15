'''
__author__: Alessandro Rongoni
'''
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MagazzinoView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1102, 591)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\resources/logo/logo_small_icon_only_inverted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 20, -1)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_Aggiungi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Aggiungi.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_Aggiungi.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Aggiungi.setFont(font)
        self.pushButton_Aggiungi.setObjectName("pushButton_Aggiungi")
        self.verticalLayout_2.addWidget(self.pushButton_Aggiungi)
        self.pushButton_Modifica = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Modifica.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_Modifica.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Modifica.setFont(font)
        self.pushButton_Modifica.setObjectName("pushButton_Modifica")
        self.verticalLayout_2.addWidget(self.pushButton_Modifica)
        self.pushButton_Elimina = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Elimina.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_Elimina.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Elimina.setFont(font)
        self.pushButton_Elimina.setObjectName("pushButton_Elimina")
        self.verticalLayout_2.addWidget(self.pushButton_Elimina)
        self.pushButton_Salva = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Salva.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_Salva.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Salva.setFont(font)
        self.pushButton_Salva.setObjectName("pushButton_Salva")
        self.verticalLayout_2.addWidget(self.pushButton_Salva)
        self.pushButton_Annulla = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Annulla.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_Annulla.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Annulla.setFont(font)
        self.pushButton_Annulla.setObjectName("pushButton_Annulla")
        self.verticalLayout_2.addWidget(self.pushButton_Annulla)
        self.pushButton_StampaPDF = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_StampaPDF.setMinimumSize(QtCore.QSize(0, 20))
        self.pushButton_StampaPDF.setMaximumSize(QtCore.QSize(400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_StampaPDF.setFont(font)
        self.pushButton_StampaPDF.setObjectName("pushButton_StampaPDF")
        self.verticalLayout_2.addWidget(self.pushButton_StampaPDF)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.tableWidget_MAgazzino = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_MAgazzino.sizePolicy().hasHeightForWidth())
        self.tableWidget_MAgazzino.setSizePolicy(sizePolicy)
        self.tableWidget_MAgazzino.setMaximumSize(QtCore.QSize(1050, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_MAgazzino.setFont(font)
        self.tableWidget_MAgazzino.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_MAgazzino.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_MAgazzino.setObjectName("tableWidget_MAgazzino")
        self.tableWidget_MAgazzino.setColumnCount(6)
        self.tableWidget_MAgazzino.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_MAgazzino.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_MAgazzino.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_MAgazzino.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_MAgazzino.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_MAgazzino.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_MAgazzino.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_MAgazzino.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_MAgazzino.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_MAgazzino.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_MAgazzino.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_MAgazzino.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_MAgazzino.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_MAgazzino.setItem(0, 5, item)
        self.tableWidget_MAgazzino.horizontalHeader().setDefaultSectionSize(170)
        self.tableWidget_MAgazzino.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_MAgazzino.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.tableWidget_MAgazzino)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(800, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_7.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_Costo = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.lineEdit_Costo.setFont(font)
        self.lineEdit_Costo.setClearButtonEnabled(True)
        self.lineEdit_Costo.setObjectName("lineEdit_Costo")
        self.gridLayout.addWidget(self.lineEdit_Costo, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_Codice = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.lineEdit_Codice.setFont(font)
        self.lineEdit_Codice.setClearButtonEnabled(True)
        self.lineEdit_Codice.setObjectName("lineEdit_Codice")
        self.gridLayout.addWidget(self.lineEdit_Codice, 0, 1, 1, 1)
        self.lineEdit_Consumazione = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.lineEdit_Consumazione.setFont(font)
        self.lineEdit_Consumazione.setClearButtonEnabled(True)
        self.lineEdit_Consumazione.setObjectName("lineEdit_Consumazione")
        self.gridLayout.addWidget(self.lineEdit_Consumazione, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.lineEdit_Giacenza = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.lineEdit_Giacenza.setFont(font)
        self.lineEdit_Giacenza.setClearButtonEnabled(True)
        self.lineEdit_Giacenza.setObjectName("lineEdit_Giacenza")
        self.gridLayout.addWidget(self.lineEdit_Giacenza, 0, 3, 1, 1)
        self.lineEdit_ScortaMinima = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.lineEdit_ScortaMinima.setFont(font)
        self.lineEdit_ScortaMinima.setClearButtonEnabled(True)
        self.lineEdit_ScortaMinima.setObjectName("lineEdit_ScortaMinima")
        self.gridLayout.addWidget(self.lineEdit_ScortaMinima, 0, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 4, 1, 1)
        self.lineEdit_Valore = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.lineEdit_Valore.setFont(font)
        self.lineEdit_Valore.setClearButtonEnabled(True)
        self.lineEdit_Valore.setObjectName("lineEdit_Valore")
        self.gridLayout.addWidget(self.lineEdit_Valore, 1, 5, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Magazzino"))
        self.pushButton_Aggiungi.setText(_translate("MainWindow", "Aggiungi"))
        self.pushButton_Modifica.setText(_translate("MainWindow", "Modifica"))
        self.pushButton_Elimina.setText(_translate("MainWindow", "Elimina"))
        self.pushButton_Salva.setText(_translate("MainWindow", "Salva"))
        self.pushButton_Annulla.setText(_translate("MainWindow", "Annulla"))
        self.pushButton_StampaPDF.setText(_translate("MainWindow", "Stampa PDF"))
        item = self.tableWidget_MAgazzino.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1."))
        item = self.tableWidget_MAgazzino.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Codice"))
        item = self.tableWidget_MAgazzino.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Consumazione"))
        item = self.tableWidget_MAgazzino.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Giacenza"))
        item = self.tableWidget_MAgazzino.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Costo"))
        item = self.tableWidget_MAgazzino.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Scorta minima"))
        item = self.tableWidget_MAgazzino.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Valore"))
        __sortingEnabled = self.tableWidget_MAgazzino.isSortingEnabled()
        self.tableWidget_MAgazzino.setSortingEnabled(False)
        item = self.tableWidget_MAgazzino.item(0, 0)
        item.setText(_translate("MainWindow", "000001"))
        item = self.tableWidget_MAgazzino.item(0, 1)
        item.setText(_translate("MainWindow", "Acqua"))
        item = self.tableWidget_MAgazzino.item(0, 2)
        item.setText(_translate("MainWindow", "350"))
        item = self.tableWidget_MAgazzino.item(0, 3)
        item.setText(_translate("MainWindow", "0.30"))
        item = self.tableWidget_MAgazzino.item(0, 4)
        item.setText(_translate("MainWindow", "0"))
        item = self.tableWidget_MAgazzino.item(0, 5)
        item.setText(_translate("MainWindow", "105"))
        self.tableWidget_MAgazzino.setSortingEnabled(__sortingEnabled)
        self.label_7.setText(_translate("MainWindow", "Valore Magazzino:"))
        self.lineEdit_4.setText(_translate("MainWindow", "105€"))
        self.label_5.setText(_translate("MainWindow", "Scorta minima:"))
        self.label.setText(_translate("MainWindow", "Codice:"))
        self.label_2.setText(_translate("MainWindow", "Consumazione:"))
        self.label_4.setText(_translate("MainWindow", "Costo:"))
        self.label_3.setText(_translate("MainWindow", "Giacenza:"))
        self.label_6.setText(_translate("MainWindow", "Valore:"))
