from utente.model.ModelUtente import ModelUtente

class ClienteModel(ModelUtente):
    def __init__(self,id=0, nome="", cognome="", sesso="", data_di_nascita = "", luogo_di_nascita="", residenza="",
                 provincia="", via="", cap="", cf="", nazione="", telefono="", cellulare="", email="",
                 tipo_documento="", numero_documento="", ente_rilascio="", data_rilascio="", data_scadenza="",
                 modalita_pagamento="", info_check_in=""):
        super(ClienteModel, self).__init__(id, nome, cognome, email, cellulare, data_di_nascita)
        self.sesso = sesso
        self.luogo_di_nascita = luogo_di_nascita
        self.residenza = residenza
        self.provincia = provincia
        self.via = via
        self.cap = cap
        self.cf = cf
        self.nazione = nazione
        self.telefono = telefono
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.ente_rilascio = ente_rilascio
        self.data_rilascio = data_rilascio
        self.data_scadenza = data_scadenza
        self.modalita_pagamento = modalita_pagamento
        self.info_check_in = info_check_in

    def iscompleto(self):
        if (self.nome!="" and self.cognome!="" and self.sesso!="" and self.data_di_nascita.toString("dd/MM/yyyy")!="01/01/1800"
            and self.luogo_di_nascita!="" and self.residenza!="" and self.provincia!="" and self.via!="" and self.cap!=""
            and self.cf!="" and self.nazione!="" and self.telefono!="" and self.cellulare!=""and self.email!="" and
            self.tipo_documento!="" and self.numero_documento!="" and self.ente_rilascio!="" and self.data_rilascio.toString("dd/MM/yyyy")!="01/01/1800"
            and self.data_scadenza.toString("dd/MM/yyyy")!="01/01/1800" and self.modalita_pagamento!="" and self.info_check_in!=""):

            return True
        else:
            return False

    def get_info(self):
        return (self.id, self.nome, self.cognome, self.sesso, self.data_di_nascita, self.luogo_di_nascita, self.residenza,
                self.provincia, self.via, self.cap, self.cf, self.nazione, self.telefono, self.cellulare, self.email,
                self.tipo_documento, self.numero_documento, self.ente_rilascio, self.data_rilascio,
                self.data_scadenza, self.modalita_pagamento, self.info_check_in)


    def get_sesso(self):
        return self.sesso

    def get_luogo_di_nascita(self):
        return self.luogo_di_nascita

    def get_residenza(self):
        return self.residenza

    def get_provincia(self):
        return self.provincia

    def get_via(self):
        return self.via

    def get_cap(self):
        return self.cap

    def get_cf(self):
        return self.cf

    def get_nazione(self):
        return self.nazione

    def get_telefono(self):
        return self.telefono

    def get_tipo_documento(self):
        return self.tipo_documento

    def get_numero_documento(self):
        return self.numero_documento

    def get_ente_rilascio(self):
        return self.ente_rilascio

    def get_data_rilascio(self):
        return self.data_rilascio

    def get_data_scadenza(self):
        return self.data_scadenza

    def get_modalita_pagamento(self):
        return self.modalita_pagamento

    def get_info_checkin(self):
        return self.info_check_in

    def set_sesso(self, sesso):
        self.sesso = sesso

    def set_luogo_di_nascita(self, luogo_di_nascita):
        self.luogo_di_nascita = luogo_di_nascita

    def set_residenza(self, residenza):
        self.residenza = residenza

    def set_provincia(self, provincia):
        self.provincia = provincia

    def set_via(self, via):
        self.via = via

    def set_cap(self, cap):
        self.cap = cap

    def set_cf(self, cf):
        self.cf = cf

    def set_nazione(self, nazione):
        self.nazione = nazione

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_tipo_documento(self, tipo_documento):
        self.tipo_documento = tipo_documento

    def set_numero_documento(self, numero_documento):
        self.numero_documento = numero_documento

    def set_ente_rilascio(self, ente_rilascio):
        self.ente_rilascio = ente_rilascio

    def set_data_rilascio(self, data_rilascio):
        self.data_rilascio = data_rilascio

    def set_data_scadenza(self, data_scadenza):
        self.data_scadenza = data_scadenza

    def set_modalita_pagamento(self, modalita_pagamento):
        self.modalita_pagamento = modalita_pagamento

    def set_info_checkin(self, info_check_in):
        self.info_check_in = info_check_in

    def __str__(self):
        return (f"""<tr><td> {self.id}</td><td>{self.nome}</td><td>{self.cognome}</td><td>{self.sesso}</td><td>
        {self.data_di_nascita}</td><td>{self.luogo_di_nascita}</td><td>{self.residenza}</td><td>{self.provincia}
        </td><td>{self.via}</td><td>{self.cap}</td><td>{self.cf}</td><td>{self.nazione}</td><td> {self.telefono}
        </td><td>{self.cellulare}</td><td>{self.email}</td><td>{self.tipo_documento}</td><td>{self.numero_documento}
        </td><td>{self.ente_rilascio}</td><td>{self.data_rilascio}</td><td>{self.data_scadenza}</td><td>{self.modalita_pagamento}
        </td><td style=\"min-width:150px;\">{self.info_check_in} </td></tr>""")