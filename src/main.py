import cv2

from send_to_server import ServerCommunicator
from shape_detector import detect_shape, are_two_images_similar

if __name__ == '__main__':

    server = ServerCommunicator()
    
    cap = cv2.VideoCapture(2)

    lastImage = None
    shapeList = []

    while True:
        success, img = cap.read()

        if success and not are_two_images_similar(lastImage, img):
            lastImage = img

            shape = detect_shape(img)
            if shape:
                shapeList.append(shape)

        if len(shapeList) > 4:
            server.send(shapeList)
            shapeList = []
