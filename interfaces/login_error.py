# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_error.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Error_Login(object):
    def setupUi(self, Dialog_Error_Login):
        Dialog_Error_Login.setObjectName("Dialog_Error_Login")
        Dialog_Error_Login.setWindowModality(QtCore.Qt.NonModal)
        Dialog_Error_Login.resize(300, 131)
        Dialog_Error_Login.setMinimumSize(QtCore.QSize(300, 131))
        Dialog_Error_Login.setMaximumSize(QtCore.QSize(300, 131))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource_logo/logo_small_icon_only_inverted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_Error_Login.setWindowIcon(icon)
        Dialog_Error_Login.setAccessibleName("")
        Dialog_Error_Login.setAccessibleDescription("")
        Dialog_Error_Login.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog_Error_Login.setSizeGripEnabled(False)
        Dialog_Error_Login.setModal(False)
        self.label_2 = QtWidgets.QLabel(Dialog_Error_Login)
        self.label_2.setGeometry(QtCore.QRect(80, 10, 186, 39))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog_Error_Login)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Dialog_Error_Login)
        self.label.setGeometry(QtCore.QRect(-10, 10, 81, 41))
        self.label.setWhatsThis("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/resource_error/cross_error_rosso.png"))
        self.label.setObjectName("label")
        self.pushButton_OK_Error = QtWidgets.QPushButton(Dialog_Error_Login)
        self.pushButton_OK_Error.setGeometry(QtCore.QRect(105, 90, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.pushButton_OK_Error.setFont(font)
        self.pushButton_OK_Error.setObjectName("pushButton_OK_Error")

        self.retranslateUi(Dialog_Error_Login)
        self.pushButton_OK_Error.clicked.connect(Dialog_Error_Login.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Error_Login)

    def retranslateUi(self, Dialog_Error_Login):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Error_Login.setWindowTitle(_translate("Dialog_Error_Login", "Error"))
        Dialog_Error_Login.setWhatsThis(_translate("Dialog_Error_Login", "Errore di autentificazione. Controllare Username e Password, o consultare l\'admin per la loro reimpostazione."))
        self.label_2.setText(_translate("Dialog_Error_Login", "ACCESSO NEGATO!"))
        self.label_3.setText(_translate("Dialog_Error_Login", "Username o Password errati. Riprovare."))
        self.pushButton_OK_Error.setText(_translate("Dialog_Error_Login", "OK"))
        self.pushButton_OK_Error.setShortcut(_translate("Dialog_Error_Login", "Return"))

