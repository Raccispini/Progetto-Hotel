from PyQt5.QtWidgets import QMainWindow
from ristorante.view.Ui_RistoranteView import Ui_RistoranteView
from ristorante.controller.RistoranteController import RistoranteController
from ristorante.view.PrenotaRistoranteView import PrenotaRistoranteView
from ristorante.view.OrdinazioniRistoranteView import OrdinazioniRistoranteView
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from threading import Timer
from datetime import datetime, timedelta

class RistoranteView(QMainWindow, Ui_RistoranteView):
    def __init__(self, parent = None):
        super(RistoranteView, self).__init__(parent)
        self.setupUi(self)
        self.controller = RistoranteController
        self.connect_all()
        self.erase_all()

    def connect_all(self):
        for push_button in self.pB_Tavoli:
            push_button.clicked.connect(lambda: self.prenota_tavolo())
        self.pB_ricerca.clicked.connect(lambda: self.ricerca_tavolo_disponibile)
        self.pB_elimina.clicked.connect(lambda: self.elimina_prenotazione)
        self.tabella_prenotazioni.itemSelectionChanged.connect(lambda: self.table_click())
        self.pB_checkout.clicked.connect(lambda: self.open_checkout())



    def open_checkout(self):
        self.checkout_window = OrdinazioniRistoranteView()
        self.checkout_window.show()

    def table_click(self):
        if len(self.tabella_prenotazioni.selectionModel().selectedRows()) > 0:
            self.pB_checkout.setEnabled(True)
            self.pB_elimina.setEnabled(True)
        else:
            self.pB_checkout.setEnabled(False)
            self.pB_elimina.setEnabled(False)

    def erase_all(self):
        self.cb_orario.setCurrentIndex(-1) #comboBox ricerca tavolo disponibile
        self.cb_orario_2.setCurrentIndex(0) #comboBox filtraggio tavoli prenotati
        self.de_data.setDate(QDate.currentDate()) #dateEdit ricerca tavolo dispobile
        self.de_data_2.setDate(QDate.currentDate()) #dateEdit filtraggio tavoli prenotati
        self.cb_tavolo.setCurrentIndex(0) #comboBox filtraggio tavoli prenotati

    def prenota_tavolo(self):
        nome_tavolo = self.sender().objectName() #Restituisce il nome del pulsante che fa partire l'azione
        self.prenota_window = PrenotaRistoranteView()
        self.prenota_window.show()