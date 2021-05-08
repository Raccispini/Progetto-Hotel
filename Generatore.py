import random
import sqlite3

class Generatore(object):

    def genera(self,numero_camere,max_plane=10):
        allestimento = ["bilocale","deluxe","executive","honey_moon","luxury","studio","suite","superior","trilocale","singola"]
        #print("id\tallestimento\tmatrimoniale\tnumeroSingoli\tpiano\taria condizionata\tidromassaggio\tculla\tanimale\tfumatori\tminiBar\tsauna\tvista\ttavolo")
        piano = 1
        query = "INSERT INTO Camere(allestimento,matrimoniale,numeroSingoli,piano,ariaCondizionata,vascaIdromassaggio,culla,animaleDomestico,fumatori,miniBar,saunaInterna,vistamPanoramica,prenotazioneTavolo,extra,prezzo) VALUES "
        for i in range(numero_camere):
            letti_singoli=random.randint(0,4)
            letti_matrimoniali = random.randint(0,2)
            if letti_singoli==0:
                letti_matrimoniali = random.randint(1,2)
            #cambio piano
            if random.randint(0,1) == 1 and piano<max_plane:
                piano +=1
            aria_condizionata = True if random.randint(0,1) == 1 else False
            idromassaggio = True if random.randint(0,1) == 1 else False
            culla = True if random.randint(0,1) == 1 else False
            animale = True if random.randint(0,1) == 1 else False
            fumatori = True if random.randint(0,1) == 1 else False
            minbar = True if random.randint(0,1) == 1 else False
            sauna = True if random.randint(0,1) == 1 else False
            vista = True if random.randint(0,1) == 1 else False
            tavolo = True if random.randint(0,1) == 1 else False
            prezzo = letti_singoli*30+letti_matrimoniali*60
            query += "(\'"+str(allestimento[random.randint(0,len(allestimento)-1)])+"\',"+str(letti_matrimoniali)+","+str(letti_singoli)+","+str(piano)+","+str(aria_condizionata)+","+str(idromassaggio)+","+str(idromassaggio)+","+str(culla)+","+str(animale)+","+str(fumatori)+","+str(minbar)+","+str(sauna)+","+str(vista)+","+str(tavolo)+","+str(prezzo)+"),"
            #print(str(i+1)+"\t"+str(allestimento[random.randint(0,len(allestimento)-1)])+"\t\t\t"+str(letti_matrimoniali)+"\t"+str(letti_singoli)+"\t"+str(piano)+"\t"+str(aria_condizionata)+"\t"+str(idromassaggio)+"\t"+str(idromassaggio)+"\t"+str(culla)+"\t"+str(animale)+"\t"+str(fumatori)+"\t"+str(minbar)+"\t"+str(sauna)+"\t"+str(vista)+"\t"+str(tavolo))
        query = query[:-1]
        return query+";"

gen = Generatore()
while 1==1:
    query = gen.genera(10)
    print(query)
    question = input("va bene come query?(Si/No) ")
    if question == 'Si' or question == 'si':
        con =sqlite3.connect('database.db')
        con.execute(query)
        con.commit()
        break
    else:
        print('Rigenero ...')










