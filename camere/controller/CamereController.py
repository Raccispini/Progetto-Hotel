from camere.model.ModelCamere import ModelCamere

class CamereController():
    def __init__(self):
        self.model = ModelCamere()

    def get_lista_camere(self):
        return self.model.get_lista_camere_prenotate()