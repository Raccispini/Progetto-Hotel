from camere.model.ModelCamere import ModelCamere

class CamereController():
    def __init__(self):
        self.model = ModelCamere()

    def get_lista_camere(self):
        return self.model.get_lista_camere_prenotate()

    def add_extra(self, camera, prezzo, descrizione):
        self.model.add_extra(camera, prezzo, descrizione)

    def remove_extra(self, lista_id_prenotazione):
        self.model.remove_extra(lista_id_prenotazione)

    def get_extra(self, id_prenotazione):
        self.model.get_extra(id_prenotazione)



