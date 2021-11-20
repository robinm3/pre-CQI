import time
import cv2

from capture_from_camera import VideoFeed
from send_to_server import ServerCommunicator
from shape_detector import detect_shape

if __name__ == '__main__':

    server = ServerCommunicator()
    
    video_feed = VideoFeed()

    while(1):
        video_feed.show_frame()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    lastImage = None
    shapeList = []

    while True:
        success, img = cap.read()
        cv2.imshow('img', img)
        time.sleep(10)
        if success and img != lastImage:
            lastImage = img

            shape = detect_shape(img)
            shapeList.append(shape)

        if len(shapeList) > 4:
            server.send(shapeList)
            shapeList = []
