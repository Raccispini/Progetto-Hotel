'''
__author__: Federico Pretini
'''
from PyQt5 import QtGui
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox,  QTableWidgetItem

from anagrafiche.view.RicercaAnagraficheView import RicercaAnagraficheView
from anagrafiche.view.Ui_AnagraficheView import Ui_AnagraficheView
from GeneratorePDF_Tabelle import GeneratorePDF_Tabelle
from anagrafiche.controller.AnagraficheController import AnagraficheController
from cliente.controller.ClienteController import ClienteController
from dipendente.controller.DipendenteController import DipendenteController
from fornitore.controller.FornitoreController import FornitoreController


class AnagraficheView(QMainWindow, Ui_AnagraficheView):
    def __init__(self, parent=None):
        super(AnagraficheView, self).__init__(parent)
        self.setupUi(self)
        self.controller = AnagraficheController()
        self.controller_cliente = ClienteController()
        self.aggiornaTabelle(self.tableWidget_Clienti, self.controller.get_listaclienti())
        self.controller_fornitore = FornitoreController()
        self.aggiornaTabelle(self.tableWidget_Fornitore, self.controller.get_listafornitori())
        self.controller_dipendente = DipendenteController()
        self.aggiornaTabelle(self.tableWidget_Dipendente, self.controller.get_listadipendenti())
        self.annulla_cliente()
        self.annulla_dipendente()
        self.annulla_fornitore()
        self.connectAction()
        self.checkpB_to_enable()


#========================================================================================================================
##############################METODO CHE COLLEGA AL CLICK DI OGNI PULSANTE UN'AZIONE###################################

    def connectAction(self):

        ########################################PULSANTI CLIENTE#######################################################
        self.pB_aggiungi_Cliente.clicked.connect(lambda: self.add_cliente())
        self.pB_modifica_Cliente.clicked.connect(lambda: self.modifica_cliente())
        self.pB_elimina_Cliente.clicked.connect(lambda: self.elimina_cliente())
        self.pB_ricerca_Cliente.clicked.connect(lambda: self.ricerca_cliente())
        self.pB_salva_Cliente.clicked.connect(lambda: self.salva_cliente())
        self.pB_annulla_Cliente.clicked.connect(lambda: self.on_annulla_cliente_clicked())
        self.pB_creaPDF_Cliente.clicked.connect(lambda: self.stampaPDF(self.controller.get_listaclienti(),
                                                                       "HTML/Tabelle/tabella_clienti.html"))
        self.tableWidget_Clienti.itemSelectionChanged.connect(lambda: self.enable_pB(self.pB_modifica_Cliente, self.pB_elimina_Cliente, self.tableWidget_Clienti))

        ########################################PULSANTI DIPENDENTE######################################################
        self.pB_aggiungi_Dipendente.clicked.connect(lambda: self.add_dipendente())
        self.pB_modifica_Dipendente.clicked.connect(lambda: self.modifica_dipendente())
        self.pB_elimina_Dipendente.clicked.connect(lambda: self.elimina_dipendente())
        self.pB_ricerca_Dipendente.clicked.connect(lambda: self.ricerca_dipendente())
        self.pB_salva_Dipendente.clicked.connect(lambda: self.salva_dipendente())
        self.pB_annulla_Dipendente.clicked.connect(lambda: self.on_annulla_dipendente_clicked())
        self.pB_creaPDF_Dipendente.clicked.connect(lambda: self.stampaPDF(self.controller.get_listadipendenti(),
                                                                          "HTML/Tabelle/tabella_dipendenti.html"))
        self.tableWidget_Dipendente.itemSelectionChanged.connect(lambda: self.enable_pB(self.pB_modifica_Dipendente, self.pB_elimina_Dipendente, self.tableWidget_Dipendente))
        #######################################PULSANTI FORNITORE######################################################
        self.pB_aggiungi_Fornitore.clicked.connect(lambda: self.add_fornitore())
        self.pB_modifica_Fornitore.clicked.connect(lambda: self.modifica_fornitore())
        self.pB_elimina_Fornitore.clicked.connect(lambda: self.elimina_fornitore())
        self.pB_ricerca_Fornitore.clicked.connect(lambda: self.ricerca_fornitore())
        self.pB_salva_Fornitore.clicked.connect(lambda: self.salva_fornitore())
        self.pB_annulla_Fornitore.clicked.connect(lambda: self.on_annulla_fornitore_clicked())
        self.pB_creaPDF_Fornitore.clicked.connect(lambda: self.stampaPDF(self.controller.get_listafornitori(),
                                                                         "HTML/Tabelle/tabella_fornitori.html"))
        self.tableWidget_Fornitore.itemSelectionChanged.connect(lambda: self.enable_pB(self.pB_modifica_Fornitore, self.pB_elimina_Fornitore, self.tableWidget_Fornitore))


