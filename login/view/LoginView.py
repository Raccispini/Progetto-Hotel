'''
__author__: Federico Pretini
'''
from PyQt5.QtWidgets import QMessageBox, QMainWindow
from home.view.HomeView import HomeView
from login.controller.LoginController import LoginController
from login.view.Ui_LoginView import Ui_LoginView

class LoginView(QMainWindow, Ui_LoginView):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.controller = LoginController()
        self.pushButton_Login.clicked.connect(lambda: self.accesso())

    def accesso(self):
        if self.controller.is_utente(self.LE_Username.text(), self.LE_Password.text()):
            main_window = HomeView(self.controller.get_utente().get_dipendente(),self)
            main_window.showMaximized()
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', 'I dati inseriti non sono stati inseriti\nin maniera corretta, per favore ritenta.', QMessageBox.Ok, QMessageBox.Ok)



