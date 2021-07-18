import sqlite3
from datetime import date

class ModelPrenotazioni():
	@staticmethod
	def check_out(id,data):
		db = sqlite3.connect("database.db")
		query = "UPDATE Prenotazioni_camere SET check_out = '"+str(data)+"' WHERE id = "+str(id)+";"
		db.execute(query)
		db.commit()
	@staticmethod
	def elimina_prenotazione(id):
		db = sqlite3.connect("database.db")
		query = "DELETE FROM Prenotazioni_camere  WHERE Prenotazioni_camere.id = "+id+";"
		db.execute(query)
		db.commit()
	@staticmethod
	def get_prenotazioni():
		db = sqlite3.connect("database.db")
		today = date.today().strftime("%d/%m/%Y")
		query = "SELECT Prenotazioni_camere.id,Clienti.NOME,Clienti.COGNOME,Prenotazioni_camere.id_camere,Prenotazioni_camere.check_in,Prenotazioni_camere.check_out,Prenotazioni_camere.data_prenotazione,Prenotazioni_camere.costo,Prenotazioni_camere.pagamento,Prenotazioni_camere.dipendente FROM Prenotazioni_camere,Clienti WHERE Clienti.ID = Prenotazioni_camere.cliente_id AND Prenotazioni_camere.check_out > '"+ today + "';"
		return db.execute(query).fetchall()

	def __init__(self):
		pass