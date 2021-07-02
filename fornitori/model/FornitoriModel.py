class ModelFornitore():
    def __init__(self, id, nome, fornitura1, fornitura2, riferimento, cellulare_rif, email, indirizzo, iva, mod_pagamento, telefono, fax):
        self.id = id
        self.nome = nome
        self.fornitura1 = fornitura1
        self.fornitura2 = fornitura2
        self.riferimento = riferimento
        self.cellulare_rif = cellulare_rif
        self.email = email
        self.indirizzo = indirizzo
        self.iva = iva
        self.mod_pagamento = mod_pagamento
        self.telefono = telefono
        self.fax = fax

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_fornitura1(self):
        return self.fornitura1

    def get_fornitura2(self):
        return self.fornitura2

    def get_riferimento(self):
        return self.riferimento

    def get_cellulare_rif(self):
        return self.cellulare_rif

    def get_email(self):
        return self.email

    def get_indirizzo(self):
        return self.indirizzo

    def get_iva(self):
        return self.iva

    def get_mod_pagamento(self):
        return self.mod_pagamento

    def get_telefono(self):
        return self.telefono

    def get_fax(self):
        return self.fax

    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome

    def set_fornitura1(self, fornitura1):
        self.fornitura1 = fornitura1

    def set_fornitura2(self, fornitura2):
        self.fornitura2 = fornitura2

    def set_riferimento(self, riferimento):
        self.riferimento = riferimento

    def set_cellulare_rif(self, cellulare_rif):
        self.cellulare_rif = cellulare_rif

    def set_email(self, email):
        self.email = email

    def set_indirizzo(self, indirizzo):
        self.indirizzo = indirizzo

    def set_iva(self, iva):
        self.iva = iva

    def set_mod_pagamento(self, mod_pagamento):
        self.mod_pagamento = mod_pagamento

    def set_telefono(self, telefono):
        self.telefono = telefono

    def set_fax(self, fax):
        self.fax = fax

    def __str__(self):
        return (f"""<tr><td> {self.id}</td><td>{self.nome}</td><td>{self.fornitura1}</td><td>{self.fornitura2}</td><td>
        {self.riferimento}</td><td>{self.cellulare_rif}</td><td>{self.email}</td><td>{self.indirizzo}
        </td><td>{self.iva}</td><td>{self.mod_pagamento}</td><td>{self.telefono}</td><td>{self.fax}</td></tr>""")