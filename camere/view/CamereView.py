from PyQt5.QtWidgets import QMainWindow
from camere.view.Ui_CamereView import Ui_CamereView
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class CamereView(QMainWindow, Ui_CamereView):
    def __init__(self, parent = None):
        super(CamereView, self).__init__(parent)
        self.setupUi(self)
        self.update_table()
    
    def get_camere(self,numero=0, letti_doppi=False, letti_singoli=0, prezzo=0, check_in=None, check_out=None):
        con = sqlite3.connect("database.db")
        query = "select * from Camere"
        if numero != 0 or letti_doppi != 0 or letti_singoli != 0 or prezzo != 0 or check_in != None or check_out != None:
            query += " WHERE "

            if numero != 0:
                query += "Camere.numeroCamera = "+str(numero)+" and "
            if letti_doppi != 0:
                query += "Camere.matrimoniale = "+str(letti_doppi)+" and "
            if letti_singoli != 0:
                query += "Camere.numeroSingoli >= "+str(letti_singoli)+" and "
            if prezzo != 0:
                query += "prezzo <="+str(prezzo)+" and"
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
        camere = self.get_camere()
        print(len(camere[0]))
        self.tabellaCamere.setRowCount(0)
        for i in range(0, len(camere)):
            self.tabellaCamere.insertRow(i)
            for j in range(15):
                if j > 2 and j != 14:
                    self.tabellaCamere.setItem(i, j, QtWidgets.QTableWidgetItem("Si" if camere[i][j] == 1 else "No"))
                else:
                    self.tabellaCamere.setItem(i, j , QtWidgets.QTableWidgetItem(str(camere[i][j])))