#=======================================================================================================================
#########################################METODI PULSANTI################################################################


###########################################METODI PER CLIENTE###########################################################
    def add_cliente(self):
        self.controller_cliente.set_info(self.get_info_cliente_from_view())
        if self.controller_cliente.iscompleto():
            self.controller.add_cliente(self.controller_cliente.get_cliente())
            self.aggiornaTabelle(self.tableWidget_Clienti, self.controller.get_listaclienti())
            QMessageBox.information(self, 'Informazione', 'Il cliente è stato registrato con successo', QMessageBox.Ok, QMessageBox.Ok)
            self.checkpB_to_enable()
            self.annulla_cliente()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)



    def modifica_cliente(self):
        self.pB_salva_Cliente.setEnabled(True)
        self.pB_modifica_Cliente.setEnabled(False)
        self.pB_aggiungi_Cliente.setEnabled(False)
        info = self.tableWidget_Clienti.selectedItems()
        self.lineE_nome_Cliente.setText(info[1].text())
        self.lineE_cognome_Cliente.setText(info[2].text())
        self.cB_sesso_Cliente.setCurrentText(info[3].text())
        self.dE_nascita_Cliente.setDate(QDate.fromString(info[4].text(), "dd/MM/yyyy"))
        self.lineE_nascita_Cliente.setText(info[5].text())
        self.lineE_residenza_Cliente.setText(info[6].text())
        self.lineE_provincia_Cliente.setText(info[7].text())
        self.lineE_via_Cliente.setText(info[8].text())
        self.lineE_cap_Cliente.setText(info[9].text())
        self.lineE_cf_Cliente.setText(info[10].text())
        self.lineE_nazione_Cliente.setText(info[11].text())
        self.lineE_telefono_Cliente.setText(info[12].text())
        self.lineE_cellulare_Cliente.setText(info[13].text())
        self.lineE_email_Cliente.setText(info[14].text())
        self.cB_documento_Cliente.setCurrentText(info[15].text())
        self.lineE_numeroDoc_Cliente.setText(info[16].text())
        self.lineE_enteRilascio_Cliente.setText(info[17].text())
        self.dE_dataRilascio_Cliente.setDate(QDate.fromString(info[18].text(), "dd/MM/yyyy"))
        self.dE_dataScadenza_Cliente.setDate(QDate.fromString(info[19].text(), "dd/MM/yyyy"))
        self.cB_modalitaPag_Cliente.setCurrentText(info[20].text())
        self.lineE_infoCheckin_Cliente.setText(info[21].text())


    def elimina_cliente(self):
        self.pB_aggiungi_Cliente.setEnabled(True)
        self.pB_salva_Cliente.setEnabled(False)
        info = self.tableWidget_Clienti.selectedItems()
        lista_id = []
        # Salvo l'ID dei clienti da eliminare all'interno di una variabile
        for i in range(0, len(info)):
            if i % self.tableWidget_Clienti.columnCount() == 0:
                lista_id.append(info[i].text())
        if len(lista_id) == 1:
            button = QMessageBox.warning(self, "Attenzione", "Sei sicuro di voler eliminare definitivamente\n il cliente dalla lista?", QMessageBox.Yes, QMessageBox.No)
        else:
            button = QMessageBox.warning(self, "Attenzione","Sei sicuro di voler eliminare definitivamente\n i clienti dalla lista?", QMessageBox.Yes, QMessageBox.No)
        if button == QMessageBox.Yes:
            self.controller.elimina_clienti(lista_id)
            self.aggiornaTabelle(self.tableWidget_Clienti, self.controller.get_listaclienti())
            if len(lista_id) == 1:
                QMessageBox.information(self, 'Informazione', 'Il cliente è stato eliminato con successo', QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.information(self, 'Informazione', 'I clienti sono stati eliminati con successo', QMessageBox.Ok, QMessageBox.Ok)
            self.pB_elimina_Cliente.setEnabled(False)
            self.checkpB_to_enable()


    def salva_cliente(self):
        self.pB_aggiungi_Cliente.setEnabled(True)
        self.controller_cliente.set_info(self.get_info_cliente_from_view())
        if self.controller_cliente.get_cliente().iscompleto():
            self.controller.salva_cliente(self.controller_cliente.get_cliente())
            self.aggiornaTabelle(self.tableWidget_Clienti, self.controller.get_listaclienti())
            self.pB_salva_Cliente.setEnabled(False)
            QMessageBox.information(self, 'Informazione', 'Il clienti è stato modificato con successo', QMessageBox.Ok, QMessageBox.Ok)
            self.annulla_cliente()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)


    def on_annulla_cliente_clicked(self):
        button = QMessageBox.warning(self, "Attenzione", "Sei sicuro di voler annullare?\nIn tal caso dovrai ricominciare la compilazione",
                                     QMessageBox.Yes, QMessageBox.No)
        if button == QMessageBox.Yes:
            self.annulla_cliente()
            QMessageBox.information(self, "Informazione", "La compilazione è stata annullata correttamente")

    def ricerca_cliente(self):
        buttons_ricerca = [self.pB_ricerca_Cliente, self.pB_ricerca_Dipendente, self.pB_ricerca_Fornitore]
        self.ricerca_window = RicercaAnagraficheView(self.controller, self.aggiornaTabelle, self.tableWidget_Clienti, buttons_ricerca, "Cliente", self)
        self.ricerca_window.show()

    def annulla_cliente(self):
            self.pB_salva_Cliente.setEnabled(False)
            self.pB_aggiungi_Cliente.setEnabled(True)
            self.lineE_nome_Cliente.clear()
            self.lineE_cognome_Cliente.clear()
            self.cB_sesso_Cliente.setCurrentIndex(0)
            self.dE_nascita_Cliente.setDate(QDate.fromString("01/01/1800", "dd/MM/yyyy"))
            self.lineE_nascita_Cliente.clear()
            self.lineE_residenza_Cliente.clear()
            self.lineE_provincia_Cliente.clear()
            self.lineE_via_Cliente.clear()
            self.lineE_cap_Cliente.clear()
            self.lineE_cf_Cliente.clear()
            self.lineE_nazione_Cliente.clear()
            self.lineE_telefono_Cliente.clear()
            self.lineE_cellulare_Cliente.clear()
            self.lineE_email_Cliente.clear()
            self.cB_documento_Cliente.setCurrentIndex(0)
            self.lineE_numeroDoc_Cliente.clear()
            self.lineE_enteRilascio_Cliente.clear()
            self.dE_dataRilascio_Cliente.setDate(QDate.fromString("01/01/1800", "dd/MM/yyyy"))
            self.dE_dataScadenza_Cliente.setDate(QDate.fromString("01/01/1800", "dd/MM/yyyy"))
            self.cB_modalitaPag_Cliente.setCurrentIndex(0)
            self.lineE_infoCheckin_Cliente.clear()



    def get_info_cliente_from_view(self):
        item = self.tableWidget_Clienti.selectedItems()
        if len(item) == 0:
            id = 0
        else:
            id = item[0].text()
        info = (id, self.lineE_nome_Cliente.text(), self.lineE_cognome_Cliente.text(), self.cB_sesso_Cliente.currentText(),
                self.dE_nascita_Cliente.date().toString("dd/MM/yyyy"), self.lineE_nascita_Cliente.text(),
                self.lineE_residenza_Cliente.text(), self.lineE_provincia_Cliente.text(), self.lineE_via_Cliente.text(),
                self.lineE_cap_Cliente.text(), self.lineE_cf_Cliente.text(), self.lineE_nazione_Cliente.text(),
                self.lineE_telefono_Cliente.text(), self.lineE_cellulare_Cliente.text(), self.lineE_email_Cliente.text(),
                self.cB_documento_Cliente.currentText(), self.lineE_numeroDoc_Cliente.text(), self.lineE_enteRilascio_Cliente.text(),
                self.dE_dataRilascio_Cliente.date().toString("dd/MM/yyyy"), self.dE_dataScadenza_Cliente.date().toString("dd/MM/yyyy"),
                self.cB_modalitaPag_Cliente.currentText(), self.lineE_infoCheckin_Cliente.text())
        return info


