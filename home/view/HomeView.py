from PyQt5.QtWidgets import QMainWindow
from bar.view.BarView import BarView
from home.view.Ui_HomeWindow import Ui_HomeWindow
from magazzino.view.MagazzinoView import MagazzinoView
from meteo.view.MeteoView import MeteoView
from ombrellone.view.OmbrelloneView import OmbrelloneView
from ristorante.view.RistoranteView import RistoranteView


class HomeView(QMainWindow, Ui_HomeWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectButton()

    def openBar(self):
        self.bar_window = BarView()
        self.bar_window.show()

    def openCamere(self):
        self.camere_window = CamereView()
        self.camere_window.show()
        print("Finestra Camere Aperta")

    def openAnagrafiche(self):
        #self.anagrafiche_window = AnagraficheView()
        #self.anagrafiche_window.show()
        print("Finestra Anagrafiche Aperta")

    def openMagazzino(self):
        self.magazzino_window = MagazzinoView()
        self.magazzino_window.show()

    def openMeteo(self):
        self.meteo_window = MeteoView()
        self.meteo_window.show()

    def openOmbrelloni(self):
        self.ombrelloni_window = OmbrelloneView()
        self.ombrelloni_window.show()

    def openRistorante(self):
        self.ristorante_window = RistoranteView()
        self.ristorante_window.show()





    def connectButton(self):
        self.pB_Camere.clicked.connect(lambda: self.openCamere())
        self.pB_Anagrafiche.clicked.connect(lambda: self.openAnagrafiche())
        self.pB_Magazzino.clicked.connect(lambda: self.openMagazzino())
        self.pB_Meteo.clicked.connect(lambda: self.openMeteo())
        self.pB_Ombrelloni.clicked.connect(lambda: self.openOmbrelloni())
        self.pB_Ristorante.clicked.connect(lambda: self.openRistorante())
        self.pB_Bar.clicked.connect(lambda: self.openBar())
        self.pB_Uscita.clicked.connect(lambda: self.close())





