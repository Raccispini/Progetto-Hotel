from PyQt5.QtWidgets import QMainWindow
from ristorante.view.Ui_PrenotazioneRistoranteView import Ui_PrenotaRistoranteView


class PrenotaRistoranteView(QMainWindow, Ui_PrenotaRistoranteView):
    def __init__(self, controller, nome_tavolo, data, ora, parent = None):
        super(PrenotaRistoranteView, self).__init__(parent)
        self.setupUi(self)
        self.nome_tavolo = nome_tavolo
        self.data = data
        self.ora = ora
        self.controller = controller
        self.connect_all()

    def connect_all(self):
        self.pB_prenota.clicked.connect(lambda: self.prenota_tavolo())

    def prenota_tavolo(self):
        nominativo = self.cB_nominativo.currentText()
        num_persone = self.sb_persone.value()
        info_prenotazione = [self.nome_tavolo, nominativo, num_persone, self.data, self.ora[0], self.ora[1]]
        self.controller.prenota_tavolo(info_prenotazione)


