import cv2
import numpy as np
import math
from PIL import Image
from Lab1.task1.metrics import *

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
opencvImage2 = cv2.cvtColor(np.array(img2), cv2.COLOR_RGB2BGR)  #convert from PIL to cv2
cv2.imshow('my_averange', opencvImage2)

img3 = cv2.imread("firstimage.jpg")
gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
img3 = np.zeros_like(img)
img3[:,:,0] = gray
img3[:,:,1] = gray
img3[:,:,2] = gray
cv2.imshow('cv_GrayScale', img3)

print(calculate_ssim(opencvImage2, img3))
print(PSNR(opencvImage2, img3))
cv2.waitKey()
