import sqlite3
from datetime import datetime

class Log():
	def __init__(self,dipendente):
		self.dipendente = dipendente

	def print_log_add(self,descrizione):
		con = sqlite3.connect("database.db")
		lastid = con.execute("SELECT last_insert_rowid()").fetchall()[0][0]
		con.close()
		now = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
		string = now + " - Dipendente : "+ str(self.dipendente.get_id())+ ", "+ descrizione+" id : "+str(lastid)+"\n"
		file = open("Log/Log.txt","a")
		file.write(string)
		file.close()
	def print_log_delete(self,descrizione):
		now = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
		string = now + " - Dipendente : " + str(self.dipendente.get_id()) + ", " + descrizione + "\n"
		file = open("Log/Log.txt", "a")
		file.write(string)
		file.close()

