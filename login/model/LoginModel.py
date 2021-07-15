'''
__author__: Federico Pretini
'''
import sqlite3
from dipendente.controller.DipendenteController import DipendenteController


class LoginModel:

    def __init__(self):
        super(LoginModel, self).__init__()
        self.dipendente_controller = DipendenteController()
        self.db = sqlite3.connect("database.db")
        self.dipendente = None

    def is_dipedente(self, username, password):
        query = "SELECT * FROM Dipendenti WHERE Dipendenti.username=\'%s\' AND Dipendenti.password=\'%s\';" % (username, password)
        self.dipendente_controller.set_info(self.db.execute(query).fetchone())
        self.dipendente = self.dipendente_controller.get_dipendente()
        return self.dipendente.iscompleto()

    def get_dipendente(self):
        return self.dipendente
