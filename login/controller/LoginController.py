'''
__author__: Federico Pretini
'''
from login.model.LoginModel import LoginModel


class LoginController(object):

    def __init__(self):
        super(LoginController, self).__init__()
        self.model = LoginModel()

    def is_dipendente(self, username, password):
        return self.model.is_dipedente(username, password)

    def get_dipendente(self):
        return self.model.get_dipendente()

