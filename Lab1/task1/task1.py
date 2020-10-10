import cv2

from Lab1.task1.metrics import *

img = cv2.imread("firstimage.jpg", 1)
img2 = cv2.imread("secondimage.jpg", 1)
print(psnr(img, img2))
cv2.imshow('image', img)
cv2.imshow('image2', img2)
cv2.waitKey(10000)
