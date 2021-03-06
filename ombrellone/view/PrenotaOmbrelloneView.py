'''
__author__: Federico Pretini
'''
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from ombrellone.view.Ui_PrenotaOmbrellone import Ui_PrenotaOmbrellone
from anagrafiche.controller.AnagraficheController import AnagraficheController


class PrenotaOmbrelloneView(QMainWindow, Ui_PrenotaOmbrellone):
    def __init__(self,log,controller,callback, nome_ombrellone, data, tipo, orario =  "", parent = None):
        super(PrenotaOmbrelloneView, self).__init__(parent)
        self.setupUi(self)
        self.log = log
        self.controller = controller
        self.callback = callback
        self.nome_ombrellone = nome_ombrellone
        self.data = data
        self.tipo = tipo
        self.orario = orario
        self.totale = 0
        self.update_view()
        self.connect_action()

    def update_view(self):
        self.controller_cliente = AnagraficheController()
        info_cliente = [""]
        for cliente in self.controller_cliente.get_listaclienti():
            info_cliente.append(f"{cliente.get_nome()} {cliente.get_cognome()} - {cliente.get_tipo_documento()}: {cliente.get_numero_documento()}")
        self.cB_nominativo.addItems(info_cliente)

    def connect_action(self):
        self.pB_prenota_ombrellone.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_elimina_ombrellone.clicked.connect(lambda: self.elimina_prenotazione())
        self.cB_nominativo.currentIndexChanged.connect(lambda: self.check_prenota())
        self.cB_pagamento.currentIndexChanged.connect(lambda: self.check_prenota())

    def check_prenota(self):
        if self.cB_nominativo.currentText() != "" and self.cB_pagamento.currentText() != "":
            self.pB_prenota_ombrellone.setEnabled(True)
        else:
            self.pB_prenota_ombrellone.setEnabled(False)

    def prenota_ombrellone(self):
        nominativo = self.cB_nominativo.currentText().split("-")
        listino_prezzi = self.controller.get_listino_prezzi(self.nome_ombrellone)
        if self.orario == "Mattina":
            orario_inizio = "08:00"
            orario_fine = "14:00"
            self.totale = listino_prezzi[2]
        elif self.orario == "Pomeriggio":
            orario_inizio = "14:00"
            orario_fine = "20:00"
            self.totale = listino_prezzi[2]
        elif self.tipo == "Giornata Intera":
            orario_inizio = "08:00"
            orario_fine = "20:00"
            self.totale = listino_prezzi[1]
        pagamento = self.cB_pagamento.currentText()
        n_sedie = self.sB_sedie.value()
        n_sdraie = self.sB_sdraie.value()
        if n_sedie > 1:
            self.totale += float(listino_prezzi[3]) * n_sedie
        if n_sdraie > 1:
            self.totale += float(listino_prezzi[4]) * n_sdraie
        info = [self.nome_ombrellone, nominativo[0], self.data, self.tipo, orario_inizio, orario_fine, n_sedie, n_sdraie, pagamento, self.totale]
        self.controller.prenota_ombrellone(info)
        self.log .print_log_add("aggiunta prenotazione ombrelloni")
        self.callback()
        self.close()

    def elimina_prenotazione(self):
        button = QMessageBox.question(self, "Attenzione", "Sei sicuro di voler eliminare la prenotazione?\nIn tal caso dovrai ripetere la compilazione", QMessageBox.Yes, QMessageBox.No)
        if button == QMessageBox.Yes:
            self.cB_pagamento.setCurrentIndex(0)
            self.cB_nominativo.setCurrentIndex(0)
            self.sB_sedie.setValue(0)
            self.sB_sdraie.setValue(0)
            self.log.print_log_delete("eliminata prenotazione ombrelloni")
