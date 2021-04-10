class Sezione(object):
    #attivita e' un array di attivita
    def __init__(self,nome,descrizione=None,attivita=None):
        self.nome = nome
        self.descrizione = descrizione
        self.attivita = attivita

    def add_attivita(self,attivita):
        self.attivita.append(attivita)

    def remove_attivita(self,nome):
        for i in range(len(self.attivita)):
            if self.attivita[i].nome == nome:
                self.attivita.remove(i)

    def print_activities(self):
        for i in range(len(self.attivita)):   
            print(str(i+1)+") "+str(self.attivita[i].nome))