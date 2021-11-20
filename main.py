from capture_from_camera import capture_from_camera
from send_to_server import send_to_server

if __name__ == '__main__':
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
            send_to_server(shapeList)
            shapeList = []
