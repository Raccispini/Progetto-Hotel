import sqlite3


def get_camere():
    con = sqlite3.connect("database.db")
    camere = con.execute("select * from camere")
    return camere.fetchall()

# Cerca nel database i letti con le determinate caratteristiche , nel caso dei letti prende in considerazione anche i valori superiori


def search_camere(numero=0, letti_doppi=0, letti_singoli=0, prezzo=0, check_in=None, check_out=None):
    con = sqlite3.connect("database.db")
    query = "select * from camere"
    if numero != 0 or letti_doppi != 0 or letti_singoli != 0 or prezzo != 0 or check_in != None or check_out != None:
        query += " WHERE "

        if numero != 0:
            query += "camere.numero = "+str(numero)+" and "
        if letti_doppi != 0:
            query += "letti_doppi >= "+str(letti_doppi)+" and "
        if letti_singoli != 0:
            query += "letti_singoli >= "+str(letti_singoli)+" and "
        if prezzo != 0:
            query += "prezzo <="+str(prezzo)+" and"
        if check_in != None or check_out != None:
            query += "camere.numero NOT IN ( SELECT prenotazioni.numero_camera from prenotazioni WHERE NOT("
            if check_in != None and check_out != None:
                query += "prenotazioni.check_out<'" + \
                    str(check_in)+"' OR prenotazioni.check_in > '" + \
                    str(check_out)+"'))   "
            else:
                if check_in != None:
                    query += "prenotazioni.check_out<'"+str(check_in)+"'"
                else:
                    query += "prenotazioni.check_in>'"+str(check_out)+"'"
                query += "))   "
        query = query[:-3]
    query += " ORDER BY camere.numero;"
    print(query)
    camere = con.execute(query)
    return camere.fetchall()


def add_camera(numero, letti_singoli, letti_doppi, prezzo):
    con = sqlite3.connect('database.db')
    query = "INSERT INTO camere (numero,letti_singoli,letti_doppi,prezzo) VALUES ("+str(
        numero)+","+str(letti_singoli)+","+str(letti_doppi)+","+str(prezzo)+");"
    # print(query)
    try:
        con.execute(query)
        con.commit()
        print("Query eseguita con successo!")
    except:
        print("Errore creazione riga")


def print_table(table):
    print("________________________________________________________________")
    print("|\t\t|\t\t|\t\t|\t\t|")
    print("|    numero\t| letti singoli\t|  letti doppi\t|     prezzo\t|")
    print("|\t\t|\t\t|\t\t|\t\t|")
    print("________________________________________________________________")

    for i in range(len(table)):
        print("|\t\t|\t\t|\t\t|\t\t|")
        print("|\t"+str(table[i][0])+"\t|\t"+str(table[i][1]) +
              "\t|\t"+str(table[i][2])+"\t|\t"+str(table[i][3])+"\t|")
        # print(table[i][0])
    print("|\t\t|\t\t|\t\t|\t\t|")
    print("________________________________________________________________")


def prenota(camera, check_in, check_out):
    con = sqlite3.connect("database.db")
    if len(search_camere(numero=camera, check_in=check_in, check_out=check_out)) > 0:
        query = "INSERT INTO prenotazioni(numero_camera,check_in,check_out) VALUES ("+str(
            camera)+",'"+str(check_in)+"','"+str(check_out)+"');"
        print(query)
        con.execute(query)
        con.commit()
    else:
        print("Camera non disponibile!")


#add_camera(5, 0, 3, 70.0)
#print(search_camere(check_in="2021-03-10", check_out="2021-03-15"))
check_in = "2021-03-10"
check_out = "2021-03-15"
print_table(search_camere(check_in=check_in,check_out=check_out, letti_singoli=1))
#prenota(3, check_in, check_out)
