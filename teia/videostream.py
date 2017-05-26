import sys
import cv2
import numpy
from threading import Thread
from PyQt5 import QtCore, QtGui
import face_recognition

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

    def run(self):
        self.stream = cv2.VideoCapture(-1)

        while self.streaming:
            self.grabbed, self.frame = self.stream.read()

            img = cv2.resize(self.frame, (self.window_width, self.window_height), interpolation=cv2.INTER_CUBIC)

            if self.target != None:
                img = self.facereq(img)

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


    def facereq(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        face_locations = []
        face_names = []
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces([self.target], face_encoding)
            name = "Desconhecido"

            if match[0]:
                name = "Alvo encontrado"

            face_names.append(name)

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        return frame
