'''
__author__: Federico Pretini
'''
from datetime import datetime
from datetime import timedelta

from ristorante.view.AggiornaMenuView import AggiornaMenuView
from ristorante.view.Ui_Ristorante import Ui_RistoranteView
from ristorante.controller.RistoranteController import RistoranteController
from ristorante.view.PrenotaRistoranteView import PrenotaRistoranteView
from ristorante.view.OrdinazioniRistoranteView import OrdinazioniRistoranteView
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui


class RistoranteView(QMainWindow, Ui_RistoranteView):
    def __init__(self, dipendente, parent = None):
        super(RistoranteView, self).__init__(parent)
        self.setupUi(self)
        self.controller = RistoranteController()
        self.update_table(self.controller.get_lista_prenotazioni())
        self.dipendente = dipendente
        self.erase_all()
        self.connect_all()

    def connect_all(self):
        for push_button in self.pB_Tavoli:
            push_button.clicked.connect(lambda: self.prenota_tavolo())
        self.pB_ricerca.clicked.connect(lambda: self.ricerca_tavolo_disponibile())
        self.pB_elimina.clicked.connect(lambda: self.elimina_prenotazione())
        self.tabella_prenotazioni.itemSelectionChanged.connect(lambda: self.table_click())
        self.tabella_prenotazioni.doubleClicked.connect(lambda: self.update_table(self.controller.get_lista_prenotazioni()))
        self.pB_chiusura_conto.clicked.connect(lambda: self.open_chiusura_conto())
        self.de_data_2.dateChanged.connect(lambda: self.filtraggio_tavoli())
        self.cb_tavolo.currentIndexChanged.connect(lambda: self.filtraggio_tavoli())
        self.cb_orario_2.currentIndexChanged.connect(lambda: self.filtraggio_tavoli())
        self.pB_aggiorna_menu.clicked.connect(lambda: self.aggiorna_menu())



    def open_chiusura_conto(self):
        item = self.tabella_prenotazioni.selectedItems()
        self.chiusura_conto_window = OrdinazioniRistoranteView(self.controller, item)
        self.chiusura_conto_window.showMaximized()

    def table_click(self):

        if len(self.tabella_prenotazioni.selectionModel().selectedRows()) == 1:
            self.pB_chiusura_conto.setEnabled(True)
            self.pB_elimina.setEnabled(True)
        elif len(self.tabella_prenotazioni.selectionModel().selectedRows()) > 1:
            self.pB_chiusura_conto.setEnabled(False)
            self.pB_elimina.setEnabled(True)
        elif len(self.tabella_prenotazioni.selectionModel().selectedRows()) == 0:
            self.pB_chiusura_conto.setEnabled(False)
            self.pB_elimina.setEnabled(False)


    def erase_all(self):
        if datetime.now() > datetime.now().replace(hour=0, minute=0, second=0) and datetime.now() < datetime.now().replace(hour=14, minute=0,second=0):
            self.cb_orario.setCurrentIndex(1) #comboBox ricerca tavolo disponibile
            self.cb_orario_2.setCurrentIndex(1) #comboBox filtraggio tavoli prenotati
        elif datetime.now() >= datetime.now().replace(hour=14, minute=0, second=0) and datetime.now() < datetime.now().replace(hour=16, minute=0,second=0):
            self.cb_orario.setCurrentIndex(2)  # comboBox ricerca tavolo disponibile
            self.cb_orario_2.setCurrentIndex(2)  # comboBox filtraggio tavoli prenotati
        elif datetime.now() >= datetime.now().replace(hour=16, minute=0, second=0) and datetime.now() < datetime.now().replace(hour=21, minute=0,second=0):
            self.cb_orario.setCurrentIndex(3) #comboBox ricerca tavolo disponibile
            self.cb_orario_2.setCurrentIndex(3) #comboBox filtraggio tavoli prenotati
        elif datetime.now() > datetime.now().replace(hour=21, minute=0, second=0) and datetime.now() < datetime.now().replace(hour=0, minute=0,second=0)+ timedelta(days=1):
            self.cb_orario.setCurrentIndex(4) #comboBox ricerca tavolo disponibile
            self.cb_orario_2.setCurrentIndex(4) #comboBox filtraggio tavoli prenotati
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
            button.setStyleSheet("#" + button.objectName() +"{background-image: url(ui/resources/ristorante/tpg.png);\nborder-radius:16px;\nborder-style: outset;\nborder: 5px solid black;\nborder-style: outset;\nbackground-color: green;}\n\n"
                                 "#"+ button.objectName() + ":pressed{border-style: inset;\n border:4px solid gray;}")
            button.setEnabled(True)

        lista_prenotati = self.controller.check_tavoli_prenotati(data.toString("dd/MM/yyyy"),orario)
        for button in self.pB_Tavoli:
            for tavolo_prenotato in  lista_prenotati:
                if button.objectName() == tavolo_prenotato[1]:
                    button.setStyleSheet("#" + button.objectName() +"{background-image: url(ui/resources/ristorante/tpg.png);\nborder-radius:16px;\nborder-style: outset;\nborder: 5px solid black;\nborder-style: outset;\nbackground-color: red;}\n\n"
                                         "#"+ button.objectName() + ":pressed{border-style: inset;\n border:4px solid gray;}")
                    button.setEnabled(False)


    def update_table(self, lista):
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
        self.tabella_prenotazioni.setRowCount(0)
        i = 0
        for prenotazione in lista:
            self.tabella_prenotazioni.insertRow(i)
            j = 0
            for info in prenotazione:
                if j==5:
                    fascia_oraria = info
                    j+=1
                    continue

                elif j==6:
                    fascia_oraria += "-"+info
                    self.tabella_prenotazioni.setItem(i,j-1,get_item(fascia_oraria))
                    j+=1
                    continue
                else:
                    self.tabella_prenotazioni.setItem(i, j, get_item(info))
                    j += 1
                    continue
            i += 1


    def prenota_tavolo(self):
        nome_tavolo = self.sender().objectName() #Restituisce il nome del pulsante che fa partire l'azione
        data = self.de_data.date()
        ora = self.cb_orario.currentText().split("-")
        self.prenota_window = PrenotaRistoranteView(self.controller, self.ricerca_tavolo_disponibile, self.update_table, nome_tavolo, data, ora)
        self.prenota_window.show()

    def filtraggio_tavoli(self):
        info_filtraggio = [self.cb_tavolo.currentText(), self.de_data_2.date(), self.cb_orario_2.currentText()]
        lista_filtrata = self.controller.get_lista_prenotazioni_filtrata(info_filtraggio)
        self.update_table(lista_filtrata)

    def elimina_prenotazione(self):
        item = self.tabella_prenotazioni.selectedItems()
        lista_id = []
        contatore = 0
        for info in item:
            if contatore % 6 == 0:
                lista_id.append(info.text())
            contatore += 1
        self.controller.elimina_prenotazione(lista_id)
        self.update_table(self.controller.get_lista_prenotazioni())
        self.ricerca_tavolo_disponibile()

    def aggiorna_menu(self):
        if self.dipendente.get_permessi() == "Responsabile":
            self.aggiorna_menu_window = AggiornaMenuView(self.controller)
            self.aggiorna_menu_window.show()
        else:
            QMessageBox.critical(self, "Errore", "Spiacente, non godi dei permessi necessari per poter accedere.\nSolo i responsabili possono accedere a quest'area")