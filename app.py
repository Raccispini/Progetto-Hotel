import sys

import PyQt5 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QPushButton
from interfacce import *
from interfacce.login_window_ui import Ui_Dialog_Login
from PyQt5 import uic

#prova
    
username="admin"
password="admin"

class Window_Login(QtWidgets.QMainWindow, Ui_Dialog_Login, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_Login.clicked.connect(self.accesso)

    def accesso(self):
        user=self.lineEdit_User.text()
        pw=self.lineEdit_User_2.text()
        if((user=="admin")&(pw=="admin")):
            print ("Accesso eseguito")
            
        else: 
            print("Accesso fallito")
            uic.loadUi("ui/login_error.ui")
      

if __name__ == "__main__":
    app = QApplication([])
    win = Window_Login()
    win.show()
    sys.exit(app.exec())

     