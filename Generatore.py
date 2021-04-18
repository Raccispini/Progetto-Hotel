import random
class Generatore(object):

    def genera(self,numero_camere):
        allestimento = ["bilocale","deluxe","executive","honey_moon","luxury","studio","suite","superior","trilocale","singola"]
        print("id\tallestimento\tmatrimoniale\tnumeroSingoli\tpiano\taria condizionata\tidromassaggio\tculla\tanimale\tfumatori\tminiBar\tsauna\tvista\ttavolo")
        for i in range(numero_camere):
            letti_singoli=random.randint(0,4)
            letti_matrimoniali = random.randint(0,2)
            if letti_singoli==0:
                letti_matrimoniali = random.randint(1,2)

            print(str(i+1)+"\t"+str(allestimento[random.randInt(len(allestimento))])+"\t"+str(letti_matrimoniali)+"\t"+str(letti_singoli))