from PyQt5 import QtCore, QtGui, QtWidgets, uic

from teia.welcomewindow import WelcomeWindow


class TeiaApp(QtWidgets.QApplication):

    def __init__(self, args):
        super(TeiaApp, self).__init__(args)

        self.windows = WelcomeWindow()

