'''
__author__: Federico Pretini
'''
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import QtGui, QtCore
from GeneratoreScontriniBar import GeneratoreScontriniBar
from bar.controller.BarController import BarController
from bar.view.AggiornaListinoView import AggiornaListinoView
from bar.view.Ui_BarView import Ui_BarView


class BarView(QMainWindow, Ui_BarView):
    def __init__(self, dipendente):
        super().__init__()
        self.setupUi(self)
        self.controller = BarController()
        self.dipendente = dipendente
        self.lista_consumazioni = []
        self.totale = 0
        self.update_cB()
        self.connect_all()
        self.update_totale()

    def update_cB(self):
        self.controller.update_liste() #Aggiorno tutte le liste
        nomi_alcolici = self.get_nomi(self.controller.get_lista_alcolici())
        self.cB_alcolici.clear()
        self.cB_alcolici.addItems(nomi_alcolici) #Aggiungo alla comboBox i nomi
        nomi_analcolici = self.get_nomi(self.controller.get_lista_analcolici())
        self.cB_analcolici.clear()
        self.cB_analcolici.addItems(nomi_analcolici)  # Aggiungo alla comboBox i nomi
        nomi_bibite = self.get_nomi(self.controller.get_lista_bibite())
        self.cB_bibite.clear()
        self.cB_bibite.addItems(nomi_bibite)  # Aggiungo alla comboBox i nomi
        nomi_caffetteria = self.get_nomi(self.controller.get_lista_caffetteria())
        self.cB_caffetteria
        self.cB_caffetteria.addItems(nomi_caffetteria)  # Aggiungo alla comboBox i nomi
        nomi_aperitivi = self.get_nomi(self.controller.get_lista_aperitivi())
        self.cB_aperitivi.clear()
        self.cB_aperitivi.addItems(nomi_aperitivi)  # Aggiungo alla comboBox i nomi
        nomi_vini = self.get_nomi(self.controller.get_lista_vini())
        self.cB_vini.clear()
        self.cB_vini.addItems(nomi_vini)  # Aggiungo alla comboBox i nomi
        nomi_liquori = self.get_nomi(self.controller.get_lista_liquori())
        self.cB_liquori.clear()
        self.cB_liquori.addItems(nomi_liquori)  # Aggiungo alla comboBox i nomi
        nomi_pasticceria = self.get_nomi(self.controller.get_lista_pasticceria())
        self.cB_pasticceria
        self.cB_pasticceria.addItems(nomi_pasticceria)  # Aggiungo alla comboBox i nomi

    def get_nomi(self, lista_bar):
        lista_nomi = [""]
        for elemento in lista_bar:
            lista_nomi.append(elemento[0])  # salvo dentro una lista ogni nome di ogni elemento della lista bar passata
        return lista_nomi

    #Collego tutte le azioni da svolgere in caso di click con i bottoni
    def connect_all(self):
        self.pB_alcolici.clicked.connect(lambda: self.aggiungi_clicked(self.cB_alcolici.currentText(),self.sB_alcolici.value()))
        self.pB_analcolici.clicked.connect(lambda: self.aggiungi_clicked(self.cB_analcolici.currentText(), self.sB_analcolici.value()))
        self.pB_bibite.clicked.connect(lambda: self.aggiungi_clicked(self.cB_bibite.currentText(), self.sB_bibite.value()))
        self.pB_caffetteria.clicked.connect(lambda: self.aggiungi_clicked(self.cB_caffetteria.currentText(), self.sB_caffetteria.value()))
        self.pB_aperitivi.clicked.connect(lambda: self.aggiungi_clicked(self.cB_aperitivi.currentText(), self.sB_aperitivi.value()))
        self.pB_vini.clicked.connect(lambda: self.aggiungi_clicked(self.cB_vini.currentText(), self.sB_vini.value()))
        self.pB_liquori.clicked.connect(lambda: self.aggiungi_clicked(self.cB_liquori.currentText(), self.sB_liquori.value()))
        self.pB_pasticceria.clicked.connect(lambda: self.aggiungi_clicked(self.cB_pasticceria.currentText(), self.sB_pasticceria.value()))

        self.pB_elimina.clicked.connect(lambda: self.elimina_consumazione())
        self.pB_salva.clicked.connect(lambda: self.get_scontrino())
        self.pB_aggiorna_listino.clicked.connect(lambda: self.open_aggiornalistino())
        self.tableWidget_Scontrino.itemSelectionChanged.connect(lambda : self.table_clicked())

    #Dato un nome e una quantità aggiorno la lista da aggiungere alla tableWidget
    def aggiungi_clicked(self, nome_consumazione, quantita):
        if quantita == 0 or nome_consumazione=="":
            QMessageBox.warning(self,"Attenzione","Non hai inserito una quantità oppure un nome.\nPer favore ritenta inserendo correttamente i dati", QMessageBox.Ok, QMessageBox.Ok)
            return

        prezzo_singolo = self.controller.get_prezzo(nome_consumazione)
        TOT = prezzo_singolo * quantita
        info_consumazione = [nome_consumazione, quantita, prezzo_singolo, TOT]

        if self.lista_consumazioni == []:
            self.lista_consumazioni.append(info_consumazione)
            self.pB_salva.setEnabled(True)
            self.update_totale()
            self.update_table()
            return
        else:
            for index in range (0,len(self.lista_consumazioni)):
                if self.lista_consumazioni[index][0] == info_consumazione[0]:
                    self.lista_consumazioni[index][1] += info_consumazione[1]
                    self.lista_consumazioni[index][3] += info_consumazione[3]
                    self.pB_salva.setEnabled(True)
                    self.update_totale()
                    self.update_table()
                    return

        self.lista_consumazioni.append(info_consumazione)  # Se la lista non era inizialmente vuota e la consumazione non
                                                           # era già presente nella lista allora l'aggiungo semplicemente
        self.pB_salva.setEnabled(True)
        self.update_totale()
        self.update_table()


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
        self.tableWidget_Scontrino.setRowCount(0)
        i=0
        for consumazione in self.lista_consumazioni:
            self.tableWidget_Scontrino.insertRow(i)
            j=0
            for info in consumazione:
                if j==2 or j==3:  #Se l'indice è su prezzo oppure su totale aggiungo alla stringa il simbolo €
                     info = str(info) + " €"
                self.tableWidget_Scontrino.setItem(i, j, get_item(info))
                j+=1
            i+=1


    def table_clicked(self):
        if len(self.tableWidget_Scontrino.selectionModel().selectedRows()) > 0:
            self.pB_elimina.setEnabled(True)
        else:
            self.pB_elimina.setEnabled(False)

    def elimina_consumazione(self):
        indexes = self.tableWidget_Scontrino.selectionModel().selectedRows()
        i=0
        for index in sorted(indexes):
            self.lista_consumazioni.pop(index.row()-i) #-i perchè ogni volta che elimino una consumazione l'indice
                                                       # dell'altra consumazione da eliminare diminuisce di uno
            i+=1
        if self.lista_consumazioni == []:
            self.pB_salva.setEnabled(False)
        self.update_totale()
        self.update_table()

    def update_totale(self):
        self.totale = 0
        for consumazione in self.lista_consumazioni:
            self.totale += consumazione[3]
        self.lineE_totale.setText(str(self.totale)+' €')

    def get_scontrino(self):
        if self.cB_metodopagamento.currentText() != "":
            scontrino = GeneratoreScontriniBar()
            scontrino.stampa(self.lista_consumazioni, self.totale, self.cB_metodopagamento.currentText())
            self.annulla()
            QMessageBox.information(self,"Informazione", "Nella cartella PDF/ScontriniBar è\nstato aggiunto un nuovo scontrino", QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Errore", "Seleziona prima un metodo di pagamento idoneo", QMessageBox.Ok, QMessageBox.Ok)

    def open_aggiornalistino(self):
        if self.dipendente.is_responsabile():
            self.aggiornalistino_window = AggiornaListinoView(self.controller, self.update_cB, self)
            self.aggiornalistino_window.show()
        else:
            QMessageBox.critical(self, "Errore", "Non godi dei permessi necessari per poter accedere.\nSolo i responsabili possono accedere a questa funzione.",QMessageBox.Ok,QMessageBox.Ok)

    def annulla(self):
        self.lista_consumazioni = []
        self.update_table()













