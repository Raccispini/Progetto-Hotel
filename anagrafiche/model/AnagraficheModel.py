'''
__author__: Federico Pretini
'''

import sqlite3

from cliente.controller.ClienteController import ClienteController
from dipendente.controller.DipendenteController import DipendenteController
from dipendente.model.DipendenteModel import DipendenteModel
from fornitore.controller.FornitoreController import FornitoreController
from fornitore.model.FornitoreModel import FornitoreModel


class AnagraficheModel():
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.listaclienti = []
        self.listafornitori = []
        self.listadipendeti = []


    def update_listaclienti(self):
        self.listaclienti.clear()
        tab_clienti = self.db.execute('SELECT * FROM Clienti;').fetchall()
        for cliente in tab_clienti:
            self.controller_cliente = ClienteController()
            info_cliente = []
            for info in cliente:
                info_cliente.append(info)
            self.controller_cliente.set_info(info_cliente)
            self.listaclienti.append(self.controller_cliente.get_cliente())

    def add_cliente(self, cliente):
        query = "INSERT INTO Clienti(NOME, COGNOME, SESSO, DATA_NASCITA, LUOGO_NASCITA, RESIDENZA, PROVINCIA, VIA, CAP," \
                "CF, NAZIONE, TELEFONO, CELLULARE, EMAIL, DOCUMENTO, NUMERO_DOCUMENTO, ENTE_RILASCIO, DATA_RILASCIO, " \
                "DATA_SCADENZA, MODALITA_PAGAMENTO, INFO_CHECKIN) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"

        data = list(cliente.get_info())
        data.pop(0)  # Tolgo l'ID che viene incrementato automaticamente nel DB
        self.db.execute(query, data)
        self.db.commit()

    def salva_cliente(self, cliente):
        query = "UPDATE Clienti SET NOME=(?), COGNOME=(?), SESSO=(?), DATA_NASCITA=(?), LUOGO_NASCITA=(?), RESIDENZA=(?)," \
                " PROVINCIA=(?), VIA=(?), CAP=(?), CF=(?), NAZIONE=(?), TELEFONO=(?), CELLULARE=(?), EMAIL=(?), DOCUMENTO=(?)," \
                " NUMERO_DOCUMENTO=(?), ENTE_RILASCIO=(?), DATA_RILASCIO=(?), DATA_SCADENZA=(?), MODALITA_PAGAMENTO=(?)," \
                " INFO_CHECKIN=(?) WHERE ID=" + str(cliente.get_id()) + ";"

        data = list(cliente.get_info())
        data.pop(0)  # Tolgo l'ID che viene utilizzato come criterio di ricerca
        self.db.execute(query, data)
        self.db.commit()

    def ricerca_cliente(self, info_ricerca):
        query = "SELECT * FROM Clienti WHERE " + info_ricerca[0] + "=\'" + info_ricerca[1] + "\';"
        lista_clienti = self.db.execute(query).fetchall()
        lista_trovati = []
        for cliente in lista_clienti:
            self.controller_cliente = ClienteController()
            self.controller_cliente.set_info(cliente)
            lista_trovati.append(self.controller_cliente.get_cliente())
        return lista_trovati

    def elimina_clienti(self, lista_id):
        for id in lista_id:
            query = ("DELETE FROM Clienti WHERE ID=" + id + ";")
            self.db.execute(query)
            self.db.commit()

    def update_listadipendenti(self):
        self.listadipendeti.clear()
        tab_dipendenti = self.db.execute('SELECT * FROM Dipendenti;').fetchall()
        for dipendente in tab_dipendenti:
            self.controller_dipedente = DipendenteController()
            info_dipendente = []
            for info in dipendente:
                info_dipendente.append(info)
            self.controller_dipedente.set_info(info_dipendente)
            self.listadipendeti.append(self.controller_dipedente.get_dipendente())

    def add_dipendente(self, dipendente):
        query = "INSERT INTO Dipendenti(NOME, COGNOME, USERNAME, PASSWORD, EMAIL, CELLULARE, DATA_NASCITA, "\
                "AMBITO, PERMESSI) VALUES (?,?,?,?,?,?,?,?,?);"

        data = list(dipendente.get_info())
        data.pop(0)  # Tolgo l'ID che viene incrementato automaticamente nel DB
        self.db.execute(query, data)
        self.db.commit()

    def salva_dipendente(self, dipendente):
        query = "UPDATE Dipendenti SET NOME=(?), COGNOME=(?), USERNAME=(?), PASSWORD=(?), EMAIL=(?), CELLULARE=(?), DATA_NASCITA=(?), "\
                "AMBITO=(?), PERMESSI=(?) WHERE ID=" + str(dipendente.get_id()) + ";"
        data = list(dipendente.get_info())
        data.pop(0)  # Tolgo l'ID che viene utilizzato come criterio di ricerca
        self.db.execute(query, data)
        self.db.commit()

    def ricerca_dipendente(self, info_ricerca):
        query = "SELECT * FROM Dipendenti WHERE " + info_ricerca[0] + "=\'" + info_ricerca[1] + "\';"
        lista_dipendenti = self.db.execute(query).fetchall()
        lista_trovati = []
        for dipendente in lista_dipendenti:
            self.controller_dipedente = DipendenteController()
            self.controller_dipedente.set_info(dipendente)
            lista_trovati.append(self.controller_dipedente.get_dipendente())

        return lista_trovati

    def elimina_dipendenti(self, lista_id):
        for id in lista_id:
            query = ("DELETE FROM Dipendenti WHERE ID=" + id + ";")
            self.db.execute(query)
            self.db.commit()



    def update_listafornitori(self):
        self.listafornitori.clear()
        tab_fornitori = self.db.execute('SELECT * FROM Fornitori;').fetchall()
        for fornitore in tab_fornitori:
            self.controller_fornitore = FornitoreController()
            info_fornitore = []
            for info in fornitore:
                info_fornitore.append(info)
            self.controller_fornitore.set_info(info_fornitore)
            self.listafornitori.append(self.controller_fornitore.get_fornitore())

    def add_fornitore(self, fornitore):
        query = "INSERT INTO Fornitori(NOME_FORNITORE, FORNITURA1, FORNITURA2, IVA, RIFERIMENTO, CELLULARE_RIFERIMENTO,"\
                " INDIRIZZO, TELEFONO, EMAIL, MODALITA_PAGAMENTO, FAX) VALUES (?,?,?,?,?,?,?,?,?,?,?);"

        data = list(fornitore.get_info())
        data.pop(0)  # Tolgo l'ID che viene incrementato automaticamente nel DB
        self.db.execute(query, data)
        self.db.commit()

    def salva_fornitore(self, fornitore):
        query = "UPDATE Fornitori SET NOME_FORNITORE=(?), FORNITURA1=(?), FORNITURA2=(?), IVA=(?), RIFERIMENTO=(?)," \
                " CELLULARE_RIFERIMENTO=(?), INDIRIZZO=(?), TELEFONO=(?), EMAIL=(?), MODALITA_PAGAMENTO=(?), FAX=(?)" \
                " WHERE ID=" + str(fornitore.get_id()) + ";"
        data = list(fornitore.get_info())
        data.pop(0)  # Tolgo l'ID che viene utilizzato come criterio di ricerca
        self.db.execute(query, data)
        self.db.commit()

    def ricerca_fornitore(self, info_ricerca):
        query = "SELECT * FROM Fornitori WHERE " + info_ricerca[0] + "=\'" + info_ricerca[1] + "\';"
        lista_fornitori = self.db.execute(query).fetchall()
        lista_trovati = []
        for fornitore in lista_fornitori:
            self.controller_fornitore = FornitoreController()
            self.controller_fornitore.set_info(fornitore)
            lista_trovati.append(self.controller_fornitore.get_fornitore())

        return lista_trovati

    def elimina_fornitori(self, lista_id):
        for id in lista_id:
            query = ("DELETE FROM Fornitori WHERE ID=" + id + ";")
            self.db.execute(query)
            self.db.commit()






