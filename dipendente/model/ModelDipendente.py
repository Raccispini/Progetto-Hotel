

class ModelDipendente(ModelUtente):
    def __init__(self, username, password, nome, cognome, ambito, permessi, email, cellulare, data_di_nascita):
        super(ModelDipendente, self).__init__(nome, cognome, email, cellulare, data_di_nascita)
        self.username = username
        self.password = password
        self.ambito = ambito
        self.permessi = permessi

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_ambito(self):
        return self.ambito

    def get_permessi(self):
        return self.permessi

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_ambito(self, ambito):
        self.ambito = ambito

    def set_permessi(self, permessi):
        self.permessi = permessi