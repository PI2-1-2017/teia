# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teia_welcomewindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WelcomeWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.image = QtWidgets.QLabel(self.layoutWidget)
        self.image.setObjectName("image")
        self.gridLayout.addWidget(self.image, 0, 0, 1, 1)
        self.enterButton = QtWidgets.QPushButton(self.layoutWidget)
        self.enterButton.setObjectName("enterButton")
        self.enterButton.setToolTip('Entrar')
        self.gridLayout.addWidget(self.enterButton, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.layoutWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("WelcomeWindow", "Form"))
        self.image.setText(_translate("WelcomeWindow", "<html><head/><body><p align=\"center\"><img src=\":/newPrefix/teia.png\"/></p></body></html>"))
        self.enterButton.setText(_translate("WelcomeWindow", "Entrar"))

from teia.design import image
