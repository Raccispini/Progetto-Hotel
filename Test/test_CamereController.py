from unittest import TestCase
from camere.controller.CamereController import CamereController

class TestCamereController(TestCase):


    def test_get_camere(self):
        options={}
        options["letti_matrimoniali"] = 10
        options["letti_singoli"] = 2
        options["allestimento"] = "Nessuno"
        options["aria_condizionata"] = True
        options["animale"] = False
        options["idromassaggio"] = False
        options["fumatori"] = True
        options["vista"] = True
        options["culla"] = True
        options["minibar"] = True
        options["cassaforte"] = True
        options["check_in"] = None
        options["check_out"] = None
        controller = CamereController()
        self.assertEqual(controller.getCamere(options),[])




    def test_get_prenotazioni(self):
        self.fail()
