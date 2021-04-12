import sys 
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QPushButton
from interfacce import *
from interfacce.login_window_ui import Ui_Dialog_Login
from interfacce.main_window_ui import Ui_MainWindow


#prova
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
            self.main = Window_Main()
            self.main.show()
            self.hide()
        else: 
            print("Accesso fallito")
            window_error = Ui_Login_Error(self)
            window_error.exec()


class Ui_Login_Error(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('ui\login_error.ui', self)

class Window_Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalSlot()

    def connectSignalSlot(self):
        self.actionAmministrativo.triggered.connect(lambda: print("Finestra Amministrativo Aperta"))
        self.actionCamere.triggered.connect(lambda: print("Finestra Camere Aperta"))
        self.actionAnagrafiche.triggered.connect(lambda: print("Finestra Anagrafiche Aperta"))
        self.actionMagazzino.triggered.connect(lambda: print("Finestra Magazzino Aperta"))
        self.actionMeteo.triggered.connect(lambda: print("Finestra Meteo Aperta"))
        self.actionOmbrelloni.triggered.connect(lambda: print("Finestra Ombrelloni Aperta"))
        self.actionRicerca.triggered.connect(lambda: print("Finestra Ricerca Aperta"))
        self.actionRistorante.triggered.connect(lambda: print("Finestra Ristorante Aperta"))
        self.actionStrumenti.triggered.connect(lambda: print("Finestra Strumenti Aperta"))
        self.actionBar.triggered.connect(lambda: print("Finestra Bar Aperta"))
        self.actionUscita.triggered.connect(self.close)
        

if __name__ == "__main__":
    app = QApplication([])
    win = Window_Login()
    win.show()
    app.exec()
