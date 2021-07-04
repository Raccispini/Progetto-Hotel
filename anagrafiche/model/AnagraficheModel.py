import sqlite3
from cliente.model.ClienteModel import ClienteModel
from dipendente.model.DipendenteModel import DipendenteModel
from fornitore.model.FornitoreModel import FornitoreModel


class AnagraficheModel():
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.listaclienti = []
        self.listafornitori = []
        self.listadipendeti = []
        self.get_listaclienti()
        self.get_listafornitori()
        self.get_listadipendenti()

    def get_listaclienti(self):
        tab_clienti = self.db.execute('SELECT * FROM Clienti;').fetchall()
        for cliente in tab_clienti:
            self.listaclienti.append(ClienteModel(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4],
                                                  cliente[5], cliente[6], cliente[7], cliente[8], cliente[9],
                                                  cliente[10], cliente[11], cliente[12], cliente[13], cliente[14],
                                                  cliente[15], cliente[16], cliente[17], cliente[18], cliente[19],
                                                  cliente[20], cliente[21]))
    def get_listafornitori(self):
        tab_fornitori = self.db.execute('SELECT * FROM Fornitori;').fetchall()
        for fornitore in tab_fornitori:
            self.listafornitori.append(FornitoreModel(fornitore[0], fornitore[1], fornitore[2], fornitore[3], fornitore[4],
                                                      fornitore[5], fornitore[6], fornitore[7], fornitore[8], fornitore[9],
                                                      fornitore[10], fornitore[11]))

    def get_listadipendenti(self):
        tab_dipendenti = self.db.execute('SELECT * FROM Dipendenti;').fetchall()
        for dipendente in tab_dipendenti:
            self.listadipendeti.append(DipendenteModel(dipendente[0], dipendente[1], dipendente[2], dipendente[3], dipendente[4],
                                                       dipendente[5], dipendente[6], dipendente[7], dipendente[8], dipendente[9]))

    def add_cliente(self, cliente):

        query = "INSERT INTO Clienti(nome, cognome, sesso, data_nascita, luogo_nascita, residenza, provincia, via, CAP,"\
                " CF, nazione, telefono, cellulare, email, documento, numero_documento, ente_rilascio,"\
                " data_rilascio, data_scadenza, modalita_pagamento, info_checkin) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"


        data =  (cliente.get_nome(), cliente.get_cognome(), cliente.get_sesso(), cliente.get_data_di_nascita().toString("dd/MM/yyyy"),
                cliente.get_luogo_di_nascita(), cliente.get_residenza(), cliente.get_provincia(), cliente.get_via(),
                cliente.get_cap(), cliente.get_cf(), cliente.get_nazione(), cliente.get_telefono(), cliente.get_cellulare(),
                cliente.get_email(), cliente.get_tipo_documento(), cliente.get_numero_documento(), cliente.get_ente_rilascio(),
                cliente.get_data_rilascio().toString("dd/MM/yyyy"), cliente.get_data_scadenza().toString("dd/MM/yyyy"),
                cliente.get_modalita_pagamento(), cliente.get_info_check_in())

        self.db.execute(query, data)
        self.db.commit()

    def add_fornitore(self, fornitore):
        query = "INSERT INTO Fornitori(nome_fornitore, tipo_fornitura, tipo_fornitura_2, riferimento, cellulare_riferimento," \
                " email, indirizzo, IVA, modalita_pagamento, telefono, fax)  VALUES (?,?,?,?,?,?,?,?,?,?,?);"

        data = (fornitore.get_nome(), fornitore.get_fornitura1(), fornitore.get_fornitura2(), fornitore.get_riferimento(),
                fornitore.get_cellulare_rif(), fornitore.get_email(), fornitore.get_indirizzo(), fornitore.get_iva(),
                fornitore.get_mod_pagamento(), fornitore.get_telefono(), fornitore.get_fax() )

        print(data)

        self.db.execute(query, data)
        self.db.commit()




