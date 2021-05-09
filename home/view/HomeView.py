import webbrowser
from PyQt5.QtWidgets import QMainWindow
from bar.view.BarView import BarView
from home.view.Ui_HomeWindow import Ui_HomeWindow


class HomeView(QMainWindow, Ui_HomeWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectButton()

    def openBar(self):
        self.bar_window = BarView()
        self.bar_window.show()
        self.hide()


    def connectButton(self):
        self.pB_Camere.clicked.connect(lambda: print("Finestra Camere Aperta"))
        self.pB_Anagrafiche.clicked.connect(lambda: print("Finestra Anagrafiche Aperta"))
        self.pB_Magazzino.clicked.connect(lambda: print("Finestra Magazzino Aperta"))
        self.pB_Meteo.clicked.connect(lambda: webbrowser.open("https://www.ilmeteo.it/meteo/Cagliari", new=1))
        self.pB_Ombrelloni.clicked.connect(lambda: print("Finestra Ombrelloni Aperta"))
        self.pB_Ristorante.clicked.connect(lambda: print("Finestra Ristorante Aperta"))
        self.pB_Bar.clicked.connect(lambda: self.openBar())
        self.pB_Uscita.clicked.connect(self.close)





