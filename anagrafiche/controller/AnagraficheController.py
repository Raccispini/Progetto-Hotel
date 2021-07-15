
'''
__author__:  Federico Pretini
'''

from anagrafiche.model.AnagraficheModel import AnagraficheModel

class AnagraficheController():
    def __init__(self):
        self.model = AnagraficheModel()

    def get_listaclienti(self):
        self.model.update_listaclienti()
        return self.model.listaclienti

    def add_cliente(self, cliente):
        self.model.add_cliente(cliente)

    def elimina_clienti(self, lista_id):
        self.model.elimina_clienti(lista_id)

    def salva_cliente(self, cliente):
        self.model.salva_cliente(cliente)

    def ricerca_cliente(self, info_ricerca):
        return  self.model.ricerca_cliente(info_ricerca)

    def get_listadipendenti(self):
        self.model.update_listadipendenti()
        return self.model.listadipendeti

    def add_dipendente(self, dipendente):
        self.model.add_dipendente(dipendente)

    def elimina_dipendenti(self, lista_id):
        self.model.elimina_dipendenti(lista_id)

    def salva_dipendente(self, dipendente):
        self.model.salva_dipendente(dipendente)

    def ricerca_dipendente(self, info_ricerca):
        return  self.model.ricerca_dipendente(info_ricerca)

    def get_listafornitori(self):
        self.model.update_listafornitori()
        return self.model.listafornitori

    def add_fornitore(self, fornitore):
        self.model.add_fornitore(fornitore)

    def elimina_fornitori(self, lista_id):
        self.model.elimina_fornitori(lista_id)

    def salva_fornitore(self, fornitore):
        self.model.salva_fornitore(fornitore)

    def ricerca_fornitore(self, info_ricerca):
        return  self.model.ricerca_fornitore(info_ricerca)






