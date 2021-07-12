from PyQt5.QtWidgets import QMainWindow
from ristorante.view.Ui_PrenotazioneRistoranteView import Ui_PrenotaRistoranteView


class RistoranteView(QMainWindow, Ui_PrenotaRistoranteView):
    def __init__(self, parent = None):
        super(RistoranteView, self).__init__(parent)
        self.setupUi(self)
