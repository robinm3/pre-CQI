import cv2

from send_to_server import ServerCommunicator
from shape_detector import detect_shape, are_two_images_similar
from capture_from_camera import ShapeImageCaptor

if __name__ == '__main__':

    server = ServerCommunicator()
    shape_image_captor = ShapeImageCaptor()
    currentShapeList = []

    shape_image_captor.launch()

    while True:
        if shape_image_captor.queue:
            with shape_image_captor.lock:
                image = shape_image_captor.queue.pop()
            shape = detect_shape(image)
            print (f"Evaluation of shape: {shape}")
            if shape and isinstance(shape, str):
                currentShapeList.append(shape)
            if len(currentShapeList) > 4:
                server.send(currentShapeList)
                currentShapeList = []
