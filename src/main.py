from src.InputOutput.ServerCommunicator import ServerCommunicator
from shape_detector import detect_shape
from src.InputOutput.ShapeImageCaptor import ShapeImageCaptor

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
