import time

from ImageProceccing.Lab2.task2.task2 import *

if __name__ == "__main__":
    noised_image = Image.open('../images/testimage2.jpg')
    source_img = cv2.cvtColor(np.array(noised_image), cv2.COLOR_RGB2BGR)

    start_time_median_cv = time.time()
    median_cv = cv2.medianBlur(source_img, 5)
    cv2.imshow('source_image', source_img)
    cv2.imshow('median_cv_image', median_cv)
    time_median_cv = time.time() - start_time_median_cv
    print("Время обработки медианного фильра от opencv =  ", time_median_cv)

    start_time_median = time.time()
    median = process_image(noised_image, 1)
    median_img = cv2.cvtColor(np.array(median), cv2.COLOR_RGB2BGR)
    cv2.imshow('my_median_image', median_img)
    time_median = time.time() - start_time_median
    print("Время обработки медианного фильра собственной реализации =  ", time_median)

    start_time_gaussian_cv = time.time()
    gaussian_cv = cv2.GaussianBlur(source_img, (5, 5), 0)
    cv2.imshow('gaussian_cv_image', gaussian_cv)
    time_gaussian_cv = time.time() - start_time_gaussian_cv
    print("Время обработки фильра Гаусса от opencv =  ", time_gaussian_cv)

    start_time_gaussian = time.time()
    gaussian = process_image(noised_image, 2)
    gaussian_img = cv2.cvtColor(np.array(gaussian), cv2.COLOR_RGB2BGR)  # convert from PIL to cv2
    cv2.imshow('my_gaussian_image', gaussian_img)
    time_gaussian = time.time() - start_time_gaussian
    print("Время обработки фильра Гаусса собственной реализации =  ", time_gaussian)

    cv2.waitKey()
