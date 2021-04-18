import sqlite3

class Login_Model():
    def __init__(self):
        super(Login_Model, self).__init__()


    def is_utente(self, username, password):
        print("Sono di qua")
        connection = sqlite3.connect("database.db")
        print("Ho letto il db")
        query = "SELECT * FROM Utenti WHERE Utenti.username=\'"+str(username)+"\' AND Utenti.password=\'"+password+"\';"
        database_utenti = connection.execute(query).fetchall()
        print("Ho trovato la tabela Utenti")
        if len(database_utenti) == 0:
            return False
        else:
            return True
        connection.close()




if __name__ == '__main__':
    Og = Login_Model()
    Og.is_utente("admin", "admin")





