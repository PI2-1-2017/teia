import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
 
class MessageConfirmation(QWidget):
 
	def __init__(self):
		super().__init__()

	def showMessage(self, HomeWindow):
		btnResponse = QMessageBox.question(self, 'Mensagem', "Tem certeza que deseja sair?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if btnResponse == QMessageBox.Yes:
			return True
		else:
			return False
