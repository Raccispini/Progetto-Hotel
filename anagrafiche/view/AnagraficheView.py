import sqlite3
from PyQt5.QtWidgets import QMainWindow
from anagrafiche.view.Ui_AnagraficheView import Ui_AnagraficheView
from GeneratorePDF_Tabelle import GeneratorePDF_Tabelle
from anagrafiche.controller.AnagraficheController import AnagraficheController

class AnagraficheView(QMainWindow, Ui_AnagraficheView):
    def __init__(self, parent=None):
        super(AnagraficheView, self).__init__(parent)
        self.setupUi(self)
        self.controller = AnagraficheController()
        self.connectButton()

#========================================================================================================================
##############################METODO CHE COLLEGA AL CLICK DI OGNI PULSANTE UN'AZIONE###################################

    def connectButton(self):

        ########################################PULSANTI CLIENTE#######################################################
        self.pB_add_Cliente.clicked.connect(lambda: self.add_cliente())
        self.pB_modifica_Cliente.clicked.connect(lambda: self.mod_cliente())
        self.pB_Elimina_Cliente.clicked.connect(lambda: self.elimina_cliente())
        self.pB_ricerca_Cliente.clicked.connect(lambda: self.ricerca_cliente())
        self.pB_salva_Cliente.clicked.connect(lambda: self.salva_cliente())
        self.pB_Annulla_Cliente.clicked.connect(lambda: self.annulla_cliente())
        self.pB_CreaPDF_Cliente.clicked.connect(lambda: self.stampaPDF(self.controller.get_listaclienti() ,
                                                                       "HTML/Tabelle/tabella_clienti.html"))

        ########################################PULSANTI DIPENDENTE######################################################
        self.pB_Aggiungi_Dipendente.clicked.connect(lambda: self.add_dipendente())
        self.pB_Modifica_Dipendente.clicked.connect(lambda: self.mod_dipendente())
        self.pB_Elimina_Dipendente.clicked.connect(lambda: self.elimina_dipendente())
        self.pB_Ricerca_Dipendente.clicked.connect(lambda: self.ricerca_dipendente())
        self.pB_Salva_Dipendente.clicked.connect(lambda: self.salva_dipendente())
        self.pB_Annulla_Dipendente.clicked.connect(lambda: self.annulla_dipendente())
        self.pB_CreaPDF_Dipendente.clicked.connect(lambda: self.stampaPDF(self.controller.get_listadipendenti(),
                                                                          "HTML/Tabelle/tabella_dipendenti.html"))
        #######################################PULSANTI FORNITORE######################################################
        self.pB_add_Fornitore.clicked.connect(lambda: self.add_fornitore())
        self.pB_modifica_Fornitore.clicked.connect(lambda: self.mod_fornitore())
        self.pB_Elimina_Fornitore.clicked.connect(lambda: self.elimina_fornitore())
        self.pB_ricerca_Fornitore.clicked.connect(lambda: self.ricerca_fornitore())
        self.pB_salva_Fornitore.clicked.connect(lambda: self.salva_fornitore())
        self.pB_Annulla_Fornitore.clicked.connect(lambda: self.annulla_fornitore())
        self.pB_CreaPDF_Fornitore.clicked.connect(lambda: self.stampaPDF(self.controller.get_listafornitori(),
                                                                         "HTML/Tabelle/tabella_fornitori.html"))


#=======================================================================================================================
#########################################METODI PULSANTI################################################################


###########################################METODI PER CLIENTE###########################################################
    def add_cliente(self):
        db = sqlite3.connect("database.db")
        query = """INSERT INTO Clienti(ID, nome, cognome, sesso, data_nascita, luogo_nascita, residenza,  
                                       provincia, via, CAP, CF, nazione, telefono, cellulare, email, documento,
                                        numero_documento, ente_rilascio, data_rilascio, data_scadenza,
                                        modalita_pagamento, info_checkin) VALUES ('prova','prova','prova','prova', null 
                                        ,'prova','prova','prova','prova','prova','prova','prova','prova','prova','prova'
                                        ,'prova',12,'prova',null,null,'prova','prova');"""
        print(query)
        id = db.execute("SELECT MAX(ID) FROM Clienti").fetchone()

        print(int(id[0]))
        id = int(id[0])+1
        nuovo_id = str(id).zfill(10)
        print(nuovo_id)
        #db.execute(query)
        db.commit()



    def mod_cliente(self):
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
    def add_dipendente(self):
        print("Dipendente Aggiunto")

    def mod_dipendente(self):
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
    def add_fornitore(self):
        print("Fornitore Aggiunto")

    def mod_fornitore(self):
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