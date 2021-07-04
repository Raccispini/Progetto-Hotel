from anagrafiche.model.AnagraficheModel import AnagraficheModel

class AnagraficheController():
    def __init__(self):
        self.model = AnagraficheModel()

    def get_listaclienti(self):
        return self.model.listaclienti

    def get_listafornitori(self):
        return self.model.listafornitori

    def get_listadipendenti(self):
        return self.model.listadipendeti

    def add_cliente(self, cliente):
        self.model.add_cliente(cliente)

    def add_fornitore(self, fornitore):
        self.model.add_fornitore(fornitore)


