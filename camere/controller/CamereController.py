from camere.model.ModelCamere import ModelCamere
"__author__: Nicolò Raccichini"

class CamereController():
    def __init__(self):
        self.model = ModelCamere()

    def get_lista_camere(self):
        return self.model.get_lista_camere_prenotate()

    def get_prenotazioni(self):
        return self.model.get_prenotazioni()

    def getCamere(self,options={}):
       return self.model.getCamere(options=options)

    def get_tipo(self):
       return self.model.get_tipo()

    def get_lista_camere_prenotate(self):
        return self.model.get_lista_camere_prenotate()

    def get_camere_prenotate(self,data_inizio,data_fine):
        return self.model.get_camere_prenotate(data_inizio,data_fine)

    def getClienti(self):
        return self.model.getClienti()

    def prenota(self,check_in, check_out, data, camera, cliente_id, costo, dipendente, note=""):
        self.model.prenota(check_in, check_out, data, camera, cliente_id, costo, dipendente, note=note)

    def check_out(self,id,data):
        self.model.check_out(id,data)

    def elimina_prenotazione(self,id):
        self.model.elimina_prenotazione(id)

    def get_prenotazioni(self):
        return self.model.get_prenotazioni()


