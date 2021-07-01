import sqlite3
from cliente.model.ModelCliente import ModelCliente


class AnagraficheModel():
    def __init__(self):
        self.listaclienti = []
        self.listafornitori = []
        self.listadipendeti = []
        self.get_listaclienti()

    def get_listaclienti(self):
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        tab_clienti = cursor.execute('SELECT * FROM Clienti;').fetchall()
        for cliente in tab_clienti:
            self.listaclienti.append(ModelCliente(cliente[0], cliente[1], cliente[2],cliente[3], cliente[4],
                                                  cliente[5],cliente[6], cliente[7], cliente[8], cliente[9],
                                                  cliente[10], cliente[11], cliente[12], cliente[13], cliente[14],
                                                  cliente[15], cliente[16], cliente[17], cliente[18], cliente[19],
                                                  cliente[20]))

