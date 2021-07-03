from utente.model.ModelUtente import ModelUtente

class DipendenteModel(ModelUtente):
    def __init__(self, id=0, username="", password="", nome="", cognome="", email="", cellulare="", data_di_nascita="", ambito="", permessi=""):
        super(DipendenteModel, self).__init__(id, nome, cognome, email, cellulare, data_di_nascita)
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

    def __str__(self):
        return (f"""<tr><td> {self.id}</td><td>{self.username}</td><td>{self.password}</td><td>{self.nome}</td><td>
        {self.cognome}</td><td>{self.email}</td><td>{self.cellulare}</td><td>{self.data_di_nascita}
        </td><td>{self.ambito}</td><td>{self.permessi}</td></tr>""")