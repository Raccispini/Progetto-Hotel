from camere.model.ModelCamere import ModelCamere

class CamereController():
    def __init__(self):
        self.model = ModelCamere()

    def get_lista_camere(self):
        return self.model.get_lista_camere_prenotate()

    def update_extra(self, extra, numero_camera):
        self.model.update_extra(extra, numero_camera)