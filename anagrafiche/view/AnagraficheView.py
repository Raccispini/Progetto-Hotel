from PyQt5 import QtGui
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox,  QTableWidgetItem
from anagrafiche.view.Ui_AnagraficheView import Ui_AnagraficheView
from GeneratorePDF_Tabelle import GeneratorePDF_Tabelle
from anagrafiche.controller.AnagraficheController import AnagraficheController
from cliente.model.ClienteModel import ClienteModel
from dipendente.model.DipendenteModel import DipendenteModel
from fornitore.model.FornitoreModel import FornitoreModel


class AnagraficheView(QMainWindow, Ui_AnagraficheView):
    def __init__(self, parent=None):
        super(AnagraficheView, self).__init__(parent)
        self.setupUi(self)
        self.controller = AnagraficheController()
        self.cliente = ClienteModel()
        self.aggiornaTabelle(self.tableWidget_Clienti, self.controller.get_listaclienti())
        self.fornitore = FornitoreModel()
        self.aggiornaTabelle(self.tableWidget_Fornitore, self.controller.get_listafornitori())
        self.dipendente = DipendenteModel()
        self.aggiornaTabelle(self.tableWidget_Dipendente, self.controller.get_listadipendenti())
        self.connectAction()
        self.checkpB_to_enable()


#========================================================================================================================
##############################METODO CHE COLLEGA AL CLICK DI OGNI PULSANTE UN'AZIONE###################################

    def connectAction(self):

        ########################################PULSANTI CLIENTE#######################################################
        self.pB_aggiungi_Cliente.clicked.connect(lambda: self.add_cliente())
        self.pB_modifica_Cliente.clicked.connect(lambda: self.mod_cliente())
        self.pB_elimina_Cliente.clicked.connect(lambda: self.elimina_cliente())
        self.pB_ricerca_Cliente.clicked.connect(lambda: self.ricerca_cliente())
        self.pB_salva_Cliente.clicked.connect(lambda: self.salva_cliente())
        self.pB_annulla_Cliente.clicked.connect(lambda: self.annulla_cliente())
        self.pB_creaPDF_Cliente.clicked.connect(lambda: self.stampaPDF(self.controller.get_listaclienti() ,
                                                                       "HTML/Tabelle/tabella_clienti.html"))
        self.tableWidget_Clienti.itemSelectionChanged.connect(lambda: self.enable_pB(self.pB_modifica_Cliente, self.pB_elimina_Cliente, self.tableWidget_Clienti))

        ########################################PULSANTI DIPENDENTE######################################################
        self.pB_aggiungi_Dipendente.clicked.connect(lambda: self.add_dipendente())
        self.pB_modifica_Dipendente.clicked.connect(lambda: self.mod_dipendente())
        self.pB_elimina_Dipendente.clicked.connect(lambda: self.elimina_dipendente())
        self.pB_ricerca_Dipendente.clicked.connect(lambda: self.ricerca_dipendente())
        self.pB_salva_Dipendente.clicked.connect(lambda: self.salva_dipendente())
        self.pB_annulla_Dipendente.clicked.connect(lambda: self.annulla_dipendente())
        self.pB_creaPDF_Dipendente.clicked.connect(lambda: self.stampaPDF(self.controller.get_listadipendenti(),
                                                                          "HTML/Tabelle/tabella_dipendenti.html"))
        self.tableWidget_Dipendente.itemSelectionChanged.connect(lambda: self.enable_pB(self.pB_modifica_Dipendente, self.pB_elimina_Dipendente, self.tableWidget_Dipendente))
        #######################################PULSANTI FORNITORE######################################################
        self.pB_aggiungi_Fornitore.clicked.connect(lambda: self.add_fornitore())
        self.pB_modifica_Fornitore.clicked.connect(lambda: self.mod_fornitore())
        self.pB_elimina_Fornitore.clicked.connect(lambda: self.elimina_fornitore())
        self.pB_ricerca_Fornitore.clicked.connect(lambda: self.ricerca_fornitore())
        self.pB_salva_Fornitore.clicked.connect(lambda: self.salva_fornitore())
        self.pB_annulla_Fornitore.clicked.connect(lambda: self.annulla_fornitore())
        self.pB_creaPDF_Fornitore.clicked.connect(lambda: self.stampaPDF(self.controller.get_listafornitori(),
                                                                         "HTML/Tabelle/tabella_fornitori.html"))
        self.tableWidget_Fornitore.itemSelectionChanged.connect(lambda: self.enable_pB(self.pB_modifica_Fornitore, self.pB_elimina_Fornitore, self.tableWidget_Fornitore))


#=======================================================================================================================
#########################################METODI PULSANTI################################################################


