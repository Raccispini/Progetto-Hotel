from cliente.model.ClienteModel import ClienteModel


class ClienteController():
     def __init__(self):
         self.model = ClienteModel()

     def iscompleto(self):
         return self.model.iscompleto()

     def get_info(self):
         return self.model.get_info()

     def set_info(self, info):
         self.model.set_info(info)

     def get_cliente(self):
         return self.model