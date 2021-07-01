from anagrafiche.model.AnagraficheModel import AnagraficheModel

class AnagraficheController():
    def __init__(self):
        self.model = AnagraficheModel()

    def get_lista_clienti(self):
        return self.model.listaclienti


