from interfacce.main_window_ui import Window_Main
from login.model.LoginModel import LoginModel
from login.view.login_window_ui import  Ui_Dialog_Login
from PyQt5 import QtWidgets


class LoginView(QtWidgets.QMainWindow, Ui_Dialog_Login):
    def __init__(self, parent=None):
        super(LoginView, self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.pushButton_Login.clicked.connect(self.accesso)

    def accesso(self):
        login_model = LoginModel(self.lineEdit_User.text(),self.lineEdit_User_2.text())
        if login_model.accedi:
            main_window = Window_Main()
            main_window.show()
            self.hide()
        else:
            # da mettere la finestra di errore
            print("errore")




