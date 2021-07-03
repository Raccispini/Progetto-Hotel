from PyQt5.QtWidgets import QMainWindow
from camere.view.Ui_CamereView import Ui_CamereView
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class CamereView(QMainWindow, Ui_CamereView):
    def __init__(self, parent = None):
        super(CamereView, self).__init__(parent)
        self.setupUi(self)
        self.update_table()
        self.spin_singoli.valueChanged.connect(lambda: self.update_table())

    
    def get_camere(self,numero=-1,singoli=-1,matrimoniali=-1,check_in=None,check_out=None,tipo=-1,aria=-1,animale=-1,sauna=-1,idromassaggio=-1,fumatori=-1,vista=-1,culla=-1,minibar=-1,cassaforte=-1):
        con = sqlite3.connect("database.db")
        query = "select * from Camere"
        if numero != -1 or matrimoniali != -1 or singoli != -1 or  check_in != None or check_out != None:
            query += " WHERE "

            if numero != -1:
                query += "Camere.numeroCamera = "+str(numero)+" and "
            if matrimoniali != -1:
                query += "Camere.matrimoniale >= "+str(matrimoniali)+"' and "
            if singoli != -1:
                query += "Camere.numeroSingoli >= '"+str(singoli)+"' and "
            if tipo != -1:
                query += "Camere.allestimento = '"+str(tipo) +"' and "
            if aria != -1 :
                query += "Camere.ariaCondizionata = "+str(aria)+" and "
            if animale != -1:
                query += "Camere.animaleDomestico = "+str(animale)+" and "
            if sauna != -1:
                query += "Camere.vascaIdromassaggio = "+str(idromassaggio)+" and"
            if fumatori != -1:
                query += "Camere.fumatori = "+str(fumatori)+" and "
            if vista != -1:
                query += "Camere.vistaPanoramica = "+str(vista)+" and "
            if culla != -1:
                query += "Camere.culla = " + str(culla) + " and "
            if minibar != -1:
                query += "Camere.miniBar = "+str(minibar)+" and "
            if cassaforte != -1:
                query += "Camere.cassaforte = "+str(cassaforte)+" and "
            if check_in != None or check_out != None:
                query += "Camere.numeroCamera NOT IN ( SELECT Prenotazioni_camere.numero_camera from Prenotazioni_camere WHERE NOT("
                if check_in != None and check_out != None:
                    query += "Prenotazioni_camere.check_out<'" + \
                        str(check_in)+"' OR Prenotazioni_camere.check_in > '" + \
                        str(check_out)+"'))   "
                else:
                    if check_in != None:
                        query += "Prenotazioni_camere.check_out<'"+str(check_in)+"'"
                    else:
                        query += "Prenotazioni_camere.check_in>'"+str(check_out)+"'"
                    query += "))   "
            query = query[:-3]
        query += " ORDER BY Camere.numeroCamera;"
        print(query)
        camere = con.execute(query)
        return camere.fetchall()
    
    def update_table(self):
        options= self.check_options()
        camere = self.get_camere(singoli=options[0],matrimoniali=options[1],check_in=options[2],check_out=options[3],tipo=options[4],aria=options[5],animale=options[6],sauna=options[7],idromassaggio=options[8],fumatori=options[9],vista=options[10],culla=options[11],minibar=options[12],cassaforte=options[13])
        print(len(camere[0]))
        self.tabellaCamere.setRowCount(0)
        for i in range(0, len(camere)):
            self.tabellaCamere.insertRow(i)
            for j in range(16):
                if j > 2 and (j != 15 and j!=4 and j != 3):
                    self.tabellaCamere.setItem(i, j, QtWidgets.QTableWidgetItem("Si" if camere[i][j] == 1 else "No"))
                else:
                    self.tabellaCamere.setItem(i, j , QtWidgets.QTableWidgetItem(str(camere[i][j])))

    def check_options(self):
        options = []
        #letti
        options.append(self.spin_singoli.value())
        options.append(self.spin_matrim.value())
        #date
        options.append(self.QdateToDate(self.date_dal.date().getDate()))
        options.append(self.QdateToDate(self.date_al.date().getDate()))
        #allestimento
        options.append(self.combo_tipo.currentText())
        #checkbox
        if self.cb_ariaCondizionata.isChecked():
            options.append(1)
        else:
            options.append(-1)
        if self.cb_animaledomestico.isChecked():
            options.append(1)
        else:
            options.append(-1)
        if self.cb_saunainterna.isChecked():
            options.append(1)
        else:
            options.append(-1)
        if self.cb_vascaidromassaggio.isChecked():
            options.append(1)
        else:
            options.append(-1)
        if self.cb_fumatori.isChecked():
            options.append(1)
        else:
            options.append(-1)
        if self.cb_vistapanoramica.isChecked():
            options.append(1)
        else:
            options.append(-1)
        if self.cb_culla_2.isChecked():
            options.append(1)
        else:
            options.append(-1)
        if self.cb_minibar.isChecked():
            options.append(1)
        else:
            options.append(-1)
        if self.cb_cassaforte.isChecked():
            options.append(1)
        else:
            options.append(-1)

        print(options)
        return options

    def QdateToDate(self,qdate):
        return str(qdate[2])+"/"+str(qdate[1])+"/"+str(qdate[0])