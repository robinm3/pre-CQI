import cv2
import numpy as np


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


def are_two_images_similar(image1, image2):
    diffLevel = 0.5
    if image1 is None:
        return False
    average1 = np.average(np.average(np.average(image1, axis=0), axis=0))
    average2 = np.average(np.average(np.average(image2, axis=0), axis=0))
    if average1 - diffLevel <= average2 <= average1 + diffLevel:
        return True
    return False

def detect_png(image):
    image1 = cv2.imread(image)
    detect_shape(image1)


if __name__ == '__main__':
    detect_png("../img/square.png")
    print("-------------------")
    detect_png("../img/arrow.png")
    print("-------------------")
    detect_png("../img/circle.png")
    print("-------------------")
    detect_png("../img/croix.png")
