from PyQt5.QtWidgets import QMainWindow

from ristorante.view.Ui_RistoranteView_1 import Ui_RistoranteView_1


class RistoranteView(QMainWindow, Ui_RistoranteView_1):
    def __init__(self, parent = None):
        super(RistoranteView, self).__init__(parent)
        self.setupUi(self)