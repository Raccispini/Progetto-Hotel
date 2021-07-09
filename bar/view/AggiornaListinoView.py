from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import QtGui, QtCore

from bar.view.Ui_AggiornaListinoView import Ui_AggiornaListinoView


class AggiornaListinoView(QMainWindow, Ui_AggiornaListinoView):
    def __init__(self,  controller, callback, parent=None):
        super(AggiornaListinoView, self).__init__(parent)
        self.setupUi(self)
        self.controller = controller
        self.callback = callback
        self.listino_bar=[]
        self.update_tableBar()
        self.update_cB_categoria()
        self.connect_all()

    def connect_all(self):
        self.pB_aggiungi.clicked.connect(lambda: self.aggiungi_consumazione())
        self.pB_elimina.clicked.connect(lambda: self.elimina_consumazione())
        self.pB_annulla.clicked.connect(lambda: self.annulla_consumazione())
        self.tableWidget_ListinoBar.itemSelectionChanged.connect(lambda: self.table_selected())

    def update_listinoBar(self):
        self.controller.update_liste()
        self.listino_bar = [self.controller.get_lista_alcolici(), self.controller.get_lista_analcolici(), self.controller.get_lista_bibite(),
                            self.controller.get_lista_caffetteria(), self.controller.get_lista_aperitivi(), self.controller.get_lista_vini(),
                            self.controller.get_lista_liquori(), self.controller.get_lista_pasticceria()]


    def update_tableBar(self):
        def get_item(info):
            item = QTableWidgetItem(str(info))
            font = QtGui.QFont()
            font.setBold(False)
            font.setFamily("Arial")
            font.setPointSize(12)
            item.setFont(font)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            return item

        self.update_listinoBar()
        self.tableWidget_ListinoBar.setRowCount(0)
        self.listino_bar.reverse()  #Aggiorna la tabella a partire dagli alcolici
        for categoria in self.listino_bar:
            i = 0
            for consumazione in categoria:
                self.tableWidget_ListinoBar.insertRow(i)
                j = 0
                for info in consumazione:
                    self.tableWidget_ListinoBar.setItem(i,j, get_item(info))
                    j+=1
                i+=1

    def update_cB_categoria(self):
        lista_categoria = set([""]) #Utlizzo il tipo set che non può avere duplicati al suo interno
        for categoria in self.listino_bar:
            for consumazione in categoria:
                lista_categoria.add(consumazione[1])
        self.cB_categoria.addItems(lista_categoria)

    def table_selected(self):
        if len(self.tableWidget_ListinoBar.selectionModel().selectedRows()) > 0:
            self.pB_elimina.setEnabled(True)
        else:
            self.pB_elimina.setEnabled(False)

    def aggiungi_consumazione(self):
        nome_consumazione = self.lineE_nome.text()
        categoria = self.cB_categoria.currentText()
        prezzo = self.spinB_prezzo.value()
        if nome_consumazione == "" or categoria == "" or prezzo == 0:
            QMessageBox.critical(self, "Errore", "Inserisci tutti i dati richiesti prima di premere aggiungi")
            return
        self.controller.aggiungi_consumazione([nome_consumazione, categoria, prezzo])
        self.callback() #Aggiorna le comboBox sull'altra interfaccia
        self.update_tableBar() #Aggiorna la lista della mio listino bar
        self.annulla_consumazione()


    def elimina_consumazione(self):
        item = self.tableWidget_ListinoBar.selectedItems()
        lista_nomi = []
        contatore = 0
        for info in item:
            if contatore%3 == 0:
              lista_nomi.append(info.text())
            contatore+=1
        self.controller.elimina_consumazione(lista_nomi)
        self.callback()
        self.update_tableBar()


    def annulla_consumazione(self):
        self.cB_categoria.setCurrentIndex(0)
        self.lineE_nome.clear()
        self.spinB_prezzo.setValue(0)









