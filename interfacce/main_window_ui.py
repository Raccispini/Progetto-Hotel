# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1200, 655)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 655))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 655))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\resources/logo/logo_small_icon_only_inverted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(200, 45))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolBar.setMouseTracking(False)
        self.toolBar.setIconSize(QtCore.QSize(250, 45))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionCamere = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\resources/Toolbar_main/Icona_Camere.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCamere.setIcon(icon1)
        self.actionCamere.setObjectName("actionCamere")
        self.actionAnagrafiche = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui\\resources/Toolbar_main/Icona_anagrafiche.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnagrafiche.setIcon(icon2)
        self.actionAnagrafiche.setObjectName("actionAnagrafiche")
        self.actionMagazzino = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui\\resources/Toolbar_main/Icona_magazzino.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMagazzino.setIcon(icon3)
        self.actionMagazzino.setObjectName("actionMagazzino")
        self.actionBar = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui\\resources/Toolbar_main/Icona_bar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBar.setIcon(icon4)
        self.actionBar.setObjectName("actionBar")
        self.actionOmbrelloni = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui\\resources/Toolbar_main/Icona_ombrelloni.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOmbrelloni.setIcon(icon5)
        self.actionOmbrelloni.setObjectName("actionOmbrelloni")
        self.actionRistorante = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ui\\resources/Toolbar_main/Icona_ristorante.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRistorante.setIcon(icon6)
        self.actionRistorante.setObjectName("actionRistorante")
        self.actionAmministrativo = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ui\\resources/Toolbar_main/Icona_amministrativo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAmministrativo.setIcon(icon7)
        self.actionAmministrativo.setObjectName("actionAmministrativo")
        self.actionStrumenti = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("ui\\resources/Toolbar_main/Icona_strumenti.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStrumenti.setIcon(icon8)
        self.actionStrumenti.setObjectName("actionStrumenti")
        self.actionRicerca = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("ui\\resources/Toolbar_main/Icona_ricerca.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRicerca.setIcon(icon9)
        self.actionRicerca.setObjectName("actionRicerca")
        self.actionMeteo = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("ui\\resources/Toolbar_main/Icona_Meteo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMeteo.setIcon(icon10)
        self.actionMeteo.setObjectName("actionMeteo")
        self.actionUscita = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("ui\\resources/Toolbar_main/Icona_uscita.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUscita.setIcon(icon11)
        self.actionUscita.setObjectName("actionUscita")
        self.toolBar.addAction(self.actionCamere)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAnagrafiche)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMagazzino)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionOmbrelloni)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRistorante)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAmministrativo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionStrumenti)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRicerca)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMeteo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUscita)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        return MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hotel Management"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionCamere.setText(_translate("MainWindow", "Camere"))
        self.actionCamere.setToolTip(_translate("MainWindow", "Apre il gestore dei gruppi"))
        self.actionCamere.setShortcut(_translate("MainWindow", "F1"))
        self.actionAnagrafiche.setText(_translate("MainWindow", "Anagrafiche"))
        self.actionAnagrafiche.setToolTip(_translate("MainWindow", "Apre il gestore delle anagrafiche"))
        self.actionAnagrafiche.setShortcut(_translate("MainWindow", "F2"))
        self.actionMagazzino.setText(_translate("MainWindow", "Magazzino"))
        self.actionMagazzino.setToolTip(_translate("MainWindow", "Apre il gestore del magazzino"))
        self.actionMagazzino.setShortcut(_translate("MainWindow", "F3"))
        self.actionBar.setText(_translate("MainWindow", "Bar"))
        self.actionBar.setToolTip(_translate("MainWindow", "Apre il gestore dei bar"))
        self.actionBar.setShortcut(_translate("MainWindow", "F4"))
        self.actionOmbrelloni.setText(_translate("MainWindow", "Ombrelloni"))
        self.actionOmbrelloni.setToolTip(_translate("MainWindow", "Apre il gestore degli Ombrelloni"))
        self.actionOmbrelloni.setShortcut(_translate("MainWindow", "F5"))
        self.actionRistorante.setText(_translate("MainWindow", "Ristorante"))
        self.actionRistorante.setToolTip(_translate("MainWindow", "Apre il gestore del ristornate"))
        self.actionRistorante.setShortcut(_translate("MainWindow", "F6"))
        self.actionAmministrativo.setText(_translate("MainWindow", "Amministrativo"))
        self.actionAmministrativo.setToolTip(_translate("MainWindow", "Apre il gestore dell\'amministrativo"))
        self.actionAmministrativo.setShortcut(_translate("MainWindow", "F7"))
        self.actionStrumenti.setText(_translate("MainWindow", "Strumenti"))
        self.actionStrumenti.setToolTip(_translate("MainWindow", "Apre il gestore degli Strumenti"))
        self.actionStrumenti.setShortcut(_translate("MainWindow", "F8"))
        self.actionRicerca.setText(_translate("MainWindow", "Ricerca"))
        self.actionRicerca.setToolTip(_translate("MainWindow", "Apre una finestra per la ricerca di un cliente"))
        self.actionRicerca.setShortcut(_translate("MainWindow", "F9"))
        self.actionMeteo.setText(_translate("MainWindow", "Meteo"))
        self.actionMeteo.setToolTip(_translate("MainWindow", "Apre una finestra che mostra il meteo"))
        self.actionMeteo.setShortcut(_translate("MainWindow", "F10"))
        self.actionUscita.setText(_translate("MainWindow", "Uscita"))
        self.actionUscita.setToolTip(_translate("MainWindow", "Arresta l\'esecuzione del programma"))
        self.actionUscita.setShortcut(_translate("MainWindow", "F11"))