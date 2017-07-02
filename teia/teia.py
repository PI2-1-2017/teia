from PyQt5 import QtCore, QtGui, QtWidgets, uic

from teia.homewindow import HomeWindow


class TeiaApp(QtWidgets.QApplication):

    def __init__(self, args):
        super(TeiaApp, self).__init__(args)

        self.windows = HomeWindow()

