import numpy as np

from capture_from_camera import capture_from_camera
from send_to_server import ServerCommunicator
from shape_detector import detect_shape, are_two_images_similar

if __name__ == '__main__':

    server = ServerCommunicator()
    cap = capture_from_camera()

    lastImage = None
    shapeList = []

    while True:
        success, img = cap.read()

        if success and not are_two_images_similar(lastImage, img):
            lastImage = img

            shape = detect_shape(img)
            if shape and isinstance(shape, str):
                shapeList.append(shape)

        if len(shapeList) > 4:
            server.send(shapeList)
            shapeList = []
