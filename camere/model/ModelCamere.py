import sqlite3


class ModelCamere():
	#options è un dict che contiene i vecchi parametri di query
	@staticmethod
	def getCamere(options={}):
		con = sqlite3.connect("database.db")
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
				query += "Camere.allestimento = " + str(options["allestimento"]) + " and "
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
		print(query)
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
		lista_prenotate = db.execute("SELECT Prenotazioni_camere.id_camere, Clienti.NOME, Clienti.COGNOME FROM Prenotazioni_camere, Clienti WHERE Prenotazioni_camere.cliente_id = Clienti.ID").fetchall()
		return lista_prenotate

	def update_extra(self, extra, numero_camera):
		db = sqlite3.connect("database.db")
		query = "SELECT extra FROM Camere WHERE numeroCamera=\'" + numero_camera + "\';"
		old_extra = db.execute(query).fetchone()[0]
		new_extra = old_extra + extra
		query = "UPDATE Camere SET extra = (?)  WHERE numeroCamera = \'"+ numero_camera + "\';"
		db.execute(query, new_extra)
		db.commit()
	@staticmethod
	def get_camere_prenotate(data_inizio,data_fine):
		db = sqlite3.connect("database.db")
		query = "SELECT Camere.numeroCamera FROM Camere,Prenotazioni_camere WHERE Camere.numeroCamera IN (SELECT Prenotazioni_camere.id_camere from Prenotazioni_camere WHERE NOT(Prenotazioni_camere.check_out<'"+data_inizio+"' OR Prenotazioni_camere.check_in>'"+data_fine+"'))"




	def __init__(self):
		pass