import numpy as np
import math
def psnr(original, compressed):
    if not original.shape == compressed.shape:
        raise ValueError('Input images must have the same dimensions.')
    mse = np.mean((original - compressed) ** 2)
    if (mse == 0):
        return 100
    max_pixel = 255.0
    result = 20 * math.log10(max_pixel / math.sqrt(mse))
    return result

