from PyQt5 import QtCore, QtGui, QtWidgets
from ui.resources.Camere import camere_rc

class Ui_CamereView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1558, 842)
        MainWindow.setMinimumSize(QtCore.QSize(1223, 665))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/logo/logo_small_icon_only_inverted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-image: url(:/camere/Grand-Hotel-Fleming-2.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setMaximumSize(QtCore.QSize(200, 260))
        self.logo.setStyleSheet("background-image: url(:/camere/tpg.png);")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("resources/logo/logo_small_200x230.png"))
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.date_dal = QtWidgets.QDateEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.date_dal.setFont(font)
        self.date_dal.setStyleSheet("background-image: url(:/camere/8-85556_silver-mat-color.jpg);\n"
"")
        self.date_dal.setCalendarPopup(True)
        self.date_dal.setDate(QtCore.QDate(2021, 4, 15))
        self.date_dal.setObjectName("date_dal")
        self.gridLayout_7.addWidget(self.date_dal, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 2, 0, 1, 1)
        self.date_al = QtWidgets.QDateEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.date_al.setFont(font)
        self.date_al.setStyleSheet("background-image: url(:/camere/8-85556_silver-mat-color.jpg);")
        self.date_al.setCalendarPopup(True)
        self.date_al.setDate(QtCore.QDate(2021, 4, 17))
        self.date_al.setObjectName("date_al")
        self.gridLayout_7.addWidget(self.date_al, 0, 3, 1, 1)
        self.combo_tipo = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.combo_tipo.setFont(font)
        self.combo_tipo.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.combo_tipo.setObjectName("combo_tipo")
        self.combo_tipo.addItem("")
        self.combo_tipo.addItem("")
        self.combo_tipo.addItem("")
        self.gridLayout_7.addWidget(self.combo_tipo, 2, 1, 1, 3)
        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 4, 1, 1)
        self.spin_singoli = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.spin_singoli.setFont(font)
        self.spin_singoli.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spin_singoli.setObjectName("spin_singoli")
        self.gridLayout_6.addWidget(self.spin_singoli, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
        self.spin_matrim = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.spin_matrim.setFont(font)
        self.spin_matrim.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spin_matrim.setObjectName("spin_matrim")
        self.gridLayout_6.addWidget(self.spin_matrim, 0, 3, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_6)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cb_animaledomestico = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        self.cb_animaledomestico.setFont(font)
        self.cb_animaledomestico.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.cb_animaledomestico.setObjectName("cb_animaledomestico")
        self.gridLayout_3.addWidget(self.cb_animaledomestico, 0, 1, 1, 1)
        self.cb_fumatori = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        self.cb_fumatori.setFont(font)
        self.cb_fumatori.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.cb_fumatori.setObjectName("cb_fumatori")
        self.gridLayout_3.addWidget(self.cb_fumatori, 1, 1, 1, 1)
        self.cb_vascaidromassaggio = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        self.cb_vascaidromassaggio.setFont(font)
        self.cb_vascaidromassaggio.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.cb_vascaidromassaggio.setObjectName("cb_vascaidromassaggio")
        self.gridLayout_3.addWidget(self.cb_vascaidromassaggio, 1, 0, 1, 1)
        self.cb_vistapanoramica = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        self.cb_vistapanoramica.setFont(font)
        self.cb_vistapanoramica.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.cb_vistapanoramica.setObjectName("cb_vistapanoramica")
        self.gridLayout_3.addWidget(self.cb_vistapanoramica, 1, 2, 1, 1)
        self.cb_saunainterna = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        self.cb_saunainterna.setFont(font)
        self.cb_saunainterna.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.cb_saunainterna.setObjectName("cb_saunainterna")
        self.gridLayout_3.addWidget(self.cb_saunainterna, 0, 2, 1, 1)
        self.cb_ariaCondizionata = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        self.cb_ariaCondizionata.setFont(font)
        self.cb_ariaCondizionata.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.cb_ariaCondizionata.setObjectName("cb_ariaCondizionata")
        self.gridLayout_3.addWidget(self.cb_ariaCondizionata, 0, 0, 1, 1)
        self.cb_culla_2 = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        self.cb_culla_2.setFont(font)
        self.cb_culla_2.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.cb_culla_2.setObjectName("cb_culla_2")
        self.gridLayout_3.addWidget(self.cb_culla_2, 2, 0, 1, 1)
        self.cb_cassaforte = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        self.cb_cassaforte.setFont(font)
        self.cb_cassaforte.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.cb_cassaforte.setObjectName("cb_cassaforte")
        self.gridLayout_3.addWidget(self.cb_cassaforte, 2, 2, 1, 1)
        self.cb_minibar = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        self.cb_minibar.setFont(font)
        self.cb_minibar.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.cb_minibar.setObjectName("cb_minibar")
        self.gridLayout_3.addWidget(self.cb_minibar, 2, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_ricerca = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.pb_ricerca.setFont(font)
        self.pb_ricerca.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.pb_ricerca.setObjectName("pb_ricerca")
        self.verticalLayout.addWidget(self.pb_ricerca)
        self.pb_azzera = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.pb_azzera.setFont(font)
        self.pb_azzera.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.pb_azzera.setObjectName("pb_azzera")
        self.verticalLayout.addWidget(self.pb_azzera)
        self.pb_preventivo = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.pb_preventivo.setFont(font)
        self.pb_preventivo.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.pb_preventivo.setObjectName("pb_preventivo")
        self.verticalLayout.addWidget(self.pb_preventivo)
        self.pb_prenota = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.pb_prenota.setFont(font)
        self.pb_prenota.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.pb_prenota.setObjectName("pb_prenota")
        self.verticalLayout.addWidget(self.pb_prenota)
        self.pb_prenota_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.pb_prenota_2.setFont(font)
        self.pb_prenota_2.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.pb_prenota_2.setObjectName("pb_prenota_2")
        self.verticalLayout.addWidget(self.pb_prenota_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelCamere = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.labelCamere.setFont(font)
        self.labelCamere.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));")
        self.labelCamere.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCamere.setObjectName("labelCamere")
        self.verticalLayout_2.addWidget(self.labelCamere)
        self.tabellaCamere = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.tabellaCamere.setFont(font)
        self.tabellaCamere.setStyleSheet("background-image: url(:/camere/tpg.png);\n"
"font: 11pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 225), stop:1 rgba(255, 255, 255, 227));")
        self.tabellaCamere.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabellaCamere.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tabellaCamere.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tabellaCamere.setObjectName("tabellaCamere")
        self.tabellaCamere.setColumnCount(16)
        self.tabellaCamere.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        self.tabellaCamere.setHorizontalHeaderItem(15, item)
        self.tabellaCamere.horizontalHeader().setDefaultSectionSize(225)
        self.tabellaCamere.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tabellaCamere)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ricerca Camere"))
        self.label_7.setText(_translate("MainWindow", "Al"))
        self.label_6.setText(_translate("MainWindow", "Dal"))
        self.label_5.setText(_translate("MainWindow", "Tipo"))
        self.combo_tipo.setItemText(0, _translate("MainWindow", "Single"))
        self.combo_tipo.setItemText(1, _translate("MainWindow", "Deluxe"))
        self.combo_tipo.setItemText(2, _translate("MainWindow", "Bilocale"))
        self.label_4.setText(_translate("MainWindow", "Letti matrimoniali"))
        self.label_3.setText(_translate("MainWindow", "Letti singoli"))
        self.cb_animaledomestico.setText(_translate("MainWindow", "Animale Domestico"))
        self.cb_fumatori.setText(_translate("MainWindow", "Fumatori"))
        self.cb_vascaidromassaggio.setText(_translate("MainWindow", "Vasca Idromassaggio"))
        self.cb_vistapanoramica.setText(_translate("MainWindow", "Vista Panoramica"))
        self.cb_saunainterna.setText(_translate("MainWindow", "Sauna Interna"))
        self.cb_ariaCondizionata.setText(_translate("MainWindow", "Aria Condizionata"))
        self.cb_culla_2.setText(_translate("MainWindow", "Culla"))
        self.cb_cassaforte.setText(_translate("MainWindow", "Cassaforte"))
        self.cb_minibar.setText(_translate("MainWindow", "Minibar"))
        self.pb_ricerca.setText(_translate("MainWindow", "Ricerca"))
        self.pb_azzera.setText(_translate("MainWindow", "Azzera"))
        self.pb_preventivo.setText(_translate("MainWindow", "Preventivo"))
        self.pb_prenota.setText(_translate("MainWindow", "Prenota"))
        self.pb_prenota_2.setText(_translate("MainWindow", "Checkout"))
        self.labelCamere.setText(_translate("MainWindow", " Camere Disponibili"))
        item = self.tabellaCamere.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PIANO"))
        item = self.tabellaCamere.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "N° CAMERA"))
        item = self.tabellaCamere.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ALLESTIMENTO"))
        item = self.tabellaCamere.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "MATRIMONIALE"))
        item = self.tabellaCamere.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "N° SINGOLI"))
        item = self.tabellaCamere.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ARIA CONDIZIONATA"))
        item = self.tabellaCamere.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "VASCA IDROMASSAGGIO"))
        item = self.tabellaCamere.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "CULLA"))
        item = self.tabellaCamere.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "ANIMALE DOMESTICO"))
        item = self.tabellaCamere.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "FUMATORI"))
        item = self.tabellaCamere.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "MINI BAR"))
        item = self.tabellaCamere.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "SAUNA INTERNA"))
        item = self.tabellaCamere.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "VISTA PANORAMICA"))
        item = self.tabellaCamere.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "CASSAFORTE"))
        item = self.tabellaCamere.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "PRENOTAZIONE TAVOLO"))
        item = self.tabellaCamere.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "PREZZO"))
