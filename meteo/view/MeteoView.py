'''
__author__: Federico Pretini
__author__: Alessandro Rongoni
'''
import webbrowser
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5 import QtGui, QtCore

class MeteoView(QDialog):
    def __init__(self):
        super().__init__()

        self.setObjectName("window_meteo")
        self.setStyleSheet("#window_meteo{border-image: url(ui/resources/meteo/meteo.jpg) 0 0 0 0 stretch stretch}")
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        lB_message = QLabel("Inserisci il nome della città da cercare:")
        font_label= lB_message.font()
        font_label.setPointSize(15)
        font_label.setBold(True)
        lB_message.setFont(font_label)
        self.le_citta = QLineEdit()
        font_lineEdit = self.le_citta.font()
        font_lineEdit.setPointSize(15)
        self.pB_Continua = self.get_generic_button("Continua")
        self.pB_Continua.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.pB_Annulla = self.get_generic_button("Annulla")
        self.pB_Annulla.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.le_citta.setFont(font_lineEdit)
        h_layout.addWidget(self.pB_Continua)
        h_layout.addWidget(self.pB_Annulla)
        v_layout.addWidget(lB_message)
        v_layout.addWidget(self.le_citta)
        v_layout.addLayout(h_layout)
        self.setLayout(v_layout)
        self.setWindowTitle("Ricerca Meteo")
        self.setMinimumSize((QtCore.QSize(550,150)))
        self.setMaximumSize((QtCore.QSize(550,150)))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\resources/logo/logo_small_icon_only_inverted.png"), QtGui.QIcon.Normal)
        self.setWindowIcon(icon)
        self.pB_Continua.clicked.connect(lambda: self.ricerca())
        self.pB_Annulla.clicked.connect(lambda: self.close())

    def ricerca(self):
        webbrowser.open("https://www.ilmeteo.it/meteo/" + self.le_citta.text(), new=1)

    def get_generic_button(self, testo):
        button = QPushButton()
        button.setText(testo)
        font = button.font()
        font.setPointSize(11)
        font.setBold(True)
        button.setFont(font)
        button.setMaximumSize(250, 30)
        button.setMinimumSize(250, 30)
        return button






