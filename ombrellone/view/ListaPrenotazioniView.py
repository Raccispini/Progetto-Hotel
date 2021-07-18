'''
__author__: Federico Pretini
__author__:Alessandro Rongoni
'''
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5 import QtGui, QtCore

from camere.controller.CamereController import CamereController
from ombrellone.view.Ui_PrenotazioniOmbrellone import Ui_PrenotazioniOmbrellone


class ListaPrenotazioniView(QMainWindow, Ui_PrenotazioniOmbrellone):
    def __init__(self,controller, parent = None):
        super(ListaPrenotazioniView, self).__init__(parent)
        self.setupUi(self)
        self.controller = controller
        self.camere_controller = CamereController()
        self.lista_prenotazioni = []
        self.update_table()
        self.connect_all()


    def connect_all(self):
        self.tW_lista_ombrelloni.itemSelectionChanged.connect(lambda: self.table_click())
        self.pB_elimina.clicked.connect(lambda: self.elimina_prenotazione())

    def update_table(self):
        def get_item(info):
            item = QTableWidgetItem(str(info))
            font = QtGui.QFont()
            font.setBold(False)
            font.setFamily("Arial")
            font.setPointSize(15)
            item.setFont(font)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            return item
        self.lista_prenotazioni = self.controller.get_lista_prenotazioni()
        self.tW_lista_ombrelloni.setRowCount(0)
        i=0
        for prenotazione in self.lista_prenotazioni:
            self.tW_lista_ombrelloni.insertRow(i)
            j=0
            for info in prenotazione:
                if j==9:
                    info = str(info)+" €"
                self.tW_lista_ombrelloni.setItem(i, j, get_item(info))
                j+=1
            i+=1
    def table_click(self):
        if len(self.tW_lista_ombrelloni.selectionModel().selectedRows()) > 0:
           self.pB_elimina.setEnabled(True)
        else:
            self.pB_elimina.setEnabled(False)

    def elimina_prenotazione(self):
        item = self.tW_lista_ombrelloni.selectedItems()
        lista_numeri = []
        contatore = 0
        for info in item:
            if contatore % 10 == 0:
                lista_numeri.append(info.text())
            contatore += 1
        self.controller.elimina_prenotazione(lista_numeri)
        self.update_table()



