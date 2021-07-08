import sqlite3
from cliente.model.ClienteModel import ClienteModel
from cliente.model.ClienteModel import ClienteModel

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
            self.listaclienti.append(ClienteModel(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4],
                                                  cliente[5], cliente[6], cliente[7], cliente[8], cliente[9],
                                                  cliente[10], cliente[11], cliente[12], cliente[13], cliente[14],
                                                  cliente[15], cliente[16], cliente[17], cliente[18], cliente[19],
                                                  cliente[20]))

    def get_listafornitori(self):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        tab_clienti = cursor.execute('SELECT * FROM Clienti;').fetchall()
        for cliente in tab_clienti:
            self.listaclienti.append(ModelCliente(cliente[0], cliente[1], cliente[2],cliente[3], cliente[4],
                                                  cliente[5],cliente[6], cliente[7], cliente[8], cliente[9],
                                                  cliente[10], cliente[11], cliente[12], cliente[13], cliente[14],
                                                  cliente[15], cliente[16], cliente[17], cliente[18], cliente[19],
                                                  cliente[20]))

    def get_listadipendenti(self):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        tab_clienti = cursor.execute('SELECT * FROM Clienti;').fetchall()
        for cliente in tab_clienti:
            self.listaclienti.append(ModelCliente(cliente[0], cliente[1], cliente[2],cliente[3], cliente[4],
                                                  cliente[5],cliente[6], cliente[7], cliente[8], cliente[9],
                                                  cliente[10], cliente[11], cliente[12], cliente[13], cliente[14],
                                                  cliente[15], cliente[16], cliente[17], cliente[18], cliente[19],
                                                  cliente[20],cliente[21]))

    def get_listafornitori(self):
        tab_fornitori = self.db.execute('SELECT * FROM Fornitori;').fetchall()
        for fornitore in tab_fornitori:
            self.listafornitori.append(FornitoreModel(fornitore[0], fornitore[1], fornitore[2], fornitore[3], fornitore[4],
                                                      fornitore[5], fornitore[6], fornitore[7], fornitore[8], fornitore[9],
                                                      fornitore[10], fornitore[11]))
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
            self.listadipendeti.append(DipendenteModel(dipendente[0], dipendente[1], dipendente[2], dipendente[3], dipendente[4],
                                                       dipendente[5], dipendente[6], dipendente[7], dipendente[8], dipendente[9]))

    def add_cliente(self, info):
        #Metodo che ci permette di calcolare il nuovo ID da assegnare
        def take_new_ID():
            id = self.db.execute("SELECT MAX(ID) FROM Clienti").fetchone()
            id_int = int(id[0]) + 1
            id_str = str(id_int).zfill(15)
            return id_str

        new_id = take_new_ID()
        query = ("""INSERT INTO Clienti(nome, cognome, sesso, data_nascita, luogo_nascita, residenza, provincia, via, CAP,
                                       CF, nazione, telefono, cellulare, email, documento, numero_documento, 
                                       ente_rilascio, data_rilascio, data_scadenza, modalita_pagamento, info_checkin) 
                                       VALUES (""" + info["Nome"] + ")")
                 #(, info["Cognome"], info["Sesso"])
        #cur.execute('INSERT INTO name VALUES(?, ?, ?, ?);', (0, "0123", "034", 23))
        self.db.execute(query)
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






