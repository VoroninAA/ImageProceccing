import cv2
import numpy as np

from Lab3.task1.task1 import canny

if __name__ == "__main__":
    img = cv2.imread('../images/img.jpg', 1)
    cv_canny = cv2.Canny(img, 75, 255)
    my_canny = canny(img)
    cv2.imshow('cv2 image', cv_canny)
    cv2.imshow('my image', np.uint8(my_canny))
    cv2.waitKey()
