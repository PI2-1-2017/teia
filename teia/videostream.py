import sys
import cv2
import numpy as np
from threading import Thread
from PyQt5 import QtCore, QtGui
import face_recognition
import dlib
import openface
from skimage.feature import local_binary_pattern

class VideoStream(QtCore.QThread):

    newFrame = QtCore.pyqtSignal(QtGui.QImage)

    def __init__(self, window_width, window_height, target=None, parent=None):
        super(VideoStream, self).__init__(parent)
        self.streaming = True
        self.window_height = window_height
        self.window_width = window_width
        if target:
            self.setTarget(target)
        self.target = None
        self.predictor = dlib.shape_predictor("./models/shape_predictor_68_face_landmarks.dat")
        self.detector = dlib.get_frontal_face_detector()
        self.face_aligner = openface.AlignDlib("./models/shape_predictor_68_face_landmarks.dat")

    def run(self):
        # url = urllib.request.urlopen('http://localhost:8090/cam2.mjpeg')
        self.stream = cv2.VideoCapture('http://localhost:8090/cam2.mjpeg')

        while self.streaming:
            self.grabbed, self.frame = self.stream.read()

            small_frame = cv2.resize(self.frame, (0, 0), fx=0.25, fy=0.25)
            face_locations = self.detector(small_frame, 1)
            aligned_faces = []
            for k, d in enumerate(face_locations):
                shape = self.predictor(small_frame, d)
                cv2.rectangle(self.frame, (shape.rect.left()*4, shape.rect.top()*4), (shape.rect.right()*4, shape.rect.bottom()*4), (0, 255, 0), 1)

                aligned_face = self.face_aligner.align(534, small_frame, d, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
                aligned_faces.append(aligned_face)

            if self.target != None:
                for face in aligned_faces:
                    self.lbp_match(self.target, face)

            img = cv2.resize(self.frame, (self.window_width, self.window_height), interpolation=cv2.INTER_CUBIC)

            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            height, width, bpc = img.shape
            bpl = bpc * width

            image = QtGui.QImage(img.data, width, height, bpl, QtGui.QImage.Format_RGB888)

            self.newFrame.emit(image)

        self.stream.release()

    def quit(self):
        self.streaming = False

    def setTarget(self, target):
        image = face_recognition.load_image_file(target)
        self.target = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def kullback_leibler_divergence(self, p, q):
        p = np.asarray(p)
        q = np.asarray(q)
        filt = np.logical_and(p != 0, q != 0)

        return np.sum(p[filt] * np.log2(p[filt] / q[filt]))

    def lbp_match(self, ref, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        lbp = local_binary_pattern(img, 24, 8, 'uniform')
        n_bins = int(lbp.max() + 1)
        hist, _ = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))
        ref_hist, _ = np.histogram(ref, normed=True, bins=n_bins, range=(0, n_bins))
        score = self.kullback_leibler_divergence(hist, ref_hist)
        print (score)
        if score < 0.8:
            return True
        return False
