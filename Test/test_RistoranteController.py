from unittest import TestCase
from ristorante.controller.RistoranteController import RistoranteController

class TestRistoranteController(TestCase):

	def test_get_lista_prenotazioni(self):
		controller = RistoranteController()
		self.assertEqual(len(controller.get_lista_prenotazioni().fetchall()),12)
