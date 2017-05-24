import sys
import cv2
import numpy
from threading import Thread
from PyQt5 import QtCore, QtGui

class VideoThread(QtCore.QThread):

    newFrame = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, window_width, window_height, parent=None):
        super(VideoThread, self).__init__(parent)

        # initialize the video camera stream
        self.stream = VideoStream(src=-1).start()

        # read the first frame from the stream
        self.frame = self.stream.read()

        # initialize the variable used to indicate if the thread should be stopped
        self.stopped = False
        self.window_height = window_height
        self.window_width = window_width

    def run(self):
        # keep looping infinitely until the thread is stopped
        while True:

            # if the thread indicator variable is set, stop the thread
            if self.stopped:

                # stop camera thread
                self.stream.stop()
                return

            # read the next frame from the stream
            self.frame = self.stream.read()

            # resize the frame to the size of the window
            img = cv2.resize(self.frame, (self.window_width, self.window_height), interpolation=cv2.INTER_CUBIC)

            # convert the color from cv2 to QImage format
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # get the dimensions of the image
            height, width, bpc = img.shape
            bpl = bpc * width

            # convert image to QImage
            # QImage class provides a hardware-independent image representation that allows direct access to the pixel data, and can be used as a paint device
            image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)

            # emit signal from thread
            self.newFrame.emit(image)

    def stop(self):

        # indicate that the thread should be stopped
        self.stopped = True

class VideoStream:
    def __init__(self, src=-1):

        # initialize the video camera stream and read the first frame from the stream
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()

        # initialize the variable used to indicate if the thread should be stopped
        self.stopped = False

    def start(self):

        # start the thread to read frames from the video stream
        Thread(target=self.update, args=()).start()

        return self

    def update(self):

        # keep looping infinitely until the thread is stopped
        while True:

           # if the thread indicator variable is set, stop the thread
            if self.stopped:

                return

            # otherwise, read the next frame from the stream
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):

        # return the frame most recently read
        return self.frame

    def stop(self):

        # indicate that the thread should be stopped
        self.stopped = True
