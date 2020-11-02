import time

import cv2

from ImageProceccing.Lab1.task1.metrics import *


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
                S = delta / Cmax

            V = Cmax

            # rounding
            H = round(H / 360 * 255)
            S = round(S * 255)
            V = round(V * 255)

            src[x, y, :] = (H, S, V)


def my_hsv_2_rgb(src):
    width = src.shape[0]
    height = src.shape[1]
    for x in range(width):
        for y in range(height):
            H = src[x, y, 0] / 255 * 360
            S = src[x, y, 1] / 255
            V = src[x, y, 2] / 255

            C = V * S
            X = C * (1 - abs((H / 60) % 2 - 1))
            m = V - C

            if 0 <= H < 60:
                r, g, b = C, X, 0
            elif 60 <= H < 120:
                r, g, b = X, C, 0
            elif 120 <= H < 180:
                r, g, b = 0, C, X
            elif 180 <= H < 240:
                r, g, b = 0, X, C
            elif 240 <= H < 300:
                r, g, b = X, 0, C
            elif 300 <= H <= 360:
                r, g, b = C, 0, X
            r = (r + m) * 255
            g = (g + m) * 255
            b = (b + m) * 255
            src[x, y, :] = (r, g, b)


def brightness_rgb(src, value):
    width = src.shape[0]
    height = src.shape[1]
    for x in range(width):
        for y in range(height):
            R = src[x, y, 0]
            G = src[x, y, 1]
            B = src[x, y, 2]

            R = max(0, min(R + value, 255))
            G = max(0, min(G + value, 255))
            B = max(0, min(B + value, 255))

            src[x, y, :] = (R, G, B)


def brightness_hsv(src, value):
    width = src.shape[0]
    height = src.shape[1]
    for x in range(width):
        for y in range(height):
            V = src[x, y, 2]

            V = max(0, min(V + value, 255))

            src[x, y, 2] = V


# shows source image
img = cv2.imread("img.png")
cv2.imshow('original', img)

# shows HSVed by me image
start_time_my_HSV = time.time()
my_rgb_2_hsv(img)
time_my_HSV = time.time() - start_time_my_HSV
cv2.imshow('HSV_my', img)

# shows HSVed by CV image
img2 = cv2.imread("img.png")
start_time_cv_HSV = time.time()
hsv_cv = cv2.cvtColor(img2, cv2.COLOR_RGB2HSV)
time_cv_HSV = time.time() - start_time_cv_HSV
cv2.imshow('HSV_cv', hsv_cv)

print("Схожесть RGB -> HSV")
print(psnr(img, hsv_cv))
print("По внешнему виду изображения практически практически не отличаются")
print("Время выполнения конвертации по формуле: ", time_my_HSV)
print("Время выполнения конвертации в OpenCV: ", time_cv_HSV)
print("В OpenCV изображение обрабатывается гораздо быстрее.")

img3 = img
start_time_my_RGB = time.time()
my_hsv_2_rgb(img3)
time_my_RGB = time.time() - start_time_my_RGB
cv2.imshow("RGB_my", img3)

start_time_cv_RGB = time.time()
rgb_cv = cv2.cvtColor(hsv_cv, cv2.COLOR_HSV2RGB)
time_cv_RGB = time.time() - start_time_cv_RGB
cv2.imshow("RGB_cv", rgb_cv)
print("Схожесть HSV -> RGB")
print(psnr(rgb_cv, img3))
print("По внешнему виду изображения практически практически не отличаются")
print("Время выполнения конвертации по формуле: ", time_my_RGB)
print("Время выполнения конвертации в OpenCV: ", time_cv_RGB)
print("В OpenCV изображение обрабатывается гораздо быстрее.")

start_time_brit_rgb = time.time()
brightness_rgb(img3, 150)
time_brit_rgb = time.time() - start_time_brit_rgb
cv2.imshow("brightness_my", img3)

start_time_brit_hsv = time.time()
brightness_hsv(hsv_cv, 200)
rgb_cv = cv2.cvtColor(hsv_cv, cv2.COLOR_HSV2RGB)
time_brit_hsv = time.time() - start_time_brit_hsv
cv2.imshow("brightness_hsv", rgb_cv)

print("Схожесть яркости RGB and HSV")
print(psnr(img3, rgb_cv))
print("Время выполнения конвертации по RGB: ", time_brit_rgb)
print("Время выполнения конвертации по HSV: ", time_brit_hsv)

cv2.waitKey()
