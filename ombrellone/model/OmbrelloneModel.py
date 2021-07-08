import sqlite3
from datetime import datetime

class OmbrelloneModel():
    def __init__(self):
        self.lista_prenotati = []
        self.lista_disponibili = []


    def get_Prenotazioni(self):
        db = sqlite3.connect("database.db")
        now = datetime.now()
        query='SELECT * FROM Prenotazioni_ombrelloni WHERE data_fine > "'+ now.strftime("%d/%m/%Y")+'";'
        self.lista_prenotati = db.execute(query).fetchall()
        return self.lista_prenotati


    def get_OmbrelloniDisponibili(self, data_inizio, data_fine):
        query='SELECT * FROM Ombrelloni WHERE Ombrelloni.n_ombrellone NOT IN (SELECT n_ombrellone FROM Prenotazioni_ombrelloni WHERE data_inizio > "' + data_inizio + '" OR data_fine < "' + data_fine +'");'
        db= sqlite3.connect("database.db")
        self.lista_disponibili = db.execute(query).fetchall()
        return  self.lista_disponibili


