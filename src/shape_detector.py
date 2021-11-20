import cv2


def detect_shape(image):
    image = cv2.imread(image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, threshold = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        print("circle")
        return "circle"

    approx = cv2.approxPolyDP(contours[1], 0.005 * cv2.arcLength(contours[1], True), True)

    if len(approx) == 4:
        print("square")
        return "square"

    elif len(approx) == 3:
        print("croix")
        return "croix"

    else:
        print("arrow")
        return "arrow"
        

if __name__ == '__main__':
    detect_shape("../img/square.png")
    print("-------------------")
    detect_shape("../img/arrow.png")
    print("-------------------")
    detect_shape("../img/circle.png")
    print("-------------------")
    detect_shape("../img/croix.png")

