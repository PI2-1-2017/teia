import sys
from PyQt5.QtWidgets import QWidget, QFileDialog

class ImageUploader(QWidget):

	def __init__(self):
		super().__init__()
		self.fileName = None

	def inputFile(self):
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self, "Selecionar Imagem", "/home", "Images (*.png *.xpm *.jpg)", options=options)
		if fileName:
			self.fileName = fileName

		return self.fileName
