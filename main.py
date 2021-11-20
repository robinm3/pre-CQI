from capture_from_camera import capture_from_camera
from send_to_server import ServerCommunicator
from shape_detector import detect_shape

if __name__ == '__main__':
    #test, to be removed
    detect_shape("square.png")

    server = ServerCommunicator()
    cap = capture_from_camera()

    lastImage = None
    shapeList = []

    while True:
        success, img = cap.read()
        if success and img != lastImage:
            lastImage = img

            shape = detect_shape(img)
            shapeList.append(shape)

        if len(shapeList) > 4:
            server.send(shapeList)
            shapeList = []
