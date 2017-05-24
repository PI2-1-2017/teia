from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Teia')
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        self.show()
