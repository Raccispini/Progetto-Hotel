from PyQt5.QtWidgets import QMainWindow
from camere.view.Ui_CamereView import Ui_CamereView
from camere.model.ModelCamere import ModelCamere
from PyQt5 import QtCore, QtGui, QtWidgets


class CamereView(QMainWindow, Ui_CamereView):
    def __init__(self, parent = None):
        super(CamereView, self).__init__(parent)
        self.setupUi(self)
        self.update_tipo()
        self.update_table(onstart=True)
        self.spin_singoli.valueChanged.connect(lambda: self.update_table())

    

    
    def update_table(self,onstart=False):
        camere = []
        options = self.check_options()
        if onstart:
            camere = ModelCamere.getCamere()
        else:
            camere = ModelCamere.getCamere(self,options)
        print(options)
        print(len(camere[0]))
        self.tabellaCamere.setRowCount(0)
        for i in range(0, len(camere)):
            self.tabellaCamere.insertRow(i)
            for j in range(16):
                if j > 2 and (j != 15 and j!=4 and j != 3):
                    self.tabellaCamere.setItem(i, j, QtWidgets.QTableWidgetItem("Si" if camere[i][j] == 1 else "No"))
                else:
                    self.tabellaCamere.setItem(i, j , QtWidgets.QTableWidgetItem(str(camere[i][j])))
    def update_tipo(self):
        allestimenti = ModelCamere.get_tipo()
        for i in range(len(allestimenti)):
            self.combo_tipo.addItem(allestimenti[i])
    def check_options(self):
        options = {}
        #letti
        options["letti_singoli"] = self.spin_singoli.value()
        options["letti_matrimoniali"] = self.spin_matrim.value()
        #date
        options["check_in"] = self.QdateToDate(self.date_dal.date().getDate())
        options["check_out"] = self.QdateToDate(self.date_al.date().getDate())
        #allestimento
        options["allestimento"] = self.combo_tipo.currentText()
        #checkbox
        options["aria_condizionata"] = True if self.cb_ariaCondizionata.isChecked() else False
        options["animale"] = True if self.cb_animaledomestico.isChecked() else False
        options["sauna"] = True if self.cb_saunainterna.isChecked() else False
        options["idromassaggio"] = True if self.cb_vascaidromassaggio.isChecked() else False
        options["fumatori"] = True if self.cb_fumatori.isChecked() else False
        options["vista"] = True if self.cb_vistapanoramica.isChecked() else False
        options["culla"] = True if self.cb_culla_2.isChecked() else False
        options["minibar"] = True if self.cb_minibar.isChecked() else False
        options["cassaforte"] = True if self.cb_cassaforte.isChecked() else False
        print(options)
        return options

    def QdateToDate(self,qdate):
        return str(qdate[2])+"/"+str(qdate[1])+"/"+str(qdate[0])