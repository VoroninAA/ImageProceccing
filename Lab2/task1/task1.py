import cv2
import numpy as np

from ImageProceccing.Lab1.task1.metrics import *

# TODO  refactor noise generation as im not sure if its right

def show_two_images(source_image, noised_image):
    cv2.imshow('Result Image ', source_image)
    cv2.imshow('Noised Image', noised_image)


def gaussian_noise(sourceimage):
    rand = np.random.normal(0, 9, size=[sourceimage.shape[0], sourceimage.shape[1]])
    rand = np.uint8(rand)
    noised_img = sourceimage + rand
    noised_img[noised_img < 0] = 0
    noised_img[noised_img > 255] = 255
    return noised_img


if __name__ == "__main__":
    image = cv2.imread('../images/testimage.jpg', 0)
    noised_image = gaussian_noise(image)
    cv2.imshow('source_image', image)
    cv2.imshow('noised_image', noised_image)
    cv2.waitKey(3000)

