import cv2


def detect_shape(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print("circle")
        return "circle"

    for contour in contours:

        area = cv2.contourArea(contour)

        if area > 5000:

            approx = cv2.approxPolyDP(contour, 0.005 * cv2.arcLength(contour, True), True)

            if len(approx) == 4:
                print("square")
                return "square"

            elif len(approx) == 12:
                print("croix")
                return "croix"

            elif len(approx) == 7:
                print("arrow")
                return "arrow"
            

if __name__ == '__main__':
    detect_shape(cv2.imread("../img/square.png"))
    print("-------------------")
    detect_shape(cv2.imread("../img/arrow.png"))
    print("-------------------")
    detect_shape(cv2.imread("../img/circle.png"))
    print("-------------------")
    detect_shape(cv2.imread("../img/croix.png"))

