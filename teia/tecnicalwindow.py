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


		# Text
		#self.teiaProject.

		# Buttons
		self.backButton.clicked.connect(self.back_home_window)

		# Show window
		self.show()
	

	def back_home_window(self):
		self.close()

	def tec_main_call(self):
		back = back_home_window()
		


