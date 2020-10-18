import copy

from Lab2.task1.task1 import *


def get_possible_value(cur, min, max):
    if cur < min:
        return min
    if cur > max:
        return max
    return cur


def process_image(source_image, processing_type):
    processing_image = copy.copy(source_image)
    if processing_type == 1:
        for i in range(0, processing_image.shape[0] - 1):
            for j in range(0, processing_image.shape[1] - 1):
                processing_image[i, j] = get_median(processing_image, i, j)
    else:
        for i in range(0, processing_image.shape[0] - 1):
            for j in range(0, processing_image.shape[1] - 1):
                processing_image[i, j] = gaussian_filter(processing_image, i, j)
    return processing_image


def get_median(source_image, x, y):
    radius_x = 3 // 2
    radius_y = 3 // 2
    result = np.arange(9, dtype=np.uint8)
    for i in range(-radius_x, radius_x + 1):
        for j in range(-radius_y, radius_y + 1):
            idX = get_possible_value(x + i, 0, source_image.shape[0] - 1)
            idY = get_possible_value(y + j, 0, source_image.shape[1] - 1)
            neighbor_color = source_image[idX, idY];
            array_pointer = np.uint8(i + radius_x + (j + radius_y) * 3)
            result[array_pointer] = neighbor_color
    result.sort()
    return result[4]


def get_gaussian_kernel(radius, sigma):
    size = 2 * radius + 1;
    result = np.ndarray(shape=(size, size), dtype=np.float)
    norm = np.float64(0)
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            result[i + radius, j + radius] = math.exp(-(i * i + j * j) / (2 * sigma * sigma)) * (
                    1 / (2 * math.pi * sigma * sigma))
            norm += np.float(result[i + radius][j + radius])

    for i in range(0, size):
        for j in range(0, size):
            result[i, j] /= norm
    return result * 7


def gaussian_filter(source_image, x, y):
    radius_x = 3 // 2
    radius_y = 3 // 2
    kernel = get_gaussian_kernel(3, 3)
    result = 0
    for i in range(-radius_x, radius_x + 1):
        for j in range(-radius_y, radius_y + 1):
            idX = get_possible_value(x + i, 0, source_image.shape[0] - 1)
            idY = get_possible_value(y + j, 0, source_image.shape[1] - 1)
            neighbor_color = source_image[idX, idY]
            result += neighbor_color * kernel[i + radius_x, j + radius_y]

    return get_possible_value(result, 0, 255)


if __name__ == "__main__":
    image = cv2.imread('../images/testimage.jpg', 0)
    noised_image = gaussian_noise(image)

    # Check the median filter result
    median = process_image(noised_image, 1)
    show_two_images(median, noised_image)

    # Check the gaussian filter result
    gaussian = process_image(noised_image, 2)
    show_two_images(gaussian, noised_image)
