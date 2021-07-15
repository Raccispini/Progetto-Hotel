'''
__author__: Federico Pretini
'''
from ombrellone.model.OmbrelloneModel import OmbrelloneModel

class OmbrelloneController():
    def __init__(self):
        self.model = OmbrelloneModel()

    def get_ombrelloni_prenotati(self, data, tipo, orario):
        return self.model.get_ombrelloni_prenotati(data, tipo, orario)

    def get_lista_prenotazioni(self):
        return self.model.get_lista_prenotazioni()

    def elimina_prenotazione(self, lista_numeri):
        self.model.elimina_prenotazione(lista_numeri)

    def prenota_ombrellone(self, info):
        self.model.prenota_ombrellone(info)

    def get_listino_prezzi(self, nome_ombrellone):
        return self.model.get_listino_prezzi(nome_ombrellone)
