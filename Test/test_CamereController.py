from unittest import TestCase
from camere.controller.CamereController import CamereController
from datetime import date
import sqlite3
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




    def test_get_camere_prenotate(self):
        d1 = "01/01/2000"
        d2 = "10/01/2000"
        controller = CamereController()
        self.assertEqual(controller.get_camere_prenotate(d1,d2),[])
    def test_prenotazione(self):
        check_in = "01/01/2021"
        check_out = "01/02/2021"
        data = "31/12/2020"
        camera = "10"
        cliente_id = "10"
        controller = CamereController()
        db = sqlite3.connect("database.db")
        count = len(db.execute("SELECT * FROM Prenotazioni_camere").fetchall())
        controller.prenota(check_in,check_out,data,camera,cliente_id)
        self.assertEqual(len(db.execute("SELECT * FROM Prenotazioni_camere").fetchall()),count+1)
