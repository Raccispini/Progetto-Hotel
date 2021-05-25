from PyQt5.QtWidgets import QMainWindow
from magazzino.view.Ui_MagazzinoView import Ui_MagazzinoView



class MagazzinoView(QMainWindow, Ui_MagazzinoView):
    def __init__(self, parent = None):
        super(MagazzinoView, self).__init__(parent)
        self.setupUi(self)
