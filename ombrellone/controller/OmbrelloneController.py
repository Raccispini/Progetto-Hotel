from ombrellone.model.OmbrelloneModel import OmbrelloneModel

class OmbrelloneController():
    def __init__(self):
        self.model = OmbrelloneModel()

    def get_Prenotazioni(self):
        self.model.get_Prenotazioni()
        return self.model.lista_prenotati

    def get_OmbrelloniDisponibili(self, data_inizio, data_fine):
        self.model.get_OmbrelloniDisponibili(data_inizio,data_fine)
        return self.model.lista_disponibili
