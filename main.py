from capture_from_camera import capture_from_camera
from send_to_server import send_to_server

if __name__ == '__main__':
    cap = capture_from_camera()

    lastImage = None
    while True:
        success, img = cap.read()
        if success and img != lastImage:
            lastImage = img

            shapes = detect_shape(img)

            send_to_server(shapes)





