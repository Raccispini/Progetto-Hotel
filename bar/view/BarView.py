from PyQt5.QtWidgets import QMainWindow
from bar.view.Ui_BarView import Ui_BarView

class BarView(QMainWindow, Ui_BarView):
    def __init__(self, parent=None):
        super(BarView, self).__init__(parent)
        self.setupUi(self)

    def closeEvent(self):
        print("Chiudi")
        







