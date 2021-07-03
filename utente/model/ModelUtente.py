class ModelUtente(object):
    def __init__(self, nome, cognome, email, cellulare, data_di_nascita):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.cellulare = cellulare
        self.data_di_nascita = data_di_nascita


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

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_email(self, email):
        self.email = email

    def set_cellulare(self, cellulare):
        self.cellulare = cellulare

    def set_data_di_nascita(self, data_di_nascita):
        self.data_di_nascita = data_di_nascita

