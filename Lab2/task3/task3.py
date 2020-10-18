from Lab2.task1.task1 import *

image = cv2.imread('../images/testimage.jpg', 0)
noised_image = gaussian_noise(image)
median = cv2.medianBlur(image, 5)
gaussian = cv2.GaussianBlur(image, (5, 5), 0)
show_two_images(noised_image, gaussian)
show_two_images(noised_image, median)
