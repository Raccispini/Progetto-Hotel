class ModelUtente(object):
    def __init__(self, id, nome, cognome, email, cellulare, data_di_nascita):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.cellulare = cellulare
        self.data_di_nascita = data_di_nascita


    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_email(self):
        return self.email

    def get_cellulare(self):
        return self.cellulare

    def get_data_di_nascita(self):
        return self.data_di_nascita

    def set_id(self, id):
        self.id = id

    def set_nome(self, nome):
        self.nome = nome

    def set_cognome(self, cognome):
        self.cognome = cognome

    def set_email(self, email):
        self.email = email

    def set_cellulare(self, cellulare):
        self.cellulare = cellulare

    def set_data_di_nascita(self, data_di_nascita):
        self.data_di_nascita = data_di_nascita

