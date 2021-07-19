from unittest import TestCase
from anagrafiche.controller.AnagraficheController import AnagraficheController

class TestAnagraficheController(TestCase):
	def test_get_listaclienti(self):
		controller = AnagraficheController()
		self.assertEqual(len(controller.get_listaclienti()),19)

	def test_ricerca_cliente(self):
		info_ricerca = ['Clienti.ID',"2"]
		controller = AnagraficheController()
		self.assertEqual(len(controller.ricerca_cliente(info_ricerca)),1)

	def test_get_listadipendenti(self):
		controller = AnagraficheController()
		self.assertEqual(len(controller.get_listadipendenti()),11)

	def test_get_listafornitori(self):
		controller = AnagraficheController()
		self.assertEqual(len(controller.get_listafornitori()),10)
