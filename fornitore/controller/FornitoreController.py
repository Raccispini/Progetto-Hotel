from fornitore.model.FornitoreModel import FornitoreModel


class FornitoreController():
     def __init__(self):
         self.model = FornitoreModel()

     def iscompleto(self):
         return self.model.iscompleto()

     def get_info(self):
         return self.model.get_info()

     def set_info(self, info):
         self.model.set_info(info)

     def get_fornitore(self):
         return self.model