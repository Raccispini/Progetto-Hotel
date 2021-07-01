import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.resources.Bar import resource_bar_rc

class Ui_BarView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1244, 946)
        MainWindow.setWindowTitle("Gestionale Bar")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\resources/logo/logo_small_icon_only_inverted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{background-image: url(:/resource_bar/bar.jpg) 0 0 0 0 stretch stretch;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(34, 0))
        self.label_8.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border: 2px solid black;\n"
"border-radius : 10px;\n"
"color: solid black;\n"
"font: 700 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 24, 0, 1, 1)
        self.cB_pasticceria = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cB_pasticceria.setFont(font)
        self.cB_pasticceria.setStyleSheet("font: 13pt \"Arial\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);\n"
"background-color: rgb(255, 255, 255);")
        self.cB_pasticceria.setEditable(True)
        self.cB_pasticceria.setEditable(True)
        line_edit = self.cB_pasticceria.lineEdit()
        line_edit.setAlignment(QtCore.Qt.AlignCenter)
        line_edit.setReadOnly(True)
        self.cB_pasticceria.setCurrentText("")
        self.cB_pasticceria.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.cB_pasticceria.setObjectName("cB_pasticceria")
        self.gridLayout_2.addWidget(self.cB_pasticceria, 29, 0, 1, 1)
        self.sB_aperitivi = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sB_aperitivi.setFont(font)
        self.sB_aperitivi.setStyleSheet("")
        self.sB_aperitivi.setAlignment(QtCore.Qt.AlignCenter)
        self.sB_aperitivi.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sB_aperitivi.setObjectName("sB_aperitivi")
        self.gridLayout_2.addWidget(self.sB_aperitivi, 18, 0, 1, 1)
        self.sB_vini = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sB_vini.setFont(font)
        self.sB_vini.setStyleSheet("")
        self.sB_vini.setAlignment(QtCore.Qt.AlignCenter)
        self.sB_vini.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sB_vini.setObjectName("sB_vini")
        self.gridLayout_2.addWidget(self.sB_vini, 22, 0, 1, 1)
        self.cB_liquori = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cB_liquori.setFont(font)
        self.cB_liquori.setStyleSheet("font: 13pt \"Arial\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);\n"
"background-color: rgb(255, 255, 255);")
        self.cB_liquori.setEditable(True)
        self.cB_liquori.setEditable(True)
        line_edit = self.cB_liquori.lineEdit()
        line_edit.setAlignment(QtCore.Qt.AlignCenter)
        line_edit.setReadOnly(True)
        self.cB_liquori.setCurrentText("")
        self.cB_liquori.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.cB_liquori.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.cB_liquori.setObjectName("cB_liquori")
        self.gridLayout_2.addWidget(self.cB_liquori, 25, 0, 1, 1)
        self.sB_analcolici = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sB_analcolici.setFont(font)
        self.sB_analcolici.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sB_analcolici.setStyleSheet("")
        self.sB_analcolici.setAlignment(QtCore.Qt.AlignCenter)
        self.sB_analcolici.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sB_analcolici.setObjectName("sB_analcolici")
        self.gridLayout_2.addWidget(self.sB_analcolici, 6, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(34, 0))
        self.label_9.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border: 2px solid black;\n"
"border-radius : 10px;\n"
"color: solid black;\n"
"font: 700 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 28, 0, 1, 1)
        self.sB_pasticceria = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sB_pasticceria.sizePolicy().hasHeightForWidth())
        self.sB_pasticceria.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sB_pasticceria.setFont(font)
        self.sB_pasticceria.setStyleSheet("")
        self.sB_pasticceria.setAlignment(QtCore.Qt.AlignCenter)
        self.sB_pasticceria.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sB_pasticceria.setObjectName("sB_pasticceria")
        self.gridLayout_2.addWidget(self.sB_pasticceria, 30, 0, 1, 1)
        self.sB_liquori = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sB_liquori.setFont(font)
        self.sB_liquori.setStyleSheet("")
        self.sB_liquori.setAlignment(QtCore.Qt.AlignCenter)
        self.sB_liquori.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sB_liquori.setObjectName("sB_liquori")
        self.gridLayout_2.addWidget(self.sB_liquori, 26, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 19, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(34, 0))
        self.label_7.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border: 2px solid black;\n"