#############################################METODI PER DIPENDETE#######################################################
    def add_dipendente(self):
        self.controller_dipendente.set_info(self.get_info_dipendente_from_view())
        if self.controller_dipendente.iscompleto():
            self.controller.add_dipendente(self.controller_dipendente.get_dipendente())
            self.aggiornaTabelle(self.tableWidget_Dipendente, self.controller.get_listadipendenti())
            QMessageBox.information(self, 'Informazione', 'Il dipendente è stato registrato con successo', QMessageBox.Ok, QMessageBox.Ok)
            self.checkpB_to_enable()
            self.annulla_dipendente()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)

    def modifica_dipendente(self):
        self.pB_salva_Dipendente.setEnabled(True)
        self.pB_modifica_Dipendente.setEnabled(False)
        self.pB_aggiungi_Dipendente.setEnabled(False)
        info = self.tableWidget_Dipendente.selectedItems()
        self.lineE_nome_Dipendente.setText(info[1].text())
        self.lineE_cognome_Dipendente.setText(info[2].text())
        self.lineE_username_Dipendente.setText(info[3].text())
        self.lineE_password_Dipendente.setText(info[4].text())
        self.lineE_email_Dipendente.setText(info[5].text())
        self.lineE_cellulare_Dipendente.setText(info[6].text())
        self.dE_nascita_Dipendente.setDate(QDate.fromString(info[7].text(), "dd/MM/yyyy"))
        self.lineE_ambito_Dipendente.setText(info[8].text())
        self.cB_permessi_Dipendente.setCurrentText(info[9].text())

    def elimina_dipendente(self):
        self.pB_aggiungi_Dipendente.setEnabled(True)
        self.pB_salva_Dipendente.setEnabled(False)
        info = self.tableWidget_Dipendente.selectedItems()
        lista_id = []
        # Salvo l'ID dei dipendenti da eliminare all'interno di una variabile
        for i in range(0, len(info)):
            if i % self.tableWidget_Dipendente.columnCount() == 0:
                lista_id.append(info[i].text())
        if len(lista_id) == 1:
            button = QMessageBox.warning(self, "Attenzione", "Sei sicuro di voler eliminare definitivamente\n il dipendente dalla lista?", QMessageBox.Yes, QMessageBox.No)
        else:
            button = QMessageBox.warning(self, "Attenzione","Sei sicuro di voler eliminare definitivamente\n i dipendenti dalla lista?", QMessageBox.Yes, QMessageBox.No)
        if button == QMessageBox.Yes:
            self.controller.elimina_dipendenti(lista_id)
            self.aggiornaTabelle(self.tableWidget_Dipendente, self.controller.get_listadipendenti())
            if len(lista_id) == 1:
                QMessageBox.information(self, 'Informazione', 'Il dipendente è stato eliminato con successo', QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.information(self, 'Informazione', 'I dipendenti sono stati eliminati con successo', QMessageBox.Ok, QMessageBox.Ok)
            self.pB_elimina_Dipendente.setEnabled(False)
            self.checkpB_to_enable()

    def ricerca_dipendente(self):
        buttons_ricerca = [self.pB_ricerca_Cliente, self.pB_ricerca_Dipendente, self.pB_ricerca_Fornitore]
        self.ricerca_window = RicercaAnagraficheView(self.controller, self.aggiornaTabelle, self.tableWidget_Dipendente, buttons_ricerca, "Dipendente", self)
        self.ricerca_window.show()


    def salva_dipendente(self):
        self.pB_aggiungi_Dipendente.setEnabled(True)
        self.controller_dipendente.set_info(self.get_info_dipendente_from_view())
        if self.controller_dipendente.get_dipendente().iscompleto():
            self.controller.salva_dipendente(self.controller_dipendente.get_dipendente())
            self.aggiornaTabelle(self.tableWidget_Dipendente, self.controller.get_listadipendenti())
            self.pB_salva_Dipendente.setEnabled(False)
            QMessageBox.information(self, 'Informazione', 'Il dipendente è stato modificato con successo', QMessageBox.Ok, QMessageBox.Ok)
            self.annulla_dipendente()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)

    def on_annulla_dipendente_clicked(self):
        button = QMessageBox.warning(self, "Attenzione", "Sei sicuro di voler annullare?\nIn tal caso dovrai ricominciare la compilazione",
                                     QMessageBox.Yes, QMessageBox.No)
        if button == QMessageBox.Yes:
            self.annulla_dipendente()
            QMessageBox.information(self, "Informazione", "La compilazione è stata annullata correttamente")



    def annulla_dipendente(self):
        self.pB_salva_Dipendente.setEnabled(False)
        self.pB_aggiungi_Dipendente.setEnabled(True)
        self.lineE_username_Dipendente.clear()
        self.lineE_password_Dipendente.clear()
        self.lineE_ambito_Dipendente.clear()
        self.cB_permessi_Dipendente.setCurrentIndex(0)
        self.lineE_nome_Dipendente.clear()
        self.lineE_cognome_Dipendente.clear()
        self.lineE_email_Dipendente.clear()
        self.lineE_cellulare_Dipendente.clear()
        self.dE_nascita_Dipendente.setDate(QDate.fromString("01/01/1800", "dd/MM/yyyy"))

    def get_info_dipendente_from_view(self):
        item = self.tableWidget_Dipendente.selectedItems()
        if len(item) == 0:
            id = 0
        else:
            id = item[0].text()
        info = (id, self.lineE_nome_Dipendente.text(), self.lineE_cognome_Dipendente.text(), self.lineE_username_Dipendente.text(),
                self.lineE_password_Dipendente.text(), self.lineE_email_Dipendente.text(), self.lineE_cellulare_Dipendente.text(),
                self.dE_nascita_Dipendente.date().toString("dd/MM/yyyy"), self.lineE_ambito_Dipendente.text(), self.cB_permessi_Dipendente.currentText())
        return info

    #########################################METODI PER FORNITORE#######################################################
    def add_fornitore(self):
        self.controller_fornitore.set_info(self.get_info_fornitore_from_view())
        if self.controller_fornitore.iscompleto():
            self.controller.add_fornitore(self.controller_fornitore.get_fornitore())
            self.aggiornaTabelle(self.tableWidget_Fornitore, self.controller.get_listafornitori())
            QMessageBox.information(self, 'Informazione', 'Il fornitore è stato registrato con successo', QMessageBox.Ok, QMessageBox.Ok)
            self.checkpB_to_enable()
            self.annulla_fornitore()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)

    def modifica_fornitore(self):
        self.pB_salva_Fornitore.setEnabled(True)
        self.pB_modifica_Fornitore.setEnabled(False)
        self.pB_aggiungi_Fornitore.setEnabled(False)
        info = self.tableWidget_Fornitore.selectedItems()
        self.lineE_nome_Fornitore.setText(info[1].text())
        self.lineE_fornitura1_Fornitore.setText(info[2].text())
        self.lineE_fornitura2_Fornitore.setText(info[3].text())
        self.lineE_IVA_Fornitore.setText(info[4].text())
        self.lineE_riferimento_Fornitore.setText(info[5].text())
        self.lineE_telefonoRif_Fornitore.setText(info[6].text())
        self.lineE_indirizzo_Fornitore.setText(info[7].text())
        self.lineE_telefono_Fornitore.setText(info[8].text())
        self.lineE_email_Fornitore.setText(info[9].text())
        self.cB_modalitaPag_Fornitore.setCurrentText(info[10].text())
        self.lineE_fax_Fornitore.setText(info[11].text())

    def elimina_fornitore(self):
        self.pB_aggiungi_Fornitore.setEnabled(True)
        self.pB_salva_Fornitore.setEnabled(False)
        info = self.tableWidget_Fornitore.selectedItems()
        lista_id = []
        # Salvo l'ID dei fornitori da eliminare all'interno di una variabile
        for i in range(0, len(info)):
            if i % self.tableWidget_Fornitore.columnCount() == 0:
                lista_id.append(info[i].text())
        if len(lista_id) == 1:
            button = QMessageBox.warning(self, "Attenzione", "Sei sicuro di voler eliminare definitivamente\n il fornitore dalla lista?", QMessageBox.Yes, QMessageBox.No)
        else:
            button = QMessageBox.warning(self, "Attenzione","Sei sicuro di voler eliminare definitivamente\n i fornitori dalla lista?", QMessageBox.Yes, QMessageBox.No)
        if button == QMessageBox.Yes:
            self.controller.elimina_fornitori(lista_id)
            self.aggiornaTabelle(self.tableWidget_Fornitore, self.controller.get_listafornitori())
            if len(lista_id) == 1:
                QMessageBox.information(self, 'Informazione', 'Il fornitore è stato eliminato con successo', QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.information(self, 'Informazione', 'I fornitori sono stati eliminati con successo', QMessageBox.Ok, QMessageBox.Ok)
            self.pB_elimina_Fornitore.setEnabled(False)
            self.checkpB_to_enable()

    def ricerca_fornitore(self):
        buttons_ricerca = [self.pB_ricerca_Cliente, self.pB_ricerca_Dipendente, self.pB_ricerca_Fornitore]
        self.ricerca_window = RicercaAnagraficheView(self.controller, self.aggiornaTabelle, self.tableWidget_Fornitore, buttons_ricerca, "Fornitore", self)
        self.ricerca_window.show()


    def salva_fornitore(self):
        self.pB_aggiungi_Fornitore.setEnabled(True)
        self.controller_fornitore.set_info(self.get_info_fornitore_from_view())
        if self.controller_fornitore.get_fornitore().iscompleto():
            self.controller.salva_fornitore(self.controller_fornitore.get_fornitore())
            self.aggiornaTabelle(self.tableWidget_Fornitore, self.controller.get_listafornitori())
            self.pB_salva_Fornitore.setEnabled(False)
            QMessageBox.information(self, 'Informazione', 'Il fornitore è stato modificato con successo', QMessageBox.Ok, QMessageBox.Ok)
            self.annulla_fornitore()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)

    def on_annulla_fornitore_clicked(self):
        button = QMessageBox.warning(self, "Attenzione", "Sei sicuro di voler annullare?\nIn tal caso dovrai ricominciare la compilazione",
                                     QMessageBox.Yes, QMessageBox.No)
        if button == QMessageBox.Yes:
            self.annulla_fornitore()
            QMessageBox.information(self, "Informazione", "La compilazione è stata annullata correttamente")

    def annulla_fornitore(self):
        self.pB_salva_Fornitore.setEnabled(False)
        self.pB_aggiungi_Fornitore.setEnabled(True)
        self.lineE_nome_Fornitore.clear()
        self.lineE_fornitura1_Fornitore.clear()
        self.lineE_fornitura2_Fornitore.clear()
        self.lineE_riferimento_Fornitore.clear()
        self.lineE_telefonoRif_Fornitore.clear()
        self.lineE_email_Fornitore.clear()
        self.lineE_indirizzo_Fornitore.clear()
        self.lineE_IVA_Fornitore.clear()
        self.cB_modalitaPag_Fornitore.setCurrentIndex(0)
        self.lineE_telefono_Fornitore.clear()
        self.lineE_fax_Fornitore.clear()

    def get_info_fornitore_from_view(self):
        item = self.tableWidget_Fornitore.selectedItems()
        if len(item) == 0:
            id = 0
        else:
            id = item[0].text()
        info = (id, self.lineE_nome_Fornitore.text(), self.lineE_fornitura1_Fornitore.text(), self.lineE_fornitura2_Fornitore.text(),
                self.lineE_IVA_Fornitore.text(),  self.lineE_riferimento_Fornitore.text(), self.lineE_telefonoRif_Fornitore.text(),
                self.lineE_indirizzo_Fornitore.text(), self.lineE_telefono_Fornitore.text(), self.lineE_email_Fornitore.text(),
                self.cB_modalitaPag_Fornitore.currentText(), self.lineE_fax_Fornitore.text())
        return info


    def stampaPDF(self, lista, path):
        gen = GeneratorePDF_Tabelle()
        gen.stampa(lista, path)

