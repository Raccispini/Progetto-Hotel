'''
__author__: Federico Pretini
'''
class FornitoreModel():
    def __init__(self, id=0, nome="", fornitura1="", fornitura2="", iva="", riferimento="", cellulare_rif="",
                 indirizzo="", telefono="", email="", mod_pagamento="", fax=""):
        self.id = id
        self.nome = nome
        self.fornitura1 = fornitura1
        self.fornitura2 = fornitura2
        self.iva = iva
        self.riferimento = riferimento
        self.cellulare_rif = cellulare_rif
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.email = email
        self.mod_pagamento = mod_pagamento
        self.fax = fax

    def iscompleto(self):
        if (self.nome!="" and self.fornitura1!="" and self.fornitura2!="" and self.iva!="" and self.riferimento!="" and
            self.cellulare_rif!="" and self.indirizzo!="" and self.telefono!="" and self.email!=""  and  self.mod_pagamento!=""
            and self.fax!=""):
            return True
        else:
            return False

    def get_info(self):
        return(self.id, self.nome, self.fornitura1, self.fornitura2,  self.iva, self.riferimento, self.cellulare_rif,
               self.indirizzo, self.telefono, self.email, self.mod_pagamento,  self.fax)

    def set_info(self, info):
        self.id = info[0]
        self.nome = info[1]
        self.fornitura1 = info[2]
        self.fornitura2 = info[3]
        self.iva = info[4]
        self.riferimento = info[5]
        self.cellulare_rif = info[6]
        self.indirizzo = info[7]
        self.telefono = info[8]
        self.email = info[9]
        self.mod_pagamento = info[10]
        self.fax = info[11]


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