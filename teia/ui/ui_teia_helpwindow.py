# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teia_tecnicalwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_HelpWindow(object):
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
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignJustify)
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.layoutWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("TecnicalWindow", "Form"))
        self.backButton.setText(_translate("TecnicalWindow", "Voltar"))
        self.label.setText(_translate("TecnicalWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Ajuda ao usuário</span></p><p><span style=\" font-size:14pt; font-weight:600;\"> </span></p><p>O sistema Teia visa permitir o reconhecimento de uma pessoa, através da captura de sua face, realizada por uma câmera posicionada em um drone. </p><p>    Para efetuar essa busca, é necessário selecionar a opção no Menu principal de 'Procurar Alvo'.</p><p> Na tela de busca, selecione a opção 'Iniciar busca'. Quando a busca iniciar, a transmissão do video aparecerá em tempo real.</p><p> Em seguida, para escolher o alvo a ser buscado, basta selecionar a opção 'Imagem', buscar a imagem dele na máquina e selecioná-la.</p><p>Então o sistema realizará a busca, retornando o resultado.</p></body></html>"))

from teia.design import text
