from PyQt5.QtWidgets import  QMainWindow
from camere.view.Ui_PrenotaCamere import  Ui_PrenotaCamere
from datetime import date
from PyQt5 import QtWidgets
from magazzino.view.ComingSoonView import ComingSoonView
from camere.controller.CamereController import CamereController


class PrenotaCamereView(QMainWindow,Ui_PrenotaCamere):
	def __init__(self,parent=None,camera_id=0,check_in=0,check_out=0):
		super(PrenotaCamereView,self).__init__(parent)
		self.setupUi(self)
		self.controller = CamereController()
		self.camera = camera_id
		self.check_in = check_in
		self.check_out = check_out
		self.update_clienti()
		self.check_prenotabile()

		self.tableWidget.itemSelectionChanged.connect(lambda: self.check_prenotabile())
		self.pB_prenota.clicked.connect(lambda: self.prenota())
		self.pB_annulla.clicked.connect(lambda: self.close())
		self.pb_aggiungi_cliente.clicked.connect(lambda: self.aggiungi_cliente())

	def aggiungi_cliente(self):
		c = ComingSoonView()
		c.show()
		#agg = AnagraficheView(dipendente=self.dipendente)
		#agg.showMaximized()

	def update_clienti(self):
		clienti = self.controller.getClienti()
		self.tableWidget.setRowCount(0)
		for i in range(len(clienti)):
			self.tableWidget.insertRow(i)
			for j in range(len(clienti[0])):
				self.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(clienti[i][j])))

	def check_prenotabile(self):
		if len(self.tableWidget.selectedItems())!=0:
			self.pB_prenota.setEnabled(True)
		else:
			self.pB_prenota.setEnabled(False)

	def prenota(self):
		now = date.today()
		print(now.strftime("%d/%m/%Y"))
		self.controller.prenota(self.check_in,self.check_out,now.strftime("%d/%m/%Y"),self.camera,self.get_selected_cliente())
		#self.update_table()
		self.close()


	def get_selected_cliente(self):
		cliente = self.tableWidget.selectedItems()
		return cliente[0].text()
