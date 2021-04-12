import sys 
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QPushButton
from interfacce import *
from interfacce.login_window_ui import Ui_Dialog_Login
from interfacce.main_window_ui import Ui_MainWindow


#prova
    
username="admin"
password="admin"

class Window_Login(QtWidgets.QMainWindow, Ui_Dialog_Login):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_Login.clicked.connect(self.accesso)

    def accesso(self):
        user=self.lineEdit_User.text()
        pw=self.lineEdit_User_2.text()
        if((user=="admin")&(pw=="admin")):
            print ("Accesso eseguito")
            self.main_window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.main_window)
            self.main_window.show()
            self.hide()
        else: 
            print("Accesso fallito")
            window_error = Ui_Login_Error(self)
            window_error.exec()


class Ui_Login_Error(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('ui\login_error.ui', self)


if __name__ == "__main__":
    app = QApplication([])
    win = Window_Login()
    win.show()
    app.exec()
     