from ristorante.model.RistoranteModel import RistoranteModel

class RistoranteController():
    def __init__(self):
        self.model = RistoranteModel()


    def prenota_tavolo(self, info_prenotazione):
        self.model.prenota_tavolo(info_prenotazione)

    def check_tavoli_prenotati(self, data, orario):
        return self.model.get_tavoli_prenotati(data, orario)

    def get_lista_prenotazioni(self):
        return self.model.get_lista_prenotazioni()