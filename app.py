import sys

import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from interfacce import *
from interfacce.login_window_ui import Ui_Dialog_Login

class Window(QtWidgets.QMainWindow, Ui_Dialog_Login):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
      #  self.connectSignalsSlots()      

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

    