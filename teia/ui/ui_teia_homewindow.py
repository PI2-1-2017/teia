# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teia_homewindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HomeWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.exitButton = QtWidgets.QPushButton(self.layoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout.addWidget(self.exitButton, 4, 0, 1, 1)
        self.searchTargetButton = QtWidgets.QPushButton(self.layoutWidget)
        self.searchTargetButton.setAutoDefault(False)
        self.searchTargetButton.setDefault(False)
        self.searchTargetButton.setObjectName("searchTargetButton")
        self.gridLayout.addWidget(self.searchTargetButton, 1, 0, 1, 1)
        self.tecnicalButton = QtWidgets.QPushButton(self.layoutWidget)
        self.tecnicalButton.setEnabled(True)
        self.tecnicalButton.setObjectName("tecnicalButton")
        self.gridLayout.addWidget(self.tecnicalButton, 2, 0, 1, 1)
        self.image2 = QtWidgets.QLabel(self.layoutWidget)
        self.image2.setObjectName("image2")
        self.gridLayout.addWidget(self.image2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.layoutWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("HomeWindow", "Form"))
        self.exitButton.setText(_translate("HomeWindow", "Sair"))
        self.searchTargetButton.setText(_translate("HomeWindow", "Procurar Alvo"))
        self.tecnicalButton.setText(_translate("HomeWindow", "Especificações Técnicas"))
        self.image2.setText(_translate("HomeWindow", "<html><head/><body><p align=\"center\"><img src=\":/image2/teia2.PNG\"/></p></body></html>"))

from teia.design import image2