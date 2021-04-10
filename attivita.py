import sqlite3

class Attivita(object):

    #params is a dict that contains the name of the property and his type es: {'id','INT'}
    def __init__(self,nome,params):
        self.nome = nome
        self.params = params
        self.crea_tabella()
    #Create the table related to this class
    def crea_tabella(self):
        con = sqlite3.connect('database.db')
        query = "CREATE TABLE "+ str(self.nome)+ "(id INT PRIMARY KEY,"
        for i in self.params:
            query += i + self.params[i]+","
        query = query[:-1]
        query += ");"
        try:
            con.execute(query)
            print('Tabella principale creta con successo !')
        except :
            print('Errore creazione tabella principale !')

        query = 'CREATE TABLE '+str(self.nome)+'_prenotazioni (id INT PRIMARY KEY, posto_id INT, date_int DATE, date_out DATE, FOREIGN KEY(posto_id) REFERENCES '+self.nome+'(id));'
        try:
            con.execute(query)
            print('Tabella prenotazioni creata con successo !')
        except:
            print('Errore creazione tabella prenotazioni !!')

        con.commit()

        print('Creazione tabelle completata.')
    #Params is a dict that contains {'name of the parameter':'value'}
    def add_row(self,params):
        con = sqlite3.connect('database.db')
        query = 'INSERT INTO '+str(self.nome)+ '('
        for i in params:
            query += i+','
        query = query[:-1]
        query+= ') VALUES('
        for i in params:
            query += str(params[i])+','
        query = query[:-1]
        query += ');'

        print(query)
        try:
            con.execute(query)
            con.commit()
            print('Riga aggiunta con successo !')
        except :
            print('Errore aggiunta riga nella tabella!')

    def remove_row(self,id):
        con = sqlite3.connect('database.db')
        query = 'DELETE FROM '+str(self.nome)+'WHERE id == '+id+';'

        try:
            con.execute(query)
            con.commit()
            print('Query eseguita con successo !!')
        except :
            print('Errore nell\'eliminare la riga! ')
    #Params is a dict that contains the params to modify a
    def edit_row(self,params,id):
        con = sqlite3.connect('database.db')
        query = 'UPDATE '+ str(self.nome) + 'SET '
        for i in params:
            query += i + ' = ' + params[i] + ','
        query + query[:-1]
        query += 'WHERE id == '+ str(id) + ';'

        try:
            con.execute(query)
            con.commit()
            print('Modifica avvenuta con successo !')
        except :
            print('Errore modifica riga!')
            

            






