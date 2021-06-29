import sqlite3


class LoginModel:

    def __init__(self, username, password):
        super(LoginModel, self).__init__()
        #Utente(username, password)
        self.username=username
        self.password=password
        self.is_utente()

    def is_utente(self):
        connection = sqlite3.connect("database.db")
        query = "SELECT * FROM Utenti WHERE Utenti.username=\'%s\' AND Utenti.password=\'%s\';" % (self.username, self.password)
        database_utenti = connection.execute(query).fetchall()
        connection.close()
        if database_utenti:
            return True
        else:
            return False
