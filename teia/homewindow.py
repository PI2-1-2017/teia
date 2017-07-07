import sys
from PyQt5 import QtWidgets
from teia.ui.ui_teia_homewindow import Ui_HomeWindow
from teia.mainwindow import MainWindow
from teia.tecnicalwindow import TecnicalWindow
from teia.helpwindow import HelpWindow

class HomeWindow(QtWidgets.QMainWindow, Ui_HomeWindow):

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Projeto Teia')
		self.setMinimumWidth(400)
		self.setMinimumHeight(300)

		# Buttons
		self.searchTargetButton.clicked.connect(self.search_target)
		self.tecnicalButton.clicked.connect(self.tecnical)
		self.helpButton.clicked.connect(self.help)
		self.exitButton.clicked.connect(self.close)
             
		# Show window
		self.show()
	
	def search_target(self):
		search = MainWindow().main_call()

	def tecnical(self):
		tec = TecnicalWindow().__init__()

	def help(self):
		help = HelpWindow().__init__()

	def home_main_call(self):
		srch = search_target()
		tcn = tecnical()
		hp = help()

		


