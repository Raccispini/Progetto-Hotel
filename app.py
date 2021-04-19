import sys
from PyQt5.QtWidgets import QApplication
from login.view.LoginView import LoginView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LoginView()
    win.show()
    sys.exit(app.exec())
