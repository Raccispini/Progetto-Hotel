from login.model.LoginModel import LoginModel



class LoginController(object):

    def __init__(self):
        super(LoginController, self).__init__()


    def accesso(self, username,password):
        print(username)
        print(password)
        login_model = LoginModel(username, password)
        if login_model.accedi:
           print("Main Window")
        else:
            print("errore")
