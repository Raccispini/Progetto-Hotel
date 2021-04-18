import sys
from PyQt5.QtWidgets import QApplication
from login.views.login_window_ui import Window_Login
      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window_Login()
    win.show()
    sys.exit(app.exec())
