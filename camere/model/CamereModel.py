import sqlite3
from datetime import date

class ModelCamere():
	def __init__(self):
		self.db = sqlite3.connect("database.db")

	def getCamere(self, options={}):
		query = "SELECT * FROM Camere "
		flag = False
		if len(options) != 0:
			query +="WHERE "
			if options["letti_matrimoniali"] != 0:
				query += "Camere.matrimoniale >= " + str(options["letti_matrimoniali"]) + " and "
				flag = True
			if options["letti_singoli"] != 0:
				query += "Camere.numeroSingoli >= " + str(options["letti_singoli"]) + " and "
				flag = True
			if options["allestimento"] != "Nessuno":
				query += "Camere.allestimento = '" + str(options["allestimento"]) + "' and "
				flag = True
			if options["aria_condizionata"] :
				query += "Camere.ariaCondizionata = " + str(options["aria_condizionata"]) + " and "
				flag = True
			if options["animale"] :
				query += "Camere.animaleDomestico = " + str(options["animale"]) + " and "
				flag = True
			if options["idromassaggio"] :
				query += "Camere.vascaIdromassaggio = " + str(options["idromassaggio"]) + " and "
				flag = True
			if options["fumatori"]:
				query += "Camere.fumatori = " + str(options["fumatori"]) + " and "
				flag = True
			if options["vista"] :
				query += "Camere.vistaPanoramica = " + str(options["vista"]) + " and "
				flag = True
			if options["culla"]:
				query += "Camere.culla = " + str(options["culla"]) + " and "
				flag = True
			if options["minibar"]:
				query += "Camere.miniBar = " + str(options["minibar"]) + " and "
				flag = True
			if options["cassaforte"] :
				query += "Camere.cassaforte = " + str(options["aria_condizionata"]) + " and "
				flag = True
			if options["check_in"] != None or options["check_out"] != None:
				query += "Camere.numeroCamera NOT IN ( SELECT Prenotazioni_camere.id_camere from Prenotazioni_camere WHERE NOT("
				flag = True
				if options["check_in"] != None and options["check_out"] != None:
					query += "Prenotazioni_camere.check_out<'" + \
							 str(options["check_in"]) + "' OR Prenotazioni_camere.check_in > '" + \
							 str(options["check_out"]) + "'))   "
				else:
					if options["check_in"] != None:
						query += "Prenotazioni_camere.check_out<'" + str(options["check_in"]) + "'"
					else:
						query += "Prenotazioni_camere.check_in>'" + str(options["check_out"]) + "'"
					query += "))   "
				query = query[:-3]
			else:
				if not flag:
					query = query[:-6]
				else:
					query = query[:-4]
		query += " ORDER BY Camere.numeroCamera;"
		return self.db.execute(query).fetchall()

	def get_tipo(self):
		query = "SELECT Camere.allestimento FROM Camere Group by Camere.allestimento "
		tipi = self.db.execute(query).fetchall()
		allestimenti = ["Nessuno"]

		for i in range(len(tipi)):
			allestimenti.append(tipi[i][0])
		return allestimenti

	def get_cliente_prenotazione(self):
		lista_prenotate = self.db.execute("SELECT Prenotazioni_camere.id_camere, Clienti.NOME, Clienti.COGNOME FROM Prenotazioni_camere, Clienti WHERE Prenotazioni_camere.cliente_id = Clienti.ID").fetchall()
		return lista_prenotate


	def get_camere_prenotate_by_date(self, data_inizio, data_fine):
		query = "SELECT Camere.numeroCamera FROM Camere,Prenotazioni_camere WHERE Camere.numeroCamera IN (SELECT Prenotazioni_camere.id_camere from Prenotazioni_camere WHERE NOT(Prenotazioni_camere.check_out<'"+data_inizio+"' OR Prenotazioni_camere.check_in>'"+data_fine+"'))"
		return self.db.execute(query).fetchall()


	def getClienti(self):
		query = "SELECT * FROM Clienti Order By Clienti.ID"
		return self.db.execute(query).fetchall()


	def prenota(self,check_in, check_out, data, camera, cliente_id, costo, dipendente, note=""):
		query = "INSERT INTO Prenotazioni_camere(id_camere,check_in,check_out,data_prenotazione,cliente_id,note,costo,dipendente) VALUES (" + str(camera) + ",'" + check_in + "','" + check_out + "','" + data + "'," + cliente_id + ",'" + note + "'," + str(costo) + "," + str(dipendente) + ");"
		self.db.execute(query)
		self.db.commit()


	def check_out(self,id, data):
		query = "UPDATE Prenotazioni_camere SET check_out = '" + data + "' WHERE id = " + id + ";"
		self.db.execute(query)
		self.db.commit()

	def elimina_prenotazione(self,id):
		query = "DELETE FROM Prenotazioni_camere  WHERE Prenotazioni_camere.id = " + id + ";"
		self.db.execute(query)
		self.db.commit()

	def get_info_prenotazione_da_oggi(self):
		today = date.today().strftime("%d/%m/%Y")
		query = "SELECT Prenotazioni_camere.id,Clienti.NOME,Clienti.COGNOME,Prenotazioni_camere.id_camere,Prenotazioni_camere.check_in,Prenotazioni_camere.check_out,Prenotazioni_camere.data_prenotazione,Prenotazioni_camere.costo, Prenotazioni_camere.dipendente FROM Prenotazioni_camere,Clienti WHERE Clienti.ID = Prenotazioni_camere.cliente_id AND Prenotazioni_camere.check_out > '" + today + "';"
		return self.db.execute(query).fetchall()
