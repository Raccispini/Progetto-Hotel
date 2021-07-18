'''
__author__: Federico Pretini
'''
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from anagrafiche.controller.AnagraficheController import AnagraficheController
from ristorante.view.Ui_PrenotazioneRistoranteView import Ui_PrenotaRistoranteView


class PrenotaRistoranteView(QMainWindow, Ui_PrenotaRistoranteView):
    def __init__(self, controller,callback_1,callback_2, nome_tavolo, data, ora, parent = None):
        super(PrenotaRistoranteView, self).__init__(parent)
        self.setupUi(self)
        self.nome_tavolo = nome_tavolo
        self.data = data
        self.ora = ora
        self.controller = controller
        self.callback_1 = callback_1
        self.callback_2 = callback_2
        self.connect_action()
        self.update_view()

    def connect_action(self):
        self.pB_prenota.clicked.connect(lambda: self.prenota_tavolo())

    def update_view(self):
        self.controller_cliente = AnagraficheController()
        info_cliente = [""]
        info_prenotazione = [""]
        for cliente in self.controller_cliente.get_listaclienti():
            info_cliente.append(f"{cliente.get_nome()} {cliente.get_cognome()} - {cliente.get_tipo_documento()}: {cliente.get_numero_documento()}")
        self.cB_camera.addItems(info_prenotazione)
        self.cB_nominativo.addItems(info_cliente)


    def prenota_tavolo(self):
        nominativo = self.cB_nominativo.currentText()
        num_persone = self.sb_persone.value()
        info_prenotazione = [self.nome_tavolo, nominativo, num_persone, self.data.toString("dd/MM/yyyy"), self.ora[0], self.ora[1]]
        if self.nome_tavolo=="" or nominativo=="" or num_persone<=0:
            QMessageBox.critical(self, "Errore", "Inserisci prima correttamente tutti i dati necessari")
        else:
            self.controller.prenota_tavolo(info_prenotazione)
            self.callback_1()
            self.callback_2(self.controller.get_lista_prenotazioni())
            self.close()


