import sqlite3


class BarModel():
    def __init__(self):
        super(BarModel, self).__init__()
        self.db = sqlite3.connect("database.db")
        self.lista_alcolici = []
        self.lista_analcolici = []
        self.lista_bibite = []
        self.lista_caffetteria = []
        self.lista_aperitivi = []
        self.lista_vini = []
        self.lista_liquori = []
        self.lista_pasticceria = []

    def update_liste(self):
        self.lista_alcolici = self.db.execute("SELECT * FROM Bar WHERE CATEGORIA= \'Alcolici\';").fetchall()
        self.lista_analcolici = self.db.execute("SELECT * FROM Bar WHERE CATEGORIA= \'Analcolici\'").fetchall()
        self.lista_bibite = self.db.execute("SELECT * FROM Bar WHERE CATEGORIA= \'Bibite\';").fetchall()
        self.lista_caffetteria = self.db.execute("SELECT * FROM Bar WHERE CATEGORIA= \'Caffetteria\';").fetchall()
        self.lista_aperitivi = self.db.execute("SELECT * FROM Bar WHERE CATEGORIA= \'Aperitivi\';").fetchall()
        self.lista_vini = self.db.execute("SELECT * FROM Bar WHERE CATEGORIA= \'Vini\';").fetchall()
        self.lista_liquori = self.db.execute("SELECT * FROM Bar WHERE CATEGORIA= \'Liquori\';").fetchall()
        self.lista_pasticceria = self.db.execute("SELECT * FROM Bar WHERE CATEGORIA= \'Pasticceria\';").fetchall()

    def get_prezzo(self, nome_consumazione):
        prezzo = self.db.execute("SELECT PREZZO FROM Bar WHERE NOME_PRODOTTO="+"\'"+nome_consumazione+"\'"+";").fetchone()
        return int(prezzo[0])

    def aggiungi_consumazione(self, consumazione):
        query = "INSERT INTO Bar(NOME_PRODOTTO, CATEGORIA, PREZZO) VALUES (?,?,?);"
        self.db.execute(query, consumazione)
        self.db.commit()

    def elimina_consumazione(self, lista_nomi):
        for nome in lista_nomi:
            self.db.execute("DELETE FROM Bar WHERE NOME_PRODOTTO=\'"+  nome + "\';")
            self.db.commit()



