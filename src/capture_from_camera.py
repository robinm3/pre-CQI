import threading
import cv2
from threading import Thread, Condition, current_thread
from shape_detector import are_two_images_similar


class ShapeImageCaptor():

    def __init__(self):
        self._capture = cv2.VideoCapture(2)
        self.queue = []
        self.lock = threading.Lock()

    def launch(self):
        self._thread = Thread(target=self._loop)
        self._running = True
        self._thread.start()
        print("Launched video capture thread")

    def stop(self):
        self._running = False
        self._thread.join()
        print("Stopped video capture thread")

    def _loop(self):
        lastImage = None
        while(self._running):
            success, currentImage = self._capture.read()

            if success and not are_two_images_similar(lastImage, currentImage):
                lastImage = currentImage
                with self.lock:
                    self.queue.append(currentImage)
                    print(f"New shape found. Current queue size: {len(self.queue)}")

