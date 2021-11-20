from src.InputOutput.ServerCommunicator import ServerCommunicator
from ShapeDetector import ShapeDetector
from src.InputOutput.ShapeImageCaptor import ShapeImageCaptor

if __name__ == '__main__':

    server = ServerCommunicator()
    shape_image_captor = ShapeImageCaptor()
    shape_detector = ShapeDetector()
    currentShapeList = []

    shape_image_captor.launch()

    while True:
        if shape_image_captor.queue:
            with shape_image_captor.lock:
                image = shape_image_captor.queue.pop()
            shape = shape_detector.detect_shape(image)
            print(f"Evaluation of shape: {shape}")
            if shape and isinstance(shape, str):
                currentShapeList.append(shape)
            if len(currentShapeList) > 4:
                server.send(currentShapeList)
                currentShapeList = []
