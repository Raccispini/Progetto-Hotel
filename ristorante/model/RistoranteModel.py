import sqlite3
from datetime import datetime

class RistoranteModel():
    def __init__(self):
        self.db = sqlite3.connect("database.db")
        self.update_database()


"""   


    def update_database(self):



    def get_tavoli_prenotati(self):



    def get_lista_prenotazioni(self):



    def get_menu(self):
        
        

    def elimina_prenotazione(self):
    
    
"""