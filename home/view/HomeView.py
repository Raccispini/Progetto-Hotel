from PyQt5.QtWidgets import QMainWindow

from anagrafiche.view.AnagraficheView import AnagraficheView
from bar.view.BarView import BarView
from camere.view.CamereView import CamereView
from home.view.Ui_HomeView import Ui_HomeView
from magazzino.view.MagazzinoView import MagazzinoView
from meteo.view.MeteoView import MeteoView
from ombrellone.view.OmbrelloneView import OmbrelloneView
from ristorante.view.RistoranteView import RistoranteView


class HomeView(QMainWindow, Ui_HomeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connect_button()

    def open_bar(self):
       self.bar_window = BarView()
       self.bar_window.showMaximized()

    def open_camere(self):
        self.camere_window = CamereView()
        self.camere_window.show()

    def open_anagrafiche(self):
        self.anagrafiche_window = AnagraficheView()
        self.anagrafiche_window.showMaximized()

    def open_magazzino(self):
        self.magazzino_window = MagazzinoView()
        self.magazzino_window.show()

    def open_meteo(self):
        self.meteo_window = MeteoView()
        self.meteo_window.show()

    def open_ombrelloni(self):
        self.ombrelloni_window = OmbrelloneView()
        self.ombrelloni_window.show()

    def open_ristorante(self):
        self.ristorante_window = RistoranteView()
        self.ristorante_window.show()

    def connect_button(self):
        self.pB_Camere.clicked.connect(lambda: self.open_camere())
        self.pB_Anagrafiche.clicked.connect(lambda: self.open_anagrafiche())
        self.pB_Magazzino.clicked.connect(lambda: self.open_magazzino())
        self.pB_Meteo.clicked.connect(lambda: self.open_meteo())
        self.pB_Ombrelloni.clicked.connect(lambda: self.open_ombrelloni())
        self.pB_Ristorante.clicked.connect(lambda: self.open_ristorante())
        self.pB_Bar.clicked.connect(lambda: self.open_bar())
        self.pB_Uscita.clicked.connect(lambda: self.close())





