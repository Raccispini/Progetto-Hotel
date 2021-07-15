'''
__author__: Federico Pretini
'''
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from threading import Timer
from datetime import datetime, timedelta

from ombrellone.view.ListaPrenotazioniView import ListaPrenotazioniView
from ombrellone.view.ListinoPrezziView import ListinoPrezziView
from ombrellone.view.PrenotaOmbrelloneView import PrenotaOmbrelloneView
from ombrellone.view.Ui_Ombrellone import Ui_Ombrellone
from ombrellone.controller.OmbrelloneController import OmbrelloneController


class OmbrelloneView(QMainWindow, Ui_Ombrellone):
    def __init__(self, parent = None):
        super(OmbrelloneView, self).__init__(parent)
        self.controller = OmbrelloneController()
        self.setupUi(self)
        self.connect_all()
        #self.tempo_alla_chiusura() #Funzione che mi permette di non far prenotare più nulla dopo le 20:00
        self.erase_all()


    def connect_all(self):
        for push_button in self.pB_Ombrelloni:
            push_button.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_ricerca.clicked.connect(lambda: self.ricerca_ombrellone_disponibile())
        self.pB_lista_prenotazioni.clicked.connect(lambda: self.open_lista_prenotazioni())
        self.pB_listino.clicked.connect(lambda: self.show_listino_prezzi())
        self.cB_tipo.currentIndexChanged.connect(lambda: self.cB_tipo_changed())


    def erase_all(self):
        self.cB_orario.setCurrentIndex(0)
        self.cB_tipo.setCurrentIndex(0)
        self.dE_data.setDate(QDate.currentDate())

    def cB_tipo_changed(self):
        if self.cB_tipo.currentText()=="Mezza Giornata":
            self.cB_orario.setEnabled(True)
        else:
            self.cB_orario.setCurrentIndex(0)
            self.cB_orario.setEnabled(False)


    def set_Enabled(self):
        if self.cB_tipo.currentIndex()==0:
            self.cB_orario.setEnabled(False)
            self.cB_orario.setCurrentIndex(0)
        else:
            self.cB_orario.setEnabled(True)
            self.cB_orario.setCurrentIndex(0)


    def show_listino_prezzi(self):
        self.prezzi_window = ListinoPrezziView(self.controller, self)
        self.prezzi_window.show()


    def prenota_ombrellone(self):
        nome_ombrellone = self.sender().objectName() #Restituisce il nome del pulsante che fa partire l'azione
        self.prenota_window = PrenotaOmbrelloneView( self.controller, self.ricerca_ombrellone_disponibile, nome_ombrellone,
                                                     self.dE_data.date().toString("dd/MM/yyyy") , self.cB_tipo.currentText(),
                                                     self.cB_orario.currentText(), self)
        self.prenota_window.show()

    def open_lista_prenotazioni(self):
        self.prenotazioni_window = ListaPrenotazioniView(self.controller, self)
        self.prenotazioni_window.show()


    def ricerca_ombrellone_disponibile(self):
        data = self.dE_data.date()
        tipo = self.cB_tipo.currentText()
        orario = self.cB_orario.currentText()

        if QDate.currentDate() > data or tipo == "" or (tipo == "Mezza Giornata" and orario == ""):
            for button in self.pB_Ombrelloni:
                button.setEnabled(False)
            QMessageBox.critical(self,"Errore","Compila prima correttamente tutti i campi, poi premi ricerca")
            return

        for button in self.pB_Ombrelloni:
            button.setStyleSheet("background-color: green")
            button.setEnabled(True)

        for button in self.pB_Ombrelloni:
            for ombrellone_prenotato in  self.controller.get_ombrelloni_prenotati(data.toString("dd/MM/yyyy"), tipo, orario):
                if button.objectName() == ombrellone_prenotato[0]:
                    button.setStyleSheet("background-color: red")
                    button.setEnabled(False)

    def beach_closed(self):
        for button in self.pB_Ombrelloni:
            button.setStyleSheet("background-color: red")
            button.setEnabled(False)
        self.pB_ricerca.setEnabled(False)
        self.tempo_alla_chiusura()

    def tempo_alla_chiusura(self):
        today = datetime.today()
        tomorrow = today.replace(day=today.day, hour=20, minute=00, second=00) + timedelta(days=1)
        delta_t = tomorrow - today
        delay = delta_t.total_seconds()
        t = Timer(delay, self.beach_closed)
        t.start()



