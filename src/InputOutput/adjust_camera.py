import cv2

if __name__ == "__main__":
    capture = cv2.VideoCapture(2)

    while True:
        ret, frame = capture.read()

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    