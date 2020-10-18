import time

from Lab2.task2.task2 import *

if __name__ == "__main__":
    image = cv2.imread('../images/testimage.jpg', 0)
    noised_image = gaussian_noise(image)

    start_time_median_cv = time.time()
    median_cv = cv2.medianBlur(image, 5)
    show_two_images(noised_image, median_cv)
    time_median_cv = time.time() - start_time_median_cv
    print("Время обработки медианного фильра от opencv =  ", time_median_cv)

    start_time_median = time.time()
    median = process_image(noised_image, 1)
    show_two_images(noised_image, median)
    time_median = time.time() - start_time_median
    print("Время обработки медианного фильра собственной реализации =  ", time_median)

    start_time_gaussian_cv = time.time()
    gaussian_cv = cv2.GaussianBlur(image, (5, 5), 0)
    show_two_images(noised_image, gaussian_cv)
    time_gaussian_cv = time.time() - start_time_gaussian_cv
    print("Время обработки фильра Гаусса от opencv =  ", time_gaussian_cv)

    start_time_gaussian = time.time()
    gaussian = process_image(noised_image, 2)
    show_two_images(noised_image, gaussian)
    time_gaussian = time.time() - start_time_gaussian
    print("Время обработки фильра Гаусса собственной реализации =  ", time_gaussian)