"border-radius : 10px;\n"
"color: solid black;\n"
"font: 700 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 20, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 23, 0, 1, 1)
        self.cB_aperitivi = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cB_aperitivi.setFont(font)
        self.cB_aperitivi.setStyleSheet("font: 13pt \"Arial\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);\n"
"background-color: rgb(255, 255, 255);")
        self.cB_aperitivi.setEditable(True)
        self.cB_aperitivi.setEditable(True)
        line_edit = self.cB_aperitivi.lineEdit()
        line_edit.setAlignment(QtCore.Qt.AlignCenter)
        line_edit.setReadOnly(True)
        self.cB_aperitivi.setCurrentText("")
        self.cB_aperitivi.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.cB_aperitivi.setObjectName("cB_aperitivi")
        self.gridLayout_2.addWidget(self.cB_aperitivi, 17, 0, 1, 1)
        self.cB_bibite = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cB_bibite.setFont(font)
        self.cB_bibite.setStyleSheet("font: 13pt \"Arial\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);\n"
"background-color: rgb(255, 255, 255);")
        self.cB_bibite.setEditable(True)
        self.cB_bibite.setEditable(True)
        line_edit = self.cB_bibite.lineEdit()
        line_edit.setAlignment(QtCore.Qt.AlignCenter)
        line_edit.setReadOnly(True)
        self.cB_bibite.setCurrentText("")
        self.cB_bibite.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.cB_bibite.setObjectName("cB_bibite")
        self.gridLayout_2.addWidget(self.cB_bibite, 9, 0, 1, 1)
        self.sB_bibite = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sB_bibite.setFont(font)
        self.sB_bibite.setStyleSheet("")
        self.sB_bibite.setAlignment(QtCore.Qt.AlignCenter)
        self.sB_bibite.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sB_bibite.setObjectName("sB_bibite")
        self.gridLayout_2.addWidget(self.sB_bibite, 10, 0, 1, 1)
        self.pB_alcolici = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_alcolici.sizePolicy().hasHeightForWidth())
        self.pB_alcolici.setSizePolicy(sizePolicy)
        self.pB_alcolici.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pB_alcolici.setFont(font)
        self.pB_alcolici.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_alcolici.setStyleSheet("QPushButton{background-image: url(:/resource_bar/tpg.png);\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,     stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"                    border: 2px rgb(221, 34, 24);\n"
"                    border-style: outset;\n"
"                    border-radius: 10px;}\n"
"QPushButton:pressed{ \n"
"                                border-style: inset;\n"
"                                }")
        self.pB_alcolici.setObjectName("pB_alcolici")
        self.gridLayout_2.addWidget(self.pB_alcolici, 2, 1, 1, 1)
        self.pB_aperitivi = QtWidgets.QPushButton(self.centralwidget)
        self.pB_aperitivi.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pB_aperitivi.setFont(font)
        self.pB_aperitivi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_aperitivi.setStyleSheet("QPushButton{background-image: url(:/resource_bar/tpg.png);\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,     stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"                    border: 2px rgb(221, 34, 24);\n"
"                    border-style: outset;\n"
"                    border-radius: 10px;}\n"
"QPushButton:pressed{ \n"
"                                border-style: inset;\n"
"                                }")
        self.pB_aperitivi.setObjectName("pB_aperitivi")
        self.gridLayout_2.addWidget(self.pB_aperitivi, 18, 1, 1, 1)
        self.pB_liquori = QtWidgets.QPushButton(self.centralwidget)
        self.pB_liquori.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pB_liquori.setFont(font)
        self.pB_liquori.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_liquori.setStyleSheet("QPushButton{background-image: url(:/resource_bar/tpg.png);\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,     stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"                    border: 2px rgb(221, 34, 24);\n"
"                    border-style: outset;\n"
"                    border-radius: 10px;}\n"
"QPushButton:pressed{ \n"
"                                border-style: inset;\n"
"                                }")
        self.pB_liquori.setObjectName("pB_liquori")
        self.gridLayout_2.addWidget(self.pB_liquori, 26, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(34, 0))
        self.label_3.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: 2px solid black;\n"
"border-radius : 10px;\n"
"color: solid black;\n"
"font: 700 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(34, 0))
        self.label_4.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: 2px solid black;\n"
"border-radius : 10px;\n"
"color: solid black;\n"
"font: 700 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 8, 0, 1, 1)
        self.cB_alcolici = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cB_alcolici.sizePolicy().hasHeightForWidth())
        self.cB_alcolici.setSizePolicy(sizePolicy)
        self.cB_alcolici.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cB_alcolici.setFont(font)
        self.cB_alcolici.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cB_alcolici.setAutoFillBackground(False)
        self.cB_alcolici.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"font: 13pt \"Arial\";\n"
