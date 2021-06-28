from PyQt5.QtWidgets import QMainWindow
from ombrellone.view.Ui_OmbrelloniView import Ui_OmbrelloniView


class OmbrelloneView(QMainWindow, Ui_OmbrelloniView):
    def __init__(self, parent = None):
        super(OmbrelloneView, self).__init__(parent)
        self.setupUi(self)