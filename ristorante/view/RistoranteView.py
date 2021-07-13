from datetime import datetime

from ristorante.view.Ui_RistoranteView import Ui_RistoranteView
from ristorante.controller.RistoranteController import RistoranteController
from ristorante.view.PrenotaRistoranteView import PrenotaRistoranteView
from ristorante.view.OrdinazioniRistoranteView import OrdinazioniRistoranteView
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui


class RistoranteView(QMainWindow, Ui_RistoranteView):
    def __init__(self, parent = None):
        super(RistoranteView, self).__init__(parent)
        self.setupUi(self)
        self.controller = RistoranteController()
        self.connect_all()
        self.update_table()
        self.erase_all()

    def connect_all(self):
        for push_button in self.pB_Tavoli:
            push_button.clicked.connect(lambda: self.prenota_tavolo())
        self.pB_ricerca.clicked.connect(lambda: self.ricerca_tavolo_disponibile())
        self.pB_elimina.clicked.connect(lambda: self.elimina_prenotazione())
        self.tabella_prenotazioni.itemSelectionChanged.connect(lambda: self.table_click())
        self.pB_chiusura_conto.clicked.connect(lambda: self.open_checkout())



    def open_checkout(self):
        self.chiusura_conto_window = OrdinazioniRistoranteView()
        self.chiusura_conto_window.showMaximized()

    def table_click(self):
        if len(self.tabella_prenotazioni.selectionModel().selectedRows()) > 0:
            self.pB_chiusura_conto.setEnabled(True)
            self.pB_elimina.setEnabled(True)
        else:
            self.pB_chiusura_conto.setEnabled(False)
            self.pB_elimina.setEnabled(False)

    def erase_all(self):
        self.cb_orario.setCurrentIndex(0) #comboBox ricerca tavolo disponibile
        self.cb_orario_2.setCurrentIndex(0) #comboBox filtraggio tavoli prenotati
        self.de_data.setDate(QDate.currentDate()) #dateEdit ricerca tavolo dispobile
        self.de_data_2.setDate(QDate.currentDate()) #dateEdit filtraggio tavoli prenotati
        self.cb_tavolo.setCurrentIndex(0) #comboBox filtraggio tavoli prenotati

    def ricerca_tavolo_disponibile(self):
        data = self.de_data.date()
        orario = self.cb_orario.currentText().split("-")
        if QDate.currentDate() > data or datetime.strptime(data.toString('dd-MM-yyyy')+ " " + orario[1], '%d-%m-%Y %H:%M') < datetime.now():
            for button in self.pB_Tavoli:
                button.setEnabled(False)
            QMessageBox.critical(self,"Errore","Compila prima correttamente tutti i campi, poi premi ricerca")
            return

        for button in self.pB_Tavoli:
            button.setStyleSheet("border-color: green;")
            button.setEnabled(True)

        for button in self.pB_Tavoli:
            for tavolo_prenotato in  self.controller.check_tavoli_prenotati(data.toString("dd/MM/yyyy"),orario):
                if button.objectName() == tavolo_prenotato[0]:
                    button.setStyleSheet("background-color: red")
                    button.setEnabled(False)

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
        fascia_oraria = ""
        self.lista_prenotazioni = self.controller.get_lista_prenotazioni()
        self.tabella_prenotazioni.setRowCount(0)
        i = 0
        for prenotazione in self.lista_prenotazioni:
            self.tabella_prenotazioni.insertRow(i)
            j = 0
            for info in prenotazione:
                if j==4:
                    fascia_oraria = info
                    j+=1

                elif j==5:
                    fascia_oraria += "-"+info
                    self.tabella_prenotazioni.setItem(i,j-1,get_item(fascia_oraria))
                    j+=1

                else:
                    self.tabella_prenotazioni.setItem(i, j, get_item(info))
                    j += 1
            i += 1


    def prenota_tavolo(self):
        nome_tavolo = self.sender().objectName() #Restituisce il nome del pulsante che fa partire l'azione
        data = self.de_data.date()
        ora = self.cb_orario.currentText().split("-")
        self.prenota_window = PrenotaRistoranteView(self.controller, nome_tavolo, data, ora)
        self.prenota_window.show()