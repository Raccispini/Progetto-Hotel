from PyQt5.QtWidgets import QMainWindow
from anagrafiche.view.Ui_AnagraficheView import Ui_AnagraficheView
from GeneratorePDF_Clienti import GeneratorePDF_Clienti
from anagrafiche.controller.AnagraficheController import AnagraficheController

class AnagraficheView(QMainWindow, Ui_AnagraficheView):
    def __init__(self, parent=None):
        super(AnagraficheView, self).__init__(parent)
        self.setupUi(self)
        self.controller = AnagraficheController()
        self.connectButton()


    def connectButton(self):
        self.PB_CreaPDF.clicked.connect(lambda: self.stampaPDF())
        self.pB_Salva_Utenti.clicked.connect(lambda: print("Nuovo dipendente salvato"))

    def stampaPDF(self):
        gen = GeneratorePDF_Clienti()
        gen.stampa(self.controller.get_lista_clienti())