"background-image: url(:/resource_bar/tpg.png);\n"
"background-color: rgb(255, 255, 255);")
        self.cB_alcolici.setEditable(True)
        self.cB_alcolici.setEditable(True)
        line_edit = self.cB_alcolici.lineEdit()
        line_edit.setAlignment(QtCore.Qt.AlignCenter)
        line_edit.setReadOnly(True)
        self.cB_alcolici.setCurrentText("")
        self.cB_alcolici.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.cB_alcolici.setObjectName("cB_alcolici")
        self.gridLayout_2.addWidget(self.cB_alcolici, 1, 0, 1, 1)
        self.sB_alcolici = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sB_alcolici.sizePolicy().hasHeightForWidth())
        self.sB_alcolici.setSizePolicy(sizePolicy)
        self.sB_alcolici.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sB_alcolici.setFont(font)
        self.sB_alcolici.setStyleSheet("")
        self.sB_alcolici.setAlignment(QtCore.Qt.AlignCenter)
        self.sB_alcolici.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sB_alcolici.setObjectName("sB_alcolici")
        self.gridLayout_2.addWidget(self.sB_alcolici, 2, 0, 1, 1)
        self.cB_analcolici = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cB_analcolici.setFont(font)
        self.cB_analcolici.setStyleSheet("font: 13pt \"Arial\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);\n"
"background-color: rgb(255, 255, 255);")
        self.cB_analcolici.setEditable(True)
        self.cB_analcolici.setEditable(True)
        line_edit = self.cB_analcolici.lineEdit()
        line_edit.setAlignment(QtCore.Qt.AlignCenter)
        line_edit.setReadOnly(True)
        self.cB_analcolici.setCurrentText("")
        self.cB_analcolici.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.cB_analcolici.setObjectName("cB_analcolici")
        self.gridLayout_2.addWidget(self.cB_analcolici, 5, 0, 1, 1)
        self.cB_caffetteria = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cB_caffetteria.sizePolicy().hasHeightForWidth())
        self.cB_caffetteria.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cB_caffetteria.setFont(font)
        self.cB_caffetteria.setStyleSheet("font: 13pt \"Arial\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);\n"
"background-color: rgb(255, 255, 255);")
        self.cB_caffetteria.setEditable(True)
        self.cB_caffetteria.setEditable(True)
        line_edit = self.cB_caffetteria.lineEdit()
        line_edit.setAlignment(QtCore.Qt.AlignCenter)
        line_edit.setReadOnly(True)
        self.cB_caffetteria.setCurrentText("")
        self.cB_caffetteria.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.cB_caffetteria.setObjectName("cB_caffetteria")
        self.gridLayout_2.addWidget(self.cB_caffetteria, 13, 0, 1, 1)
        self.sB_caffetteria = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.sB_caffetteria.setFont(font)
        self.sB_caffetteria.setStyleSheet("")
        self.sB_caffetteria.setAlignment(QtCore.Qt.AlignCenter)
        self.sB_caffetteria.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sB_caffetteria.setObjectName("sB_caffetteria")
        self.gridLayout_2.addWidget(self.sB_caffetteria, 14, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(34, 0))
        self.label_5.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: 2px solid black;\n"
"border-radius : 10px;\n"
"color: solid black;\n"
"font: 700 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 12, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(34, 0))
        self.label_6.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: 2px solid black;\n"
