'''
__author__: Federico Pretini
'''
from login.model.LoginModel import LoginModel


class LoginController(object):

    def __init__(self):
        super(LoginController, self).__init__()
        self.model = LoginModel()

    def is_utente(self, username, password):
        return self.model.is_utente(username, password)

    def get_utente(self):
        return self.model.get_utente()

