from magazzino.view.Ui_ComingSoonView import Ui_ComingSoonView
from PyQt5.QtWidgets import QDialog



class ComingSoonView(QDialog, Ui_ComingSoonView):
    def __init__(self, parent = None):
        super(ComingSoonView, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_OK.clicked.connect(lambda: self.close())
