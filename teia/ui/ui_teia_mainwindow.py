# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/teia_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TeiaMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(QtCore.QRect(0, 0, 644, 405))
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 0, 642, 404))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.imageButton = QtWidgets.QPushButton(self.layoutWidget)
        self.imageButton.setEnabled(True)
        self.imageButton.setObjectName("imageButton")
        self.gridLayout.addWidget(self.imageButton, 0, 1, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.layoutWidget)
        self.startButton.setAutoDefault(False)
        self.startButton.setDefault(False)
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.searchFrame = QtWidgets.QWidget(self.layoutWidget)
        self.searchFrame.setMinimumSize(QtCore.QSize(640, 360))
        self.searchFrame.setObjectName("SearchFrame")
        self.gridLayout_2.addWidget(self.searchFrame, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.layoutWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("TeiaMainWindow", "Form"))
        self.imageButton.setText(_translate("TeiaMainWindow", "Imagem"))
        self.startButton.setText(_translate("TeiaMainWindow", "Iniciar Busca"))
