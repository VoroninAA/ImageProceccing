import copy

from ImageProceccing.Lab2.task1.task1 import *
from PIL import Image

def get_possible_value(cur, min, max):
    if cur < min:
        return round(min)
    if cur > max:
        return round(max)
    return round(cur)


def process_image(source_image, processing_type):
    processing_image = source_image
    width, height = processing_image.size
    if processing_type == 1:
        for i in range(width):
            for j in range(height):
                processing_image.putpixel((i, j), (get_median(processing_image, i, j)))
    else:
        for i in range(0, width):
            for j in range(0, height):
                processing_image.putpixel((i, j), (gaussian_filter(processing_image, i, j)))
    return processing_image


def get_median(source_image, x, y):
    radius_x = 3 // 2
    radius_y = 3 // 2
    resultR = 0
    resultG = 0
    resultB = 0
    width, height = source_image.size
    arr_ = []
    arr = []
    for i in range(-radius_x, radius_x + 1):
        for j in range(-radius_y, radius_y + 1):
            idX = get_possible_value(x + i, 0, width - 1)
            idY = get_possible_value(y + j, 0, height - 1)
            resultR, resultG, resultB = source_image.getpixel((idX, idY))
            tmp = (resultR + resultG + resultB) // 3
            arr.append(tmp)
            arr_.append((resultR, resultG, resultB))
    arr.sort()
    for l in arr_:
        resultR, resultG, resultB = l
        tmp = (resultR + resultG + resultB) // 3
        if (tmp == arr[4]):
            return (resultR, resultG, resultB)
    return (0, 0, 0)


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
    width, height = source_image.size
    kernel = get_gaussian_kernel(3, 3)
    resultR = 0
    resultG = 0
    resultB = 0
    for i in range(-radius_x, radius_x + 1):
        for j in range(-radius_y, radius_y + 1):
            idX = get_possible_value(x + i, 0, width - 1)
            idY = get_possible_value(y + j, 0, height - 1)
            neighbor_colorR, neighbor_colorG, neighbor_colorB,  = source_image.getpixel((idX, idY));
            resultR += neighbor_colorR * kernel[i + radius_x, j + radius_y]
            resultG += neighbor_colorG * kernel[i + radius_x, j + radius_y]
            resultB += neighbor_colorB * kernel[i + radius_x, j + radius_y]

    return get_possible_value(resultR, 0, 255), get_possible_value(resultG, 0, 255), get_possible_value(resultB, 0, 255)


if __name__ == "__main__":
    noised_image = Image.open('../images/testimage2.jpg')
    source_img = cv2.cvtColor(np.array(noised_image), cv2.COLOR_RGB2BGR)  # convert from PIL to cv2
    cv2.imshow('Source_image', source_img)

    # Check the median filter result
    median = process_image(noised_image, 1)
    median_img = cv2.cvtColor(np.array(median), cv2.COLOR_RGB2BGR)  # convert from PIL to cv2
    cv2.imshow('Median_image', median_img)

    # Check the gaussian filter result
    gaussian = process_image(noised_image, 2)
    gaussian_img = cv2.cvtColor(np.array(gaussian), cv2.COLOR_RGB2BGR)  # convert from PIL to cv2
    cv2.imshow('Gaussian_image', gaussian_img)

    cv2.waitKey()
