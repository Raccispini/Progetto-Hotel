from PyQt5.QtWidgets import  QMainWindow
from camere.Ui.Ui_PrenotaCamere import  Ui_PrenotaCamere


class PrenotaCamereView(QMainWindow,Ui_PrenotaCamere):
	def __init__(self,parent=None,camera_id=0):
		super(PrenotaCamereView,self).__init__(parent)
		self.setupUi(self)
		self.camera = camera_id