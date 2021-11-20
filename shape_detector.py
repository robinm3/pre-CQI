import cv2


def detect_shape(image):
    image = cv2.imread(image)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, threshold = cv2.threshold(gray_image, 240, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        print(approx)
        if len(approx) == 4:
            print(approx, "square")

        if len(approx) == 12:
            print(approx, "croix")

        if len(approx) == 7:
            print(approx, "arrow")


if __name__ == '__main__':
    detect_shape("square.png")
    print("-------------------")
    detect_shape("arrow.png")
    print("-------------------")
    detect_shape("circle.png")
