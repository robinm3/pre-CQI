import cv2
import numpy as np


class ShapeDetector:

    def __init__(self):
        pass

    def detect_shape(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray_image, 135, 255, cv2.THRESH_BINARY)
        threshold = cv2.bitwise_not(threshold)

        contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) == 0:
            return "circle"

        for contour in contours:
            area = cv2.contourArea(contour)

            if area > 500:

                approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

                if len(approx) == 4:
                    return "square"

                elif len(approx) == 12:
                    return "plus"
                else:
                    return "arrow"

    def detect_png(self, image):
        image1 = cv2.imread(image)
        return self.detect_shape(image1)


def are_two_images_similar(image1, image2):
    if image1 is None or image2 is None:
        return False

    precision_black_bytes = 1
    precision_average_color = 1

    if len(image1) < 1 or len(image2) < 1:
        return False
    non_zero = np.sum(image1 == 255)
    non_zero2 = np.sum(image2 == 255)
    average1 = np.average(np.average(np.average(image1, axis=0), axis=0))
    average2 = np.average(np.average(np.average(image2, axis=0), axis=0))

    if abs(non_zero - non_zero2) <= precision_black_bytes or abs(average1 - average2) <= precision_average_color:
        return True
    return False


if __name__ == '__main__':
    shapeDetector = ShapeDetector()
    print(shapeDetector.detect_png("../img/square.png"))
    print("-------------------")
    print(shapeDetector.detect_png("../img/arrow.png"))
    print("-------------------")
    print(shapeDetector.detect_png("../img/circle.png"))
    print("-------------------")
    print(shapeDetector.detect_png("../img/croix.png"))
