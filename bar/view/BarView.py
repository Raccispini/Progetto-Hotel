from PyQt5.QtWidgets import QMainWindow
from bar.view.Ui_BarView import Ui_BarView
import sqlite3

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
    def closeEvent(self):
        print("Chiudi")

        

    def button_add_action(self,combo,category):
        item = self.get_item(combo,category)
        #print(self.cB_alcolici.currentText())
        flag = False
        print(item)
        for i in range(0, len(self.lista)):
            print(str(self.lista[i][0]) == str(item[0][1]))
            if str(self.lista[i][0]) == str(item[0][1]):
                x = list(self.lista[i])
                x[1] += int(item[1])
                #aggiornamento prezzo
                
                x[3] = int(x[1]) * float(x[2])
                print('Prezzo = '+ str(x[1])+' * '+str(x[2]))
                self.lista[i] = tuple(x)
                flag = True
                break
        if not flag:
            self.lista.append((item[0][1], item[1], item[0][3], int(item[1])*float(item[0][3])))
        print(self.lista)
        self.update_table()
        self.update_tot()


    def on_combobox_changed(self):
        print(self.cB_metodopagamento.currentText())
        if self.cB_metodopagamento.currentText()=="Acconto":
            self.cB_camera.setEnabled(True)
        else:
            self.cB_camera.setEnabled(False)

    def update_camere(self):
        con = sqlite3.connect('database.db')
        camere = con.execute('Select Camere.numeroCamera from Camere Order by Camere.numeroCamera;').fetchall()
        self.cB_camera.clear()
        for i in camere:
            self.cB_camera.addItem(str(i[0]))


