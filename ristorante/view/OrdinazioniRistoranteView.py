from PyQt5.QtWidgets import QMainWindow
from ristorante.view.Ui_OrdinazioniRistoranteView import Ui_OrdinazioniRistoranteView


class OrdinazioniRistoranteView(QMainWindow, Ui_OrdinazioniRistoranteView):
    def __init__(self, parent = None):
        super(OrdinazioniRistoranteView, self).__init__(parent)
        self.setupUi(self)