"border-radius : 10px;\n"
"color: solid black;\n"
"font: 700 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 16, 0, 1, 1)
        self.cB_vini = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cB_vini.setFont(font)
        self.cB_vini.setStyleSheet("font: 13pt \"Arial\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);\n"
"background-color: rgb(255, 255, 255);")
        self.cB_vini.setEditable(True)
        self.cB_vini.setEditable(True)
        line_edit = self.cB_vini.lineEdit()
        line_edit.setAlignment(QtCore.Qt.AlignCenter)
        line_edit.setReadOnly(True)
        self.cB_vini.setCurrentText("")
        self.cB_vini.setInsertPolicy(QtWidgets.QComboBox.InsertAlphabetically)
        self.cB_vini.setObjectName("cB_vini")
        self.gridLayout_2.addWidget(self.cB_vini, 21, 0, 1, 1)
        self.pB_analcolici = QtWidgets.QPushButton(self.centralwidget)
        self.pB_analcolici.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pB_analcolici.setFont(font)
        self.pB_analcolici.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_analcolici.setStyleSheet("QPushButton{background-image: url(:/resource_bar/tpg.png);\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,     stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"                    border: 2px rgb(221, 34, 24);\n"
"                    border-style: outset;\n"
"                    border-radius: 10px;}\n"
"QPushButton:pressed{ \n"
"                                border-style: inset;\n"
"                                }")
        self.pB_analcolici.setObjectName("pB_analcolici")
        self.gridLayout_2.addWidget(self.pB_analcolici, 6, 1, 1, 1)
        self.pB_vini = QtWidgets.QPushButton(self.centralwidget)
        self.pB_vini.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pB_vini.setFont(font)
        self.pB_vini.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_vini.setStyleSheet("QPushButton{background-image: url(:/resource_bar/tpg.png);\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,     stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"                    border: 2px rgb(221, 34, 24);\n"
"                    border-style: outset;\n"
"                    border-radius: 10px;}\n"
"QPushButton:pressed{ \n"
"                                border-style: inset;\n"
"                                }")
        self.pB_vini.setObjectName("pB_vini")
        self.gridLayout_2.addWidget(self.pB_vini, 22, 1, 1, 1)
        self.pB_bibite = QtWidgets.QPushButton(self.centralwidget)
        self.pB_bibite.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pB_bibite.setFont(font)
        self.pB_bibite.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_bibite.setStyleSheet("QPushButton{background-image: url(:/resource_bar/tpg.png);\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,     stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"                    border: 2px rgb(221, 34, 24);\n"
"                    border-style: outset;\n"
"                    border-radius: 10px;}\n"
"QPushButton:pressed{ \n"
"                                border-style: inset;\n"
"                                }")
        self.pB_bibite.setObjectName("pB_bibite")
        self.gridLayout_2.addWidget(self.pB_bibite, 10, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 3, 0, 1, 1)
        self.pB_caffetteria = QtWidgets.QPushButton(self.centralwidget)
        self.pB_caffetteria.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pB_caffetteria.setFont(font)
        self.pB_caffetteria.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_caffetteria.setStyleSheet("QPushButton{background-image: url(:/resource_bar/tpg.png);\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,     stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"                    border: 2px rgb(221, 34, 24);\n"
"                    border-style: outset;\n"
"                    border-radius: 10px;}\n"
"QPushButton:pressed{ \n"
"                                border-style: inset;\n"
"                                }")
        self.pB_caffetteria.setObjectName("pB_caffetteria")
        self.gridLayout_2.addWidget(self.pB_caffetteria, 14, 1, 1, 1)
        self.pB_pasticceria = QtWidgets.QPushButton(self.centralwidget)
        self.pB_pasticceria.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pB_pasticceria.setFont(font)
        self.pB_pasticceria.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_pasticceria.setStyleSheet("QPushButton{background-image: url(:/resource_bar/tpg.png);\n"
"                    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1,     stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"                    border: 2px rgb(221, 34, 24);\n"
"                    border-style: outset;\n"
"                    border-radius: 10px;}\n"
"QPushButton:pressed{ \n"
"                                border-style: inset;\n"
"                                }")
        self.pB_pasticceria.setObjectName("pB_pasticceria")
        self.gridLayout_2.addWidget(self.pB_pasticceria, 30, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(34, 0))
        self.label_2.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 2px solid black;\n"
"border-radius : 10px;\n"
"color: solid black;\n"
"font: 700 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 7, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 15, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 11, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 27, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(30, 10, 20, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tW_scontrino = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tW_scontrino.setFont(font)
        self.tW_scontrino.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tW_scontrino.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tW_scontrino.setStyleSheet("background-image: url(:/resource_bar/tpg.png);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(255, 255, 255, 225), stop:1 rgba(255, 255, 255, 227));")
        self.tW_scontrino.setAutoScrollMargin(16)
        self.tW_scontrino.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tW_scontrino.setAlternatingRowColors(True)
        self.tW_scontrino.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tW_scontrino.setShowGrid(True)
        self.tW_scontrino.setRowCount(5)
        self.tW_scontrino.setColumnCount(4)
        self.tW_scontrino.setObjectName("tW_scontrino")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_scontrino.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_scontrino.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_scontrino.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_scontrino.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tW_scontrino.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tW_scontrino.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tW_scontrino.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tW_scontrino.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tW_scontrino.setItem(3, 3, item)
        self.tW_scontrino.horizontalHeader().setVisible(True)
        self.tW_scontrino.horizontalHeader().setDefaultSectionSize(175)
        self.tW_scontrino.horizontalHeader().setHighlightSections(True)
        self.tW_scontrino.horizontalHeader().setMinimumSectionSize(40)
        self.tW_scontrino.horizontalHeader().setSortIndicatorShown(False)
        self.tW_scontrino.horizontalHeader().setStretchLastSection(True)
        self.tW_scontrino.verticalHeader().setVisible(True)
        self.tW_scontrino.verticalHeader().setCascadingSectionResizes(False)
        self.tW_scontrino.verticalHeader().setDefaultSectionSize(24)
        self.tW_scontrino.verticalHeader().setHighlightSections(True)
        self.tW_scontrino.verticalHeader().setMinimumSectionSize(24)
        self.tW_scontrino.verticalHeader().setSortIndicatorShown(False)
        self.tW_scontrino.verticalHeader().setStretchLastSection(False)
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
        #self.tW_scontrino.setHorizontalHeaderLabels("Consumazione;Quantità;Costo Unitario;Costo Totale").split(";")
