from datetime import date,datetime

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from camere.Ui.Ui_CamereView import Ui_CamereView
from camere.model.ModelCamere import ModelCamere
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from camere.view.PrenotaCamereView import PrenotaCamereView
from camere.view.ListaPrenotazioniCamereView import ListaPrenotazioniCamereView



class CamereView(QMainWindow, Ui_CamereView):
	def __init__(self,dipendente, parent=None,):
		super(CamereView, self).__init__(parent)
		self.dipendente = dipendente
		self.setupUi(self)
		self.update_tipo()
		self.update_table()
		self.onTableClick()
		# letti
		self.spin_singoli.valueChanged.connect(lambda: self.update_table())
		self.spin_matrim.valueChanged.connect(lambda: self.update_table())
		# tipo
		self.combo_tipo.currentTextChanged.connect(lambda: self.update_table())
		# date
		#self.date_al.dateChanged.connect(lambda: self.update_table())
		#self.date_dal.dateChanged.connect(lambda: self.update_table())
		# checkbox
		self.cb_ariaCondizionata.clicked.connect(lambda: self.update_table())
		self.cb_animaledomestico.clicked.connect(lambda: self.update_table())
		self.cb_saunainterna.clicked.connect(lambda: self.update_table())
		self.cb_vascaidromassaggio.clicked.connect(lambda: self.update_table())
		self.cb_fumatori.clicked.connect(lambda: self.update_table())
		self.cb_vistapanoramica.clicked.connect(lambda: self.update_table())
		self.cb_culla_2.clicked.connect(lambda: self.update_table())
		self.cb_minibar.clicked.connect(lambda: self.update_table())
		self.cb_cassaforte.clicked.connect(lambda: self.update_table())

		self.checkBox.clicked.connect(lambda: self.attiva())
		# bottoni laterali
		# self.pb_ricerca.clicked.connect(lambda: self.update_table())
		self.pb_azzera.clicked.connect(lambda: self.azzera())
		self.pb_prenota.clicked.connect(lambda: self.prenota())
		self.pb_prenotazioni.clicked.connect(lambda: self.prenotazioni())
		self.pb_preventivo.clicked.connect(lambda: self.preventivo())

		# Eventi
		self.tabellaCamere.itemSelectionChanged.connect(lambda: self.onTableClick())
		self.date_dal.dateChanged.connect(lambda: self.on_date_dal_changed())
		self.date_al.dateChanged.connect(lambda: self.on_date_al_changed())
		self.date_dal.setDate(QDate.currentDate())
		self.date_al.setDate(QDate.currentDate())
        
	def on_date_dal_changed(self):
		d1 = self.date_dal.date().getDate()
		d2 = self.date_al.date().getDate()
		#print(d1)
		if d1 > d2 or d1 < QDate.currentDate().getDate():
			#QMessageBox.critical(self,"Errore!","L'arco di tempo non esite !! ")
			if d1 < QDate.currentDate().getDate():
				self.date_dal.setDate(QDate.currentDate())
				#QMessageBox.critical(self, "Errore!", "L'arco di tempo non esite !! ")
			self.date_al.setDate(self.date_dal.date())
		self.update_table()
	def on_date_al_changed(self):
		d1 = self.date_dal.date().getDate()
		d2 = self.date_al.date().getDate()
		# print(d1)
		if d1 > d2 or d1 < QDate.currentDate().getDate():
			if d1 < QDate.currentDate().getDate():
				#QMessageBox.critical(self, "Errore!", "L'arco di tempo non esite !! ")
				self.date_al.setDate(QDate.currentDate())
			self.date_dal.setDate(self.date_al.date())
			#self.date_al.setDate(QDate.currentDate())
		self.update_table()


	def prenota(self):
		prenotacamere = PrenotaCamereView(self,dipendente=self.dipendente, camera_id=self.getSelectedRoom(),check_in=self.QdateToDate(self.date_dal.date().getDate()),check_out=self.QdateToDate(self.date_al.date().getDate()))
		prenotacamere.show()

	def attiva(self):
		self.update_table()
		if self.checkBox.isChecked():
			self.date_al.setEnabled(False)
			self.date_dal.setEnabled(False)
		else:
			self.date_al.setEnabled(True)
			self.date_dal.setEnabled(True)

	def getSelectedRoom(self):
		items = self.tabellaCamere.selectedItems()
		return int(items[1].text())

	def onTableClick(self):
		prenotate = ModelCamere.get_camere_prenotate(self.date_dal.date().toString(), self.date_al.date().toString())
		selected = self.tabellaCamere.selectedItems()

		if len(self.tabellaCamere.selectedItems()) != 0:
			self.pb_prenota.setEnabled(True)
			self.pb_preventivo.setEnabled(True)
		else:
			self.pb_prenota.setEnabled(False)
			self.pb_preventivo.setEnabled(False)

	def prenotazioni(self):
		l = ListaPrenotazioniCamereView(self)
		l.show()

	def azzera(self):
		self.spin_singoli.setValue(0)
		self.spin_matrim.setValue(0)

		self.cb_ariaCondizionata.setChecked(False)
		self.cb_animaledomestico.setChecked(False)
		self.cb_saunainterna.setChecked(False)
		self.cb_vascaidromassaggio.setChecked(False)
		self.cb_fumatori.setChecked(False)
		self.cb_vistapanoramica.setChecked(False)
		self.cb_culla_2.setChecked(False)
		self.cb_minibar.setChecked(False)
		self.cb_cassaforte.setChecked(False)
		self.update_table()

	def update_table(self, onstart=False):
		camere = []
		options = self.check_options()
		if onstart:
			camere = ModelCamere.getCamere()
		else:
			camere = ModelCamere.getCamere(options=options)
		# print(options)
		# print(len(camere[0]))
		self.tabellaCamere.setRowCount(0)
		for i in range(0, len(camere)):
			self.tabellaCamere.insertRow(i)
			for j in range(16):
				if j > 2 and (j != 14 and j != 4 and j != 3):
					self.tabellaCamere.setItem(i, j, QtWidgets.QTableWidgetItem("Si" if camere[i][j] == 1 else "No"))
				else:
					self.tabellaCamere.setItem(i, j, QtWidgets.QTableWidgetItem(str(camere[i][j])))

	def update_tipo(self):
		allestimenti = ModelCamere.get_tipo()
		self.combo_tipo.clear()
		for i in range(len(allestimenti)):
			self.combo_tipo.addItem(allestimenti[i])

	def check_options(self):
		options = {}
		# letti
		options["letti_singoli"] = self.spin_singoli.value()
		options["letti_matrimoniali"] = self.spin_matrim.value()
		# date
		options["check_in"] = self.QdateToDate(
			self.date_dal.date().getDate()) if not self.checkBox.isChecked() else None
		options["check_out"] = self.QdateToDate(
			self.date_al.date().getDate()) if not self.checkBox.isChecked() else None
		# allestimento
		options["allestimento"] = self.combo_tipo.currentText()
		# checkbox
		options["aria_condizionata"] = True if self.cb_ariaCondizionata.isChecked() else False
		options["animale"] = True if self.cb_animaledomestico.isChecked() else False
		options["sauna"] = True if self.cb_saunainterna.isChecked() else False
		options["idromassaggio"] = True if self.cb_vascaidromassaggio.isChecked() else False
		options["fumatori"] = True if self.cb_fumatori.isChecked() else False
		options["vista"] = True if self.cb_vistapanoramica.isChecked() else False
		options["culla"] = True if self.cb_culla_2.isChecked() else False
		options["minibar"] = True if self.cb_minibar.isChecked() else False
		options["cassaforte"] = True if self.cb_cassaforte.isChecked() else False
		# print(options)
		return options

	def QdateToDate(self, qdate):
		print(qdate[0])
		return str(qdate[2]) + "/" + str(qdate[1]) + "/" + str(qdate[0])

	def preventivo(self):
		d1 = self.QdateToDate(self.date_dal.date().getDate())
		d2 = self.QdateToDate(self.date_al.date().getDate())
		# print(d1)
		item = self.tabellaCamere.selectedItems()
		msg = float(item[len(item) - 1].text()) * self.dateOffset(d1, d2)
		QMessageBox.information(self, "Preventivo", "Il preventivo della camera è " + str(msg))

	def dateOffset(self, d1, d2):
		d1 = datetime.strptime(d1, "%d/%m/%Y")
		d2 = datetime.strptime(d2, "%d/%m/%Y")
		return abs((d2 - d1).days)
