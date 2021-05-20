from PyQt5.QtWidgets import QMainWindow
from bar.view.Ui_BarView import Ui_BarView

class BarView(QMainWindow, Ui_BarView):
    def __init__(self, parent=None):
        super(BarView, self).__init__(parent)
        self.setupUi(self)
        self.update_data(QMainWindow)
        self.update_table()
        self.update_tot()
        self.pB_alcolici.clicked.connect(lambda: self.button_add_action(self.cB_alcolici,"Alcolici"))

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
                x[3] = int(self.lista[i][1]) * float(self.lista[i][3])
                self.lista[i] = tuple(x)
                flag = True
                break
        if not flag:
            self.lista.append((item[0][1], item[1], item[0][3], int(item[1])*float(item[0][3])))
        print(self.lista)
        self.update_table()
        self.update_tot()






