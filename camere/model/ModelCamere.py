import sqlite3


class ModelCamere():
	#options è un dict che contiene i vecchi parametri di query
	@staticmethod
	def getCamere(options={}):
		con = sqlite3.connect("database.db")
		query = "SELECT * FROM Camere "
		if len(options) != 0:
			query +="WHERE "
			if options["letti_matrimoniali"] != 0:
				query += "Camere.matrimoniale >= " + str(options["letti_matrimoniali"]) + " and "
			if options["letti_singoli"] != 0:
				query += "Camere.numeroSingoli >= " + str(options["letti_singoli"]) + " and "
			if options["allestimento"] != "Nessuno":
				query += "Camere.allestimento = " + str(options["allestimento"]) + " and "
			if options["aria_condizionata"] :
				query += "Camere.ariaCondizionata = " + str(options["aria_condizionata"]) + " and "
			if options["animale"] :
				query += "Camere.animaleDomestico = " + str(options["animale"]) + " and "
			if options["idromassaggio"] :
				query += "Camere.vascaIdromassaggio = " + str(options["idromassaggio"]) + " and "
			if options["fumatori"]:
				query += "Camere.fumatori = " + str(options["fumatori"]) + " and "
			if options["vista"] :
				query += "Camere.vistaPanoramica = " + str(options["vista"]) + " and "
			if options["culla"]:
				query += "Camere.culla = " + str(options["culla"]) + " and "
			if options["minibar"]:
				query += "Camere.miniBar = " + str(options["minibar"]) + " and "
			if options["cassaforte"] :
				query += "Camere.cassaforte = " + str(options["aria_condizionata"]) + " and "
			if options["check_in"] != None or options["check_out"] != None:
				query += "Camere.numeroCamera NOT IN ( SELECT Prenotazioni_camere.id_camere from Prenotazioni_camere WHERE NOT("
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
		query += " ORDER BY Camere.numeroCamera;"
		#print(query)
		return con.execute(query).fetchall()
	@staticmethod
	def get_tipo():
		con = sqlite3.connect("database.db")
		query = "SELECT Camere.allestimento FROM Camere Group by Camere.allestimento "
		tipi = con.execute(query).fetchall()
		allestimenti = ["Nessuno"]

		for i in range(len(tipi)):
			allestimenti.append(tipi[i][0])
		return allestimenti

	def get_lista_camere_prenotate(self):
		db = sqlite3.connect("database.db")
		lista_prenotate = db.execute("SELECT id_camera FROM Prenotazioni_camere").fetchall()
		return lista_prenotate
	def __init__(self):
		pass