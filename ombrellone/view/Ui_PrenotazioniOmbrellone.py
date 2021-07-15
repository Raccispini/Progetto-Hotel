'''
__author__: Alessandro Rongoni
'''
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PrenotazioniOmbrellone(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(1041, 721)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\resources/logo/logo_small_icon_only_inverted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(ui/resources/Ombrelloni/thumb-1920-325895.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tW_lista_ombrelloni = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tW_lista_ombrelloni.setFont(font)
        self.tW_lista_ombrelloni.setStyleSheet("background-image: url(ui/resources/Ombrelloni/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 225), stop:1 rgba(255, 255, 255, 227));")
        self.tW_lista_ombrelloni.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tW_lista_ombrelloni.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tW_lista_ombrelloni.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tW_lista_ombrelloni.setObjectName("tW_lista_ombrelloni")
        self.tW_lista_ombrelloni.setColumnCount(10)
        self.tW_lista_ombrelloni.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_ombrelloni.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_ombrelloni.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_ombrelloni.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_ombrelloni.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_ombrelloni.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_ombrelloni.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_ombrelloni.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_ombrelloni.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_ombrelloni.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_lista_ombrelloni.setHorizontalHeaderItem(9, item)
        self.tW_lista_ombrelloni.horizontalHeader().setDefaultSectionSize(250)
        self.tW_lista_ombrelloni.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tW_lista_ombrelloni)
        self.pB_elimina = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pB_elimina.setFont(font)
        self.pB_elimina.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_elimina.setStyleSheet("background-image: url(ui/resources/Ombrelloni/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.pB_elimina.setObjectName("pB_elimina")
        self.pB_elimina.setEnabled(0)
        self.verticalLayout.addWidget(self.pB_elimina)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lista Ombrelloni Prenotati"))
        item = self.tW_lista_ombrelloni.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "N° OMBRELLONE"))
        item = self.tW_lista_ombrelloni.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NOMINATIVO"))
        item = self.tW_lista_ombrelloni.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DATA"))
        item = self.tW_lista_ombrelloni.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "TIPO"))
        item = self.tW_lista_ombrelloni.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ORARIO INIZIO"))
        item = self.tW_lista_ombrelloni.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ORARIO FINE"))
        item = self.tW_lista_ombrelloni.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "N° SEDIE"))
        item = self.tW_lista_ombrelloni.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "N° SDRAIE"))
        item = self.tW_lista_ombrelloni.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "PAGAMENTO"))
        item = self.tW_lista_ombrelloni.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "COSTO TOT."))
        self.pB_elimina.setText(_translate("MainWindow", "Elimina"))

