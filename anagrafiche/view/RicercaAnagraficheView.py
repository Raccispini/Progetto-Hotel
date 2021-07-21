'''
__author__: Federico Pretini
'''
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from anagrafiche.view.Ui_RicercaAnagraficheView import Ui_RicercaAnagraficheView


class RicercaAnagraficheView(QMainWindow, Ui_RicercaAnagraficheView):
    def __init__(self,controller, callback, table, buttons, tipo_ricerca, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.controller = controller
        self.callback = callback
        self.table = table
        self.buttons = buttons
        if tipo_ricerca == "Cliente":
            self.ricerca_cliente()
        elif tipo_ricerca == "Dipendente":
            self.ricerca_dipendente()
        elif tipo_ricerca == "Fornitore":
            self.ricerca_fornitore()

    def ricerca_cliente(self):
        self.callback(self.table, [])
        for button in self.buttons:
            button.setEnabled(False)
        # Metodo che gestisce la visualizzazione dei clienti filtrati quando viene premuto il pulsante ricerca
        cB_element = ["", "ID", "NOME", "COGNOME", "SESSO", "DATA_NASCITA", "LUOGO_NASCITA", "RESIDENZA", "PROVINCIA",
                      "VIA", "CAP",
                      "CF", "NAZIONE", "TELEFONO", "CELLULARE", "EMAIL", "DOCUMENTO", "NUMERO_DOCUMENTO",
                      "ENTE_RILASCIO",
                      "DATA_RILASCIO", "DATA_SCADENZA", "MODALITA_PAGAMENTO", "INFO_CHECKIN"]
        self.set_cB(cB_element)
        self.pB_ricerca.clicked.connect(lambda: self.on_ricercaclicked(self.controller.ricerca_cliente([self.cB_criterio_ricerca.currentText(), self.lineE_parola.text()])))
        self.pB_annulla.clicked.connect(lambda: self.on_annullaclicked(self.controller.get_listaclienti()))

    def ricerca_dipendente(self):
        self.callback(self.table, [])
        for button in self.buttons:
            button.setEnabled(False)

        cB_element = ["", "ID", "USERNAME", "PASSWORD", "NOME", "COGNOME", "EMAIL", "CELLULARE", "DATA_NASCITA", "AMBITO", "PERMESSI"]
        self.set_cB(cB_element)
        self.pB_ricerca.clicked.connect(lambda: self.on_ricercaclicked(self.controller.ricerca_dipendente([self.cB_criterio_ricerca.currentText(), self.lineE_parola.text()])))
        self.pB_annulla.clicked.connect(lambda: self.on_annullaclicked(self.controller.get_listadipendenti()))


    def ricerca_fornitore(self):
        self.callback(self.table, [])
        for button in self.buttons:
            button.setEnabled(False)

        cB_element = ["", "ID","NOME_FORNITORE", "FORNITURA1", "FORNITURA2", "IVA", "RIFERIMENTO", "CELLULARE_RIFERIMENTO",
                      "INDIRIZZO", "TELEFONO", "EMAIL", "MODALITA_PAGAMENTO", "FAX"]

        self.set_cB(cB_element)
        self.pB_ricerca.clicked.connect(lambda: self.on_ricercaclicked(self.controller.ricerca_fornitore([self.cB_criterio_ricerca.currentText(), self.lineE_parola.text()])))
        self.pB_annulla.clicked.connect(lambda: self.on_annullaclicked(self.controller.get_listafornitori()))




    def on_ricercaclicked(self, lista_trovati):
        if len(lista_trovati) == 0:
            QMessageBox.information(self, 'Informazione', 'I criteri di ricerca non hanno prodotto nessun risultato.\nPer favore cambia i criteri e ritenta',
                                    QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.callback(self.table, lista_trovati)
            QMessageBox.information(self, 'Informazione', 'I risultati della ricerca vengono mostrati sulla tabella.\nPer farla tornare allo stato iniziale premere annulla',
                                    QMessageBox.Ok, QMessageBox.Ok)

        self.lineE_parola.clear()
        self.cB_criterio_ricerca.setCurrentIndex(0)

    def on_annullaclicked(self, lista):
        self.callback(self.table, lista)
        self.close()
        for button in self.buttons:
            button.setEnabled(True)