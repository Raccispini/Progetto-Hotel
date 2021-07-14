from PyQt5.QtWidgets import QMainWindow
from ristorante.view.Ui_OrdinazioniRistoranteView import Ui_OrdinazioniRistoranteView


class OrdinazioniRistoranteView(QMainWindow, Ui_OrdinazioniRistoranteView):
    def __init__(self,controller, item, parent = None):
        super(OrdinazioniRistoranteView, self).__init__(parent)
        self.setupUi(self)
        self.item_selected = item
        self.controller = controller
        self.update_all()

    def update_all(self):
        info_tavolo = []
        for info in self.item_selected:
            info_tavolo.append(info.text())

        self.lineE_tavolo.setText(info_tavolo[1].split("_"[1]))
        self.lineE_nominativo.setText(info_tavolo[2])
        self.lineE_persone.setText(info_tavolo[3])
        self.cB_antipasti.addItems(self.controller.get_menu("Antipasti"))
