class UserModel(Object):
    def __init__(self, username, password):
        super(Utente, self).__init__()
        self.username = username
        self.password = password


    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_username(self):
        self.username = username

    def set_password(self):
        self.password = password
