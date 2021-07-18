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
        return self.model.get_extra(id_prenotazione)

    def getCamere(self,options={}):
       return self.model.getCamere(options=options)

    def get_tipo(self):
       return self.model.get_tipo()

    def get_lista_camere_prenotate(self):
        return self.model.get_lista_camere_prenotate()

    def get_camere_prenotate(self,data_inizio,data_fine):
        return self.model.get_camere_prenotate(data_inizio,data_fine)

    def add_extra(self,id):
        self.model.add_extra(id)

    def get_extra(self,id):
        return self.model.get_extra(id)

    def remove_extra(self,lista):
        self.model.remove_extra(lista)

    def getClienti(self):
        return self.model.getClienti()

    def prenota(self,check_in, check_out, data, camera, cliente_id, note=""):
        self.model.prenota(check_in, check_out, data, camera, cliente_id, note=note)

    def check_out(self,id,data):
        self.model.check_out(id,data)

    def elimina_prenotazione(self,id):
        self.model.elimina_prenotazione(id)

    def get_prenotazioni(self):
        return self.model.get_prenotazioni()


