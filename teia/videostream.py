import sys
import cv2
import numpy
from threading import Thread
from PyQt5 import QtCore, QtGui

class VideoStream(QtCore.QThread):

    newFrame = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, parent=None):
        super(VideoStream, self).__init__(parent)
        self.streaming = True
        
    def run(self):
        self.stream = cv2.VideoCapture(-1)

        while self.streaming:
            self.grabbed, self.frame = self.stream.read()

            img = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            height, width, bpc = img.shape
            bpl = bpc * width

            image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)

            self.newFrame.emit(image)

        self.stream.release()

    def quit(self):
        self.streaming = False