######################################METODI GENERICI PER LE 3 TABLE####################################################
    def checkpB_to_enable(self):
        n_dipendenti = len(self.controller.get_listadipendenti())
        n_clienti = len(self.controller.get_listaclienti())
        n_fornitori = len(self.controller.get_listafornitori())
        if n_dipendenti > 0:
            self.pB_creaPDF_Dipendente.setEnabled(True)
            self.pB_ricerca_Dipendente.setEnabled(True)
        else:
            self.pB_creaPDF_Dipendente.setEnabled(False)
            self.pB_ricerca_Dipendente.setEnabled(False)

        if n_clienti > 0:
            self.pB_creaPDF_Cliente.setEnabled(True)
            self.pB_ricerca_Cliente.setEnabled(True)
        else:
            self.pB_creaPDF_Dipendente.setEnabled(False)
            self.pB_ricerca_Cliente.setEnabled(False)

        if n_fornitori > 0:
            self.pB_creaPDF_Fornitore.setEnabled(True)
            self.pB_ricerca_Fornitore.setEnabled(True)
        else:
            self.pB_creaPDF_Fornitore.setEnabled(False)
            self.pB_ricerca_Fornitore.setEnabled(False)




    def enable_pB(self, button_modifica, button_elimina, table):
        n_righe_selezionate = len(table.selectionModel().selectedRows())
        if  n_righe_selezionate == 1:
            button_modifica.setEnabled(True)
            button_elimina.setEnabled(True)
        elif  n_righe_selezionate > 1:
            button_modifica.setEnabled(False)
            button_elimina.setEnabled(True)
        elif n_righe_selezionate == 0:
            button_modifica.setEnabled(False)
            button_elimina.setEnabled(False)

    def aggiornaTabelle(self, tabella, lista):
        tabella.setRowCount(0)
        i = 0
        for persona in lista:
            tabella.insertRow(i)
            j=0
            for info in persona.get_info():
                tabella.setItem(i, j, self.get_item(info))
                j+=1
            i+=1

    def get_item(self, info):
        item = QTableWidgetItem(str(info))
        font = QtGui.QFont()
        font.setBold(False)
        font.setFamily("Arial")
        font.setPointSize(9)
        item.setFont(font)
        item.setTextAlignment(Qt.AlignCenter)
        return item
