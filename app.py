'''
__author__: Federico Pretini
'''
import sys
from PyQt5.QtWidgets import QApplication
from login.view.LoginView import LoginView


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginView()
    login_window.show()
    sys.exit(app.exec())
