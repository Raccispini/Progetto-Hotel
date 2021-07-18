from PyQt5.QtWidgets import QMainWindow
from camere.Ui.Ui_ListaPrenotazioniCamereView import Ui_ListaPrenotazioniCamere
from camere.controller.PrenotazioniController import PrenotazioniController
from PyQt5 import QtWidgets
from datetime import date
class ListaPrenotazioniCamereView(QMainWindow, Ui_ListaPrenotazioniCamere):
    def __init__(self, parent = None):
        super(ListaPrenotazioniCamereView, self).__init__(parent)
        self.setupUi(self)
        self.update_table()
        self.controller = PrenotazioniController()

        self.pB_elimina.clicked.connect(lambda: self.elimina())
        self.pB_checkout.clicked.connect(lambda: self.checkout())


    def update_table(self):
        self.tW_lista_prenotazioni_camere.setRowCount(0)
        controller = PrenotazioniController()
        prenotazioni = controller.get_prenotazioni()
        for i in range(len(prenotazioni)):
            self.tW_lista_prenotazioni_camere.insertRow(i)
            flag = False
            for j in range(len(prenotazioni[0])-1):
                if not flag:
                    self.tW_lista_prenotazioni_camere.setItem(i,j,QtWidgets.QTableWidgetItem(str(prenotazioni[i][j])))
                else:
                    self.tW_lista_prenotazioni_camere.setItem(i, j, QtWidgets.QTableWidgetItem(str(prenotazioni[i][j+1])))
                if j == 1:
                    self.tW_lista_prenotazioni_camere.setItem(i, j, QtWidgets.QTableWidgetItem(str(prenotazioni[i][j])+" "+str(prenotazioni[i][j+1])))
                    flag = True


    def elimina(self):
        item = self.tW_lista_prenotazioni_camere.selectedItems()
        self.controller.elimina_prenotazione(item[0].text())
        self.update_table()
    def checkout(self):
        item = self.tW_lista_prenotazioni_camere.selectedItems()
        self.controller.check_out(item[0].text(),date.today().strftime("%d/%m/%Y"))
        self.update_table()


