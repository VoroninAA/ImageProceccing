import cv2
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy


def gaussian_smoothing(input_img):
    gaussian_filter = np.array([[0.109, 0.111, 0.109],
                                [0.111, 0.135, 0.111],
                                [0.109, 0.111, 0.109]])

    return cv2.filter2D(input_img, -1, gaussian_filter)


def canny_edge_detection(input):
    input = input.astype('uint8')

    # Using OTSU thresholding - bimodal image
    val, ret_matrix = cv2.threshold(input, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    lower_threshold = val * 0.4
    upper_threshold = val * 1.3

    print(lower_threshold, upper_threshold)

    # print(lower_threshold,upper_threshold)
    edges = cv2.Canny(input, lower_threshold, upper_threshold)
    return edges


def HoughCircles(input, circles):
    rows = input.shape[0]
    cols = input.shape[1]

    # initializing the angles to be computed
    sinang = dict()
    cosang = dict()
    # initializing the different radius
    radius = [i for i in range(10, 70)]             #  МОЖНО МЕНЯТЬ, ЧЕМ МЕНЬШЕ, ТЕМ БЫСТРЕЕ РАБОТАЕТ
    # For Generic Images
    # length=int(rows/2)
    # radius = [i for i in range(5,length)]

    # Initial threshold value
    threshold = 190

    for r in radius:
        # Initializing an empty 2D array with zeroes
        acc_cells = np.full((rows, cols), fill_value=0, dtype=np.uint64)

        # Iterating through the original image
        for x in range(rows):
            for y in range(cols):
                if input[x][y] == 255:  # edge
                    # increment in the accumulator cells
                    for angle in range(0, 360):
                        b = y - round(r * np.sin(angle * np.pi / 180))
                        a = x - round(r * np.cos(angle * np.pi / 180))
                        if a >= 0 and a < rows and b >= 0 and b < cols:
                            acc_cells[a][b] += 1

        print('For radius: ', r)
        acc_cell_max = np.amax(acc_cells)
        print('max acc value: ', acc_cell_max)

        if (acc_cell_max > 150):

            print("Detecting the circles for radius: ", r)

            # Initial threshold
            acc_cells[acc_cells < 150] = 0

            # find the circles for this radius
            for i in range(rows):
                for j in range(cols):
                    if (i > 0 and j > 0 and i < rows - 1 and j < cols - 1 and acc_cells[i][j] >= 150):
                        avg_sum = np.float32((acc_cells[i][j] + acc_cells[i - 1][j] + acc_cells[i + 1][j] +
                                              acc_cells[i][j - 1] + acc_cells[i][j + 1] + acc_cells[i - 1][j - 1] +
                                              acc_cells[i - 1][j + 1] + acc_cells[i + 1][j - 1] + acc_cells[i + 1][
                                                  j + 1]) / 9)
                        print("Intermediate avg_sum: ", avg_sum)
                        if (avg_sum >= 33):
                            print("For radius: ", r, "average: ", avg_sum, "\n")
                            circles.append((i, j, r))
                            acc_cells[i:i + 5, j:j + 7] = 0


def main():
    img_path = 'HoughCircles.jpg'
    # sample_inp1_path = 'circle_sample_1.jpg'

    orig_img = cv2.imread('image1.png')
    cv2.imshow('source image', orig_img)
    input_img = cv2.imread('image1.png', cv2.IMREAD_GRAYSCALE)
    # 1. Denoise using Gaussian filter and detect edges using canny edge detector
    smoothed_img = gaussian_smoothing(input_img)
#    cv2.imshow('1', smoothed_img)
    # 2. Detect Edges using Canny Edge Detector
    edged_image = canny_edge_detection(smoothed_img)
#    cv2.imshow('2', edged_image)
    circles = []
    HoughCircles(edged_image, circles)

    # Print the output
    for vertex in circles:
        cv2.circle(orig_img, (vertex[1], vertex[0]), vertex[2], (255, 0, 0), 1)
   #     cv2.rectangle(orig_img, (vertex[1] - 2, vertex[0] - 2), (vertex[1] - 2, vertex[0] - 2), (0, 0, 255), 3)

    print(circles)

    cv2.imshow('Circle Detected Image', orig_img)
    cv2.waitKey()

if __name__ == '__main__':
    main()