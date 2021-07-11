import sqlite3
class ModelPrenotaCamere:
	def __init__(self):
		pass
	@staticmethod
	def getClienti():
		con = sqlite3.connect("database.db")
		query = "SELECT * FROM Clienti Order By Clienti.ID"
		#con.close()
		return con.execute(query).fetchall()
	@staticmethod
	def prenota(check_in,check_out,data,camera):
		con = sqlite3.connect("database.db")
		query = "INSERT INTO Prenotazioni_camere(id_camere,check_in,check_out,data_prenotazione) VALUES ("+str(camera)+",'"+str(check_in)+"','"+str(check_out)+"','"+str(data)+"');"
		con.execute(query)
		con.commit()



		