import cv2

from send_to_server import send_to_server

if __name__ == '__main__':
    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10, 150)

    lastImage = None
    while True:
        success, img = cap.read()
        if success and img != lastImage:
            lastImage = img

            shapes = detect_shape(img)

            send_to_server(shapes)





