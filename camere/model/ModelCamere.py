import sqlite3


class ModelCamere():
	#options è un dict che contiene i vecchi parametri di query
	@staticmethod
	def getCamere(options,numero=-1, singoli=-1, matrimoniali=-1, check_in=None, check_out=None, tipo=-1, aria=-1, animale=-1,
				  sauna=-1, idromassaggio=-1, fumatori=-1, vista=-1, culla=-1, minibar=-1, cassaforte=-1):
		con = sqlite3.connect("database.db")
		query = "SELECT * FROM Camere WHERE"
		if options["letti_matrimoniali"] != 0:
			query += "Camere.matrimoniale >= " + str(options["letti_matrimoniali"]) + " and "
		if options["letti_singoli"] != 0:
			query += "Camere.numeroSingoli >= " + str(options["letti_singoli"]) + " and "
		if options["allestimento"] != "Nessuno":
			query += "Camere.allestimento = '" + str(options["allestimento"]) + "' and "
		if options["aria_condizionata"] :
			query += "Camere.ariaCondizionata = '" + str(options["aria_condizionata"]) + "' and "
		if options["animale"] :
			query += "Camere.animaleDomestico = " + str(animale) + " and "
		if options["idromassaggio"] :
			query += "Camere.vascaIdromassaggio = " + str(idromassaggio) + " and"
		if options["aria_condizionata"] != -1:
			query += "Camere.fumatori = " + str(fumatori) + " and "
		if vista != -1:
			query += "Camere.vistaPanoramica = " + str(vista) + " and "
		if culla != -1:
			query += "Camere.culla = " + str(culla) + " and "
		if minibar != -1:
			query += "Camere.miniBar = " + str(minibar) + " and "
		if cassaforte != -1:
			query += "Camere.cassaforte = " + str(cassaforte) + " and "
		if check_in != None or check_out != None:
			query += "Camere.numeroCamera NOT IN ( SELECT Prenotazioni_camere.numero_camera from Prenotazioni_camere WHERE NOT("
			if check_in != None and check_out != None:
				query += "Prenotazioni_camere.check_out<'" + \
						 str(check_in) + "' OR Prenotazioni_camere.check_in > '" + \
						 str(check_out) + "'))   "
			else:
				if check_in != None:
					query += "Prenotazioni_camere.check_out<'" + str(check_in) + "'"
				else:
					query += "Prenotazioni_camere.check_in>'" + str(check_out) + "'"
				query += "))   "
		query = query[:-3]
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
	def __init__(self):
		pass


