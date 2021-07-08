from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow
from ombrellone.view.Ui_OmbrelloneView import Ui_OmbrelloneView
from ombrellone.view.Ui_ListinoOmbrellone import Ui_ListinoOmbrelloneView
from ombrellone.view.Ui_PrenotaOmbrellone import Ui_PrenotaOmbrelloneView
from ombrellone.view.Ui_PrenotazioniOmbrellone import Ui_PrenotazioniOmbrelloneView
from ombrellone.controller.OmbrelloneController import OmbrelloneController
from PyQt5 import QtWidgets
#################### SETUP LISTINO PREZZI OMBRELLONI #######################################
class ListinoOmbrelloneView(QMainWindow, Ui_ListinoOmbrelloneView):
    def __init__(self, parent = None):
        super(ListinoOmbrelloneView, self).__init__(parent)
        self.setupUi(self)




############### SETUP LISTA PRENOTAZIONI OMBRELLONI #####################################
class ListaPrenotazioniView(QMainWindow, Ui_PrenotazioniOmbrelloneView):
    def __init__(self, parent = None):
        super(ListaPrenotazioniView, self).__init__(parent)
        self.setupUi(self)
        self.update_table()
        self.connectAction()


    def update_table(self):
        ombrelloni_controller = OmbrelloneController()
        ombrelloni = ombrelloni_controller.get_Prenotazioni()
        self.tW_lista_ombrelloni.setRowCount(0)
        for i in range(len(ombrelloni)):
            self.tW_lista_ombrelloni.insertRow(i)
            for j in range(len(ombrelloni[0])):
                if j==3:
                    continue
                if j>3:
                    self.tW_lista_ombrelloni.setItem(i, j-1, QtWidgets.QTableWidgetItem(str(ombrelloni[i][j])))
                else:
                    if j != 2:
                        self.tW_lista_ombrelloni.setItem(i, j, QtWidgets.QTableWidgetItem(str(ombrelloni[i][j])))
                    else:
                        self.tW_lista_ombrelloni.setItem(i, j, QtWidgets.QTableWidgetItem(
                            str(ombrelloni[i][j])))
                        j = j + 1


    def connectAction(self):
        self.tW_lista_ombrelloni.itemSelectionChanged.connect(lambda: self.pB_elimina.setEnabled(1))




##################### SETUP PRENOTAZIONE OMBRELLONE ######################################
class PrenotaOmbrelloneView(QMainWindow, Ui_PrenotaOmbrelloneView):
    def __init__(self, parent = None):
        super(PrenotaOmbrelloneView, self).__init__(parent)
        self.setupUi(self)








