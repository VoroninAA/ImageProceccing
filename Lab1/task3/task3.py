import cv2
import numpy as np
import math
from PIL import Image
from Lab1.task1.metrics import *


def my_rgb_2_hsv(src):
    width = src.shape[0]
    height = src.shape[1]
    for x in range(width):
        for y in range(height):
            R = src[x, y, 0]
            G = src[x, y, 1]
            B = src[x, y, 2]
            R = R / 255
            G = G / 255
            B = B / 255
            Cmax = np.maximum(np.maximum(R, G), B)
            Cmin = np.minimum(np.minimum(R, G), B)
            delta = Cmax - Cmin

            # calculating H
            if delta == 0:
                H = 0
            elif Cmax == R:
                H = 60 * (((G - B) / delta) % 6)
            elif Cmax == G:
                H = 60 * ((B - R) / delta + 2)
            elif Cmax == B:
                H = 60 * ((R - G) / delta + 4)

            # calculating S
            if Cmax == 0:
                S = 0
            else:
                S = delta/Cmax

            V = Cmax

            # rounding
            H = round(H / 360 * 255)
            S = round(S * 255)
            V = round(V * 255)

            src[x, y, :] = (H, S, V)


# shows source image
img = cv2.imread("img.jpg")
cv2.imshow('original', img)

# shows HSVed by me image
my_rgb_2_hsv(img)
cv2.imshow('HSC_my', img)

# shows HSVed by CV image
img2 = cv2.imread("img.jpg")
hsv_cv = cv2.cvtColor(img2, cv2.COLOR_RGB2HSV)
cv2.imshow('HSV_cv', hsv_cv)


cv2.waitKey()

