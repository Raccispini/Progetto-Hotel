from PyQt5.QtWidgets import QApplication
from interfacce.login_window_ui import Window_Login
      

if __name__ == "__main__":
    app = QApplication([])
    win = Window_Login()
    win.show()
    app.exec()
