# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1200, 800)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.chatBrowser = QtWidgets.QTextEdit(self.centralWidget)
        self.chatBrowser.setReadOnly(True)
        self.chatBrowser.setEnabled(True)
        self.chatBrowser.setGeometry(QtCore.QRect(10, 10, 861, 501))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.chatBrowser.setFont(font)
        self.chatBrowser.setObjectName("chatBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 520, 731, 211))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.connectedList = QtWidgets.QListWidget(self.centralWidget)
        self.connectedList.setGeometry(QtCore.QRect(880, 10, 311, 721))
        self.connectedList.setObjectName("connectedList")
        self.sendButton = QtWidgets.QPushButton(self.centralWidget)
        self.sendButton.setGeometry(QtCore.QRect(752, 527, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendButton.setFont(font)
        self.sendButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendButton.setObjectName("sendButton")
        self.clearButton = QtWidgets.QPushButton(self.centralWidget)
        self.clearButton.setGeometry(QtCore.QRect(750, 630, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clearButton.setFont(font)
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearButton.setObjectName("clearButton")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuConfiguraci_n = QtWidgets.QMenu(self.menuBar)
        self.menuConfiguraci_n.setObjectName("menuConfiguraci_n")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionOpciones = QtWidgets.QAction(MainWindow)
        self.actionOpciones.setObjectName("actionOpciones")
        self.menuConfiguraci_n.addAction(self.actionOpciones)
        self.menuBar.addAction(self.menuConfiguraci_n.menuAction())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sendButton.setText(_translate("MainWindow", "Enviar"))
        self.clearButton.setText(_translate("MainWindow", "Borrar"))
        self.menuConfiguraci_n.setTitle(_translate("MainWindow", "Configuración"))
        self.actionOpciones.setText(_translate("MainWindow", "Opciones"))
