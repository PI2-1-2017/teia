import sys
from PyQt5 import QtWidgets
from teia.ui.ui_teia_homewindow import Ui_HomeWindow
from teia.mainwindow import MainWindow

class HomeWindow(QtWidgets.QMainWindow, Ui_HomeWindow):

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
		self.searchTargetButton.clicked.connect(self.search_target)
		#self.technicalEspecifications.clicked.connect(self.stream)
		self.exitButton.clicked.connect(self.exit_system)


		# Show window
		self.show()
	
	def search_target(self):
		search = MainWindow().main_call()

	def exit_system(self):
		self.close()
		


