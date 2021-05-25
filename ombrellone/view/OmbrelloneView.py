from PyQt5.QtWidgets import QMainWindow
from ombrellone.view.Ui_OmbrelloniView_1 import Ui_OmbrelloniView_1


class OmbrelloneView(QMainWindow, Ui_OmbrelloniView_1):
    def __init__(self, parent = None):
        super(OmbrelloneView, self).__init__(parent)
        self.setupUi(self)