'''
__author__: Federico Pretini
'''
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5 import QtGui, QtCore

from ristorante.view.Ui_AggiornaMenuView import Ui_AggiornaMenuView


class AggiornaMenuView(QMainWindow, Ui_AggiornaMenuView):
    def __init__(self, log, controller, parent=None):
        super(AggiornaMenuView, self).__init__(parent)
        self.setupUi(self)
        self.log = log
        self.controller = controller
        self.menu_ristorante = []
        self.update_tableRistorante()
        self.update_cB_categoria()
        self.connect_all()

    def connect_all(self):
        self.pB_aggiungi.clicked.connect(lambda: self.aggiungi_piatto())
        self.pB_elimina.clicked.connect(lambda: self.elimina_piatto())
        self.pB_annulla.clicked.connect(lambda: self.annulla_piatto())
        self.tableWidget_MenuRistorante.itemSelectionChanged.connect(lambda: self.table_selected())

    def update_menu_ristorante(self):
        self.menu_ristorante = [self.controller.get_menu("Antipasti"), self.controller.get_menu("Primi"), self.controller.get_menu("Secondi"),
                                self.controller.get_menu("Contorni"), self.controller.get_menu("Dolci"), self.controller.get_menu("Bevande")]


    def update_tableRistorante(self):
        def get_item(info):
            item = QTableWidgetItem(str(info))
            font = QtGui.QFont()
            font.setBold(False)
            font.setFamily("Arial")
            font.setPointSize(12)
            item.setFont(font)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            return item

        self.update_menu_ristorante()
        self.tableWidget_MenuRistorante.setRowCount(0)
        self.menu_ristorante.reverse()  #Aggiorna la tabella a partire dagli alcolici
        for categoria in self.menu_ristorante:
            i = 0
            for piatto in categoria:
                self.tableWidget_MenuRistorante.insertRow(i)
                j = 0
                for info in piatto:
                    self.tableWidget_MenuRistorante.setItem(i,j, get_item(info))
                    j+=1
                i+=1

    def update_cB_categoria(self):
        lista_categoria = set([""]) #Utlizzo il tipo set che non può avere duplicati al suo interno
        for categoria in self.menu_ristorante:
            for piatto in categoria:
                lista_categoria.add(piatto[1])
        self.cB_categoria.addItems(lista_categoria)

    def table_selected(self):
        if len(self.tableWidget_MenuRistorante.selectionModel().selectedRows()) > 0:
            self.pB_elimina.setEnabled(True)
        else:
            self.pB_elimina.setEnabled(False)

    def aggiungi_piatto(self):
        nome_piatto = self.lineE_nome.text()
        categoria = self.cB_categoria.currentText()
        prezzo = self.spinB_prezzo.value()
        if nome_piatto == "" or categoria == "" or prezzo == 0:
            QMessageBox.critical(self, "Errore", "Inserisci tutti i dati richiesti prima di premere aggiungi")
            return
        self.controller.aggiungi_piatto([nome_piatto, categoria, prezzo])
        self.update_tableRistorante() #Aggiorna la lista della mio listino bar
        self.annulla_piatto()
        self.log.print_log_add("aggiunto piatto al menu del ristorante")


    def elimina_piatto(self):
        item = self.tableWidget_MenuRistorante.selectedItems()
        lista_nomi = []
        contatore = 0
        for info in item:
            if contatore%3 == 0:
              lista_nomi.append(info.text())
            contatore+=1
        self.controller.elimina_piatto(lista_nomi)
        self.update_tableRistorante()
        self.log.print_log_delete("eliminato piatto dal menu del ristorante")


    def annulla_piatto(self):
        self.cB_categoria.setCurrentIndex(0)
        self.lineE_nome.clear()
        self.spinB_prezzo.setValue(0)









