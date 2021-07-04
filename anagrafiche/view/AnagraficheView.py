from PyQt5.QtWidgets import QMainWindow, QMessageBox
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
        self.fornitore = FornitoreModel()
        self.dipendente = DipendenteModel()
        self.connectButton()

#========================================================================================================================
##############################METODO CHE COLLEGA AL CLICK DI OGNI PULSANTE UN'AZIONE###################################

    def connectButton(self):

        ########################################PULSANTI CLIENTE#######################################################
        self.pB_aggiungi_Cliente.clicked.connect(lambda: self.aggiungi_cliente())
        self.pB_modifica_Cliente.clicked.connect(lambda: self.modifica_cliente())
        self.pB_elimina_Cliente.clicked.connect(lambda: self.elimina_cliente())
        self.pB_ricerca_Cliente.clicked.connect(lambda: self.ricerca_cliente())
        self.pB_salva_Cliente.clicked.connect(lambda: self.salva_cliente())
        self.pB_annulla_Cliente.clicked.connect(lambda: self.annulla_cliente())
        self.pB_creaPDF_Cliente.clicked.connect(lambda: self.stampaPDF(self.controller.get_listaclienti() ,
                                                                       "HTML/Tabelle/tabella_clienti.html"))

        ########################################PULSANTI DIPENDENTE######################################################
        self.pB_aggiungi_Dipendente.clicked.connect(lambda: self.aggiungi_dipendente())
        self.pB_modifica_Dipendente.clicked.connect(lambda: self.modifica_dipendente())
        self.pB_elimina_Dipendente.clicked.connect(lambda: self.elimina_dipendente())
        self.pB_ricerca_Dipendente.clicked.connect(lambda: self.ricerca_dipendente())
        self.pB_salva_Dipendente.clicked.connect(lambda: self.salva_dipendente())
        self.pB_annulla_Dipendente.clicked.connect(lambda: self.annulla_dipendente())
        self.pB_creaPDF_Dipendente.clicked.connect(lambda: self.stampaPDF(self.controller.get_listadipendenti(),
                                                                          "HTML/Tabelle/tabella_dipendenti.html"))
        #######################################PULSANTI FORNITORE######################################################
        self.pB_aggiungi_Fornitore.clicked.connect(lambda: self.aggiungi_fornitore())
        self.pB_modifica_Fornitore.clicked.connect(lambda: self.modifica_fornitore())
        self.pB_elimina_Fornitore.clicked.connect(lambda: self.elimina_fornitore())
        self.pB_ricerca_Fornitore.clicked.connect(lambda: self.ricerca_fornitore())
        self.pB_salva_Fornitore.clicked.connect(lambda: self.salva_fornitore())
        self.pB_annulla_Fornitore.clicked.connect(lambda: self.annulla_fornitore())
        self.pB_creaPDF_Fornitore.clicked.connect(lambda: self.stampaPDF(self.controller.get_listafornitori(),
                                                                         "HTML/Tabelle/tabella_fornitori.html"))


#=======================================================================================================================
#########################################METODI PULSANTI################################################################


###########################################METODI PER CLIENTE###########################################################
    def aggiungi_cliente(self):
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
        self.cliente.set_info_check_in(self.lineE_infoCheckin_Cliente.text())
        if self.cliente.iscompleto():
            self.controller.add_cliente(self.cliente)
            QMessageBox.information(QMessageBox.information(self, "Informazione", "I dati sono stati salvati correttamente",QMessageBox.Ok, QMessageBox.Ok))
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)

    def take_data_from_label(self, interfaccia):
        return interfaccia.lineEdit_nome_Cliente.text()


    def modifica_cliente(self):
        print("Cliente pronto per la modifica")

    def elimina_cliente(self):
        print("Cliente eliminato")

    def ricerca_cliente(self):
        print("Cliente ricercato")

    def salva_cliente(self):
        print("Cliente salvato")

    def annulla_cliente(self):
        print("Cliente annullato")

#############################################METODI PER DIPENDETE#######################################################
    def aggiungi_dipendente(self):
        print("Dipendente Aggiunto")

    def modifica_dipendente(self):
        print("Dipendente pronto per la modifica")

    def elimina_dipendente(self):
        print("Dipendente eliminato")

    def ricerca_dipendente(self):
        print("Dipendente ricercato")

    def salva_dipendente(self):
        print("Dipendente salvato")

    def annulla_dipendente(self):
        print("Dipendente annullato")

    #########################################METODI PER FORNITORE#######################################################
    def aggiungi_fornitore(self):
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
            QMessageBox.information(self, "Informazione", "I dati sono stati salvati correttamente",QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.critical(self, 'Errore', 'Per favore, inserisci tutte le informazioni richieste', QMessageBox.Ok, QMessageBox.Ok)

    def modifica_fornitore(self):
        print("Fornitore pronto per la modifica")

    def elimina_fornitore(self):
        print("Fornitore eliminato")

    def ricerca_fornitore(self):
        print("Fornitore ricercato")

    def salva_fornitore(self):
        print("Fornitore salvato")

    def annulla_fornitore(self):
        print("Fornitore annullato")



    def stampaPDF(self, lista, path):
        gen = GeneratorePDF_Tabelle()
        gen.stampa(lista, path)