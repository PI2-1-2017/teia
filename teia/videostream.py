import sys
import cv2
import numpy
from threading import Thread
from PyQt5 import QtCore, QtGui
import face_recognition
import dlib
import openface

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
        self.stream = cv2.VideoCapture(-1)

        while self.streaming:
            self.grabbed, self.frame = self.stream.read()

            small_frame = cv2.resize(self.frame, (0, 0), fx=0.25, fy=0.25)
            face_locations = self.detector(small_frame, 1)
            aligned_faces = []
            for k, d in enumerate(face_locations):
                shape = self.predictor(small_frame, d)
                cv2.rectangle(self.frame, (shape.rect.left()*4, shape.rect.top()*4), (shape.rect.right()*4, shape.rect.bottom()*4), (0, 255, 0), 1)

                aligned_face = self.face_aligner.align(534, small_frame, d, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
                aligned_faces.push(aligned_face)



            # for (top, right, bottom, left) in (face_locations):
            #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            #     top *= 4
            #     right *= 4
            #     bottom *= 4
            #     left *= 4
            #
            #     # Draw a box around the face
            #     cv2.rectangle(self.frame, (left, top), (right, bottom), (0, 255, 0), 1)

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
        self.target = face_recognition.face_encodings(image)[0]


    def facereq(self, face_locations):
        for (top, right, bottom, left) in (face_locations):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 1)

        return frame
