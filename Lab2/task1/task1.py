import cv2
import numpy as np

from ImageProceccing.Lab1.task1.metrics import *

# d - deviation
# sourceimage - s(i, j)
def gaussian_noise2(sourceimage, d):
    # calculating PDF (gaussian)
    mean = np.mean(sourceimage)
    K = 1 / d * np.sqrt(2 * np.pi)
    prob = np.e ** (-(sourceimage - mean)**2 / (2*d*d)) * K

    # calculating n(i, j) - simple noise
    rand = np.random.normal(0, 20, size=[sourceimage.shape[0], sourceimage.shape[1], sourceimage.shape[2]])
    rand = np.uint8(rand)

    # calucalatin f(i, j)
    width = sourceimage.shape[0]
    height = sourceimage.shape[1]
    noised_image = sourceimage + 0
    for x in range(width):
        for y in range(height):
            for i in range(3):
                if np.random.random() * K < prob[x,y,i]:
                    noised_image[x, y, i] += rand[x, y, i]

    noised_image[noised_image < 0] = 0
    noised_image[noised_image > 255] = 255
    return noised_image

if __name__ == "__main__":
    image = cv2.imread('../images/testimage.jpg', 1)
    noised_image = gaussian_noise2(image, 10)
    cv2.imshow('source_image', image)
    cv2.imshow('noised_image', noised_image)
    cv2.waitKey(30000)

