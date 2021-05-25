from PyQt5.QtWidgets import QMessageBox, QMainWindow
from home.view.HomeView import HomeView
from login.controller.LoginController import LoginController
from login.view.login_window_ui import Ui_Dialog_Login

class LoginView(QMainWindow, Ui_Dialog_Login):
    def __init__(self, parent=None):
        super(LoginView, self).__init__(parent)
        self.setupUi(self)
        #e' sbagliato salvare in chiaro le password, comunque ho creato una classe Utente.py solo per poter far funzionare il programma, poi vediamo
        #self.utente = Utente(self.LE_Username.text(), self.LE_Password.text())
        self.controller = LoginController()
        self.pushButton_Login.clicked.connect(self.accesso)

    def accesso(self):
        if self.controller.accesso(self.LE_Username.text(), self.LE_Password.text()):
            main_window = HomeView()
            main_window.show()
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', '''I dati inseriti non sono corretti oppure\n sono stati lasciati dei campi vuoti,\n per favore ritenta.''', QMessageBox.Ok, QMessageBox.Ok)



