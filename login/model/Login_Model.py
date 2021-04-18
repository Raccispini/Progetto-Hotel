import sqlite3

class Login_Model():
    def __init__(self):
        super(Login_Model, self).__init__()


    def is_utente(self, username, password):
        print("Sono di qua")
        connection = sqlite3.connect("../../database.db")
        print("Ho letto il db")
        database_utenti = connection.execute("SELECT * FROM Utenti")
        print("Ho trovato la tabela Utenti")
        for account in database_utenti:
            if username == str(account[0]) and password == str(account[1]):
                print("Eseguito")
                return True
            else:
                print("Non eseguito")
        return False
        connection.close()




if __name__ == '__main__':
    Og = Login_Model()
    Og.is_utente("admin", "admin")





