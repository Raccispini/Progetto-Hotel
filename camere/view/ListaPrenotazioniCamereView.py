from PyQt5.QtWidgets import QMainWindow
from camere.view.Ui_ListaPrenotazioniCamereView import Ui_ListaPrenotazioniCamere
from camere.controller.CamereController import CamereController
from PyQt5 import QtWidgets
from datetime import date
class ListaPrenotazioniCamereView(QMainWindow, Ui_ListaPrenotazioniCamere):
    def __init__(self, log,parent = None):
        super(ListaPrenotazioniCamereView, self).__init__(parent)
        self.log = log
        self.setupUi(self)
        self.controller = CamereController()
        self.update_table()
        self.connect_all()

    def connect_all(self):
        self.pB_elimina.clicked.connect(lambda: self.elimina())
        self.pB_checkout.clicked.connect(lambda: self.checkout())
        self.tW_lista_prenotazioni_camere.itemSelectionChanged.connect(lambda: self.onTableClick())

    def onTableClick(self):
        if len(self.tW_lista_prenotazioni_camere.selectionModel().selectedRows()) > 0:
            self.pB_elimina.setEnabled(True)
            self.pB_checkout.setEnabled(True)
        else:
            self.pB_elimina.setEnabled(False)
            self.pB_checkout.setEnabled(False)

    def update_table(self):
        self.tW_lista_prenotazioni_camere.setRowCount(0)
        prenotazioni = self.controller.get_info_prenotazioni_da_oggi()
        print(prenotazioni)
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
        self.log.print_log_delete("eliminata prenotazione camere")
    def checkout(self):
        item = self.tW_lista_prenotazioni_camere.selectedItems()
        self.controller.check_out(item[0].text(),date.today().strftime("%d/%m/%Y"))
        self.update_table()
        self.log.print_log_delete("effettuato il checkout camera")