=======

>>>>>>> Stashed changes
=======

>>>>>>> Stashed changes
=======

>>>>>>> Stashed changes
        self.verticalLayout_4.addWidget(self.tW_scontrino)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(25, 10, 32, 10)
        self.gridLayout.setHorizontalSpacing(58)
        self.gridLayout.setVerticalSpacing(18)
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border: 2px solid black;\n"
"border-radius : 10px;\n"
"color: solid black;\n"
"font: 700 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 1, 1, 1)
        self.cB_metodopagamento = QtWidgets.QComboBox(self.centralwidget)
        self.cB_metodopagamento.setEditable(True)
        line_edit = self.cB_metodopagamento.lineEdit()
        line_edit.setAlignment(QtCore.Qt.AlignCenter)
        line_edit.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cB_metodopagamento.setFont(font)
        self.cB_metodopagamento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cB_metodopagamento.setStyleSheet("font: 18pt \"Arial\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);\n"
"background-color: rgb(255, 255, 255);")
        self.cB_metodopagamento.setObjectName("cB_metodopagamento")
        self.cB_metodopagamento.addItem("")
        self.cB_metodopagamento.addItem("")
        self.cB_metodopagamento.addItem("")
        self.gridLayout.addWidget(self.cB_metodopagamento, 1, 0, 1, 1)
        self.LE_totaleconto = QtWidgets.QLineEdit(self.centralwidget)
        self.LE_totaleconto.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LE_totaleconto.sizePolicy().hasHeightForWidth())
        self.LE_totaleconto.setSizePolicy(sizePolicy)
        self.LE_totaleconto.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LE_totaleconto.setFont(font)
        self.LE_totaleconto.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.LE_totaleconto.setAlignment(QtCore.Qt.AlignCenter)
        self.LE_totaleconto.setReadOnly(True)
        self.LE_totaleconto.setPlaceholderText("")
        self.LE_totaleconto.setObjectName("LE_totaleconto")
        self.gridLayout.addWidget(self.LE_totaleconto, 1, 3, 1, 1)
        self.cB_camera = QtWidgets.QComboBox(self.centralwidget)
        self.cB_camera.setEnabled(True)
        self.cB_camera.setEditable(True)
        line_edit = self.cB_camera.lineEdit()
        line_edit.setAlignment(QtCore.Qt.AlignCenter)
        line_edit.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cB_camera.setFont(font)
        self.cB_camera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cB_camera.setStyleSheet("font: 18pt \"Arial\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);\n"
"background-color: rgb(255, 255, 255);")
        self.cB_camera.setEditable(False)
        self.cB_camera.setObjectName("cB_camera")
        self.cB_camera.addItem("")
        self.gridLayout.addWidget(self.cB_camera, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border: 2px solid black;\n"
"border-radius : 10px;\n"
"color: solid black;\n"
"font: 700 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("border: 2px solid black;\n"
"border-radius : 10px;\n"
"color: solid black;\n"
"font: 700 14pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pB_salva = QtWidgets.QPushButton(self.centralwidget)
        self.pB_salva.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pB_salva.setFont(font)
        self.pB_salva.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_salva.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.pB_salva.setObjectName("pB_salva")
        self.horizontalLayout_2.addWidget(self.pB_salva)
        self.pB_elimina = QtWidgets.QPushButton(self.centralwidget)
        self.pB_elimina.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pB_elimina.setFont(font)
        self.pB_elimina.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_elimina.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(:/resource_bar/tpg.png);")
        self.pB_elimina.setObjectName("pB_elimina")
        self.horizontalLayout_2.addWidget(self.pB_elimina)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Funzione che aggiorna gli item nelle combo box

    def update_data(self, MainWindow):
            con = sqlite3.connect('database.db')
            query = 'select * from Bar;'
            bar = con.execute(query).fetchall()
            self.alcolici = []
            self.analcolici = []
            self.bibite = []
            self.caffetteria = []
            self.aperitivi = []
            self.vini = []
            self.liquori = []
            self.pasticceria = []

            for categoria in bar:
                    if categoria[2] == 'Alcolici':
                            self.alcolici.append(categoria)
                    if categoria[2] == 'Analcolici':
                            self.analcolici.append(categoria)
                    if categoria[2] == 'Aperitivi':
                            self.aperitivi.append(categoria)
                    if categoria[2] == 'Bibite':
                            self.bibite.append(categoria)
                    if categoria[2] == 'Caffetteria':
                            self.caffetteria.append(categoria)
                    if categoria[2] == 'Vini':
                            self.vini.append(categoria)
                    if categoria[2] == 'Liquori':
                            self.liquori.append(categoria)
                    if categoria[2] == 'Pasticceria':
                            self.pasticceria.append(categoria)
            self.cB_alcolici.clear()
            for categoria in range(0, len(self.alcolici)):
                    self.cB_alcolici.addItem(self.alcolici[categoria][1])
            self.cB_analcolici.clear()
            for categoria in range(0, len(self.analcolici)):
                    self.cB_analcolici.addItem(self.analcolici[categoria][1])
            self.cB_aperitivi.clear()
            for categoria in range(0, len(self.aperitivi)):
                    self.cB_aperitivi.addItem(self.aperitivi[categoria][1])
            self.cB_bibite.clear()
            for categoria in range(0, len(self.bibite)):
                    self.cB_bibite.addItem(self.bibite[categoria][1])
            self.cB_caffetteria.clear()
            for categoria in range(0, len(self.caffetteria)):
                    self.cB_caffetteria.addItem(self.caffetteria[categoria][1])
            self.cB_liquori.clear()
            for categoria in range(0, len(self.liquori)):
                    self.cB_liquori.addItem(self.liquori[categoria][1])
            self.cB_pasticceria.clear()
            for categoria in range(0, len(self.pasticceria)):
                    self.cB_pasticceria.addItem(self.pasticceria[categoria][1])
            self.cB_vini.clear()
            for categoria in range(0, len(self.vini)):
                    self.cB_vini.addItem(self.vini[categoria][1])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "Liquori"))
        self.cB_pasticceria.setItemText(1, _translate("MainWindow", "Brioches"))
        self.cB_pasticceria.setItemText(2, _translate("MainWindow", "Ciambellone"))
        self.cB_pasticceria.setItemText(3, _translate("MainWindow", "Pasta grande"))
        self.cB_pasticceria.setItemText(4, _translate("MainWindow", "Pasta piccola"))
        self.cB_pasticceria.setItemText(5, _translate("MainWindow", "Torta della casa"))
        self.cB_liquori.setItemText(1, _translate("MainWindow", "Amaretto"))
        self.cB_liquori.setItemText(2, _translate("MainWindow", "Baileys"))
        self.cB_liquori.setItemText(3, _translate("MainWindow", "Gin"))
        self.cB_liquori.setItemText(4, _translate("MainWindow", "Ginger Ale"))
        self.cB_liquori.setItemText(5, _translate("MainWindow", "Jack Daniel\'s"))
        self.cB_liquori.setItemText(6, _translate("MainWindow", "Malibù"))
        self.cB_liquori.setItemText(7, _translate("MainWindow", "Marsala"))
        self.cB_liquori.setItemText(8, _translate("MainWindow", "Vodka"))
        self.label_9.setText(_translate("MainWindow", "Pasticceria"))
        self.label_7.setText(_translate("MainWindow", "Vini"))
        self.cB_aperitivi.setItemText(1, _translate("MainWindow", "Aperitivo completo"))
        self.cB_aperitivi.setItemText(2, _translate("MainWindow", "Aperol"))
        self.cB_aperitivi.setItemText(3, _translate("MainWindow", "Campari"))
        self.cB_aperitivi.setItemText(4, _translate("MainWindow", "Crodino"))
        self.cB_aperitivi.setItemText(5, _translate("MainWindow", "Martini"))
        self.cB_bibite.setItemText(1, _translate("MainWindow", "Bibita alla spina"))
        self.cB_bibite.setItemText(2, _translate("MainWindow", "Bibita in lattina"))
        self.cB_bibite.setItemText(3, _translate("MainWindow", "Birra piccola"))
        self.cB_bibite.setItemText(4, _translate("MainWindow", "Birra media"))
        self.cB_bibite.setItemText(5, _translate("MainWindow", "Birra grande"))
        self.cB_bibite.setItemText(6, _translate("MainWindow", "Spremuta"))
        self.cB_bibite.setItemText(7, _translate("MainWindow", "Succo di frutta"))
        self.pB_alcolici.setText(_translate("MainWindow", "Aggiungi"))
        self.pB_aperitivi.setText(_translate("MainWindow", "Aggiungi"))
        self.pB_liquori.setText(_translate("MainWindow", "Aggiungi"))
        self.label_3.setText(_translate("MainWindow", "Analcolici"))
        self.label_4.setText(_translate("MainWindow", "Bibite"))
        self.cB_alcolici.setItemText(1, _translate("MainWindow", "Cuba Libre"))
        self.cB_alcolici.setItemText(2, _translate("MainWindow", "Gin Lemon"))
        self.cB_alcolici.setItemText(3, _translate("MainWindow", "Gin Tonic"))
        self.cB_alcolici.setItemText(4, _translate("MainWindow", "London Mule"))
        self.cB_alcolici.setItemText(5, _translate("MainWindow", "Mojito"))
        self.cB_alcolici.setItemText(6, _translate("MainWindow", "Vodka Cola"))
        self.cB_alcolici.setItemText(7, _translate("MainWindow", "Vodka Lemon"))
        self.cB_alcolici.setItemText(8, _translate("MainWindow", "Moscow Mule"))
        self.cB_alcolici.setItemText(9, _translate("MainWindow", "Vodka Redbull"))
        self.cB_analcolici.setItemText(1, _translate("MainWindow", " All Shook Up"))
        self.cB_analcolici.setItemText(2, _translate("MainWindow", "Anita"))
        self.cB_analcolici.setItemText(3, _translate("MainWindow", "Banshee"))
        self.cB_analcolici.setItemText(4, _translate("MainWindow", "Bar Vienna"))
        self.cB_analcolici.setItemText(5, _translate("MainWindow", "Caffè Astoria"))
        self.cB_analcolici.setItemText(6, _translate("MainWindow", "Carrot Cream"))
        self.cB_analcolici.setItemText(7, _translate("MainWindow", "Cool Passion"))
        self.cB_analcolici.setItemText(8, _translate("MainWindow", "Frozen Mela Kiwi"))
        self.cB_analcolici.setItemText(9, _translate("MainWindow", "Iced Mint Tea"))
        self.cB_caffetteria.setItemText(1, _translate("MainWindow", "Caffè corretto"))
        self.cB_caffetteria.setItemText(2, _translate("MainWindow", "Caffè decaffeinato"))
        self.cB_caffetteria.setItemText(3, _translate("MainWindow", "Caffè d\'orzo"))
        self.cB_caffetteria.setItemText(4, _translate("MainWindow", "Caffè espresso"))
        self.cB_caffetteria.setItemText(5, _translate("MainWindow", "Cappuccino"))
        self.cB_caffetteria.setItemText(6, _translate("MainWindow", "Cappuccino decaffeinato"))
        self.cB_caffetteria.setItemText(7, _translate("MainWindow", "Cioccolata calda"))
        self.cB_caffetteria.setItemText(8, _translate("MainWindow", "Latte"))
        self.cB_caffetteria.setItemText(9, _translate("MainWindow", "Latte macchiato"))
        self.cB_caffetteria.setItemText(10, _translate("MainWindow", "Thè"))
        self.cB_caffetteria.setItemText(11, _translate("MainWindow", "Thè caldo"))
        self.label_5.setText(_translate("MainWindow", "Caffetteria"))
        self.label_6.setText(_translate("MainWindow", "Aperitivi"))
        self.cB_vini.setItemText(1, _translate("MainWindow", "Bottiglia bianco"))
        self.cB_vini.setItemText(2, _translate("MainWindow", "Bottiglia prosecco"))
        self.cB_vini.setItemText(3, _translate("MainWindow", "Bottiglia rosso"))
        self.cB_vini.setItemText(4, _translate("MainWindow", "Calice bianco"))
        self.cB_vini.setItemText(5, _translate("MainWindow", "Calice prosecco"))
        self.cB_vini.setItemText(6, _translate("MainWindow", "Calice rosso"))
        self.cB_vini.setItemText(7, _translate("MainWindow", "Champagne"))
        self.pB_analcolici.setText(_translate("MainWindow", "Aggiungi"))
        self.pB_vini.setText(_translate("MainWindow", "Aggiungi"))
        self.pB_bibite.setText(_translate("MainWindow", "Aggiungi"))
        self.pB_caffetteria.setText(_translate("MainWindow", "Aggiungi"))
        self.pB_pasticceria.setText(_translate("MainWindow", "Aggiungi"))
        self.label_2.setText(_translate("MainWindow", "Alcolici"))
        self.lista = []
        self.tW_scontrino.setSortingEnabled(False)
        item = self.tW_scontrino.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Consumazione"))
        item = self.tW_scontrino.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantità"))
        item = self.tW_scontrino.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Importo"))
        item = self.tW_scontrino.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Importo TOT"))
        __sortingEnabled = self.tW_scontrino.isSortingEnabled()
        self.tW_scontrino.setSortingEnabled(False)
        item = self.tW_scontrino.item(0, 0)
        item.setText(_translate("MainWindow", "Vodka"))
        item = self.tW_scontrino.item(0, 1)
        item.setText(_translate("MainWindow", "3"))
        item = self.tW_scontrino.item(0, 2)
        item.setText(_translate("MainWindow", "5"))
        item = self.tW_scontrino.item(0, 3)
        item.setText(_translate("MainWindow", "15"))
        self.tW_scontrino.setSortingEnabled(__sortingEnabled)
        self.label_11.setText(_translate("MainWindow", "Camera:"))
        self.cB_metodopagamento.setItemText(0, _translate("MainWindow", "Contanti"))
        self.cB_metodopagamento.setItemText(1, _translate("MainWindow", "Carta di debito o credito"))
        self.cB_metodopagamento.setItemText(2, _translate("MainWindow", "Acconto"))
        self.LE_totaleconto.setText(_translate("MainWindow", "18.00 €"))
        self.cB_camera.setItemText(0, _translate("MainWindow", "Vuoto"))
        self.label_12.setText(_translate("MainWindow", "TOTALE:"))
        self.label_10.setText(_translate("MainWindow", "Metodo di pagamento:"))
        self.pB_salva.setText(_translate("MainWindow", "Salva"))
        self.pB_elimina.setText(_translate("MainWindow", "Elimina"))

