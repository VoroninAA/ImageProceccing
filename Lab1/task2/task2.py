from PIL import Image
from Lab1.task1.metrics import *
import cv2
import time
def my_average(img, img2):
    width, height = img.size
    for x in range(width):
        for y in range(height):
            R1, G1, B1 = img.getpixel((x, y))
            New_color = round((R1 + G1 + B1) / 3)
            img2.putpixel((x, y), (New_color, New_color, New_color))

# shows source image
img = Image.open("firstimage.jpg")
img.show()
# shows average by me image
img2 = img
start_time_my_average = time.time()
my_average(img, img2)
opencvImage2 = cv2.cvtColor(np.array(img2), cv2.COLOR_RGB2BGR)  #convert from PIL to cv2
time_my_average = time.time() - start_time_my_average
cv2.imshow('my_averange', opencvImage2)

# shows average by me cv
img3 = cv2.imread("firstimage.jpg")
start_time_cv_average = time.time()
gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
img3 = np.zeros_like(img)
img3[:,:,0] = gray
img3[:,:,1] = gray
img3[:,:,2] = gray
time_cv_average = time.time() - start_time_cv_average
cv2.imshow('cv_GrayScale', img3)

print("Схожесть изображений: ",psnr(opencvImage2, img3))
print("По внешнему виду изображения практически практически не отличаются")
print("Время выполнения конвертации по формуле: ", time_my_average)
print("Время выполнения конвертации в OpenCV: ", time_cv_average)
print("В OpenCV изображение обрабатывается гораздо быстрее.")
cv2.waitKey()
