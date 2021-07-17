'''
__author__: Federico Pretini
'''
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from ristorante.view.Ui_OrdinazioniRistoranteView import Ui_OrdinazioniRistoranteView
from GeneratoreScontriniRistorante import GeneratoreScontriniRistorante
from PyQt5 import QtGui, QtCore

class OrdinazioniRistoranteView(QMainWindow, Ui_OrdinazioniRistoranteView):
    def __init__(self,controller, item, parent = None):
        super(OrdinazioniRistoranteView, self).__init__(parent)
        self.setupUi(self)
        self.item_selected = item
        self.controller = controller
        self.lista_ordini = []
        self.sconto=0
        self.coperto=1.5
        self.update_all()
        self.connect_all()
        self.update_totale()

    def update_all(self):
        info_tavolo = []
        for info in self.item_selected:
            info_tavolo.append(info.text())

        self.lineE_tavolo.setText(info_tavolo[1].split("_")[1])
        self.lineE_nominativo.setText(info_tavolo[2])
        self.lineE_persone.setText(info_tavolo[3])
        for antipasti in self.controller.get_menu("Antipasti"):
            self.cB_antipasti.addItem(antipasti[1])
        for primi in self.controller.get_menu("Primi"):
            self.cB_primi.addItem(primi[1])
        for secondi in self.controller.get_menu("Secondi"):
            self.cB_secondi.addItem(secondi[1])
        for contorni in self.controller.get_menu("Contorni"):
            self.cB_contorni.addItem(contorni[1])
        for bevande in self.controller.get_menu("Bevande"):
            self.cB_bevande.addItem(bevande[1])
        for frutta in self.controller.get_menu("Frutta"):
            self.cB_frutta.addItem(frutta[1])
        for dolci in self.controller.get_menu("Dolci"):
            self.cB_dolci.addItem(dolci[1])

    def connect_all(self):
        for button in self.pB_Aggiungi:
            button.clicked.connect(lambda: self.aggiungi_clicked())
        self.lineE_sconto.textChanged.connect(lambda: self.update_totale())
        self.lineE_coperto.textChanged.connect(lambda: self.update_totale())
        self.tW_scontrino_tavolo.itemSelectionChanged.connect(lambda: self.table_clicked())
        self.pB_cancella.clicked.connect(lambda: self.delete_ordinazione())
        self.pB_annulla.clicked.connect(lambda: self.annulla_clicked())
        self.pB_conferma.clicked.connect(lambda: self.stampa_scontrino())

    def table_clicked(self):
        if len(self.tW_scontrino_tavolo.selectionModel().selectedRows()) > 0:
            self.pB_cancella.setEnabled(True)
        else:
            self.pB_cancella.setEnabled(False)

    def aggiungi_clicked(self):
        nome_bottone = self.sender().objectName()
        quantita = 1
        if nome_bottone == "pB_antipasti":
            nome_piatto = self.cB_antipasti.currentText()
        elif nome_bottone == "pB_primi":
            nome_piatto = self.cB_primi.currentText()
        elif nome_bottone == "pB_secondi":
            nome_piatto = self.cB_secondi.currentText()
        elif nome_bottone == "pB_contorni":
            nome_piatto = self.cB_contorni.currentText()
        elif nome_bottone == "pB_bevande":
            nome_piatto = self.cB_bevande.currentText()
        elif nome_bottone == "pB_frutta":
            nome_piatto = self.cB_frutta.currentText()
        elif nome_bottone == "pB_dolci":
            nome_piatto = self.cB_dolci.currentText()

        if nome_piatto == "":
            QMessageBox.warning(self,"Attenzione","Non hai inserito il nome del piatto.\nPer favore ritenta inserendo correttamente i dati", QMessageBox.Ok, QMessageBox.Ok)
            return

        prezzo_singolo = self.controller.get_prezzo(nome_piatto)
        TOT = prezzo_singolo
        info_ordine = [nome_piatto, quantita, prezzo_singolo, TOT]

        if self.lista_ordini == []:
            self.lista_ordini.append(info_ordine)
            self.pB_conferma.setEnabled(True)
            self.update_totale()
            self.update_table()
            return
        else:
            for index in range (0,len(self.lista_ordini)):
                if self.lista_ordini[index][0] == info_ordine[0]:
                    self.lista_ordini[index][1] += info_ordine[1]
                    self.lista_ordini[index][3] += info_ordine[3]
                    self.pB_conferma.setEnabled(True)
                    self.update_totale()
                    self.update_table()
                    return

        self.lista_ordini.append(info_ordine)  # Se la lista non era inizialmente vuota e la consumazione non
                                               # era già presente nella lista allora l'aggiungo semplicemente
        self.pB_conferma.setEnabled(True)
        self.update_totale()
        self.update_table()

    def update_totale(self):
        try:
            self.sconto = int(self.lineE_sconto.text())
            self.coperto = float(self.lineE_coperto.text())
        except:
            QMessageBox.information(self, "Informazione", "Inserisci solamente valori numerici non caratteri o lettere, non lasciare vuoti i campi sconto e coperto", QMessageBox.Ok, QMessageBox.Ok)
            return

        self.totale = 0
        for ordine in self.lista_ordini:
            self.totale += ordine[3]
        if self.sconto > 100 or self.sconto < 0:
             QMessageBox.information(self, "Informazione", "\tSconto non valido,\nInserire un numero compreso tra 0 e 100", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.totale += self.coperto * int(self.lineE_persone.text())
            self.totale -= (self.totale*(self.sconto/100))

        self.lineE_totale.setText(str(self.totale) + ' €')
        totale_diviso=float(self.totale/int(self.item_selected[3].text()))
        totale_diviso_arrotondato=f"{totale_diviso:.2f}"
        self.lineE_totale_per_persona.setText(totale_diviso_arrotondato + " €")

    def update_table(self):
        def get_item(info):
            item = QTableWidgetItem(str(info))
            font = QtGui.QFont()
            font.setBold(False)
            font.setFamily("Arial")
            font.setPointSize(15)
            item.setFont(font)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            return item

        self.tW_scontrino_tavolo.setRowCount(0)
        i = 0
        for ordine in self.lista_ordini:
            self.tW_scontrino_tavolo.insertRow(i)
            j = 0
            for info in ordine:
                if j == 2 or j == 3:  # Se l'indice è su prezzo oppure su totale aggiungo alla stringa il simbolo €
                    info = str(info) + " €"
                self.tW_scontrino_tavolo.setItem(i, j, get_item(info))
                j += 1
            i += 1

    def delete_ordinazione(self):
        indexes = self.tW_scontrino_tavolo.selectionModel().selectedRows()
        i = 0
        for index in sorted(indexes):
            self.lista_ordini.pop(index.row() - i)  # -i perchè ogni volta che elimino una consumazione l'indice
                                                    # dell'altra consumazione da eliminare diminuisce di uno
            i += 1
        if self.lista_ordini == []:
            self.pB_conferma.setEnabled(False)
        self.update_totale()
        self.update_table()

    def annulla_clicked(self):
        scelta = QMessageBox.warning(self, "Attenzione", "Sei sicuro di voler annullare l'ordine?\nIn tal caso dovrai ricominciare la compilazione", QMessageBox.Yes, QMessageBox.No)
        if scelta == QMessageBox.Yes:
            self.cB_antipasti.setCurrentIndex(0)
            self.cB_primi.setCurrentIndex(0)
            self.cB_secondi.setCurrentIndex(0)
            self.cB_contorni.setCurrentIndex(0)
            self.cB_bevande.setCurrentIndex(0)
            self.cB_dolci.setCurrentIndex(0)
            self.cB_frutta.setCurrentIndex(0)
            self.cB_pagamento.setCurrentIndex(0)
            self.lista_ordini = []
            self.update_table()
            self.update_totale()


    def stampa_scontrino(self):
        scontrino = GeneratoreScontriniRistorante()
        if self.cB_pagamento.currentText() != "" and self.cB_pagamento.currentText() != "Addebito su conto camera":
            scontrino.stampa(self.lista_ordini, self.totale, self.cB_pagamento.currentText())
        else:
            QMessageBox.information(self, "Informazione","Seleziona un metodo di pagamento in maniera idonea prima di premere salva")








