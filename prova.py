import sqlite3

def get_camere():
    con = sqlite3.connect("database.db")
    camere = con.execute("select * from camere")
    return camere.fetchall()

#Cerca nel database i letti con le determinate caratteristiche , nel caso dei letti prende in considerazione anche i valori superiori
def search_camere(numero=0,letti_doppi=0,letti_singoli=0,prezzo=0):
    con = sqlite3.connect("database.db")
    query= "select * from camere"
    if numero != 0 or letti_doppi != 0 or letti_singoli != 0 or prezzo != 0:
        query += " WHERE "

        if numero != 0:
            query += "numero = "+str(numero)+","
        if letti_doppi != 0:
            query += "letti_doppi >= "+str(letti_doppi)+","
        if letti_singoli != 0:
            query += "letti_singoli >= "+str(letti_singoli)+","
        if prezzo != 0:
            query += "prezzo <="+str(prezzo)+","
        query = query[:-1]
    query.join(';')
    camere = con.execute(query)
    return camere.fetchall()

def add_camera(numero,letti_singoli,letti_doppi,prezzo):
    con = sqlite3.connect('database.db')
    query = "INSERT INTO camere (numero,letti_singoli,letti_doppi,prezzo) VALUES ("+str(numero)+","+str(letti_singoli)+","+str(letti_doppi)+","+str(prezzo)+");"
    print(query)
    try:
        con.execute(query)
        con.commit()
        print("Query eseguita con successo!")
    except :
        print("Errore creazione riga")
add_camera(5,0,3,70.0)    
print(get_camere())
