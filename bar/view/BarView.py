from PyQt5.QtWidgets import QMainWindow
from bar.view.Ui_BarView import Ui_BarView
import sqlite3
from Scontrini import Scontrini

class BarView(QMainWindow, Ui_BarView):
    def __init__(self, parent=None):
        super(BarView, self).__init__(parent)
        self.setupUi(self)
        self.update_data(QMainWindow)
        self.update_table()
        self.update_tot()
        self.pB_alcolici.clicked.connect(lambda: self.button_add_action(self.cB_alcolici,"Alcolici"))
        self.pB_analcolici.clicked.connect(lambda: self.button_add_action(self.cB_analcolici, "Analcolici"))
        self.pB_aperitivi.clicked.connect(lambda: self.button_add_action(self.cB_aperitivi,"Aperitivi"))
        self.pB_bibite.clicked.connect(lambda :self.button_add_action(self.cB_bibite,"Bibite"))
        self.pB_caffetteria.clicked.connect(lambda: self.button_add_action(self.cB_caffetteria,"Caffetteria"))
        self.pB_vini.clicked.connect(lambda: self.button_add_action(self.cB_vini,"Vini"))
        self.pB_liquori.clicked.connect(lambda:self.button_add_action(self.cB_liquori,'Liquori'))
        self.pB_pasticceria.clicked.connect(lambda :self.button_add_action(self.cB_pasticceria,"Pasticceria"))
        self.cB_metodopagamento.currentTextChanged.connect(lambda: self.on_combobox_changed())
        self.update_camere()
        self.pB_salva.setEnabled(True)
        self.pB_salva.clicked.connect(lambda : self.stampa())
        self.tW_scontrino.itemSelectionChanged.connect(lambda : self.on_table_click())
        self.tW_scontrino.clear()

        self.pB_elimina.clicked.connect(lambda : self.on_elimina_clicked())
    
    def stampa(self):
        print("ciao")
        lista = []
        for i in self.lista:
            print(i)
            lista.append((i[0],i[1],i[3]))
        print(lista)
        tot = str(self.LE_totaleconto.text())
        print(tot)
        scontrini = Scontrini()
        scontrini.stampa(lista,tot)


    def on_elimina_clicked(self):
        #cerca le righe selezionate
        indexes = self.tW_scontrino.selectionModel().selectedRows()
        selected_rows = []
        for index in sorted(indexes):
            selected_rows.append(index.row())
            print(selected_rows)
            #print('Row %d is selected' % index.row())

        #elimina la riga
        for i in range(len(selected_rows)):
            try:
                self.lista.remove(self.lista[selected_rows[i]])
            except :
                pass
        self.update_table()
        self.update_tot()

    def on_table_click(self):
        if len(self.tW_scontrino.selectionModel().selectedRows()) > 0 :
            self.pB_elimina.setEnabled(True)
        else:
            self.pB_elimina.setEnabled(False)


    def button_add_action(self,combo,category):
        item = self.get_item(combo,category)
        #print(self.cB_alcolici.currentText())
        flag = False
        #print(item)
        for i in range(0, len(self.lista)):
            #print(str(self.lista[i][0]) == str(item[0][1]))
            if str(self.lista[i][0]) == str(item[0][1]):
                x = list(self.lista[i])
                x[1] += int(item[1])
                #aggiornamento prezzo
                
                x[3] = int(x[1]) * float(x[2])
                #print('Prezzo = '+ str(x[1])+' * '+str(x[2]))
                self.lista[i] = tuple(x)
                flag = True
                break
        if not flag:
            self.lista.append((item[0][1], item[1], item[0][3], int(item[1])*float(item[0][3])))
        #print(self.lista)
        #Aggiorna solo se la quantità è diversa da 0
        if int(item[1]) != 0:
            self.update_table()
            self.update_tot()
        self.on_table_click()


    def on_combobox_changed(self):
        #print(self.cB_metodopagamento.currentText())
        if self.cB_metodopagamento.currentText()=="Acconto":
            self.cB_camera.setEnabled(True)
        else:
            self.cB_camera.setEnabled(False)

    def update_camere(self):
        con = sqlite3.connect('database.db')
        camere = con.execute('SELECT * FROM Camere ORDER BY Camere.numeroCamera;').fetchall()
        #print(camere)
        self.cB_camera.clear()
        for camera in camere:
            self.cB_camera.addItem(str(camera[0]) + str(camera[1]) + " " + camera[2])
