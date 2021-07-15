'''
__author__: Alessandro Rongoni
'''
from PyQt5.QtWidgets import QMainWindow
from magazzino.view.Ui_MagazzinoView import Ui_MagazzinoView
from magazzino.view.ComingSoonView import ComingSoonView



class MagazzinoView(QMainWindow, Ui_MagazzinoView):
    def __init__(self, parent = None):
        super(MagazzinoView, self).__init__(parent)
        self.setupUi(self)
        self.connect_all()


    def connect_all(self):
        self.pushButton_Salva.clicked.connect(lambda: self.open_coming_soon())
        self.pushButton_Aggiungi.clicked.connect(lambda: self.open_coming_soon())
        self.pushButton_Annulla.clicked.connect(lambda: self.open_coming_soon())
        self.pushButton_StampaPDF.clicked.connect(lambda: self.open_coming_soon())
        self.pushButton_Elimina.clicked.connect(lambda: self.open_coming_soon())
        self.pushButton_Modifica.clicked.connect(lambda: self.open_coming_soon())



    def open_coming_soon(self):
        self.coming_soon_window = ComingSoonView()
        self.coming_soon_window.show()
