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
        self.pB_CreaPDF_Cliente.clicked.connect(lambda: self.stampaPDF(self.controller.get_listaclienti() ,"HTML/Tabelle/tabella_clienti.html"))
        self.pB_CreaPDF_Fornitore.clicked.connect(lambda: self.stampaPDF(self.controller.get_listafornitori(),"HTML/Tabelle/tabella_fornitori.html"))
        self.pB_CreaPDF_Dipendente.clicked.connect(lambda: self.stampaPDF(self.controller.get_listadipendenti(),"HTML/Tabelle/tabella_dipendenti.html"))
        self.pB_Salva_Dipendente.clicked.connect(lambda: print("Nuovo dipendente salvato"))

    def stampaPDF(self, lista, path):
        gen = GeneratorePDF_Tabelle()
        gen.stampa(lista, path)