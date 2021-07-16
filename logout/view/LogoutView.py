'''
__author__: Federico Pretini
'''
from PyQt5.QtWidgets import QMainWindow
from logout.view.Ui_LogoutView import Ui_LogoutView


class LogoutView(QMainWindow, Ui_LogoutView):
    def __init__(self, login_window, home_window, parent=None):
        super(LogoutView, self).__init__(parent)
        self.setupUi(self)
        self.login_window = login_window
        self.home_window = home_window
        self.pB_chiudi.clicked.connect(lambda: self.on_close())
        self.pB_disconnetti.clicked.connect(lambda: self.on_disconnetti())

    def on_disconnetti(self):
        self.login_window.LE_Username.clear()
        self.login_window.LE_Password.clear()
        self.home_window.close()
        self.close()
        self.login_window.show()

    def on_close(self):
        self.home_window.close()
        self.close()