# metodo che aggiunge l'item alla tabella a destra
    def update_table(self):
        self.tW_scontrino.setRowCount(0)
        for i in range(0, len(self.lista)):
                self.tW_scontrino.insertRow(i)
                self.tW_scontrino.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.lista[i][0])))
                self.tW_scontrino.setItem(i, 1, QtWidgets.QTableWidgetItem(str(self.lista[i][1])))
                self.tW_scontrino.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.lista[i][2])))
                self.tW_scontrino.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.lista[i][3])))


    '''def get_item(self, combo, category):
        item = str(combo.currentText())'''

    def get_item(self, combo, category):
        item = str(combo.currentText())
        if category == 'Alcolici':
                qt = int(self.sB_alcolici.text())
                for i in self.alcolici:
                        if i[1] == item:
                                return (i, qt)
        if category == 'Analcolici':
                qt = int(self.sB_analcolici.text())
                for i in self.analcolici:
                        if i[1] == item:
                                return (i, qt)
        if category == 'Aperitivi':
                qt = int(self.sB_aperitivi.text())
                for i in self.aperitivi:
                        if i[1] == item:
                                return (i, qt)
        if category == 'Bibite':
                qt = int(self.sB_bibite.text())
                for i in self.bibite:
                        if i[1] == item:
                                return (i, qt)
        if category == 'Caffetteria':
                qt = int(self.sB_caffetteria.text())
                for i in self.caffetteria:
                        if i[1] == item:
                                return (i, qt)
        if category == 'Liquori':
                qt = int(self.sB_liquori.text())
                for i in self.liquori:
                        if i[1] == item:
                                return (i, qt)
        if category == 'Pasticceria':
                qt = int(self.sB_pasticceria.text())
                for i in self.pasticceria:
                        if i[1] == item:
                                return (i, qt)
        if category == 'Vini':
                qt = int(self.sB_vini.text())
                for i in self.vini:
                        if i[1] == item:
                                return (i, qt)

    def action(self, combo, category):
        item = self.get_item(combo, category)
        self.list.append((item[0][2], item[1], item[0][3], int(item[1]) * int(item[0][3])))
        self.update_table()

    def update_tot(self):
        tot = 0
        if not len(self.lista) == 0:
                for i in range(0, len(self.lista)):
                        tot += float(self.lista[i][3])
        self.LE_totaleconto.setText(str(tot) + ' €')

