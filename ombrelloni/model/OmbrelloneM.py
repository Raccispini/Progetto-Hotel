class OmbrelloneM():
    def __init__(self, n_ombrellone="", costo_Intero=0, costo_Mezzo=0, prenotato=0):
        self.n_ombrellone = n_ombrellone
        self.costo_Intero = costo_Intero
        self.costo_Mezzo = costo_Mezzo
        self.prenotato = prenotato

    def get_n_Ombrellone(self):
        return self.n_ombrellone

    def get_costoIntero(self):
        return self.costo_Intero

    def get_costoMezzo(self):
        return self.costo_Mezzo

    def get_prenotato(self):
        return self.prenotato

    def set_prenotato(self, prenotato):
        self.prenotato = prenotato

class OmbrellonePrenotatoM():
    def __init__(self, n_ombrellone="", nominativo="", data_inizio="", data_fine="", tipo="", orario="", n_sedie=0, n_sdraie=0, pagamento="", costo_tot=0, prenotato=0):
        self.n_ombrellone=n_ombrellone
        self.nominativo=nominativo
        self.data_inizio=data_inizio
        self.data_fine=data_fine
        self.tipo=tipo
        self.orario=orario
        self.n_sedie=n_sedie
        self.n_sdraie=n_sdraie
        self.pagamento=pagamento
        self.costo_tot=costo_tot
        self.prenotato=prenotato

    def get_n_ombrellone(self):
        return self.n_ombrellone

    def get_nominativo(self):
        return self.nominativo

    def get_data_inizio(self):
        return self.data_inizio

    def get_date_fine(self):
        return self.data_fine

    def get_tipo(self):
        return self.tipo

    def get_orario(self):
        return self.orario

    def get_n_sedie(self):
        return self.n_sedie

    def get_n_sdraie(self):
        return self.n_sdraie

    def get_pagamento(self):
        return self.pagamento

    def get_costo_tot(self):
        return self.costo_tot

    def get_prenotato(self):
        return self.prenotato

    def set_n_ombrellone(self, n_ombrellone):
        self.n_ombrellone=n_ombrellone

    def set_nominativo(self, nominativo):
        self.nominativo = nominativo

    def set_data(self, data):
        self.data = data

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_orario(self, orario):
        self.orario = orario

    def set_n_sedie(self, n_sedie):
        self.n_sedie = n_sedie

    def set_n_sdraie(self, n_sdraie):
        self.n_sdraie = n_sdraie

    def set_pagamento(self, pagamento):
        self.pagamento = pagamento

    def set_costo_tot (self, costo_tot):
        self.costo_tot = costo_tot

    def set_prenotato(self,  prenotato):
        self.prenotato = prenotato