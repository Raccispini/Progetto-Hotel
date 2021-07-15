'''
__author__: Federico Pretini
'''
from bar.model.BarModel import BarModel

class BarController():
    def __init__(self):
        super(BarController, self).__init__()
        self.model = BarModel()

    def update_liste(self):
        self.model.update_liste()

    def get_lista_alcolici(self):
        return self.model.lista_alcolici

    def get_lista_analcolici(self):
        return self.model.lista_analcolici

    def get_lista_bibite(self):
        return self.model.lista_bibite

    def get_lista_caffetteria(self):
        return self.model.lista_caffetteria

    def get_lista_aperitivi(self):
        return self.model.lista_aperitivi

    def get_lista_vini(self):
        return self.model.lista_vini

    def get_lista_liquori(self):
        return self.model.lista_liquori

    def get_lista_pasticceria(self):
        return self.model.lista_pasticceria

    def get_prezzo(self, nome_consumazione):
        return self.model.get_prezzo(nome_consumazione)

    def aggiungi_consumazione(self, consumazione):
        self.model.aggiungi_consumazione(consumazione)

    def elimina_consumazione(self, lista_nomi):
        self.model.elimina_consumazione(lista_nomi)
