from ImageProceccing.Lab2.task1.task1 import *

image = cv2.imread('../images/testimage2.jpg')
#noised_image = gaussian_noise(image)
median = cv2.medianBlur(image, 5)
gaussian = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('source_image', image)
cv2.imshow('medianBlur_image', median)
cv2.imshow('GaussianBlur_image', gaussian)
cv2.waitKey()
