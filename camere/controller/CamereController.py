from camere.model.CamereModel import ModelCamere
"__author__: Nicolò Raccichini"

class CamereController():
    def __init__(self):
        self.model = ModelCamere()

    def getCamere(self,options={}):
       return self.model.getCamere(options=options)

    def get_tipo(self):
       return self.model.get_tipo()

    def get_cliente_prenotazione(self):
        return self.model.get_cliente_prenotazione()

    def get_camere_prenotate_by_date(self, data_inizio, data_fine):
        return self.model.get_camere_prenotate_by_date(data_inizio, data_fine)

    def getClienti(self):
        return self.model.getClienti()

    def prenota(self,check_in, check_out, data, camera, cliente_id, costo, dipendente, note=""):
        self.model.prenota(check_in, check_out, data, camera, cliente_id, costo, dipendente, note=note)

    def check_out(self,id,data):
        self.model.check_out(id,data)

    def elimina_prenotazione(self,id):
        self.model.elimina_prenotazione(id)

    def get_info_prenotazioni_da_oggi(self):
        return self.model.get_info_prenotazione_da_oggi()


