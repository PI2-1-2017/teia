import sys
from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import 
from teia.ui.ui_teia_welcomewindow import Ui_WelcomeWindow
from teia.homewindow import HomeWindow

class WelcomeWindow(QtWidgets.QMainWindow, Ui_WelcomeWindow):

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Bem Vindo!')
		self.setMinimumWidth(400)
		self.setMinimumHeight(300)

		# Buttons
		self.enterButton.clicked.connect(self.enter_system)

		# Show window
		self.show()


	def enter_system(self):
		self.close()
		home = HomeWindow().home_main_call()

		