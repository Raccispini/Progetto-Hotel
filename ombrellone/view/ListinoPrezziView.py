'''
__author__: Federico Pretini
'''
from PyQt5.QtWidgets import QMainWindow
from ombrellone.view.Ui_ListinoOmbrellone import Ui_ListinoPrezzi


class ListinoPrezziView(QMainWindow, Ui_ListinoPrezzi):
    def __init__(self, controller, parent = None):
        super(ListinoPrezziView, self).__init__(parent)
        self.setupUi(self)
        self.controller = controller
        self.listino_prezzi = []
        self.update_listino_prezzi()

    def update_listino_prezzi(self):
        lista_file = ["A1","B1","C1","D1"]
        for fila in lista_file:
            self.listino_prezzi.append(self.controller.get_listino_prezzi(fila))
        self.label_1f_intero.setText("Ombrelloni 1^ Fila: " + str(self.listino_prezzi[0][1])+" €")
        self.label_1f_mezza.setText("Ombrelloni 1^ Fila: " + str(self.listino_prezzi[0][2])+" €")
        self.label_2f_intero.setText("Ombrelloni 2^ Fila: " + str(self.listino_prezzi[1][1])+" €")
        self.label_2f_mezza.setText("Ombrelloni 2^ Fila: " + str(self.listino_prezzi[1][2])+" €")
        self.label_3f_intero.setText("Ombrelloni 3^ Fila: " + str(self.listino_prezzi[2][1])+" €")
        self.label_3f_mezza.setText("Ombrelloni 3^ Fila: " + str(self.listino_prezzi[2][2])+" €")
        self.label_4f_intero.setText("Ombrelloni 4^ Fila: " + str(self.listino_prezzi[3][1])+" €")
        self.label_4f_mezza.setText("Ombrelloni 4^ Fila: " + str(self.listino_prezzi[3][2])+" €")
        self.label_sdraie.setText(str(self.listino_prezzi[0][4]) + " €")
        self.label_sedie.setText(str(self.listino_prezzi[0][3]) + " €")

