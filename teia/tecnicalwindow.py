import sys
from PyQt5 import QtWidgets
from teia.ui.ui_teia_tecnicalwindow import Ui_TecnicalWindow

class TecnicalWindow(QtWidgets.QMainWindow, Ui_TecnicalWindow):

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Projeto Teia')
		self.setMinimumWidth(400)
		self.setMinimumHeight(300)

		# Buttons
		self.backButton.clicked.connect(self.close)

		# Show window
		self.show()
	
		