###########################################METODI PER CLIENTE###########################################################
    def add_cliente(self):
        self.cliente.set_nome(self.lineE_nome_Cliente.text())
        self.cliente.set_cognome(self.lineE_cognome_Cliente.text())
        self.cliente.set_sesso(self.cB_sesso_Cliente.currentText())
        self.cliente.set_data_di_nascita(self.dE_nascita_Cliente.date())
        self.cliente.set_luogo_di_nascita(self.lineE_nascita_Cliente.text())
        self.cliente.set_residenza(self.lineE_residenza_Cliente.text())
        self.cliente.set_provincia(self.lineE_provincia_Cliente.text())
        self.cliente.set_via(self.lineE_via_Cliente.text())
        self.cliente.set_cap(self.lineE_cap_Cliente.text())
        self.cliente.set_cf(self.lineE_cf_Cliente.text())
        self.cliente.set_nazione(self.lineE_nazione_Cliente.text())
        self.cliente.set_telefono(self.lineE_telefono_Cliente.text())
        self.cliente.set_cellulare(self.lineE_cellulare_Cliente.text())
        self.cliente.set_email(self.lineE_email_Cliente.text())
        self.cliente.set_tipo_documento(self.cB_documento_Cliente.currentText())
        self.cliente.set_numero_documento(self.lineE_numeroDoc_Cliente.text())
        self.cliente.set_ente_rilascio(self.lineE_enteRilascio_Cliente.text())
        self.cliente.set_data_rilascio(self.dE_dataRilascio_Cliente.date())
        self.cliente.set_data_scadenza(self.dE_dataScadenza_Cliente.date())
        self.cliente.set_modalita_pagamento(self.cB_modalitaPag_Cliente.currentText())
        self.cliente.set_info_checkin(self.lineE_infoCheckin_Cliente.text())
        if self.cliente.iscompleto():
            self.controller.add_cliente(self.cliente)
            QMessageBox.information(self, 'Informazione', 'Il cliente è stato registrato con successo', QMessageBox.Ok, QMessageBox.Ok)
            self.annulla_cliente()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)



    def mod_cliente(self):
        self.pB_salva_Cliente.setEnabled(True)
        #Codice...........
        self.pB_modifica_Cliente.setEnabled(False)


    def elimina_cliente(self):
        print("Cliente eliminato")
        self.pB_elimina_Cliente.setEnabled(False)
        self.checkpB_to_enable()


    def ricerca_cliente(self):
        print("Cliente ricercato")

    def salva_cliente(self):
        print("Cliente salvato")
        self.pB_salva_Cliente.setEnabled(False)

    def annulla_cliente(self):
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


#############################################METODI PER DIPENDETE#######################################################
    def add_dipendente(self):
        self.dipendente.set_username(self.lineE_username_Dipendente.text())
        self.dipendente.set_password(self.lineE_password_Dipendente.text())
        self.dipendente.set_ambito(self.lineE_ambito_Dipendente.text())
        self.dipendente.set_permessi(self.cB_permessi_Dipendente.currentText())
        self.dipendente.set_nome(self.lineE_nome_Dipendente.text())
        self.dipendente.set_cognome(self.lineE_cognome_Dipendente.text())
        self.dipendente.set_email(self.lineE_email_Dipendente.text())
        self.dipendente.set_cellulare(self.lineE_cellulare_Dipendente.text())
        self.dipendente.set_data_di_nascita(self.dE_nascita_Dipendente.date())
        if self.dipendente.iscompleto():
            self.controller.add_dipendente(self.dipendente)
            QMessageBox.information(self, 'Informazione', 'Il dipendente è stato registrato con successo', QMessageBox.Ok, QMessageBox.Ok)
            self.annulla_dipendente()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)

    def mod_dipendente(self):
        self.pB_salva_Dipendente.setEnabled(True)
        print("Dipendente pronto per la modifica")
        self.pB_modifica_Dipendente.setEnabled(False)

    def elimina_dipendente(self):
        print("Dipendente eliminato")

    def ricerca_dipendente(self):
        print("Dipendente ricercato")

    def salva_dipendente(self):
        print("Dipendente salvato")
        self.pB_modifica_Dipendente.setEnabled(False)

    def annulla_dipendente(self):
        self.lineE_username_Dipendente.clear()
        self.lineE_password_Dipendente.clear()
        self.lineE_ambito_Dipendente.clear()
        self.cB_permessi_Dipendente.setCurrentIndex(0)
        self.lineE_nome_Dipendente.clear()
        self.lineE_cognome_Dipendente.clear()
        self.lineE_email_Dipendente.clear()
        self.lineE_cellulare_Dipendente.clear()
        self.dE_nascita_Dipendente.setDate(QDate.fromString("01/01/1800", "dd/MM/yyyy"))

    #########################################METODI PER FORNITORE#######################################################
    def add_fornitore(self):
        self.fornitore.set_nome(self.lineE_nome_Fornitore.text())
        self.fornitore.set_fornitura1(self.lineE_fornitura1_Fornitore.text())
        self.fornitore.set_fornitura2(self.lineE_fornitura2_Fornitore.text())
        self.fornitore.set_riferimento(self.lineE_riferimento_Fornitore.text())
        self.fornitore.set_cellulare_rif(self.lineE_telefonoRif_Fornitore.text())
        self.fornitore.set_email(self.lineE_email_Fornitore.text())
        self.fornitore.set_indirizzo(self.lineE_indirizzo_Fornitore.text())
        self.fornitore.set_iva(self.lineE_IVA_Fornitore.text())
        self.fornitore.set_mod_pagamento(self.cB_modalitaPag_Fornitore.currentText())
        self.fornitore.set_telefono(self.lineE_telefono_Fornitore.text())
        self.fornitore.set_fax(self.lineE_fax_Fornitore.text())
        if self.fornitore.iscompleto():
            self.controller.add_fornitore(self.fornitore)
            QMessageBox.information(self, 'Informazione', 'Il fornitore è stato registrato con successo', QMessageBox.Ok, QMessageBox.Ok)
            self.annulla_fornitore()
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)

    def mod_fornitore(self):
        self.pB_salva_Fornitore.setEnabled(True)
        print("Fornitore pronto per la modifica")
        self.pB_modifica_Fornitore.setEnabled(False)

    def elimina_fornitore(self):
        print("Fornitore eliminato")

    def ricerca_fornitore(self):
        print("Fornitore ricercato")

    def salva_fornitore(self):
        print("Fornitore salvato")
        self.pB_salva_Fornitore.setEnabled(False)

    def annulla_fornitore(self):
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



    def stampaPDF(self, lista, path):
        gen = GeneratorePDF_Tabelle()
        gen.stampa(lista, path)

######################################METODO PER L'AGGIORNAMENTO DELLA TABELLA##########################################
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
