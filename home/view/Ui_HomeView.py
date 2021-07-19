'''
__author__: Federico Pretini
__author__: Alessandro Rongoni
'''
import datetime

from PyQt5.QtGui import QCursor, QTextCharFormat, QBrush, QColor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime


#Setto manualmente alcune particolarità dell'interfaccia e le salvo in una variabile
stylesheet = """#MainWindow{border-image: url(ui/resources/main/2690549.jpg) 0 0 0 0 stretch stretch;}
                #pB_Camere,#pB_Ristorante,#pB_Bar,#pB_Anagrafiche,#pB_Magazzino,#pB_Ombrelloni, #pB_Meteo, #pB_Uscita{
                            background-image: url(ui/resources/button/button.jpg);
                            border-style: outset;
                            border-width: 5px;
                            border-color: rgb(221,34,24);
                            border-radius: 20px;                            
                            }
                #pB_Camere:pressed,#pB_Ristorante:pressed,#pB_Bar:pressed,#pB_Anagrafiche:pressed,#pB_Magazzino:pressed
                ,#pB_Ombrelloni:pressed, #pB_Meteo:pressed, #pB_Uscita:pressed{
                            border-style: inset;
                            }   
            """


class Ui_HomeView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Hotel Management")
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        MainWindow.setMinimumSize(1200, 650)
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1279, 750)
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\resources/logo/logo_small_icon_only_inverted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(stylesheet)
        MainWindow.setIconSize(QtCore.QSize(200, 45))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, 20, -1)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")
        self.orario = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.orario.sizePolicy().hasHeightForWidth())
        self.orario.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Palatino")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(100)
        self.orario.setStyleSheet("color: rgb(221,34,24);")
        self.orario.setFont(font)
        self.orario.setAlignment(QtCore.Qt.AlignCenter)
        self.orario.setObjectName("orario")
        timer = QTimer(self)
        timer.timeout.connect(self.displayTime)
        timer.start()
        self.verticalLayout.addWidget(self.orario)
        self.pB_Camere = QtWidgets.QPushButton(self.centralwidget)
        self.pB_Camere.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_Camere.sizePolicy().hasHeightForWidth())
        self.pB_Camere.setSizePolicy(sizePolicy)
        self.pB_Camere.setMinimumSize(QtCore.QSize(400, 0))
        self.pB_Camere.setMaximumSize(QtCore.QSize(400, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\resources/main/Icona_camere.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Camere.setIcon(icon1)
        self.pB_Camere.setIconSize(QtCore.QSize(280, 75))
        self.pB_Camere.setAutoDefault(False)
        self.pB_Camere.setDefault(False)
        self.pB_Camere.setFlat(False)
        self.pB_Camere.setObjectName("pB_Camere")
        self.verticalLayout.addWidget(self.pB_Camere)
        self.pB_Ristorante = QtWidgets.QPushButton(self.centralwidget)
        self.pB_Ristorante.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_Ristorante.sizePolicy().hasHeightForWidth())
        self.pB_Ristorante.setSizePolicy(sizePolicy)
        self.pB_Ristorante.setMaximumSize(QtCore.QSize(400, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui\\resources/main/Icona_ristorante.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Ristorante.setIcon(icon2)
        self.pB_Ristorante.setIconSize(QtCore.QSize(280, 75))
        self.pB_Ristorante.setObjectName("pB_Ristorante")
        self.verticalLayout.addWidget(self.pB_Ristorante)
        self.pB_Bar = QtWidgets.QPushButton(self.centralwidget)
        self.pB_Bar.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_Bar.sizePolicy().hasHeightForWidth())
        self.pB_Bar.setSizePolicy(sizePolicy)
        self.pB_Bar.setMaximumSize(QtCore.QSize(400, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui\\resources/main/Icona_bar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Bar.setIcon(icon3)
        self.pB_Bar.setIconSize(QtCore.QSize(280, 75))
        self.pB_Bar.setObjectName("pB_Bar")
        self.verticalLayout.addWidget(self.pB_Bar)
        self.pB_Anagrafiche = QtWidgets.QPushButton(self.centralwidget)
        self.pB_Anagrafiche.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_Anagrafiche.sizePolicy().hasHeightForWidth())
        self.pB_Anagrafiche.setSizePolicy(sizePolicy)
        self.pB_Anagrafiche.setMaximumSize(QtCore.QSize(400, 16777215))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui\\resources/main/Icona_anagrafiche.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Anagrafiche.setIcon(icon4)
        self.pB_Anagrafiche.setIconSize(QtCore.QSize(280, 75))
        self.pB_Anagrafiche.setObjectName("pB_Anagrafiche")
        self.verticalLayout.addWidget(self.pB_Anagrafiche)
        self.pB_Ombrelloni = QtWidgets.QPushButton(self.centralwidget)
        self.pB_Ombrelloni.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_Ombrelloni.sizePolicy().hasHeightForWidth())
        self.pB_Ombrelloni.setSizePolicy(sizePolicy)
        self.pB_Ombrelloni.setMaximumSize(QtCore.QSize(400, 16777215))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui\\resources/main/Icona_ombrelloni.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Ombrelloni.setIcon(icon5)
        self.pB_Ombrelloni.setIconSize(QtCore.QSize(280, 75))
        self.pB_Ombrelloni.setObjectName("pB_Ombrelloni")
        self.verticalLayout.addWidget(self.pB_Ombrelloni)
        self.pB_Magazzino = QtWidgets.QPushButton(self.centralwidget)
        self.pB_Magazzino.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_Magazzino.sizePolicy().hasHeightForWidth())
        self.pB_Magazzino.setSizePolicy(sizePolicy)
        self.pB_Magazzino.setMaximumSize(QtCore.QSize(400, 16777215))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ui\\resources/main/Icona_magazzino.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Magazzino.setIcon(icon6)
        self.pB_Magazzino.setIconSize(QtCore.QSize(280, 75))
        self.pB_Magazzino.setObjectName("pB_Magazzino")
        self.verticalLayout.addWidget(self.pB_Magazzino)
        self.pB_Meteo = QtWidgets.QPushButton(self.centralwidget)
        self.pB_Meteo.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_Meteo.sizePolicy().hasHeightForWidth())
        self.pB_Meteo.setSizePolicy(sizePolicy)
        self.pB_Meteo.setMinimumSize(QtCore.QSize(400, 0))
        self.pB_Meteo.setMaximumSize(QtCore.QSize(400, 16777215))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ui\\resources/main/Icona_meteo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Meteo.setIcon(icon7)
        self.pB_Meteo.setIconSize(QtCore.QSize(280, 75))
        self.pB_Meteo.setObjectName("pB_Meteo")
        self.verticalLayout.addWidget(self.pB_Meteo)
        self.pB_Uscita = QtWidgets.QPushButton(self.centralwidget)
        self.pB_Uscita.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_Uscita.sizePolicy().hasHeightForWidth())
        self.pB_Uscita.setSizePolicy(sizePolicy)
        self.pB_Uscita.setMaximumSize(QtCore.QSize(400, 16777215))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("ui\\resources/main/Icona_uscita.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pB_Uscita.setIcon(icon8)
        self.pB_Uscita.setIconSize(QtCore.QSize(280, 75))
        self.pB_Uscita.setObjectName("pB_Uscita")
        self.verticalLayout.addWidget(self.pB_Uscita)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        weekendFormat = QTextCharFormat()
        weekendFormat.setForeground(QBrush(QColor(0,0,255)))
        self.calendarWidget.setWeekdayTextFormat(6,weekendFormat)
        self.calendarWidget.setWeekdayTextFormat(7,weekendFormat)
        self.calendarWidget.setStyleSheet("font: 75 18pt \"Arial\";")
        self.calendarWidget.setMinimumDate(QtCore.QDate(2000, 5, 18))
        self.calendarWidget.setMaximumDate(QtCore.QDate(3000, 7, 6))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout.addWidget(self.calendarWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

    #Funzione per aggiornare l'orario e mostrarlo secondon un determinato layout
    def displayTime(self):
        currentTime = QTime.currentTime()
        displayText = currentTime.toString("   hh:mm:ss")
        self.orario.setText(displayText)
