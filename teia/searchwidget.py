from PyQt5 import QtWidgets, QtGui, QtCore

from teia.videostream import VideoStream
# Ui
from teia.ui.ui_search_widget import Ui_SearchWidget

class SearchWidget(QtWidgets.QWidget, Ui_SearchWidget):

    def __init__(self, layout=None):
        super().__init__(layout)
        self.searching = None
        self.image = None
        self.setupUi(self)
        self.initUI()
        self.hide()

    def initUI(self):
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

    def stream(self):
        self.searching = not self.searching
        if self.searching:
            print ("start searching")
            self.videoStream = VideoStream()
            self.videoStream.newFrame.connect(self.update_frame)
            self.videoStream.start()
            self.show()
        else:
            print ("stop searching")
            self.videoStream.quit()
            self.hide()

    def update_frame(self, image):
        self.image = image
        self.setMinimumSize(image.size())
        self.update()

    def paintEvent(self, event):
        qtPainter = QtGui.QPainter()
        qtPainter.begin(self)
        if self.image:
            qtPainter.drawImage(QtCore.QPoint(0, 0), self.image)
        qtPainter.end()

    def closeEvent(self, event):
        self.videoStream.stop()
