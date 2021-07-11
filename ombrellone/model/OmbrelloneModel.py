import sqlite3
from datetime import datetime

class OmbrelloneModel():
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.lista_prenotati = []
        self.lista_disponibili = []
        self.update_database()

    #Aggiorna in automatico il database eliminando dalle prenotazioni gli ombrelloni che erano stati prenotati ma ora sono liberi
    def update_database(self):
        giorno_corrente = datetime.now()
        ore_14 = giorno_corrente.replace(hour=14, minute=0)
        #Elimino prima tutte le prenotazioni con una data anteriore a quella corrente
        query = "DELETE FROM Prenotazioni_ombrelloni WHERE data_prenotazione <\'" + giorno_corrente.strftime("%d/%m/%Y") + "\';"
        self.db.execute(query)
        self.db.commit()
        # Controllo se sono passate le 14:00 e in tal caso elimino anche tutte le prenotazioni di mezza giornata della data corrente
        if giorno_corrente > ore_14:
           query = "DELETE FROM Prenotazioni_ombrelloni WHERE data_prenotazione =\'" + giorno_corrente.strftime("%d/%m/%Y")  + "\'AND orario_fine ='14:00';"
           self.db.execute(query).fetchall()
           self.db.commit()


    def get_ombrelloni_prenotati(self, date, tipo, orario):
        self.update_database()
        query='SELECT * FROM Prenotazioni_ombrelloni WHERE data_prenotazione ="'+ date +'";'
        self.lista_prenotati = self.db.execute(query).fetchall()
        if tipo=="Mezza Giornata" and orario == "Mattina":
            for ombrellone_prenotato in self.lista_prenotati:
                if ombrellone_prenotato[3]=="Mezza Giornata" and ombrellone_prenotato[4]=="14:00":
                    self.lista_prenotati.remove(ombrellone_prenotato)
        elif tipo=="Mezza Giornata" and orario == "Pomeriggio":
            for ombrellone_prenotato in self.lista_prenotati:
                if ombrellone_prenotato[3]=="Mezza Giornata" and ombrellone_prenotato[5]=="14:00":
                    self.lista_prenotati.remove(ombrellone_prenotato)
        return self.lista_prenotati

    def get_lista_prenotazioni(self):
        self.update_database()
        query='SELECT * FROM Prenotazioni_ombrelloni WHERE data_prenotazione >="'+ datetime.now().strftime("%d/%m/%Y")+'";'
        self.lista_prenotati = self.db.execute(query).fetchall()
        return self.lista_prenotati

    def elimina_prenotazione(self, lista_numeri):
        for numero in lista_numeri:
            self.db.execute("DELETE FROM Prenotazioni_ombrelloni WHERE numero_ombrellone=\'"+  numero + "\';")
            self.db.commit()

    def prenota_ombrellone(self, info):
        query = "INSERT INTO Prenotazioni_ombrelloni VALUES (?,?,?,?,?,?,?,?,?,?);"
        data = info
        self.db.execute(query,data)
        self.db.commit()

    def get_listino_prezzi(self, nome_ombrellone):
        query ="SELECT * FROM Ombrelloni WHERE numero_ombrellone = \'" + nome_ombrellone + "\';"
        listino_prezzi = self.db.execute(query).fetchone()
        return listino_prezzi



