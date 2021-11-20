import cv2

if __name__ == "__main__":
    capture = cv2.VideoCapture(2)

    while True:
        ret, frame = capture.read()
    
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    