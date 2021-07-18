from camere.model.ModelPrenotazioni import ModelPrenotazioni
class PrenotazioniController():
	def __init__(self):
		self.model = ModelPrenotazioni()
	def check_out(self,id,data):
		self.model.check_out(id,data)
	def elimina_prenotazione(self,id):
		self.model.elimina_prenotazione(id)
	def get_prenotazioni(self):
		return self.model.get_prenotazioni()
