from PyQt5.QtWidgets import QMainWindow
from ristorante.view.Ui_RistoranteView import Ui_RistoranteView


class RistoranteView(QMainWindow, Ui_RistoranteView):
    def __init__(self, parent = None):
        super(RistoranteView, self).__init__(parent)
        self.setupUi(self)




