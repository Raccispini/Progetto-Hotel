'''
__author__: Federico Pretini
'''
from ristorante.model.RistoranteModel import RistoranteModel

class RistoranteController():
    def __init__(self):
        self.model = RistoranteModel()


    def prenota_tavolo(self, info_prenotazione):
        self.model.prenota_tavolo(info_prenotazione)

    def check_tavoli_prenotati(self, data, orario):
        return self.model.check_tavoli_prenotati(data, orario)

    def get_lista_prenotazioni(self):
        return self.model.get_lista_prenotazioni()

    def get_lista_prenotazioni_filtrata(self, info_filtraggio):
        return self.model.get_lista_prenotazioni_filtrata(info_filtraggio)

    def elimina_prenotazione(self, lista_id):
        self.model.elimina_prenotazione(lista_id)

    def get_menu(self, categoria):
        return self.model.get_menu(categoria)

    def get_prezzo(self, nome_piatto):
        return self.model.get_prezzo_piatto(nome_piatto)

    def aggiungi_piatto(self, piatto):
        self.model.aggiungi_piatto(piatto)

    def elimina_piatto(self, lista_nomi):
        self.model.elimina_piatto(lista_nomi)
