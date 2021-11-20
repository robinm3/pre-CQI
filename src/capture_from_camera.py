import cv2


class ShapeImageCaptor():

    def __init__(self):
        self.queue = []
        self._capture = cv2.VideoCapture(2)

    def clear(self):
        self.queue = []

    def show_frame(self):
        ret, frame = self._capture.read()
        cv2.imshow('frame', frame)
