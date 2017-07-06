import sys
from PyQt5 import QtWidgets
from teia.ui.ui_teia_homewindow import Ui_HomeWindow
from teia.mainwindow import MainWindow
from teia.tecnicalwindow import TecnicalWindow

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
		self.tecnicalButton.clicked.connect(self.tecnical)
		self.exitButton.clicked.connect(self.exit_system)


		# Show window
		self.show()
	
	def search_target(self):
		search = MainWindow().main_call()

	def tecnical(self):
		tec = TecnicalWindow().tec_main_call()

	def exit_system(self):
		self.close()

	def home_main_call(self):
		srch = search_target()
		ext = exit_system()
		


