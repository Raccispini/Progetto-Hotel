from PyQt5.QtWidgets import QMainWindow
from anagrafiche.view.Ui_AnagraficheView import Ui_AnagraficheView

class AnagraficheView(QMainWindow, Ui_AnagraficheView):
    def __init__(self, parent=None):
        super(AnagraficheView, self).__init__(parent)
        self.setupUi(self)
