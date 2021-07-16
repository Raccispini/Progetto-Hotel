from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogoutView(object):
    def setupUi(self, logout_window):
        logout_window.setObjectName("logout_window")
        logout_window.resize(600, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(logout_window.sizePolicy().hasHeightForWidth())
        logout_window.setSizePolicy(sizePolicy)
        logout_window.setMinimumSize(QtCore.QSize(600, 300))
        logout_window.setMaximumSize(QtCore.QSize(600, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/resources/logo/logo_small_icon_only_inverted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        logout_window.setWindowIcon(icon)
        logout_window.setStyleSheet("background-image: url(ui/resources/logout/acquardens.png)")
        self.centralwidget = QtWidgets.QWidget(logout_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("background-image:url(ui/resources/logout/tpg.png)")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui/resources/logout/LogoMakr-4VbtfB (1).png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: solid black;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(ui/resources/logout/tpg.png)")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pB_chiudi = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_chiudi.sizePolicy().hasHeightForWidth())
        self.pB_chiudi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pB_chiudi.setFont(font)
        self.pB_chiudi.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_chiudi.setStyleSheet("#pB_chiudi{border: 4px solid black;\n"
"color: rgb(221, 34, 24);\n"
"border-radius: 10px;\n"
"border-style:outset;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(ui/resources/logout/tpg.png);}\n"
"#pB_chiudi:pressed{\n"
"border:2px solid gray;\n"
"border-style: inset;\n"
"}")
        self.pB_chiudi.setIconSize(QtCore.QSize(20, 20))
        self.pB_chiudi.setAutoRepeatInterval(100)
        self.pB_chiudi.setObjectName("pB_chiudi")
        self.horizontalLayout.addWidget(self.pB_chiudi)
        self.pB_disconnetti = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_disconnetti.sizePolicy().hasHeightForWidth())
        self.pB_disconnetti.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pB_disconnetti.setFont(font)
        self.pB_disconnetti.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_disconnetti.setStyleSheet("#pB_disconnetti{border: 4px solid black;\n"
"color: rgb(221, 34, 24);\n"
"border-radius: 10px;\n"
"border-style:outset;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 140), stop:1 rgba(255, 255, 255, 165));\n"
"background-image: url(ui/resources/logout/tpg.png);}\n"
"#pB_disconnetti:pressed{\n"
"border:2px solid gray;\n"
"border-style: inset;\n"
"}")
        self.pB_disconnetti.setObjectName("pB_disconnetti")
        self.horizontalLayout.addWidget(self.pB_disconnetti)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        logout_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(logout_window)
        QtCore.QMetaObject.connectSlotsByName(logout_window)

    def retranslateUi(self, logout_window):
        _translate = QtCore.QCoreApplication.translate
        logout_window.setWindowTitle(_translate("logout_window", "User Logout"))
        self.label_2.setText(_translate("logout_window", "Scegli l\'azione che vuoi eseguire.\n"
"Per tornare alla schermata home premere la X in alto a destra"))
        self.pB_chiudi.setText(_translate("logout_window", "CHIUDI APPLICAZIONE"))
        self.pB_disconnetti.setText(_translate("logout_window", "DISCONNETTI UTENTE"))
