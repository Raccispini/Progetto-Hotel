from PyQt5.QtWidgets import QMainWindow
from anagrafiche.view.Ui_AnagraficheView import Ui_AnagraficheView
from GeneratorePDF_Tabelle import GeneratorePDF_Tabelle
from anagrafiche.controller.AnagraficheController import AnagraficheController

class AnagraficheView(QMainWindow, Ui_AnagraficheView):
    def __init__(self, parent=None):
        super(AnagraficheView, self).__init__(parent)
        self.setupUi(self)
        self.controller = AnagraficheController()
        self.connectButton()


    def connectButton(self):
        self.PB_CreaPDF_Cliente.clicked.connect(lambda: self.stampaPDF("HTML/Tabelle/tabella_clienti.html"))
        self.pB_Salva_Utenti.clicked.connect(lambda: print("Nuovo dipendente salvato"))

    def stampaPDF(self, path):
        gen = GeneratorePDF_Tabelle()
        gen.stampa(self.controller.get_lista_clienti(), path)