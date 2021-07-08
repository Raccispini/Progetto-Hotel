from utente.model.ModelUtente import ModelUtente

class DipendenteModel(ModelUtente):
    def __init__(self, id=0, nome="", cognome="", username="", password="",  email="", cellulare="", data_di_nascita="",
                 ambito="", permessi=""):
        super(DipendenteModel, self).__init__(id, nome, cognome, email, cellulare, data_di_nascita)
        self.username = username
        self.password = password
        self.ambito = ambito
        self.permessi = permessi

    def iscompleto(self):
        if(self.nome!="" and self.cognome!="" and self.username!="" and self.password!="" and   self.email!="" and
            self.cellulare!="" and self.data_di_nascita!="01/01/1800" and self.ambito!="" and self.permessi!=""):
            return True
        else:
            return False

    def get_info(self):
        return(self.id, self.nome, self.cognome, self.username, self.password,  self.email, self.cellulare,
               self.data_di_nascita, self.ambito, self.permessi)

    def set_info(self, info):
        self.id = info[0]
        self.nome = info[1]
        self.cognome = info[2]
        self.username = info[3]
        self.password = info[4]
        self.email = info[5]
        self.cellulare = info[6]
        self.data_di_nascita = info[7]
        self.ambito = info[8]
        self.permessi = info[9]

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