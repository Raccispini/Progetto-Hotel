import sqlite3

class Login_Model():

    @staticmethod
    def is_utente(username, password):
        connection = sqlite3.connect("database.db")
        query = "SELECT * FROM Utenti WHERE Utenti.username=\'%s\' AND Utenti.password=\'%s\';" % (username,password)
        database_utenti = connection.execute(query).fetchall()
        if database_utenti:
            return True
        else:
            return False
        connection.close()






