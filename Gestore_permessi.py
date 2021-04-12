import sqlite3
import Permessi

class Gestore_permessi(object):

    def __init__(self):
        #Costruttore
        print('Inizializzazione gestore permessi . . .')
    
    def check_permission(self,username,ambito,lv_min):
        con = sqlite3.connect('database.db')
        query = 'select Permessi.livello from Permessi WHERE Permessi.permesso IN ( select Utenti.permessi from Utenti WHERE Utenti.username = \"'+username+'\");'
        lv = con.execute(query)
        lv = lv.fetchall()[0][0]
        query = 'select Utenti.ambito from Utenti WHERE username=\"'+username+'\";'
        ambito_utente = con.execute(query).fetchall()[0][0]
        #print(ambito_utente)
        #print(lv)
        if lv == 1:
            print('Idoneo!')
            return True
        else:
            if ambito_utente == ambito and lv <= lv_min:
                print("Idoneo!")
                return True
            else:
                print("Non Idoneo!")

a = Gestore_permessi()
a.check_permission('schiavo01','bar',3)