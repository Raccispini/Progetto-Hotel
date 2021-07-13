import sqlite3
from datetime import datetime

class RistoranteModel():
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.lista_tavoli_prenotati = []


    def update_db(self):
        giorno_corrente = datetime.now()
        ore_14 = giorno_corrente.replace(hour=14, minute=0)
        ore_16 = giorno_corrente.replace(hour=16, minute=0)
        ore_21 = giorno_corrente.replace(hour=21, minute=0)
        ore_23 = giorno_corrente.replace(hour=23, minute=0)
        # Elimino prima tutte le prenotazioni con una data anteriore a quella corrente
        query = "DELETE FROM Prenotazioni_Ristorante WHERE data_prenotazione <\'" + giorno_corrente.strftime("%d/%m/%Y") + "\';"
        self.db.execute(query)
        self.db.commit()
        # Controllo se sono passate le 14:00 e in tal caso elimino anche tutte le prenotazioni di mezza giornata della data corrente
        if giorno_corrente > ore_14:
            query = "DELETE FROM Prenotazioni_ombrelloni WHERE data_prenotazione =\'" + giorno_corrente.strftime("%d/%m/%Y") + "\'AND orario_fine ='14:00';"
            self.db.execute(query).fetchall()
            self.db.commit()
        if giorno_corrente > ore_16:
            query = "DELETE FROM Prenotazioni_ombrelloni WHERE data_prenotazione =\'" + giorno_corrente.strftime("%d/%m/%Y") + "\'AND orario_fine ='16:00';"
            self.db.execute(query).fetchall()
            self.db.commit()
        if giorno_corrente > ore_21:
            query = "DELETE FROM Prenotazioni_ombrelloni WHERE data_prenotazione =\'" + giorno_corrente.strftime("%d/%m/%Y") + "\'AND orario_fine ='21:00';"
            self.db.execute(query).fetchall()
            self.db.commit()
        if giorno_corrente > ore_23:
            query = "DELETE FROM Prenotazioni_ombrelloni WHERE data_prenotazione =\'" + giorno_corrente.strftime("%d/%m/%Y") + "\'AND orario_fine ='23:00';"
            self.db.execute(query).fetchall()
            self.db.commit()

    def prenota_tavolo(self, info_prenotazione):
        print(info_prenotazione)

    def check_tavoli_prenotati(self, data, orario):
        self.update_db()
        query = 'SELECT * FROM Prenotazioni_ristorante WHERE data_prenotazione = ' + data + ' AND ora_inizio = \'' + orario[0] + '\' AND ora_fine = \''+ orario[1] + '\';'
        return self.db.execute(query).fetchall()

    def get_lista_prenotazioni(self):
        self.update_db()
        self.lista_tavoli_prenotati = self.db.execute('SELECT * FROM Prenotazioni_ristorante ORDER BY data_prenotazione')
        return self.lista_tavoli_prenotati




   # def get_lista_prenotazioni(self):



  #  def get_menu(self):
        
        

 #   def elimina_prenotazione(self):
    
