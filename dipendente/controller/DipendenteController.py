'''
__author__: Federico Pretini
'''
from dipendente.model.DipendenteModel import DipendenteModel


class DipendenteController():
     def __init__(self):
         self.model = DipendenteModel()

     def iscompleto(self):
         return self.model.iscompleto()

     def get_info(self):
         return self.model.get_info()

     def set_info(self, info):
         self.model.set_info(info)

     def get_dipendente(self):
         return self.model