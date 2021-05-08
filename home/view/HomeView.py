from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class HomeView(QMainWindow):
    def __init__(self):
        super(HomeView, self).__init__()
        uic.loadUi(r"C:\Users\aless\Desktop\Workspace_VSC\Progetto-Hotel\ui\main_window.ui", self)
    def camere_click(self):

