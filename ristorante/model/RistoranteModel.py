'''
__author__: Federico Pretini
'''
import sqlite3


class RistoranteModel():
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.lista_tavoli_prenotati = []


    def prenota_tavolo(self, info_prenotazione):
        query = "INSERT INTO Prenotazioni_ristorante(tavolo,nominativo,persone,data_prenotazione,ora_inizio,ora_fine) VALUES (?,?,?,?,?,?);"
        info_prenotazione[1] = info_prenotazione[1].split(" - ")[0]
        self.db.execute(query, info_prenotazione)
        self.db.commit()

    def check_tavoli_prenotati(self, data, orario):
        query = 'SELECT * FROM Prenotazioni_ristorante WHERE data_prenotazione = \'' + data + '\' AND ora_inizio = \'' + orario[0] + '\' AND ora_fine = \''+ orario[1] + '\';'
        return self.db.execute(query).fetchall()

    def get_lista_prenotazioni(self):
        self.lista_tavoli_prenotati = self.db.execute('SELECT * FROM Prenotazioni_ristorante ORDER BY data_prenotazione')
        return self.lista_tavoli_prenotati

    def elimina_prenotazione(self, lista_id):
        for id in lista_id:
            self.db.execute("DELETE FROM Prenotazioni_ristorante WHERE id_prenotazione = " + id)
            self.db.commit()

    def get_lista_prenotazioni_filtrata(self, info_filtraggio):
        self.lista_filtrata = []
        if info_filtraggio[0]=="Tutti" and info_filtraggio[2]=="Tutti":
            query = "SELECT * FROM Prenotazioni_ristorante WHERE data_prenotazione = \'" + info_filtraggio[1].toString("dd/MM/yyyy") + "\';"
            self.lista_filtrata = self.db.execute(query).fetchall()

        elif info_filtraggio[0]=="Tutti" and info_filtraggio[2]!="Tutti":
            query = "SELECT * FROM Prenotazioni_ristorante WHERE data_prenotazione = \'" + info_filtraggio[1].toString("dd/MM/yyyy") + "\'AND ora_inizio =\'" + info_filtraggio[2].split("-")[0] + "\' AND ora_fine = \'"+ info_filtraggio[2].split("-")[1] + "\';"
            self.lista_filtrata = self.db.execute(query).fetchall()

        elif info_filtraggio[0]!="Tutti" and info_filtraggio[2]=="Tutti":
            query = "SELECT * FROM Prenotazioni_ristorante WHERE data_prenotazione = \'" + info_filtraggio[1].toString("dd/MM/yyyy") + "\' AND tavolo = \'"+ info_filtraggio[0] + "\';"
            self.lista_filtrata = self.db.execute(query).fetchall()

        elif info_filtraggio[0]!="Tutti" and info_filtraggio[2]=="Tutti":
            query = "SELECT * FROM Prenotazioni_ristorante WHERE data_prenotazione = \'" + info_filtraggio[1].toString("dd/MM/yyyy") + "\' AND tavolo = \'" + info_filtraggio[0] + "\'AND ora_inizio =\'" + info_filtraggio[2].split("-")[0] + "\' AND ora_fine = \'"+ info_filtraggio[2].split("-")[1] + "\';"
            self.lista_filtrata = self.db.execute(query).fetchall()

        return self.lista_filtrata

    def get_menu(self, categoria):
        query = "SELECT * FROM Menu WHERE categoria = \'"+ categoria + "\';"
        return list(self.db.execute(query).fetchall())

    def get_prezzo_piatto(self, nome_piatto):
        query = "SELECT prezzo FROM Menu WHERE nome_piatto = \'" + nome_piatto + "\';"
        return self.db.execute(query).fetchone()[0]



