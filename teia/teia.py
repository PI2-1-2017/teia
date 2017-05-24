from PyQt5 import QtCore, QtGui, QtWidgets, uic
import qdarkstyle

from teia.mainwindow import MainWindow

class TeiaApp(QtWidgets.QApplication):

    def __init__(self, args):
        super(TeiaApp, self).__init__(args)
        # self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.windows = MainWindow()
