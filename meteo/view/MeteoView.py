import sys

from PyQt5.QtWidgets import QDialog, QLineEdit, QWidget, QVBoxLayout, QLabel, QApplication, QDialogButtonBox, \
    QPushButton, QHBoxLayout
from PyQt5 import QtGui, QtCore

class MeteoView(QDialog):
    def __init__(self):
        super(MeteoView, self).__init__()

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        lB_message = QLabel("Inserisci la città della quale vuoi conoscere il meteo:")
        font_label= lB_message.font()
        font_label.setPointSize(15)
        font_label.setBold(True)

        lB_message.setFont(font_label)
        le_citta = QLineEdit()
        font_lineEdit = le_citta.font()
        font_lineEdit.setPointSize(15)
        pulsante_Continua=QPushButton()
        pulsante_Annulla=QPushButton()

        pulsante_Continua.setText("Continua")
        pulsante_Annulla.setText("Annulla")

        font_button_C=pulsante_Continua.font()
        font_button_A = pulsante_Annulla.font()
        font_button_A.setPointSize(11)
        font_button_C.setPointSize(11)
        font_button_C.setBold(True)
        font_button_A.setBold(True)
        pulsante_Continua.setFont(font_button_C)
        pulsante_Annulla.setFont(font_button_A)
        pulsante_Continua.setMaximumSize(250,30)
        pulsante_Continua.setMinimumSize(250,30)
        pulsante_Annulla.setMaximumSize(271, 30)
        pulsante_Annulla.setMinimumSize(271, 30)
        le_citta.setFont(font_lineEdit)
        h_layout.addWidget(pulsante_Continua)
        h_layout.addWidget(pulsante_Annulla)
        v_layout.addWidget(lB_message)
        v_layout.addWidget(le_citta)
        v_layout.addLayout(h_layout)

        self.setLayout(v_layout)
        self.setWindowTitle("Ricerca")
        self.setMinimumSize((QtCore.QSize(550,120)))
        self.setMaximumSize((QtCore.QSize(550, 120)))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\resources/logo/logo_small_icon_only_inverted.png"), QtGui.QIcon.Normal)
        self.setWindowIcon(icon)
    def ricerca(self):


if __name__ == '__main__':
    app=QApplication(sys.argv)
    meteo=MeteoView()
    meteo.show()
    sys.exit(app.exec())

