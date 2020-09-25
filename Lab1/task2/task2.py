import cv2
import numpy as np
import math
from PIL import Image
import sys
sys.path.insert(0, '..\task1\task1')
import task1

def my_average(img, img2):
    width, height = img.size
    for x in range(width):
        for y in range(height):
            R1, G1, B1 = img.getpixel((x, y))
            New_color = round((R1 + G1 + B1) / 3)
            img2.putpixel((x, y), (New_color, New_color, New_color))

img = Image.open("firstimage.jpg")
img.show()
img2 = img
my_average(img, img2)

img3 = cv2.imread("firstimage.jpg")
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

img2.show()
cv2.imshow('image', img3)
cv2.waitKey()
