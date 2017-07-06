# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teia_tecnicalwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TecnicalWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.layoutWidget = QtWidgets.QWidget(MainWindow)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.backButton = QtWidgets.QPushButton(self.layoutWidget)
        self.backButton.setAutoDefault(False)
        self.backButton.setDefault(False)
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.layoutWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("TecnicalWindow", "Form"))
        self.backButton.setText(_translate("TecnicalWindow", "Voltar"))
        self.label.setText(_translate("TecnicalWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Especificações Técnicas do Drone</span></p><p><span style=\" font-size:14pt; font-weight:600;\">----------------------------------------------------------------------------------------------</span></p><p>Motores Tipo Brushless - DJI E300212 (x4)</p><p>Bateria Power LiPo 5200 mAh 30c 4s (x1)</p><p>Hélices DJI 9443 (x2 pares)</p><p>---------------------------------------------------------------------------------------------------------------------------------------</p><p>Controladora de Vôo: Arduino Mega</p><p>Acelerômetro e Giroscópio: MPU-6050</p><p>Controlador Eletrônico de Velocidade: Hobbysky Simonk 30A</p><p>Módulo com Microcontrolador ARM: ESP8266</p><p>Transmissor de Imagem: Eachine TS832 Boscam</p><p>Receptor de Imagem: RC832 Boscam</p><p>Rádio Controle: FlySky FS-i6</p></body></html>"))

from teia.design import text