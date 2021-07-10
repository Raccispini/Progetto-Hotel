from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PrenotaOmbrellone(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 269)
        MainWindow.setMinimumSize(QtCore.QSize(820, 269))
        MainWindow.setMaximumSize(QtCore.QSize(820, 269))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/resources/logo/logo_small_icon_only_inverted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("#MainWindow{background-image: url(ui/resources/Ombrelloni/thumb-1920-325895.jpg);}")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.cB_nominativo = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cB_nominativo.sizePolicy().hasHeightForWidth())
        self.cB_nominativo.setSizePolicy(sizePolicy)
        self.cB_nominativo.setMinimumSize(QtCore.QSize(400, 0))
        self.cB_nominativo.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cB_nominativo.setFont(font)
        self.cB_nominativo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cB_nominativo.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.cB_nominativo.setCurrentText("")
        self.cB_nominativo.setObjectName("cB_nominativo")
        self.cB_font(self.cB_nominativo)
        self.horizontalLayout_2.addWidget(self.cB_nominativo)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pB_prenota_ombrellone = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pB_prenota_ombrellone.setFont(font)
        self.pB_prenota_ombrellone.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_prenota_ombrellone.setObjectName("pB_prenota_ombrellone")
        self.horizontalLayout_4.addWidget(self.pB_prenota_ombrellone)
        self.pB_elimina_ombrellone = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pB_elimina_ombrellone.setFont(font)
        self.pB_elimina_ombrellone.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_elimina_ombrellone.setObjectName("pB_elimina_ombrellone")
        self.horizontalLayout_4.addWidget(self.pB_elimina_ombrellone)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.cB_camera = QtWidgets.QComboBox(self.centralwidget)
        self.cB_camera.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cB_camera.sizePolicy().hasHeightForWidth())
        self.cB_camera.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cB_camera.setFont(font)
        self.cB_camera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cB_camera.setObjectName("cB_camera")
        self.cB_font(self.cB_camera)
        self.horizontalLayout.addWidget(self.cB_camera)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.sB_sedie = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sB_sedie.sizePolicy().hasHeightForWidth())
        self.sB_sedie.setSizePolicy(sizePolicy)
        self.sB_sedie.setMinimumSize(QtCore.QSize(100, 0))
        self.sB_sedie.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sB_sedie.setFont(font)
        self.sB_sedie.setAlignment(QtCore.Qt.AlignCenter)
        self.sB_sedie.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sB_sedie.setKeyboardTracking(True)
        self.sB_sedie.setProperty("showGroupSeparator", False)
        self.sB_sedie.setMaximum(6)
        self.sB_sedie.setObjectName("sB_sedie")
        self.horizontalLayout.addWidget(self.sB_sedie)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.sB_sdraie = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sB_sdraie.sizePolicy().hasHeightForWidth())
        self.sB_sdraie.setSizePolicy(sizePolicy)
        self.sB_sdraie.setMinimumSize(QtCore.QSize(100, 0))
        self.sB_sdraie.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sB_sdraie.setFont(font)
        self.sB_sdraie.setAlignment(QtCore.Qt.AlignCenter)
        self.sB_sdraie.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.sB_sdraie.setKeyboardTracking(True)
        self.sB_sdraie.setProperty("showGroupSeparator", False)
        self.sB_sdraie.setMaximum(6)
        self.sB_sdraie.setObjectName("sB_sdraie")
        self.horizontalLayout.addWidget(self.sB_sdraie)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.cB_pagamento = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cB_pagamento.sizePolicy().hasHeightForWidth())
        self.cB_pagamento.setSizePolicy(sizePolicy)
        self.cB_pagamento.setMinimumSize(QtCore.QSize(0, 30))
        self.cB_pagamento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cB_pagamento.setObjectName("cB_pagamento")
        self.cB_pagamento.addItem("")
        self.cB_pagamento.addItem("")
        self.cB_pagamento.addItem("")
        self.cB_font(self.cB_pagamento)
        self.horizontalLayout_3.addWidget(self.cB_pagamento)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def cB_font(self, cB):
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setFamily("Arial")
        cB.setFont(font)
        cB.setEditable(True)
        line_Edit = cB.lineEdit()
        line_Edit.setAlignment(QtCore.Qt.AlignCenter)
        line_Edit.setFont(font)
        line_Edit.setReadOnly(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prenota ombrellone"))
        self.label.setText(_translate("MainWindow", "Nominativo:"))
        self.pB_prenota_ombrellone.setText(_translate("MainWindow", "Prenota"))
        self.pB_elimina_ombrellone.setText(_translate("MainWindow", "Elimina"))
        self.label_5.setText(_translate("MainWindow", "Camera:"))
        self.label_2.setText(_translate("MainWindow", "Sedie:"))
        self.label_3.setText(_translate("MainWindow", "Sdraie:"))
        self.label_4.setText(_translate("MainWindow", "Pagamento:"))
        self.cB_pagamento.setItemText(0, _translate("MainWindow", "Contanti"))
        self.cB_pagamento.setItemText(1, _translate("MainWindow", "Carta"))
        self.cB_pagamento.setItemText(2, _translate("MainWindow", "Addebito su conto camera"))