#################### SETUP MAIN WINDOW OMBRELLONI ###################################################
class OmbrelloneView(QMainWindow, Ui_OmbrelloneView):
    def __init__(self, parent = None):
        super(OmbrelloneView, self).__init__(parent)
        self.ombrellone_controller = OmbrelloneController()
        self.setupUi(self)
        self.connectAction()
        self.prezzi_window = ListinoOmbrelloneView()
        self.prenota_window = PrenotaOmbrelloneView()
        self.prenotazioni_window = ListaPrenotazioniView()


    def connectAction(self):
        ################################PULSANTI OMBRELLONI#######################################
        self.pB_ricerca.clicked.connect(lambda: self.ricerca_Ombrellone())
        self.pB_lista_prenotazioni.clicked.connect(lambda: self.open_lista_prenotazioni())
        self.pB_listino.clicked.connect(lambda: self.show_Prezzi())
        self.pB_A1.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_A2.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_A3.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_A4.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_A5.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_A6.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_A7.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_A8.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_A9.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_A10.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_B1.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_B2.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_B3.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_B4.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_B5.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_B6.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_B7.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_B8.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_B9.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_B10.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_C1.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_C2.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_C3.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_C4.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_C5.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_C6.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_C7.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_C8.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_C9.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_C10.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_D1.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_D2.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_D3.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_D4.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_D5.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_D6.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_D7.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_D8.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_D9.clicked.connect(lambda: self.prenota_ombrellone())
        self.pB_D10.clicked.connect(lambda: self.prenota_ombrellone())
        self.cB_tipo.currentIndexChanged.connect(lambda: self.set_Enabled())
        self.dE_data.setDate(QDate.currentDate())


    def set_Enabled(self):
        if self.cB_tipo.currentIndex()==0:
            self.cB_orario.setEnabled(False)
            self.cB_orario.setCurrentIndex(0)
        else:
            self.cB_orario.setEnabled(True)
            self.cB_orario.setCurrentIndex(0)


    def show_Prezzi(self):
        self.prezzi_window.show()


    def prenota_ombrellone(self):
        self.prenota_window.show()

    def open_lista_prenotazioni(self):
        self.prenotazioni_window.show()

    def QdateToDate(self, qdate):
        return str(qdate[2]) + "/" + str(qdate[1]) + "/" + str(qdate[0])

    def ricerca_Ombrellone(self):
        data = self.dE_data.date().toString("dd/MM/yyyy")
        date = []
        if self.cB_tipo.currentIndex()==0:
            date.insert(0, data + " 00:00:00")
            date.insert(1, data + " 23:59:59")

        else:
            #vedo se la mezza giornata va da un range di tempo diverso
            if self.cB_orario.currentIndex()==0:
                date.insert(0,data + " 08:00:00")
                date.insert(1,data + " 14:00:00")
            else:
                date.insert(0, data + " 15:00:00")
                date.insert(1, data + " 20:00:00" )

        ombrellone = self.ombrellone_controller.get_OmbrelloniDisponibili(date[0],date[1])
        for i in ombrellone:
            ############## PULSANTI PRIMA FILA ###############
            if i[0]=="A1":
                self.pB_A1.setEnabled(True)
            else:
                self.pB_A1.setEnabled(False)

            if i[0]=="A2":
                self.pB_A2.setEnabled(True)
            else:
                self.pB_A2.setEnabled(False)

            if i[0]=="A3":
                self.pB_A3.setEnabled(True)
            else:
                self.pB_A3.setEnabled(False)

            if i[0]=="A4":
                self.pB_A4.setEnabled(True)
            else:
                self.pB_A4.setEnabled(False)

            if i[0]=="A5":
                self.pB_A5.setEnabled(True)
            else:
                self.pB_A5.setEnabled(False)

            if i[0]=="A6":
                self.pB_A6.setEnabled(True)
            else:
                self.pB_A6.setEnabled(False)

            if i[0]=="A7":
                self.pB_A7.setEnabled(True)
            else:
                self.pB_A7.setEnabled(False)

            if i[0]=="A8":
                self.pB_A8.setEnabled(True)
            else:
                self.pB_A8.setEnabled(False)

            if i[0]=="A9":
                self.pB_A9.setEnabled(True)
            else:
                self.pB_A9.setEnabled(False)

            if i[0]=="A10":
                self.pB_A10.setEnabled(True)
            else:
                self.pB_A10.setEnabled(False)

            ############## PULSANTI SECONDA FILA ###############
            if i[0] == "B1":
                self.pB_B1.setEnabled(True)
            else:
                self.pB_B1.setEnabled(False)

            if i[0] == "B2":
                self.pB_B2.setEnabled(True)
            else:
                self.pB_B2.setEnabled(False)

            if i[0] == "B3":
                self.pB_B3.setEnabled(True)
            else:
                self.pB_B3.setEnabled(False)

            if i[0] == "B4":
                self.pB_B4.setEnabled(True)
            else:
                self.pB_B4.setEnabled(False)

            if i[0] == "B5":
                self.pB_B5.setEnabled(True)
            else:
                self.pB_B5.setEnabled(False)

            if i[0] == "B6":
                self.pB_B6.setEnabled(True)
            else:
                self.pB_B6.setEnabled(False)

            if i[0] == "B7":
                self.pB_B7.setEnabled(True)
            else:
                self.pB_B7.setEnabled(False)

            if i[0] == "B8":
                self.pB_B8.setEnabled(True)
            else:
                self.pB_B8.setEnabled(False)

            if i[0] == "B9":
                self.pB_B9.setEnabled(True)
            else:
                self.pB_B9.setEnabled(False)

            if i[0] == "B10":
                self.pB_B10.setEnabled(True)
            else:
                self.pB_B10.setEnabled(False)

            ############## PULSANTI TERZA FILA ###############
            if i[0] == "C1":
                self.pB_C1.setEnabled(True)
            else:
                self.pB_C1.setEnabled(False)

            if i[0] == "C2":
                self.pB_C2.setEnabled(True)
            else:
                self.pB_C2.setEnabled(False)

            if i[0] == "C3":
                self.pB_C3.setEnabled(True)
            else:
                self.pB_C3.setEnabled(False)

            if i[0] == "C4":
                self.pB_C4.setEnabled(True)
            else:
                self.pB_C4.setEnabled(False)

            if i[0] == "C5":
                self.pB_C5.setEnabled(True)
            else:
                self.pB_C5.setEnabled(False)

            if i[0] == "C6":
                self.pB_C6.setEnabled(True)
            else:
                self.pB_C6.setEnabled(False)

            if i[0] == "C7":
                self.pB_C7.setEnabled(True)
            else:
                self.pB_C7.setEnabled(False)

            if i[0] == "C8":
                self.pB_C8.setEnabled(True)
            else:
                self.pB_C8.setEnabled(False)

            if i[0] == "C9":
                self.pB_C9.setEnabled(True)
            else:
                self.pB_C9.setEnabled(False)

            if i[0] == "C10":
                self.pB_C10.setEnabled(True)
            else:
                self.pB_C10.setEnabled(False)

            ############## PULSANTI QUARTA FILA ###############
            if i[0] == "D1":
                self.pB_D1.setEnabled(True)
            else:
                self.pB_D1.setEnabled(False)

            if i[0] == "D2":
                self.pB_D2.setEnabled(True)
            else:
                self.pB_D2.setEnabled(False)

            if i[0] == "D3":
                self.pB_D3.setEnabled(True)
            else:
                self.pB_D3.setEnabled(False)

            if i[0] == "D4":
                self.pB_D4.setEnabled(True)
            else:
                self.pB_D4.setEnabled(False)

            if i[0] == "D5":
                self.pB_D5.setEnabled(True)
            else:
                self.pB_D5.setEnabled(False)

            if i[0] == "D6":
                self.pB_D6.setEnabled(True)
            else:
                self.pB_D6.setEnabled(False)

            if i[0] == "D7":
                self.pB_D7.setEnabled(True)
            else:
                self.pB_D7.setEnabled(False)

            if i[0] == "D8":
                self.pB_D8.setEnabled(True)
            else:
                self.pB_D8.setEnabled(False)

            if i[0] == "D9":
                self.pB_D9.setEnabled(True)
            else:
                self.pB_D9.setEnabled(False)

            if i[0] == "D10":
                self.pB_D10.setEnabled(True)
            else:
                self.pB_D10.setEnabled(False)