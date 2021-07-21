'''
__author__: Federico Pretini
'''
import sqlite3
from dipendente.controller.DipendenteController import DipendenteController


class LoginModel:

    def __init__(self):
        self.dipendente_controller = DipendenteController()
        self.db = sqlite3.connect("database.db")

    def is_utente(self, username, password):
        query = "SELECT * FROM Dipendenti WHERE Dipendenti.username=\'%s\' AND Dipendenti.password=\'%s\';" % (username, password)
        if self.db.execute(query).fetchone() == None:
            return False
        else:
            self.dipendente_controller.set_info(self.db.execute(query).fetchone())
            return True


    def get_utente(self):
        return self.dipendente_controller
