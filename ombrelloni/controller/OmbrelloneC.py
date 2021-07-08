from ombrelloni.model.OmbrelloneM import OmbrelloneM, OmbrellonePrenotatoM
class OmbrelloneC():
    def __init__(self):
        self.model = OmbrelloneM()

    def get_n_Ombrellone(self):
        return self.model.get_n_Ombrellone()

    def get_costoIntero(self):
        return self.model.get_costoIntero()

    def get_costoMezzo(self):
        return self.model.get_costoMezzo()

    def get_prenotato(self):
        return self.model.get_prenotato()

    def set_prenotato(self, prenotato):
        self.model.set_prenotato(prenotato)

class OmbrellonePrenotatoC():
    def __init__(self):
        self.model = OmbrellonePrenotatoM()

    def get_n_ombrellone(self):
        return self.model.get_n_ombrellone()

    def get_nominativo(self):
        return self.model.get_nominativo()

    def get_data(self):
        return self.model.get_data()

    def get_tipo(self):
        return self.model.get_tipo()

    def get_orario(self):
        return self.model.get_orario()

    def get_n_sedie(self):
        return self.model.get_n_sedie()

    def get_n_sdraie(self):
        return self.model.get_n_sdraie()

    def get_pagamento(self):
        return self.model.get_pagamento()

    def get_costo_tot(self):
        return self.model.get_costo_tot()

    def get_prenotato(self):
        return self.model.get_prenotato()

    def set_n_ombrellone(self, n_ombrellone):
        self.model.set_n_ombrellone(n_ombrellone)

    def set_nominativo(self, nominativo):
        self.model.set_nominativo(nominativo)

    def set_data(self, data):
        self.model.set_data(data)

    def set_tipo(self, tipo):
        self.model.set_tipo(tipo)

    def set_orario(self, orario):
        self.model.set_orario(orario)

    def set_n_sedie(self, n_sedie):
        self.model.set_n_sedie(n_sedie)

    def set_n_sdraie(self, n_sdraie):
        self.model.set_n_sdraie(n_sdraie)

    def set_pagamento(self, pagamento):
        self.model.set_pagamento(pagamento)

    def set_costo_tot (self, costo_tot):
        self.model.set_costo_tot(costo_tot)

    def set_prenotato(self,  prenotato):
        self.model.set_prenotato(prenotato)