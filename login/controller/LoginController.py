from login.model.LoginModel import LoginModel


class LoginController(object):

    def __init__(self):
        super(LoginController, self).__init__()

    def accesso(self, username, password):
        model = LoginModel(username, password)
        return model.is_utente()
