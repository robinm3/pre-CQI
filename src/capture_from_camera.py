import cv2


class VideoFeed():

    def __init__(self):
        self._capture = cv2.VideoCapture(2)

    def get_ca

    def clear(self):
        self.queue = []

    def show_frame(self):
        ret, frame = self._capture.read()
        cv2.imshow('frame', frame)
