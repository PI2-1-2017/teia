import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import qdarkstyle

from MainWindow import MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = MainWindow()
    sys.exit(app.exec_())
