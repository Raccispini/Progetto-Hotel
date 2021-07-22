'''
__author__: Federico Pretini
'''
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from anagrafiche.view.AnagraficheView import AnagraficheView
from bar.view.BarView import BarView
from camere.view.CamereView import CamereView
from home.view.Ui_HomeView import Ui_HomeView
from logout.view.LogoutView import LogoutView
from magazzino.view.MagazzinoView import MagazzinoView
from meteo.view.MeteoView import MeteoView
from ombrellone.view.OmbrelloneView import OmbrelloneView
from ristorante.view.RistoranteView import RistoranteView
from Log.Log import Log

class HomeView(QMainWindow, Ui_HomeView):
    def __init__(self, dipendente, login_window):
        super().__init__()
        self.setupUi(self)
        self.log = Log(dipendente)
        self.dipendente = dipendente
        #self.dipendente = dipendente
        self.login_window = login_window
        self.connect_button()

    def open_bar(self):
       if self.dipendente.get_ambito() == "ADMIN" or self.dipendente.get_ambito() == "Bar":
          self.bar_window = BarView(self.dipendente,self.log)
          self.bar_window.showMaximized()
       else:
           QMessageBox.critical(self, "Errore", "Le tue credenziali non permettono l'accesso a questo servizio")

    def open_camere(self):
        if self.dipendente.get_ambito() == "ADMIN" or self.dipendente.get_ambito() == "Camere":
            self.camere_window = CamereView(self.dipendente,self.log)
            self.camere_window.show()
        else:
            QMessageBox.critical(self, "Errore", "Le tue credenziali non permettono l'accesso a questo servizio")

    def open_anagrafiche(self):
        if (self.dipendente.get_ambito() == "Camere" and self.dipendente.get_permessi() == "Dipendente") or self.dipendente.get_permessi() == "Responsabile":
            self.anagrafiche_window = AnagraficheView(self.dipendente,self.log)
            self.anagrafiche_window.showMaximized()
        else:
            QMessageBox.critical(self, "Errore", "Le tue credenziali non permettono l'accesso a questo servizio")

    def open_magazzino(self):
        if self.dipendente.get_ambito() == "ADMIN" or self.dipendente.get_ambito() == "Magazzino":
           self.magazzino_window = MagazzinoView(self.log)
           self.magazzino_window.show()
        else:
            QMessageBox.critical(self, "Errore", "Le tue credenziali non permettono l'accesso a questo servizio")

    def open_meteo(self):
        self.meteo_window = MeteoView()
        self.meteo_window.show()

    def open_ombrelloni(self):
        if self.dipendente.get_ambito() == "ADMIN" or self.dipendente.get_ambito() == "Ombrelloni":
           self.ombrelloni_window = OmbrelloneView(self.log)
           self.ombrelloni_window.show()
        else:
            QMessageBox.critical(self, "Errore", "Le tue credenziali non permettono l'accesso a questo servizio")

    def open_ristorante(self):
        if self.dipendente.get_ambito() == "ADMIN" or self.dipendente.get_ambito() == "Ristorante":
           self.ristorante_window = RistoranteView(self.log,self.dipendente)
           self.ristorante_window.show()
        else:
            QMessageBox.critical(self, "Errore", "Le tue credenziali non permettono l'accesso a questo servizio")


    def open_logout(self):
        self.logout_window = LogoutView(self.login_window, self)
        self.logout_window.show()


    def connect_button(self):
        self.pB_Camere.clicked.connect(lambda: self.open_camere())
        self.pB_Anagrafiche.clicked.connect(lambda: self.open_anagrafiche())
        self.pB_Ombrelloni.clicked.connect(lambda: self.open_ombrelloni())
        self.pB_Magazzino.clicked.connect(lambda: self.open_magazzino())
        self.pB_Ristorante.clicked.connect(lambda: self.open_ristorante())
        self.pB_Bar.clicked.connect(lambda: self.open_bar())
        self.pB_Meteo.clicked.connect(lambda: self.open_meteo())
        self.pB_Uscita.clicked.connect(lambda: self.open_logout())






